import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="Groq Chatbot",
    page_icon="🤖"
)

st.title("🤖 Groq AI Chatbot")
st.caption("Powered by Groq")

# Sidebar
with st.sidebar:
    groq_api_key = st.text_input(
        "Groq API Key",
        type="password"
    )

if not groq_api_key:
    st.info("Enter your Groq API Key in the sidebar.")
    st.stop()

client = Groq(api_key=groq_api_key)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Type your message..."):

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        response_placeholder = st.empty()

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=st.session_state.messages,
            temperature=0.7,
            max_tokens=1024,
        )

        response = completion.choices[0].message.content

        response_placeholder.markdown(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )