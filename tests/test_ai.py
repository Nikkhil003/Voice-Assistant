# tests/test_ai.py
from modules.ai import ask_gpt

def test_ask_gpt():
    # Test a simple query
    query = "What is the capital of France?"
    response = ask_gpt(query)
    assert isinstance(response, str)
    assert len(response) > 0
    print("GPT Response:", response)