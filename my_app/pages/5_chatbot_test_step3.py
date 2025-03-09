import streamlit as st
from openai import OpenAI

api_key = st.secrets["openai"]["api_key"]
# st.write(f"API Key: {api_key}")
client = OpenAI(api_key = api_key)
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