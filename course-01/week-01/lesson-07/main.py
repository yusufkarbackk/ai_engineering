import logging
import os

logger = logging.getLogger(__name__)


def get_config():

    if not os.getenv("API_BASE_URL"):
        logger.error("API_BASE_URL kosong")
        raise ValueError

    api_base_url = os.getenv("API_BASE_URL")

    timeout_value = os.getenv("API_TIMEOUT")

    if timeout_value is None:
        logger.warning("API_TIMEOUT tidak ditemukan, menggunakan default 5")
        api_timeout = 5
    else:
        try:
            api_timeout = int(timeout_value)
        except ValueError:
            logger.error("API_TIMEOUT invalid")
            raise

    logger.info("config sukses")
    return {"api_base_url": api_base_url, "api_timeout": api_timeout}


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    print(get_config())
