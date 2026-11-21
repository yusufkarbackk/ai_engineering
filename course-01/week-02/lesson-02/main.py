import json


def parse_json(json_string):
    try:
        data = json.loads(json_string)
        return data
    except json.JSONDecodeError as e:
        raise ("Invalid JSON syntax: ", e)

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
        data = json.load(file_path)
        return data
    except json.JSONDecodeError as e:
        raise ("Invalid JSON syntax: ", e)
    except FileNotFoundError as e:
        raise ("File not found: ", e)


def write_json_file(file_path, data):
    try:
        data = json.dump(file_path)
        return data
    except json.JSONDecodeError as e:
        raise ("Invalid JSON syntax: ", e)
    except FileNotFoundError as e:
        raise ("File not found: ", e)

    """
    Persyaratan:
        - read_json_file() membaca file JSON dan mengembalikan Python object.
        - write_json_file() menyimpan Python object ke file JSON.
        - Gunakan json.load() dan json.dump(), bukan loads() dan dumps() untuk kedua fungsi ini.
        - Perhatikan error ketika file tidak ditemukan dan ketika isi JSON tidak valid.
    """
