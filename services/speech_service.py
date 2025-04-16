import speech_recognition as sr

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("🎙️ 말하세요... (듣는 중)")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='ko-KR')
        print(f"📝 인식된 내용: {text}")
        return text
    except sr.UnknownValueError:
        print("😕 음성을 인식하지 못했어요.")
        return None
    except sr.RequestError:
        print("⚠️ Google STT 서버에 연결할 수 없습니다.")
        return None
