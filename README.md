# BestYTBot-Discord

A Discord music bot that can download and play audio from YouTube links directly in voice channels.

## Features

- 🎵 Play audio from YouTube links
- ⏸️ Pause and resume playback
- ⏹️ Stop audio playback
- 🔗 Join and leave voice channels
- 📥 Download audio files locally
- 🎧 High-quality audio streaming (128kbps MP3)

## Commands

The bot uses Discord's slash commands for easy interaction:

| Command | Description |
|---------|-------------|
| `/join` | Make the bot join your current voice channel |
| `/play <link>` | Download and play audio from a YouTube URL |
| `/add <link>` | Add a YouTube link to download and play |
| `/pause` | Pause the currently playing audio |
| `/continue` | Resume paused audio |
| `/stop` | Stop audio playback |
| `/leave` | Make the bot leave the voice channel |

## Prerequisites

- Python 3.7 or higher
- FFmpeg installed on your system
- Discord Bot Token

### Installing FFmpeg

**Windows:**
1. Download FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Extract and add to your system PATH

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/BestYTBot-Discord.git
   cd BestYTBot-Discord
   ```

2. **Install required Python packages:**
   ```bash
   pip install discord.py yt-dlp
   ```

3. **Set up your Discord Bot:**
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application and bot
   - Copy the bot token
   - Enable the following bot permissions:
     - Send Messages
     - Use Slash Commands
     - Connect (Voice)
     - Speak (Voice)

4. **Configure the bot:**
   - Open `config/config.json`
   - Replace the TOKEN value with your bot's token:
   ```json
   {
       "TOKEN": "your_bot_token_here"
   }
   ```

5. **Invite the bot to your server:**
   - In the Discord Developer Portal, go to OAuth2 > URL Generator
   - Select "bot" and "applications.commands" scopes
   - Select the required permissions (Send Messages, Use Slash Commands, Connect, Speak)
   - Use the generated URL to invite the bot to your server

## Usage

1. **Start the bot:**
   ```bash
   cd src
   python main.py
   ```

2. **In Discord:**
   - Join a voice channel
   - Use `/join` to make the bot join your channel
   - Use `/play <youtube_url>` to play music
   - Control playback with `/pause`, `/continue`, `/stop`
   - Use `/leave` when done

## Project Structure

```
BestYTBot-Discord/
├── config/
│   └── config.json          # Bot configuration (token)
├── music_temp/              # Temporary audio files
├── src/
│   ├── main.py             # Main entry point
│   ├── bot.py              # Bot class definition
│   ├── commands.py         # Slash command definitions
│   ├── music_download.py   # YouTube download functionality
│   └── playlist.py         # Playlist features (if implemented)
├── LICENSE
└── README.md
```

## Dependencies

- **discord.py**: Discord API wrapper for Python
- **yt-dlp**: YouTube downloader library
- **FFmpeg**: Audio processing (external dependency)

## Troubleshooting

### Common Issues

1. **"Bot is not responding to commands"**
   - Make sure the bot has the "Use Slash Commands" permission
   - Ensure commands are synced (happens automatically on startup)

2. **"Audio not playing"**
   - Verify FFmpeg is installed and in your system PATH
   - Check that the bot has "Connect" and "Speak" permissions in voice channels

3. **"Download failed"**
   - YouTube link might be invalid or region-restricted
   - Check your internet connection
   - Some videos may have download restrictions

4. **"Permission denied errors"**
   - Ensure the `music_temp` directory is writable
   - Check file permissions for the project directory

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This bot is for educational purposes. Make sure to comply with YouTube's Terms of Service and respect copyright laws when using this bot. The developers are not responsible for any misuse of this software.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.
