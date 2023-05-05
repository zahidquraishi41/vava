import os


__api_template = '''from api.helper.api_base import APIBase
from api.helper.message import Message
from api.helper.utils import fetch
import requests


class {API_NAME}(APIBase):

    def validate(self, msg: Message):
        return False

    def run(self,  msg: Message):
        pass

    def help(self):
        return {{
            '{API_CMD}': 'COMMAND DESCRIPTION'
        }}
'''


def _get_api_dir():
    return os.path.join(os.getcwd(), 'api')


def add_api():
    api_dir = _get_api_dir()
    api_name = input('Enter API name: ')

    template = __api_template.format(
        API_NAME=api_name.title(),
        API_CMD=api_name.lower()
    )
    api_path = os.path.join(api_dir, api_name.lower() + '.py')
    with open(api_path, 'w') as f:
        f.write(template)
    update_list()
    print('Created successfully.')


def update_list():
    api_dir = _get_api_dir()
    init_path = os.path.join(api_dir, '__init__.py')

    apis = [api.rsplit('.', 1)[0] for api in os.listdir(api_dir)
            if api.endswith('.py') and api != '__init__.py']
    apis.sort()

    try:
        with open(init_path, 'w') as f:
            f.write('from api.helper.api_manager import APIManager\n\n')

            for api in apis:
                f.write(f'from api.{api} import {api.title()}\n')

            f.write(f'\napi_manager = APIManager()\n\n')

            for api in apis:
                f.write(f'api_manager.register({api.title()}())\n')
            print('Updated successfully.')
    except Exception as e:
        print(e)


def main():
    print('[1] Add new API')
    print('[2] Update API list')
    print('[3] Exit')
    while True:
        response = input('Enter a number: ')
        if response.isdigit():
            if int(response) == 1:
                add_api()
            elif int(response) == 2:
                update_list()
            elif int(response) == 3:
                break


if __name__ == '__main__':
    main()
