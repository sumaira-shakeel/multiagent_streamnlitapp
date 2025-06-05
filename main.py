# import streamlit as st
# from agents.controller import controller_agent

# st.set_page_config(page_title="AI Multi-Agent System", layout="centered")
# st.title("🤖 AI Multi-Agent System")

# task = st.selectbox("Choose a task", [
#     "analyze_data", 
#     "summarize", 
#     "translate", 
#     "write_email",
#      "use_openai_agent"
# ])

# task_input = st.text_area("Enter text for the agent to process")

# if st.button("Run Agent Task"):
#     with st.spinner("Running the AI agent..."):
#         result = controller_agent(task, task_input)
#         st.success("Done!")
#         st.write(result)


import streamlit as st
from agents.controller import controller_agent

st.set_page_config(page_title="AI Multi-Agent System", layout="centered")
st.title("🤖 AI Multi-Agent System")

# Only include the three required tasks
task = st.selectbox("Choose a task", [
    "summarize",
    "translate",
    "analyze_data"
])

task_input = st.text_area("Enter text for the agent to process")

if st.button("Run Agent Task"):
    with st.spinner("Running the AI agent..."):
        result = controller_agent(task, task_input)
        st.success("Done!")
        st.write(result)

