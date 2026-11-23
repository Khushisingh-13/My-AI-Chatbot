
import streamlit as st
import ollama


st.set_page_config(
    page_title="My AI Chatbot",
    page_icon="🤖",
    layout="centered"
)


st.sidebar.title("🤖 My AI Chatbot")
st.sidebar.write("Your personal AI assistant")
st.sidebar.divider()

st.sidebar.write("Model: Qwen3 1.7B")
st.sidebar.write("Powered by Ollama")

if st.sidebar.button("➕ New Chat"):
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant. Explain things in simple language."
        }
    ]
    st.rerun()


st.title("My AI Chatbot 🤖")
st.caption("Ask questions and learn something new!")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant. Explain things in simple language."
        }
    ]

if len(st.session_state.messages) == 1:
    st.info("Hello! 👋 I'm your AI assistant. How can I help you today?")

for message in st.session_state.messages:
    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Ask me anything...")

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            try:
                response = ollama.chat(
                    model="qwen3:1.7b",
                    messages=st.session_state.messages
                )

                answer = response["message"]["content"]

                st.write(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except ollama.ResponseError as e:
                st.error("Ollama returned an error. Please check your model.")
                st.caption(f"Technical details: {e}")

            except Exception as e:
                st.error("Something went wrong. Please check whether Ollama is running.")
                st.caption(f"Technical details: {e}")
