import speech_recognition as sr

def recognize_speech():
    # Create a recognizer object
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise levels
        recognizer.adjust_for_ambient_noise(source)

        # Listen for the user's input
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        # Use the Google Web Speech API to perform speech recognition
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Unable to recognize speech")
    except sr.RequestError as e:
        print("Error occurred during speech recognition:", str(e))

# Call the function to start voice recognition
recognize_speech()
