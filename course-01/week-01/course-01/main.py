class LLMUsage:
    def __init__(self, model, provider, input_tokens, output_tokens, latency):
        self.model = model
        self.provider = provider
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.latency = latency

    def calculate_total_token(self):
        return self.input_tokens + self.output_tokens

    def calculate_cost(self):
        input_token_cost = 0.000001
        output_token_cost = 0.000002

        input_cost = input_token_cost * self.input_tokens
        output_cost = output_token_cost * self.output_tokens

        total_cost = input_cost + output_cost
        return total_cost
    
    
LLM1 = LLMUsage("gpt-5", "openai", 1000, 500, 1.2)
LLM2 = LLMUsage("gpt-4", "openai", 2000, 1000, 1.5)

print(f"LLM1 Total Tokens: {LLM1.calculate_total_token()}")
print(f"LLM1 Cost: ${LLM1.calculate_cost():.6f}")
print(f"LLM2 Total Tokens: {LLM2.calculate_total_token()}")
print(f"LLM2 Cost: ${LLM2.calculate_cost():.6f}")


# usage = {
#     "model": "gpt-5",
#     "provider": "openai",
#     "input_tokens": 1000,
#     "output_tokens": 500,
#     "latency": 1.2,
# }
