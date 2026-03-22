import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Initialize session state on first run
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant for لحظة local brand which is an online store for old style handwritten letters, open 24/7. Greet users warmly using the brand name. Topics you can help with: prices, colors, gestures, surprises and customized letters. Always reply with a friendly tone."}
    ]

def chatBot(user_input):
    st.session_state.messages.append({"role": "user", "content": user_input})
    botReply = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.messages
    ).choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": botReply})
    return botReply

# Page title
st.title("لحظة Assistant 💌")
st.caption("Your personal handwritten letters guide")

# Display chat history
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input at the bottom
user_input = st.chat_input("Ask me anything...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    with st.chat_message("assistant"):
        with st.spinner("لحظة is typing..."):
            reply = chatBot(user_input)
        st.write(reply)
