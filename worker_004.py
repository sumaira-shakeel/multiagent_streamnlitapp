from utils.gemini_api import ask_gemini

def run_worker(task_input: str) -> str:
    prompt = f"Write a professional email about:\n\n{task_input}"
    return ask_gemini(prompt)
