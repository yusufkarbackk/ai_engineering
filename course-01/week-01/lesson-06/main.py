import os


def get_config():

    if os.getenv("API_BASE_URL") == "" or os.getenv("API_BASE_URL") == None:
        raise ValueError

    api_base_url = os.getenv("API_BASE_URL")

    if os.getenv("API_TIMEOUT") == None:
        api_timeout = 5
    else:
        api_timeout = int(os.getenv("API_TIMEOUT"))

    return {"api_base_url": api_base_url, "api_timeout": api_timeout}


if __name__ == "__main__":
    print(get_config())
