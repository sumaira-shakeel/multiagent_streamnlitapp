from utils.openai_agent import create_assistant, create_thread, run_agent
openai_assistant_id = create_assistant()
openai_thread_id = create_thread()


from agents import worker_001, worker_002, worker_003, worker_004
def openai_agent(task_input: str) -> str:
    return run_agent(openai_assistant_id, openai_thread_id, task_input)


def controller_agent(task: str, task_input: str) -> str:
    if task == "analyze_data":
        return worker_001.run_worker(task)
    elif task == "summarize":
        return worker_002.run_worker(task_input)
    elif task == "translate":
        return worker_003.run_worker(task_input)
    elif task == "write_email":
        return worker_004.run_worker(task_input)
    elif task == "use_openai_agent":
      result = openai_agent(task_input)

    else:
        return "Unknown task."
