import streamlit as st
from orchestrator import handle_query
from tinydb import TinyDB

st.title("🧠 Persistent Memory Agent")

# Initialize the DB
db = TinyDB("memory/memory_store.json")

# Load existing topics
topics = [item["name"] for item in db.all()]
selected_topic = st.selectbox("Choose or create a topic", options=topics + ["Start new topic"])

# Handle new topic creation
if selected_topic == "Start new topic":
    selected_topic = st.text_input("Enter new topic name")

# User input
user_input = st.text_area("Ask a question or input research note:")

# Query the agent
if st.button("Submit") and selected_topic and user_input:
    response, history = handle_query(selected_topic, user_input)

    # Display AI response
    st.subheader("💬 AI Response")
    st.write(response)

    # Display conversation history
    st.subheader("🧠 Topic Memory Log")
    for entry in reversed(history):
        st.markdown(f"**You**: {entry['user']}")
        st.markdown(f"**AI**: {entry['ai']}")
