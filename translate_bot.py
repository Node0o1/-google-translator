import os
from dotenv import load_dotenv
import discord
import translator

load_dotenv()
TOKEN=os.getenv("DISCORD_TOKEN")

async def send_message(message, user_message):
    try:
        response=translator.check_supported_language_handle(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

async def send_lang_list(message):
    await message.channel.send(translator.list_language_handle())

async def display_help(message):
    await message.channel.send(translator.help_handle())

def bot_online_listener():
    intents=discord.Intents.default()
    intents.message_content=True
    client=discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} active...{chr(0x0a)}')

    @client.event
    async def on_message(message):
        if(message.author==client.user):return

        if(message.content[0]=='?'):
            username=str(message.author)
            user_message=str(message.content)
            channel=str(message.channel)

            print(f'FROM: {username}{chr(0x0a)}CHANNEL: ({channel}){chr(0x0a)}MESSAGE: "{user_message}"')

            if(str(user_message).lower().startswith('?help')):
                await display_help(message)
            elif(str(user_message).lower().startswith('?langs')):
                await send_lang_list(message)
            else:
                await send_message(message, user_message)

    client.run(TOKEN)