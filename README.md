# Text to Speech Converter

This project is a simple Text to Speech (TTS) converter written in Python using the Google Text to Speech (gTTS) library. It allows users to input text and generate an audio file in various languages and accents.

## Features

- Converts text to speech using Google Text to Speech API
- Supports multiple languages: English, French, Portuguese, and Spanish
- Offers various accents for each supported language
- Saves the generated speech as an MP3 file

## Prerequisites

- Python 3.x
- gTTS (Google Text to Speech) library

## Usage

1. Run the Python script:
    ```sh
    python main.py
    ```
2. Follow the prompts to enter your text, select the language, and choose the accent.

3. The generated speech will be saved as an MP3 file named `audio.mp3` in the project directory.

## Supported Languages and Accents

### English (en)
- Australia (com.au)
- UK (co.uk)
- US (us)
- Canada (ca)
- India (co.in)
- Ireland (ie)
- South Africa (co.za)
- Nigeria (com.ng)

### French (fr)
- Canada (ca)
- France (fr)

### Portuguese (pt)
- Brazil (com.br)
- Portugal (pt)

### Spanish (es)
- Mexico (com.mx)
- Spain (es)
- US (us)

## Acknowledgments

- Thanks to the Google Text to Speech library for providing the TTS functionality.
- Inspired by the need for simple and customizable text-to-speech conversion tools.
- This program is entirely my own work.
