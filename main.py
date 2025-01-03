from record_audio import record_audio
from recognize_speech import recognize_speech_from_audio

def execute_command(command):
    if 'hello' in command:
        print("Hello! How can I help you?")
    elif 'time' in command:
        from datetime import datetime
        now = datetime.now()
        print("Current time is:", now.strftime("%H:%M:%S"))
    elif 'exit' in command:
        print("Exiting...")
        exit()
    else:
        print("Command not recognized.")

if __name__ == "__main__":
    record_audio('output.wav', duration=5)
    text = recognize_speech_from_audio('output.wav')
    if text:
        execute_command(text)