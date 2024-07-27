import cv2
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from deep_translator import GoogleTranslator
import pyttsx3
import time
 
# Inicialização do motor de síntese de voz
engine = pyttsx3.init()
 
# Inicialização do tradutor
tradutor = GoogleTranslator(source="en", target="pt")
 
# Carregar o modelo e o processador fora do loop
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
prompt = ""
 
# Inicializa a câmera
cap = cv2.VideoCapture(0)
 
 
# Verifica se a câmera está aberta corretamente
if not cap.isOpened():
    print("Erro ao abrir a câmera.")
    exit()
 
while True:
    # Captura um frame
    ret, frame = cap.read()
 
    if not ret:
        break
 
    # Exibe o video para o usuário
    #cv2.imshow('Video', frame)
 
    # Processamento do frame
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    inputs = processor(images=image, text=prompt, return_tensors="pt")
    out = model.generate(**inputs)
    generated_text = processor.decode(out[0], skip_special_tokens=True)
    traducao = tradutor.translate(generated_text)
    print(traducao)
    engine.say(traducao)
    engine.runAndWait()
 
    # Espera 5 segundos antes de capturar o próximo frame
    time.sleep(5)
 
    # Se a tecla 'a' for clicada encerra a captura
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break
 
# Libera a câmera e fecha a janela
cap.release()
cv2.destroyAllWindows()