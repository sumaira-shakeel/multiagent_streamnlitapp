# utils/openai_agent.py

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Create an assistant (GPT-4 with tools)
def create_assistant():
 assistant = client.beta.assistants.create(
    name="ControllerAgent",
    instructions="You are the main controller agent...",
    model="gpt-3.5-turbo",  # 🔄 Yeh sahi model hai
    tools=[{"type": "code_interpreter"}]
)
 return assistant.id

# Create a thread (conversation memory)
def create_thread():
    thread = client.beta.threads.create()
    return thread.id

# Ask the assistant
def run_agent(assistant_id, thread_id, user_input):
    # Add user message
    client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=user_input
    )

    # Run the assistant
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )

    # Wait until response is ready
    while True:
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )
        if run_status.status == "completed":
            break

    # Get and return the final message
    messages = client.beta.threads.messages.list(thread_id=thread_id)
    return messages.data[0].content[0].text.value
