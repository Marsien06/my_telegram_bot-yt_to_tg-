#!/usr/bin/env python3
import sys
import os
import asyncio
import yt_dlp
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")     
CHANNEL_ID = "@muyzkaa"
AUDIO_FILE = "muyzkaa.mp3"

def download_audio(url: str):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "muyzkaa.%(ext)s",
        "quiet": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

async def send_audio_to_channel():
    bot = Bot(token=BOT_TOKEN)
    with open(AUDIO_FILE, "rb") as audio:
        await bot.send_audio(
            chat_id=CHANNEL_ID,
            audio=audio,
            caption="bon voyage",
        )

def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable not set")

    url = sys.argv[1] if len(sys.argv) > 1 else input("Enter YouTube URL: ").strip()

    download_audio(url)
    asyncio.run(send_audio_to_channel())

    if os.path.exists(AUDIO_FILE):
        os.remove(AUDIO_FILE)

if __name__ == "__main__":
    main()
