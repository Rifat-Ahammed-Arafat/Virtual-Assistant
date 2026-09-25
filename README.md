# Virtual Assistant

A voice-controlled AI assistant that listens for commands and performs web browsing and music playback tasks.

## Features

- 🎤 **Voice Recognition** - Listens for commands using Google Speech API
- 🌐 **Web Browsing** - Opens popular websites on your browser
- 🎵 **Music Playback** - Play songs from the music library
- 🔊 **Text-to-Speech** - Responds with voice feedback

## Requirements

- Python 3.12
- `speech_recognition` library
- `pyttsx3` library
- `pyaudio` library (for microphone input)
- Active internet connection

## Installation

1. Install required dependencies:
   ```bash
   pip install speech_recognition pyttsx3 pyaudio
   ```

2. Make sure your microphone is properly connected and configured.

## Usage

1. Run the program:
   ```bash
   python main.py
   ```

2. Wait for the message "Yes, I am listening..."

3. Say **"hello"** to wake up the assistant

4. After hearing "Yes, how can I assist you?", give a command:

### Available Commands

#### Web Browsing
- "open google" - Opens Google
- "open youtube" - Opens YouTube
- "open facebook" - Opens Facebook
- "open instagram" - Opens Instagram
- "open messenger" - Opens Messenger
- "open ai" - Opens ChatGPT
- "open github" - Opens GitHub
- "open linkedin" - Opens LinkedIn
- "open twitter" - Opens Twitter
- "open reddit" - Opens Reddit
- "open stack overflow" - Opens Stack Overflow
- "open wikipedia" - Opens Wikipedia
- "open spotify" or "play music" - Opens Spotify

#### Music Playback (20+ Songs Available)
- "play shape of you" - Ed Sheeran
- "play perfect" - Ed Sheeran
- "play slay" - Eternxlkz
- "play blinding lights" - The Weeknd
- "play levitating" - Dua Lipa
- "play heat waves" - Glass Animals
- "play anti hero" - Taylor Swift
- "play bohemian rhapsody" - Queen
- "play stairway to heaven" - Led Zeppelin
- "play imagine" - John Lennon
- "play yesterday" - The Beatles
- "play smells like teen spirit" - Nirvana
- "play hotel california" - Eagles
- "play sweet home alabama" - Lynyrd Skynyrd
- "play wonderwall" - Oasis
- "play somebody to love" - Queen
- "play tik tok" - Kesha
- "play uptown funk" - Bruno Mars & Mark Ronson
- "play good as hell" - Lizzo
- "play stay" - Justin Bieber & Kid LAROI

#### Other Commands
- "exit" or "quit" - Exits the program

## File Structure

- `main.py` - Main application with voice recognition and command processing
- `musicLibrary.py` - Dictionary of available songs and their links
- `README.md` - Project documentation

## Notes

- The assistant requires an active microphone for voice input
- Internet connection is required for web browsing and music playback
- Speech recognition accuracy depends on audio quality and background noise
