#!/usr/bin/env python3
import speech_recognition as sr
import pyttsx3
from googletrans import Translator

# Configurar el motor de texto a voz
engine = pyttsx3.init()

# Obtener las voces disponibles
voices = engine.getProperty('voices')

# Mostrar las voces disponibles en el sistema
for i, voice in enumerate(voices):
    print(f"Voice {i}: {voice.name}")

# Seleccionar una voz en español, en este caso "Eddy (Español (España))"
engine.setProperty('voice', voices[20].id)  # Cambia el índice según tu preferencia

# Establecer la velocidad (más bajo para más lento)
engine.setProperty('rate', 125)  # Ajusta el número para hacerlo más lento o rápido

# Establecer el volumen (opcional)
engine.setProperty('volume', 1)  # El valor va de 0.0 a 1.0

# Función para traducir el texto
def traducir(audio):
    # Crear el traductor
    traductor = Translator()

    # Dividir el audio en texto
    texto = audio.lower()

    # Obtener los idiomas (en este caso, se toman como ejemplos: español a inglés)
    idioma_origen = "es"
    idioma_destino = "en"
    
    # Traducir el texto
    resultado = traductor.translate(texto, src=idioma_origen, dest=idioma_destino)
    
    # Devolver el resultado traducido
    engine.say(f"Texto traducido: {resultado.text}")
    engine.runAndWait()

# Función para reconocer el habla
def reconocer_audio():
    # Inicializar el reconocedor de audio
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Por favor, habla ahora...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        # Usar Google Speech Recognition para convertir el audio en texto
        texto = r.recognize_google(audio, language="es-ES")
        print(f"Texto reconocido: {texto}")
        traducir(texto)
    except sr.UnknownValueError:
        print("No pude entender lo que dijiste.")
        engine.say("No pude entender lo que dijiste.")
        engine.runAndWait()
    except sr.RequestError:
        print("Error al conectar con el servicio de reconocimiento.")
        engine.say("Error al conectar con el servicio de reconocimiento.")
        engine.runAndWait()

# Ejecutar el reconocimiento de audio
reconocer_audio()
