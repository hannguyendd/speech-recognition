# Speech Recognition Project

A Python-based speech recognition system that converts text to speech and speech back to text, demonstrating a complete audio processing pipeline.

## Features

- **Text-to-Speech (TTS)**: Convert text to audio using Google Text-to-Speech (gTTS)
- **Speech-to-Text (STT)**: Convert audio files back to text using Google Speech Recognition
- **Audio Format Conversion**: Convert MP3 files to WAV format for compatibility
- **Unique File Naming**: Uses Snowflake ID generator for unique audio file names
- **Modular Architecture**: Clean separation of concerns with utility modules

## Project Structure

```
speech-recognition/
├── main.py                 # Main application entry point
├── pyproject.toml         # Project configuration and dependencies
├── README.md              # Project documentation
├── core/
│   └── constant.py        # Application constants
├── utilities/
│   ├── text_to_audio.py   # Text-to-speech functionality
│   └── audio_to_text.py   # Speech-to-text functionality
└── audio/                 # Generated audio files (auto-created)
    ├── mp3/              # MP3 audio files
    └── wav/              # WAV audio files
```

## Requirements

- Python 3.12 or higher
- Internet connection (for Google TTS and Speech Recognition services)

## Dependencies

- `gtts>=2.5.4` - Google Text-to-Speech
- `pydub>=0.25.1` - Audio manipulation
- `pyttsx3` - Text-to-speech engine
- `snowflake-id` - Unique ID generation
- `soundfile` - Audio file handling
- `speechrecognition>=3.14.3` - Speech recognition

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd speech-recognition
```

2. Install dependencies using uv:

```bash
uv sync
```

## Usage

### Basic Usage

Run the main script with the default sample text:

```bash
python main.py
```

### Custom Text

Modify the `sample_text` variable in `main.py` or call the `main()` function with your own text:

```python
from main import main

main("Your custom text here")
```

### Using Individual Components

#### Text to Speech:

```python
from utilities.text_to_audio import convert_text_to_speech

audio_path = convert_text_to_speech("Hello, world!")
print(f"Audio saved to: {audio_path}")
```

#### Speech to Text:

```python
from utilities.audio_to_text import convert_audio_to_text

text = convert_audio_to_text("path/to/audio.wav")
print(f"Recognized text: {text}")
```

#### MP3 to WAV Conversion:

```python
from utilities.text_to_audio import convert_mp3_to_wav

wav_path = convert_mp3_to_wav("path/to/audio.mp3")
print(f"WAV file saved to: {wav_path}")
```

## How It Works

1. **Text Input**: The application takes text input (default sample or custom)
2. **Text-to-Speech**: Converts text to MP3 audio using Google TTS
3. **Format Conversion**: Converts MP3 to WAV format for better compatibility
4. **Speech Recognition**: Uses Google Speech Recognition to convert audio back to text
5. **Output Comparison**: Displays both original and recognized text

## Configuration

Constants can be modified in `core/constant.py`:

- `AUDIO_FOLDER`: Base directory for audio files
- `MP3_FOLDER`: Directory for MP3 files
- `WAV_FOLDER`: Directory for WAV files
- `FILE_EXTENSION`: Default file extension for audio files

## Error Handling

The application includes error handling for:

- Audio file conversion failures
- Speech recognition errors
- Missing dependencies
- File system operations

## Limitations

- Requires internet connection for Google services
- Audio quality depends on TTS service
- Recognition accuracy may vary with audio quality
- Currently supports English by default (can be configured)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source. Please check the license file for details.

## Troubleshooting

### Common Issues

1. **Import Error for pydub**: Install ffmpeg

   ```bash
   # macOS
   brew install ffmpeg

   # Ubuntu/Debian
   sudo apt update && sudo apt install ffmpeg

   # Windows
   # Download from https://ffmpeg.org/download.html
   # Or use Chocolatey:
   choco install ffmpeg

   # Or use winget:
   winget install "FFmpeg (Essentials Build)"
   ```

2. **Internet Connection**: Ensure stable internet for Google services

3. **Audio Permissions**: Make sure the application has permission to create files in the audio directory

## Future Enhancements

- Support for multiple languages
- Real-time audio processing
- GUI interface
- Batch processing capabilities
- Local TTS/STT alternatives
- Audio quality optimization
