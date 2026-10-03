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
    {
        "model": "minimax-2.5",
        "provider": "google",
        "input_tokens": 800,
        "output_tokens": 400,
        "latency": 0.9,
    },
    {
        "model": "gpt-4o",
        "provider": "openai",
        "input_tokens": 2000,
        "output_tokens": 1000,
        "latency": 2.1,
    },
]


def calculate_total_token(input_tokens, output_tokens):
    return input_tokens + output_tokens


def add_total_tokens(request):
    new_request = llm_requests.copy()

    new_request["total_tokens"] = request["input_tokens"] + request["output_tokens"]

    return new_request


def is_fast_request(request):
    return request["latency"] < 1.5


# fast_requests = filter(is_fast_request, llm_requests)


def is_openai_request(request):
    return request["provider"] == "openai"


# open_ai_requests = filter(is_openai_request, llm_requests)


def filter_requests(requests, condition):
    return condition(requests)


def process_requests(requests):
    dataset_with_tokens = list(map(add_total_tokens, requests))

    fast_requests = list(filter(is_fast_request, dataset_with_tokens))

    open_ai_requests = list(filter(is_openai_request, fast_requests))
    print(open_ai_requests)
