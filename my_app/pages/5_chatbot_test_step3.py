import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="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")
completion = client.chat.completions.create(
    model="gpt-4o",
    store=True,
    messages=[
        {"role": "user", "content": "chatGPT가 뭐야"}
    ]
)

st.write(completion)
st.write(completion.to_dict())
response = completion.to_dict()
st.write(completion.to_dict()["choices"][0]["message"]["content"])