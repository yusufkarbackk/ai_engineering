import os
from dotenv import load_dotenv

load_dotenv()


def get_config():

    if os.getenv("API_BASE_URL") == "":
        raise ValueError

    api_base_url = os.getenv("API_BASE_URL")

    if os.getenv("API_TIMEOUT") == None:
        api_timeout = 5
    else:
        api_timeout = os.getenv("API_TIMEOUT")

    return {"api_base_url": api_base_url, "api_timeout": api_timeout}
