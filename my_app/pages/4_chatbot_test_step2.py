import streamlit as st

if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"assistant", "content":"무엇을 도와드릴까요? 휴먼?"}]

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if query := st.chat_input("질문을 입력하세요."):
    st.session_state.messages.append({"role":"user", "content":query})
    st.chat_message("user").write(query)
    response = f"{query}질문에 대한 답변입니다."
    st.session_state.messages.append({"role":"assistant", "content":response})
    st.chat_message("assistant").write(response)