import os
import time
import random
from typing import Any, Callable
from openai import OpenAI
from dotenv import load_dotenv

# load bien moi truong
load_dotenv()

# Cau hinh Client cho Github
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN") 
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=GITHUB_TOKEN
)

COST_PER_1K_OUTPUT_TOKENS = {
    "gpt-4o": 0.010,
    "gpt-4o-mini": 0.0006,
}

OPENAI_MODEL = "gpt-4o"
OPENAI_MINI_MODEL = "gpt-4o-mini"

# Task 1 — Call GPT-4o
def call_openai(
    prompt: str,
    model: str = OPENAI_MODEL,
    temperature: float = 0.7,
    top_p: float = 0.9,
    max_tokens: int = 256,
) -> tuple[str, float]:
    start_time = time.perf_counter()
    
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens
    )
    
    latency = time.perf_counter() - start_time
    response_text = response.choices[0].message.content
    return response_text, latency

# Task 2 — Call GPT-4o-mini
def call_openai_mini(
    prompt: str,
    temperature: float = 0.7,
    top_p: float = 0.9,
    max_tokens: int = 256,
) -> tuple[str, float]:
    return call_openai(prompt, model=OPENAI_MINI_MODEL, temperature=temperature, top_p=top_p, max_tokens=max_tokens)

# Task 3 — Compare GPT-4o vs GPT-4o-mini
def compare_models(prompt: str) -> dict:
    # Call both gpt-4o and gpt-4o-mini with the same prompt and return a compare dict
    res_4o, lat_4o = call_openai(prompt)
    res_4o_mini, lat_4o_mini = call_openai_mini(prompt)
    
    # Hint (0.75 words ≈ 1 token is a rough approximation)
    word_count_4o = len(res_4o.split())
    tokens_estimate_4o = word_count_4o / 0.75
    cost_estimate = (tokens_estimate_4o / 1000) * COST_PER_1K_OUTPUT_TOKENS["gpt-4o"]
    
    # Task 3
    return {
        "gpt4o_response": res_4o,        
        "mini_response": res_4o_mini,    
        "gpt4o_latency": lat_4o,        
        "mini_latency": lat_4o_mini,     
        "gpt4o_cost_estimate": cost_estimate
    }

# Task 4 — Streaming chatbot with conversation history
def streaming_chatbot() -> None:
    history = []
    print("\n[Chatbot] Type 'quit' and 'exit' to end.")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["quit", "exit"]:
            break
            
        history.append({"role": "user", "content": user_input})
        
        # Trim history to the lát 3 turns
        if len(history) > 6:
            history = history[-6:]
            
        print("AI: ", end="", flush=True)
        
        stream = client.chat.completions.create(
            model=OPENAI_MINI_MODEL,
            messages=history,
            stream=True
        )
        
        reply = ""
        for chunk in stream:
            if len(chunk.choices) > 0:
                delta_content = chunk.choices[0].delta.content
                
                if delta_content is not None:
                    print(delta_content, end="", flush=True)
                    reply += delta_content
        
        print() 
        history.append({"role": "assistant", "content": reply})

# Bonus Task A — Retry with exponential backoff
def retry_with_backoff(
    fn: Callable, 
    max_retries: int = 3, 
    base_delay: float = 0.1
) -> Any:
    for attempt in range(max_retries + 1):
        try:
            return fn()
        except Exception as e:
            if attempt == max_retries:
                raise e
            delay = base_delay * (2 ** attempt) + random.uniform(0, 0.1)
            print(f"Retry {attempt+1} after {delay:.2f}s due to error: {e}")
            time.sleep(delay)

# Bonus Task B — Batch compare
def batch_compare(prompts: list[str]) -> list[dict]:
    results = []
    for p in prompts:
        res = compare_models(p)
        res["prompt"] = p
        results.append(res)
    return results

# Bonus Task C — Format comparison table
def format_comparison_table(results: list[dict]) -> str:
    header = f"{'Prompt':<20} | {'GPT-4o (s)':<10} | {'Mini (s)':<10} | {'Response Preview'}"
    separator = "-" * 80
    lines = [header, separator]
    
    for r in results:
        p_text = r['prompt'][:17] + "..." if len(r['prompt']) > 20 else r['prompt']
        res_preview = r['gpt4o_response'][:37].replace('\n', ' ') + "..."
        line = f"{p_text:<20} | {r['gpt4o_latency']:<10.2f} | {r['mini_latency']:<10.2f} | {res_preview}"
        lines.append(line)
        
    return "\n".join(lines)

# Entry point
if __name__ == "__main__":
    test_prompt = "Explain the difference between temperature and top_p in one sentence."
    print("=== Comparing models ===")
    result = compare_models(test_prompt)
    for key, value in result.items():
        print(f"{key}: {value}")

    print("\n=== Starting chatbot (type 'quit' to exit) ===")
    streaming_chatbot()