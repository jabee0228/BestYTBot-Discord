import yt_dlp
import discord
from discord.ext import commands, tasks
import asyncio

async def download_audio(url= "", filename= "", output_dir ="", channel= ""):
    options = {
        'format': 'bestaudio',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': f'{output_dir}/{filename}.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '128',
        }],
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
            await channel.send("Download successful")
        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        await channel.send("Download failed")
        return False