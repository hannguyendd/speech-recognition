from speech_recognition import Recognizer, AudioFile


def convert_audio_to_text(wav_file):
    """
    Convert audio file to text using Google's speech recognition.

    Args:
        filename (str): Path to the audio file

    Returns:
        str: Recognized text from the audio file
    """
    recognizer = Recognizer()

    # open the file
    with AudioFile(wav_file) as source:
        # listen for the data (load audio to memory)
        audio_data = recognizer.record(source)
        # recognize (convert from speech to text)
        text = recognizer.recognize_google(audio_data)

        return text
