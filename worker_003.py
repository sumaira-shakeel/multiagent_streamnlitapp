from utils.gemini_api import ask_gemini

def run_worker(task_input: str) -> str:
    prompt = f"Translate this text into Urdu:\n\n{task_input}"
    return ask_gemini(prompt)
