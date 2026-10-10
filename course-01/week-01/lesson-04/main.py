import logging

logger = logging.getLogger(__name__)
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


total_token_processed = 0
valid_request = 0
invalid_request = 0


class InvalidLLMRequestError(Exception):
    pass


def validate_request(request):
    global valid_request
    global invalid_request
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
        and request["latency"] >= 0
    ):
        logger.info("request valid")
        valid_request += 1
        return True
    else:
        logger.error("invalid request")
        invalid_request += 1
        return False


def get_total_tokens(request):
    global total_token_processed
    try:
        logger.info("total tokens valid")
        total_tokens = request["input_tokens"] + request["output_tokens"]
        total_token_processed += total_tokens
        return total_tokens
    except KeyError:
        logger.error("error key error")
        return None
    except TypeError:
        logger.error("error key error")
        return None


def validate_latency(latency):
    if latency < 0:
        logger.error("latency tidak valid")
        raise InvalidLLMRequestError("Latency cannot be negative.")
    return True


def process_request(request):
    validate_request(request)
    get_total_tokens(request)


def process_requests(requests):
    global valid_request
    global invalid_request
    total_requests = len(llm_requests)

    for request in requests:
        process_request(request)

    print(f"total requests:  {total_requests}")
    print(f"valid request: {valid_request}")
    print(f"invalid request: {invalid_request}")
    
    


process_requests(llm_requests)
