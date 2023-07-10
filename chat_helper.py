import openai
import streamlit as st

openai.api_key = st.secrets.get("OPENAI_API_KEY")

st.session_state["translated_text"] = ""


def convert_message(message: str):
    new_prompt = "Rephrase the following in NVC Language. Be careful to distinguish pseudo-feelings from feelings."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": new_prompt},
            {"role": "user", "content": message}
        ]
    )
    translated_text = response.choices[0]['message']['content']
    st.session_state["translated_text"] = translated_text


st.title("How to talk to you partner")
st.divider()

with st.container():
    st.session_state["text"] = st.text_area(label="",
                                            placeholder="Enter text you want to translate, e.g 'You never text me and I feel abandoned.','You are selfish'")
    st.markdown("")
    st.markdown("")
    if st.button(on_click=convert_message(st.session_state["text"]), label="Translate"):
        st.markdown("")
        st.markdown("")
        st.success(st.session_state["translated_text"])
    else:
        st.markdown("Click the button to translate")
