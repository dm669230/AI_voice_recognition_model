import speech_recognition as sr
import pyaudio as pu


def voice_recognize():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        try:
            r.adjust_for_ambient_noise(source,duration=5)
            print("say something >>()<< ")
            audio = r.listen(source,phrase_time_limit=3)
            if audio:
                print("Recognizing your voice...")
                text = r.recognize_google(audio)
                return f"You said : {text}"
                
            else:
                return "No speech detected. Say something.."
        except :
            return "there is no voice detected"
        
print(voice_recognize())