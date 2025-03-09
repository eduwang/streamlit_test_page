import streamlit as st
from openai import OpenAI

if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"assistant", "content":"무엇을 도와드릴까요? 휴먼?"}]

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if prompt := st.chat_input("질문을 입력하세요."):
    st.session_state.messages.append({"role":"user", "content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    client = OpenAI(api_key="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")
    completion = client.chat.completions.create(
        model="gpt-4o",
        store=True,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    response = completion.to_dict()["choices"][0]["message"]["content"]
    
    st.session_state.messages.append({"role":"assistant", "content":response})
    with st.chat_message("assistant"):
        st.markdown(response)