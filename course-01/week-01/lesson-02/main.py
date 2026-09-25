from pydantic import BaseModel

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
        "model": "gemini-3",
        "provider": "google",
        "input_tokens": 800,
        "output_tokens": 400,
        "latency": 0.9,
    },
]


class LLMRequest(BaseModel):
    model: str
    provider: str
    input_tokens: int
    output_tokens: int
    latency: float

    def total_tokens(self):
        return self.input_tokens + self.output_tokens


fast_requests = []

new_llm_request = []


def calculate_total_tokens(llm_request):
    total_tokens = 0

    for request in llm_request:
        total_tokens += request["input_tokens"] + request["output_tokens"]

    return total_tokens


def check_latency(llm_request, threshold=1.5):
    for request in llm_request:
        if request["latency"] < threshold:
            fast_requests.append(request)
    return fast_requests


def transform_dataset(llm_requests):
    new_llm_request = [
        {
            "model": llm_requests["model"],
            "latency": llm_requests["latency"],
            "total_tokens": llm_requests["input_tokens"]
            + llm_requests["output_tokens"],
        }
    ]

    return new_llm_request


def aggregate_tokens_and_latency(llm_request):
    total_tokens = 0
    latency = 0
    average_latency = 0

    for request in llm_requests:
        total_tokens += request["input_tokens"] + request["output_tokens"]
        latency += request["latency"]

    average_latency = latency / len(llm_requests)

    return f"total tokens: {total_tokens}    average latency: {average_latency}"


def check_provider(llm_request):
    checked_providers = {}

    for request in llm_request:
        provider = request["provider"]
        if provider not in checked_providers:
            # provider = request['provider']
            checked_providers[provider] = 1
        else:
            checked_providers[provider] += 1

    return checked_providers



request_1 = LLMRequest(
    model="opus 5", input_tokens=800, output_tokens=400, latency=0.9, provider="claude"
)

request_2 = LLMRequest(
    model="gemini-3.1", input_tokens=400, output_tokens=500, latency=0.9, provider="google"
)
request_3 = LLMRequest(
    model="gpt 6 astra", input_tokens=480, output_tokens=600, latency=0.9, provider="openAI"
)
request_4 = LLMRequest(
    model="gemini-3.5", input_tokens=1000, output_tokens=700, latency=0.9, provider="google"
)
request_5 = LLMRequest(
    model="opus 5", input_tokens=300, output_tokens=400, latency=0.9, provider="claude"
)


print(f"Total tokens for request_1: {request_1.total_tokens()}")
print(f"Total tokens for request_2: {request_2.total_tokens()}")
print(f"Total tokens for request_3: {request_3.total_tokens()}")
print(f"Total tokens for request_4: {request_4.total_tokens()}")
print(f"Total tokens for request_5: {request_5.total_tokens()}")