from utils.gemini_api import ask_gemini

def run_worker(task_type: str) -> str:
    if task_type == "analyze_data":
        prompt = "Please analyze this dataset and provide key trends."
    elif task_type == "write_summary":
        prompt = "Please write a short summary of a business report."
    else:
        prompt = "Perform a general task using Gemini."

    return ask_gemini(prompt)
