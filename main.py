import os
import time
from core.constant import AUDIO_FOLDER
from utilities.text_to_audio import convert_mp3_to_wav, convert_text_to_speech
from utilities.audio_to_text import convert_audio_to_text


def main(text: str = None):
    # Ensure audio folder exists
    os.makedirs(AUDIO_FOLDER, exist_ok=True)

    # Example text
    print(f"Original text: {text}")

    # Convert text to audio
    print("Converting text to audio...")
    audio_file_path = convert_text_to_speech(text)
    print(f"Audio saved to: {audio_file_path}")

    time.sleep(2)  # Wait for a moment to ensure the audio file is ready
    print_break_line()

    # Convert audio to WAV format if necessary
    if audio_file_path.endswith(".mp3"):
        print("Converting MP3 to WAV format...")
        audio_file_path = convert_mp3_to_wav(audio_file_path)
        print(f"Converted audio file path: {audio_file_path}")
        print_break_line()

    # Convert audio back to text
    print("Converting audio back to text...")
    try:
        recognized_text = convert_audio_to_text(audio_file_path)
        print(f"Recognized text => {recognized_text}")

    except Exception as e:
        print(f"Error during speech recognition: {e}")


def print_break_line():
    """Print a break line for better readability."""
    print("-" * 30)


if __name__ == "__main__":
    sample_text = (
        "Hello, this is a test of the text-to-speech and speech-to-text conversion."
    )
    main(sample_text)
