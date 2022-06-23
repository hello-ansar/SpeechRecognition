import speech_recognition



def record_and_recognize_audio(*args: tuple):
    with microphone:
        recognized_data = ""

        # қоршаған ортадағы дыбысты өңдеу
        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            print("Listening...")
            audio = recognizer.listen(microphone, 5, 5)

        except speech_recognition.WaitTimeoutError:
            print("Can you check if your microphone is on, please?")
            return

        # использование online-распознавания через Google
        try:
            print("Started recognition...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass

        # в случае проблем с доступом в Интернет происходит выброс ошибки
        except speech_recognition.RequestError:
            print("Check your Internet Connection, please")

        return recognized_data



if __name__ == "__main__":

    # дауысты еңгізу мен тану құралдарын инициализалиялау
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    while True:
        # дауыс жазбасын қосып танылған сөдерді кезектеп шығару
        voice_input = record_and_recognize_audio()
        print(voice_input)


