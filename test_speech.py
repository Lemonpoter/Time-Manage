from services.speech_service import recognize_speech_from_mic

if __name__ == '__main__':
    result = recognize_speech_from_mic()
    if result:
        print("🎉 음성 인식 성공:", result)
    else:
        print("😕 음성 인식에 실패했습니다.")
