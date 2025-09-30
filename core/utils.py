import requests
import difflib
from typing import Any
import json


def fetch(url: str, keys: Any = None, headers: dict = None) -> Any:
    """
    Sends a GET request to the provided URL, parses the JSON response,
    and returns the value of the specified key(s).

    Args:
        url : The URL to send the GET request to.
        keys : The key(s) to fetch from the JSON data.
            If None, the entire JSON data is returned. Defaults to None.
        headers : Dictionary of HTTP headers to be sent with the request.
            Defaults to None.

    Returns:
        If a single key is provided, the value for that key is returned.
        If multiple keys are provided, a list of values for those keys is returned.
        If no keys are provided, the entire JSON data is returned.
    """
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)

    if keys is None:
        return json_data

    data = []
    singular = isinstance(keys, str)
    if singular:
        keys = [keys]

    for key in keys:
        sub_keys = key.split(".")
        val = json_data
        for sub_key in sub_keys:
            if isinstance(val, list) and sub_key.isdigit():
                val = val[int(sub_key)]
            else:
                val = val[sub_key]
        data.append(val)

    return data[0] if singular else data


def is_similar(s1: str, s2: str) -> bool:
    """
    Determines if two strings are similar based on the ratio of their longest common subsequence.

    Args:
        s1 (str): The first string to compare.
        s2 (str): The second string to compare.

    Returns:
        bool: True if the ratio of the longest common subsequence is greater than or equal to 0.7, False otherwise.
    """
    ratio = difflib.SequenceMatcher(a=s1, b=s2).ratio()
    return ratio >= 0.7
