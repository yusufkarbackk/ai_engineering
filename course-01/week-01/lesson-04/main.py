import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

llm_requests = [
    {
        "model": "gpt-5",
        "provider": "openai",
        "input_tokens": 1000,
        "output_tokens": 500,
        "latency": 1.2,
    },
    {
        "model": "claude-sonnet",
        "provider": "anthropic",
        "input_tokens": 1500,
        "output_tokens": 700,
        "latency": 1.8,
    },
    {
        "model": "gemini-2.5",
        "provider": "google",
        "input_tokens": 800,
        "output_tokens": 400,
        "latency": 0.9,
    },
    # Invalid: input_tokens berupa string
    {
        "model": "gpt-4o",
        "provider": "openai",
        "input_tokens": "2000",
        "output_tokens": 1000,
        "latency": 2.1,
    },
    # Invalid: field output_tokens tidak ada
    {
        "model": "gpt-4o",
        "provider": "openai",
        "input_tokens": 1000,
        "latency": 1.5,
    },
    # Invalid: latency negatif
    {
        "model": "gemini-2.5",
        "provider": "google",
        "input_tokens": 500,
        "output_tokens": 300,
        "latency": -1,
    },
]


# total_token_processed = 0
# valid_request = 0
# invalid_request = 0


class InvalidLLMRequestError(Exception):
    pass


def validate_request(request):
    required_fields = {"model", "provider", "input_tokens", "output_tokens", "latency"}

    if not isinstance(request, dict):
        logger.warning("Request must be a dictionary")
        return False

    if not required_fields.issubset(request):
        logger.warning("Request is missing required fields")
        return False

    if not isinstance(request["model"], str) or not request["model"].strip():
        logger.warning("Model must be a non-empty string")
        return False

    if not isinstance(request["provider"], str) or not request["provider"].strip():
        logger.warning("Provider must be a non-empty string")
        return False

    # type(...) is int mencegah bool dianggap sebagai integer
    if type(request["input_tokens"]) is not int:
        logger.warning("input_tokens must be an integer")
        return False

    if type(request["output_tokens"]) is not int:
        logger.warning("output_tokens must be an integer")
        return False

    if request["input_tokens"] < 0 or request["output_tokens"] < 0:
        logger.warning("Token counts cannot be negative")
        return False

    if type(request["latency"]) not in (int, float):
        logger.warning("Latency must be numeric")
        return False

    return True


def get_total_tokens(request):
    try:
        return request["input_tokens"] + request["output_tokens"]
    except KeyError as error:
        logger.error("Missing token field: %s", error)
        return None
    except TypeError as error:
        logger.error("Token values have incompatible types: %s", error)
        return None


def validate_latency(latency):
    if latency < 0:
        raise ValueError("Latency cannot be negative.")
    else:
        return True


def process_request(request):
    if not validate_request(request):
        raise InvalidLLMRequestError("Request failed validation")

    validate_latency(request["latency"])

    total_tokens = get_total_tokens(request)
    if total_tokens is None:
        raise InvalidLLMRequestError("Unable to calculate total tokens")

    logger.info("Request processed successfully")
    return total_tokens


def process_requests(requests):
    total_token_processed = 0
    valid_request = 0
    invalid_request = 0

    try:
        for request in requests:
            try:
                tokens = process_request(request)
            except (InvalidLLMRequestError, ValueError) as error:
                invalid_request += 1
                logger.warning("Request rejected: %s", error)
                continue

            valid_request += 1
            total_token_processed += tokens

        logger.info("Total requests: %d", len(requests))
        logger.info("Valid requests: %d", valid_request)
        logger.info("Invalid requests: %d", invalid_request)
        logger.info("Total tokens processed: %d", total_token_processed)

    finally:
        logger.info("Request processing finished")


process_requests(llm_requests)

# Test KeyError: output_tokens tidak tersedia
get_total_tokens({"input_tokens": 100})

# Test TypeError: token berupa string
get_total_tokens({"input_tokens": "100", "output_tokens": 50})
