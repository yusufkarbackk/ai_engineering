import os


def get_config():

    if not os.getenv("API_BASE_URL"):
        raise ValueError

    api_base_url = os.getenv("API_BASE_URL")

    if os.getenv("API_TIMEOUT") is None:
        api_timeout = 5
    else:
        api_timeout = int(os.getenv("API_TIMEOUT"))

    return {"api_base_url": api_base_url, "api_timeout": api_timeout}


if __name__ == "__main__":
    print(get_config())
