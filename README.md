# Voice Translator Assistant

An interactive voice assistant for translation that captures speech, converts it to text, translates it to another language, and then provides the translated result as speech. This project uses the `speech_recognition`, `pyttsx3`, and `googletrans` libraries to achieve speech recognition and text-to-speech translation.

## Features

- **Speech Recognition**: Captures and converts spoken audio to text in Spanish.
- **Text Translation**: Translates the recognized text from Spanish to English.
- **Text-to-Speech**: Reads out the translated text in voice using a speech synthesis engine.

## Requirements

- `speech_recognition`
- `pyttsx3`
- `googletrans==4.0.0-rc1`
- `pyaudio` (dependency for speech recognition)

To install these dependencies, use the following command:

```bash
pip install speech_recognition pyttsx3 googletrans==4.0.0-rc1 pyaudio

To run the program:

```bash
git clone https://github.com/yourusername/Voice-Translator-Assistant.git
cd Voice-Translator-Assistant

```bash
pip install -r requirements.txt

```bash
python3 prueba1.py
