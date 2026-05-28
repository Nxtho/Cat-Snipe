import discord
import asyncio
import random

# --- CONFIG ---
TOKEN = "UR DISCORD BOT TOKEN HERE DO NOT SHARE THIS WITH ANYONE"
CHANNEL_ID =  # Replace with the numeric ID of the cat-catch channel
CAT_BOT_ID = 966695034340663367  # Replace with Cat Bot's numeric user ID (right-click -> Copy ID)
# --- END CONFIG ---

# How it works:
# Someone types "cat" → bot sees it and also types "cat" shortly after.
# This looks natural — like you saw someone else try and jumped in too.
# Triggering off other users (not Cat Bot's result) means your response
# appears alongside theirs, not instantly after a catch announcement.

DELAY_MIN = 1.1 # Minimum delay before responding, in seconds. Too low and it looks like a bot.
DELAY_MAX = 3.5 # Maximum delay before responding, in seconds. Too high and you might miss the catch window.

client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user} ({client.user.id})")
    print(f"Watching channel ID: {CHANNEL_ID}")
    print("Sniping cats...")

@client.event
async def on_message(message):
    if message.channel.id != CHANNEL_ID:
        return

    # Only act on Cat Bot's messages
    if message.author.id != CAT_BOT_ID:
        return

    # Only trigger on spawn messages, ignore catch results
    if "has appeared!" not in message.content:
        return

    print(f"Cat spawned: {message.content[:80]!r} — sniping...")
    delay = random.uniform(DELAY_MIN, DELAY_MAX)
    print(f"Waiting {delay:.1f}s...")
    await asyncio.sleep(delay)

    await message.channel.send("cat")
    print("Sent 'cat'!")

client.run(TOKEN)
