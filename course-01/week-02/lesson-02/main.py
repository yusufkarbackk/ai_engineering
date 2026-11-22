import json


def parse_json(json_string):
    data = json.loads(json_string)
    return data


def serialize_json(data):
    data = json.dumps(data, indent=4)
    return data

    """
    Persyaratan:
        - Menerima Python dictionary.
        - Mengembalikan JSON string.
        - Format JSON harus menggunakan indentasi 4 spasi.
    """


def read_json_file(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json_file(file_path, data):

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
