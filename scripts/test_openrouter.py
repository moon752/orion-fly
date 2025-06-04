import os
import time
import openai
from openai import OpenAIError

openai.api_key = os.getenv("OPENROUTER_API_KEY") or "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"
openai.api_base = "https://openrouter.ai/api/v1"

FREE_MODELS = [
    "deepseek/deepseek-r1-0528-qwen3-8b:free", "deepseek/deepseek-r1-0528:free",
    "sarvamai/sarvam-m:free", "mistralai/devstral-small:free", "google/gemma-3n-e4b-it:free",
    "meta-llama/llama-3.3-8b-instruct:free", "nousresearch/deephermes-3-mistral-24b-preview:free",
    "microsoft/phi-4-reasoning-plus:free", "microsoft/phi-4-reasoning:free", "opengvlab/internvl3-14b:free",
    "opengvlab/internvl3-2b:free", "deepseek/deepseek-prover-v2:free", "qwen/qwen3-30b-a3b:free",
    "qwen/qwen3-8b:free", "qwen/qwen3-14b:free", "qwen/qwen3-32b:free", "qwen/qwen3-235b-a22b:free",
    "tngtech/deepseek-r1t-chimera:free", "microsoft/mai-ds-r1:free", "thudm/glm-4-32b:free",
    "shisa-ai/shisa-v2-llama3.3-70b:free", "arliai/qwq-32b-arliai-rpr-v1:free", "agentica-org/deepcoder-14b-preview:free",
    "moonshotai/kimi-vl-a3b-thinking:free", "nvidia/llama-3.3-nemotron-super-49b-v1:free",
    "nvidia/llama-3.1-nemotron-ultra-253b-v1:free", "meta-llama/llama-4-maverick:free",
    "meta-llama/llama-4-scout:free", "deepseek/deepseek-v3-base:free", "qwen/qwen2.5-vl-3b-instruct:free",
    "qwen/qwen2.5-vl-32b-instruct:free", "deepseek/deepseek-chat-v3-0324:free", "featherless/qwerky-72b:free",
    "mistralai/mistral-small-3.1-24b-instruct:free", "open-r1/olympiccoder-32b:free", "google/gemma-3-1b-it:free",
    "google/gemma-3-4b-it:free", "google/gemma-3-12b-it:free", "rekaai/reka-flash-3:free", "google/gemma-3-27b-it:free",
    "deepseek/deepseek-r1-zero:free", "moonshotai/moonlight-16b-a3b-instruct:free", "nousresearch/deephermes-3-llama-3-8b-preview:free",
    "cognitivecomputations/dolphin3.0-r1-mistral-24b:free", "qwen/qwen2.5-vl-72b-instruct:free",
    "mistralai/mistral-small-24b-instruct-2501:free", "deepseek/deepseek-r1-distill-qwen-32b:free",
    "deepseek/deepseek-r1-distill-qwen-14b:free", "deepseek/deepseek-r1-distill-llama-70b:free",
    "deepseek/deepseek-chat:free", "google/gemini-2.0-flash-exp:free", "meta-llama/llama-3.3-70b-instruct:free",
    "qwen/qwen-2.5-coder-32b-instruct:free", "qwen/qwen-2.5-7b-instruct:free", "meta-llama/llama-3.2-3b-instruct:free",
    "meta-llama/llama-3.2-11b-vision-instruct:free", "meta-llama/llama-3.2-1b-instruct:free",
    "qwen/qwen-2.5-72b-instruct:free", "qwen/qwen-2.5-vl-7b-instruct:free", "meta-llama/llama-3.1-405b:free",
    "meta-llama/llama-3.1-8b-instruct:free", "mistralai/mistral-nemo:free", "google/gemma-2-9b-it:free",
    "mistralai/mistral-7b-instruct:free"
]

PROMPT = "You are ORION, an autonomous AI agent. Reply with your model ID."

for model_id in FREE_MODELS:
    print(f"\n[🔁] Trying model: {model_id}")
    try:
        response = openai.ChatCompletion.create(
            model=model_id,
            messages=[{"role": "user", "content": PROMPT}]
        )
        print(f"[✅] SUCCESS with model: {model_id}")
        print("[🧠] ORION says:", response['choices'][0]['message']['content'])
        break
    except Exception as e:
        print(f"[⚠️] Model {model_id} failed with error: {e}")
        time.sleep(1)
