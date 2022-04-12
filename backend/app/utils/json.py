import json
from typing import Dict
from app.errors.file import FileReadError, FileWriteError


def read_json_string(path: str) -> str:
    json_dict = {}
    try:
        with open(path) as file:
            for key, value in json.load(file).items():
                json_dict[key] = value

        return str(json_dict).replace("'", '"')
    except Exception as error:
        raise FileReadError(f"json, path: {path} | reason: {error}") from error


def read_json_dict(path: str) -> Dict[str, str]:
    json_dict = {}
    try:
        with open(path) as file:
            for key, value in json.load(file).items():
                json_dict[key] = value

        return json_dict
    except Exception as error:
        raise FileReadError(f"json, path: {path} | reason: {error}") from error
