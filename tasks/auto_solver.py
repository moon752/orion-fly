import json, time
from utils.ai_model import ai

def solve_task(task_json):
    task = json.loads(task_json)
    messages = [{"role": "user", "content": f"Solve: {task}"}]
    return ai(messages, model="deepseek/deepseek-moe-16b-chat")

if __name__ == "__main__":
    demo = '{"type":"write","prompt":"Hello World blog"}'
    print("Solution:", solve_task(demo))
