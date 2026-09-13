usage = {
    "model": "gpt-5",
    "provider": "openai",
    "input_tokens": 1000,
    "output_tokens": 500,
    "latency": 1.2,
}

def calculate_total_tokens(input_tokens, output_tokens):
    return input_tokens + output_tokens

def calculate_cost(input_tokens, output_tokens):
        input_token_cost = 0.000001
        output_token_cost = 0.000002

        input_cost = input_token_cost * input_tokens
        output_cost = output_token_cost * output_tokens

        total_cost = input_cost + output_cost
        return total_cost

class LLMUsage:
    def __init__(self, model, provider, input_tokens, output_tokens, latency):
        self.model = model
        self.provider = provider
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.latency = latency

    def calculate_total_tokens(self):
        return calculate_total_tokens(self.input_tokens, self.output_tokens)

    def calculate_cost(self):
        input_token_cost = 0.000001
        output_token_cost = 0.000002

        input_cost = input_token_cost * self.input_tokens
        output_cost = output_token_cost * self.output_tokens

        total_cost = input_cost + output_cost
        return total_cost
    
class LLMProvider:
    def generate(self):
        return "Generating text using the LLM provider."
    
class OpenAIProvider(LLMProvider):
    def generate(self):
        return "Generating text using OpenAI's LLM."
class AnthropicProvider(LLMProvider):
    def generate(self):
        return "Generating text using Anthropic's LLM."
    
    
llm1 = LLMUsage("gpt-5", "openai", 1000, 500, 1.2)
llm2 = LLMUsage("gpt-4", "openai", 2000, 1000, 1.5)

print(f"llm1 Total Tokens: {llm1.calculate_total_tokens()}")
print(f"llm1 Cost: ${llm1.calculate_cost():.6f}")
print(f"llm2 Total Tokens: {llm2.calculate_total_tokens()}")
print(f"llm2 Cost: ${llm2.calculate_cost():.6f}")

openai_provider = OpenAIProvider()
anthropic_provider = AnthropicProvider()

print(openai_provider.generate())
print(anthropic_provider.generate())

