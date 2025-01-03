import speech_recognition as sr

def recognize_speech_from_audio(file):
    # Initialize recognizer class (for recognizing the speech)
    recognizer = sr.Recognizer()

    # Reading the audio file as source
    # Listening the audio file and store in audio_text variable
    with sr.AudioFile(file) as source:
        audio_text = recognizer.record(source)

    try:
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        print(text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

if __name__ == "__main__":
    recognize_speech_from_audio('output.wav')