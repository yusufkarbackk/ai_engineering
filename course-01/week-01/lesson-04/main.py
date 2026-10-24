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
    if (
        "model" in request.keys()
        and "provider" in request.keys()
        and "input_tokens" in request.keys()
        and "output_tokens" in request.keys()
        and "latency" in request.keys()
        and type(request["input_tokens"]) == int
        and type(request["output_tokens"]) == int
        and (type(request["latency"]) == int or type(request["latency"]) == float)
        and request["input_tokens"] >= 0
        and request["output_tokens"] >= 0
        and validate_latency(request["latency"])
    ):
        logger.info("request valid")
        return True
    else:
        logger.warning("invalid request")
        return False


def get_total_tokens(request):
    total_token_processed = 0
    try:
        logger.info("total tokens valid")
        total_tokens = request["input_tokens"] + request["output_tokens"]
        total_token_processed += total_tokens
        return total_token_processed
    except KeyError:
        logger.error("error key error")
        return None
    except TypeError:
        logger.error("error type error")
        return None


def validate_latency(latency):
    if latency < 0:
        logger.error("latency tidak valid")
        raise ValueError("Latency cannot be negative.")
    else:
        return True


def process_request(request):
    try:
        if validate_request(request):
            validate_latency(request["latency"])
            total_tokens = get_total_tokens(request)
            return total_tokens
        else:
            logger.warning("invalid request")
            raise InvalidLLMRequestError
    except (InvalidLLMRequestError, ValueError) as error:
        return InvalidLLMRequestError


def process_requests(requests):
    total_token_processed = 0
    valid_request = 0
    invalid_request = 0
    total_requests = len(requests)

    for request in requests:
        try:
            total_token_processed += process_request(request)
            valid_request += 1
        except InvalidLLMRequestError:
            invalid_request += 1
            logger.warning("invalid request")
            continue

    logger.info(f"total requests:  {total_requests}")
    logger.info(f"valid request: {valid_request}")
    logger.info(f"invalid request: {invalid_request}")
    logger.info(f"total token processed: {total_token_processed}")


process_requests(llm_requests)
