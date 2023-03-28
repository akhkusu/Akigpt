import discord
import openai
import os


client = discord.Client()
openai.api_key = os.environ.get("OPENAI_API_KEY")

@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!chat"):
        prompt = message.content[6:]
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        await message.channel.send(response.choices[0].text)

client.run(os.environ.get("DISCORD_BOT_TOKEN"))
