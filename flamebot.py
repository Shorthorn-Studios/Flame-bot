# Work with Python 3.6
import discord

TOKEN = 'NjE3ODQ2MTkyMDYzMzgxNTQ2.XWxESw.VBm5-xbJwwWd3haj6hhmxb9aG9I'
client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('&test2'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('&info'):
        msg = 'Flame Bot is developed by ``Ryan In The Horizon#1827``. Join the Support Discord at https://discord.gg/HUZEd63!'.format(message)
        await client.send_message(message.channel, msg)
