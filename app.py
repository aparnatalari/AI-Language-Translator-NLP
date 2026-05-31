import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

# Page Settings
st.set_page_config(
    page_title="AI Translator",
    page_icon="🌍",
    layout="centered"
)

# Title
st.title("🌍 AI Language Translator")
st.write("English to Hindi Translator using NLP")

# Input
text = st.text_area(
    "Enter English Text",
    height=150,
    placeholder="Type your text here..."
)

# Translate Button
translate_btn = st.button("🔄 Translate")

# Translation
if translate_btn:

    if text.strip() == "":
        st.warning("Please enter some text")

    else:

        with st.spinner("Translating..."):

            translated_text = GoogleTranslator(
                source='en',
                target='hi'
            ).translate(text)

            st.success("Translation Completed")

            st.subheader("Translated Text")

            st.write(translated_text)

            # Save History
            with open(
                "history.txt",
                "a",
                encoding="utf-8"
            ) as file:

                file.write(f"Input: {text}\n")
                file.write(f"Output: {translated_text}\n")
                file.write("-" * 50 + "\n")

            # Voice Output
            tts = gTTS(
                text=translated_text,
                lang="hi"
            )

            tts.save("voice.mp3")

            audio_file = open(
                "voice.mp3",
                "rb"
            )

            st.audio(audio_file.read())

# Translation History
st.subheader("📜 Translation History")

if os.path.exists("history.txt"):

    with open(
        "history.txt",
        "r",
        encoding="utf-8"
    ) as file:

        history = file.read()

        st.text_area(
            "History",
            history,
            height=200
        )

# Footer
st.markdown("---")

st.caption(
    "Built with Python, Streamlit and NLP"
)