import streamlit as st
import cv2
from PIL import Image
from deep_translator import GoogleTranslator
import pyttsx3
import time
import gc

# Inicialização do motor de síntese de voz
engine = pyttsx3.init()

# Inicialização do tradutor
tradutor = GoogleTranslator(source="en", target="pt")

@st.cache_resource
def load_model():
    from transformers import BlipProcessor, BlipForConditionalGeneration
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_model()
prompt = "a photography of"

def resize_image(image, max_size=800):
    width, height = image.size
    if max(width, height) > max_size:
        scale = max_size / float(max(width, height))
        return image.resize((int(width * scale), int(height * scale)), Image.ANTIALIAS)
    return image

# Função principal
def main():
    st.title("Image Captioning com Tradução Automática")
    st.write("Clique no botão abaixo para iniciar a captura de imagens da webcam e a geração de legendas traduzidas automaticamente.")
    
    if st.button("Start"):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            st.error("Erro ao abrir a câmera.")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                st.error("Erro ao capturar a imagem.")
                break

            frame = cv2.resize(frame, (640, 480))  # Reduz a resolução do frame
            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            st.image(image, caption="Imagem capturada", use_column_width=True)

            inputs = processor(images=image, text=prompt, return_tensors="pt")
            out = model.generate(**inputs)
            generated_text = processor.decode(out[0], skip_special_tokens=True)
            traducao = tradutor.translate(generated_text)
            st.subheader("Legenda gerada:")
            st.write(generated_text)
            st.subheader("Tradução:")
            st.write(traducao)
            
            engine.say(traducao)
            engine.runAndWait()

            time.sleep(5)

            # Libere recursos não utilizados
            del image, inputs, out, generated_text, traducao, frame
            gc.collect()

        cap.release()
        cv2.destroyAllWindows()

main()