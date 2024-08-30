import os
import streamlit as st
import openai
from dotenv import load_dotenv

# Load variabel dari file .env
load_dotenv()

# Set API key OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def paraphrase_text(text):
    prompt = f"Parafrase teks berikut ini dengan tetap mempertahankan makna aslinya:\n\n{text}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that provides paraphrased versions of texts."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=150,
        temperature=0.7,
    )

    paraphrased_text = response.choices[0].message['content'].strip()
    return paraphrased_text

# Streamlit app title
st.title("Ngubah AI - Universitas Teknokrat Indonesia")

# User input for text
text = st.text_area("Masukkan teks yang ingin diparafrasekan:")

# Paraphrase button
if st.button("Parafrasekan"):
    if text:
        paraphrased_text = paraphrase_text(text)
        st.subheader("Hasil Parafrase")
        st.write(paraphrased_text)
    else:
        st.warning("Silakan masukkan teks terlebih dahulu.")

# Footer
st.markdown("Dibuat dengan ❤️ oleh Pusat Unggulan Kecerdasan Buatan Universitas Teknokrat Indonesia")
