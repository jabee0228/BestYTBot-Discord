import discord
from discord.ext import commands
import music_download

def setup_commands(bot):
    @bot.tree.command(name="join", description="Make the bot join your voice channel")
    async def join(interaction: discord.Interaction):
        if interaction.user.voice:
            channel = interaction.user.voice.channel
            await channel.connect()
            await interaction.response.send_message(f"Joined voice channel: {channel.name}")
        else:
            await interaction.response.send_message("You need to join a voice channel first!", ephemeral=True)

    @bot.tree.command(name="play", description="Play audio")
    async def play(interaction: discord.Interaction, link: str):
        if interaction.guild.voice_client:
            if interaction.guild.voice_client.is_playing():
                interaction.guild.voice_client.stop()
            channel = interaction.channel
            await interaction.response.send_message("Preparing to play music")
            await music_download.download_audio(url=link, filename="temp",
                                                output_dir="../music_temp", channel=channel)

            source = discord.FFmpegPCMAudio("../music_temp/temp.mp3")
            interaction.guild.voice_client.play(source)
            #await interaction.followup.send("Now playing music!")
            # avoid respond over 10s TimeoutError
        else:
            await interaction.response.send_message("Please let the bot join a voice channel first, use `/join` command!", ephemeral=True)

    @bot.tree.command(name="stop", description="Stop playing audio")
    async def stop(interaction: discord.Interaction):
        if interaction.guild.voice_client and interaction.guild.voice_client.is_playing():
            interaction.guild.voice_client.stop()
            await interaction.response.send_message("Stopped playing audio!")
        else:
            await interaction.response.send_message("No audio is playing!", ephemeral=True)

    @bot.tree.command(name="pause", description="Pause playing audio")
    async def pause(interaction: discord.Interaction):
        if interaction.guild.voice_client and interaction.guild.voice_client.is_playing():
            interaction.guild.voice_client.pause()
            await interaction.response.send_message("Paused playing audio!")
        elif interaction.guild.voice_client and interaction.guild.voice_client.is_paused():
            await interaction.response.send_message("Audio is already paused!", ephemeral=True)
        else:
            await interaction.response.send_message("No audio is playing!", ephemeral=True)

    @bot.tree.command(name="continue", description="Continue playing paused audio")
    async def continue_playing(interaction: discord.Interaction):
        if interaction.guild.voice_client and interaction.guild.voice_client.is_paused():
            interaction.guild.voice_client.resume()
            await interaction.response.send_message("Resumed playing audio!")
        elif interaction.guild.voice_client and interaction.guild.voice_client.is_playing():
            await interaction.response.send_message("Audio is already playing!", ephemeral=True)
        else:
            await interaction.response.send_message("No audio is paused!", ephemeral=True)
    @bot.tree.command(name="leave", description="Make the bot leave the voice channel")
    async def leave(interaction: discord.Interaction):
        voice_client = interaction.guild.voice_client
        if voice_client:
            if voice_client.is_playing():
                voice_client.stop()
                await interaction.response.send_message("Stopped playing audio, preparing to leave the voice channel!")
                await interaction.followup.send("Bot left the voice channel!")
            else:
                await interaction.response.send_message("Bot left the voice channel!")
            await voice_client.disconnect()
        else:
            await interaction.response.send_message("Bot is not in a voice channel!", ephemeral=True)

    @bot.tree.command(name="add", description="add YouTube web link")
    async def add(interaction: discord.Interaction, link: str):
        channel = interaction.channel
        await interaction.response.send_message("Downloading")
        await music_download.download_audio(url=link, filename="temp",
                       output_dir="../music_temp", channel=channel)

        source = discord.FFmpegPCMAudio("../music_temp/temp.mp3")
        interaction.guild.voice_client.play(source)
        await interaction.followup.send("Now playing audio!")

'''
@bot.tree.command(name="say", description="Make the bot say the specified text")
    async def say(interaction: discord.Interaction, message: str):
        await interaction.response.send_message(f"You said: {message}")
'''
