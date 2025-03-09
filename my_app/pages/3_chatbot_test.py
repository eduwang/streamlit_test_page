import streamlit as st
import numpy as np

with st.chat_message('user'):
    st.write("hi")
    st.write("Nice to meey you")

with st.chat_message('assistant'):
    st.write("hello too")
    st.write("who are you?")

messages = [
    {"role": "user", "content":"hi"},
    {"role": "assistant", "content":"hii"},
    {"role": "user", "content":"hello"},
    {"role": "assistant", "content":"helloooo"}
]

for m in messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if query := st.chat_input("질문을 입력하세요."):
    messages.append({"role":"user", "content":query})
    st.chat_message("user").write(query)
    response = f"{query}질문에 대한 답변입니다."
    messages.append({"role":"assistant", "content":response})
    st.chat_message("assistant").write(response)