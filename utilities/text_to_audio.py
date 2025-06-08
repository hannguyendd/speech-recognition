from gtts import gTTS
from snowflake import SnowflakeGenerator
from core.constant import FILE_EXTENSION, MP3_FOLDER, WAV_FOLDER
from pydub import AudioSegment


def convert_text_to_speech(text, lang="en", worker_id=42, folder=MP3_FOLDER):
    """
    Convert text to audio and save it to a file.

    Args:
        text (str): The text to convert to speech
        lang (str, optional): Language for speech. Defaults to "en".
        worker_id (int, optional): Worker ID for snowflake generator. Defaults to 42.

    Returns:
        str: Path to the saved audio file
    """
    tts = gTTS(text, lang=lang)
    id_generator = SnowflakeGenerator(worker_id)
    file_path = f"{folder}/{next(id_generator)}{FILE_EXTENSION}"
    tts.save(file_path)

    return file_path


def convert_mp3_to_wav(mp3_file_path, output_folder=WAV_FOLDER):
    """
    Convert an MP3 file to WAV format.

    Args:
        mp3_file_path (str): Path to the MP3 file

    Returns:
        str: Path to the converted WAV file
    """
    try:
        sound = AudioSegment.from_mp3(mp3_file_path)
        file_name = mp3_file_path.split("/")[-1].replace(FILE_EXTENSION, ".wav")
        wav_file_path = f"{output_folder}/{file_name}"

        sound.export(wav_file_path, format="wav")

        return wav_file_path
    except ImportError:
        print("Please install pydub: pip install pydub")
        return None
    except Exception as e:
        print(f"Error converting {mp3_file_path} to WAV: {e}")
        return None
