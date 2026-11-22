import json


def parse_json(json_string):
    try:
        data = json.loads(json_string)
        return data
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON syntax: {e.msg}", e.doc, e.pos) from e
    """
    Persyaratan:
        - Menerima JSON dalam bentuk string.
        - Mengembalikan Python object hasil parsing.
        - Menangani JSON yang tidak valid dengan json.JSONDecodeError.
    """


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
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON syntax: {e.msg}", e.doc, e.pos) from e
    except FileNotFoundError as e:
        raise FileNotFoundError(f"file not found: {e.msg}", e.doc, e.pos) from e


def write_json_file(file_path, data):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError("Invalid JSON syntax: ", e)
    except FileNotFoundError as e:
        raise FileNotFoundError("File not found: ", e)
    except TypeError as e:
        raise TypeError("serialization failed", e)
