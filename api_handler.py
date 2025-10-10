from api import apis
from core.command import Command
from core.base_api import BaseAPI
import re


class Wrapper:
    def __init__(self, cls: BaseAPI):
        self.instance = cls()
        self.active = True
        self.name = cls.__name__.lower()

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        return self == other

    def __lt__(self, other: BaseAPI):
        return self.instance.priority < other.instance.priority


class APIHandler:
    def __init__(self) -> None:
        self._apis = [Wrapper(cls) for cls in apis]
        self._apis.sort()
        self.last_cmd = None

    def _ping(self, cmd: Command) -> bool:
        if not cmd.is_admin:
            return "Admin privilege is required."

        if cmd.param != "all":
            if cmd.param not in self._apis:
                return f"{cmd.param} is not a valid command."
            i = self._apis.index(cmd.param)
            return self._apis[i].instance.ping()

        outputs = []
        for api in self._apis:
            outputs.append(f"{api.name} {api.instance.ping()}")
        return "\n".join(outputs)

    def _toggle(self, cmd: Command) -> str:
        if not cmd.is_admin:
            return "Admin privilege is required."

        if cmd.param in self._apis:
            api = self._apis[self._apis.index(cmd.param)]
            if cmd.command == "enable":
                if api.active:
                    return "The command is already enabled. No changes were made."
                api.active = True
                return "The command has been successfully enabled!"
            elif cmd.command == "disable":
                if not api.active:
                    return "The command is already disabled. No changes were made."
                api.active = False
                return "The command has been successfully disabled."

        if cmd.command.startswith("enable"):
            s = "List of enabled commands:"
            enabled = [api.name for api in self._apis if api.active]
            return s + "\n" + "\n".join(enabled)

        else:
            s = "List of enabled commands:"
            disabled = [api.name for api in self._apis if not api.active]
            return s + "\n" + "\n".join(disabled)

    def _help(self, cmd: Command) -> str:
        names = [api.name for api in self._apis]
        if not cmd.param:
            s = "List of commands:"
            return s + "\n" + "\n".join(sorted(names))

        if cmd.param not in names:
            return f"{cmd.param} is not a valid command."

        i = names.index(cmd.param)
        doc = apis[i].__doc__ or "No document found."
        doc = re.sub(r"(?<=\n) +", "", doc)
        return doc

    def process(self, message) -> str | None:
        cmd = Command(message)

        # system commands
        if cmd.command in ("enable", "enabled", "disable", "disabled"):
            cmd.output = self._toggle(cmd)
        elif cmd.command == "help":
            cmd.output = self._help(cmd)
        elif cmd.command == "ping":
            cmd.output = self._ping(cmd)
        elif cmd.command == ".":
            if self.last_cmd:
                cmd = self.last_cmd
            else:
                cmd.output = "No command to repeat"

        # api commands
        for api in self._apis:
            if api.active and api.instance.validate(cmd):
                cmd.output = api.instance.run(cmd)

        if cmd.is_command and cmd.command not in (".", "idk"):
            self.last_cmd = cmd

        return cmd.output
