import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Record or input audio
with sr.Microphone() as source:
    print("Speak something...")
    audio = r.listen(source)

try:
    # Use Google's speech recognition API to convert audio to text
    text = r.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, could not understand audio.")
except sr.RequestError:
    print("Sorry, could not connect to the speech recognition service.")