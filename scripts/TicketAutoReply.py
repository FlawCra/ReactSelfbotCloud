@React.listen()
async def on_guild_channel_create(channel):

    MESSAGE = "Hello, how can I help?" # Message to reply with
    TIME_TO_WAIT = 3 # Time to wait before replying to the ticket (seconds)

    try:
        await asyncio.sleep(3)
        if str(channel.name).startswith('ticket') and isinstance(channel, discord.TextChannel) and discord.Permissions(permissions=channel.permissions_for(channel.guild.get_member(channel.guild.me.id)).value).view_channel:
            print(fg.white + f'[{ fg.purple1 + datetime.now().strftime("%H:%M:%S") + fg.white}] TciketAutoReply | ' + fg.purple3 + f'Replying to {channel.name} in {TIME_TO_WAIT} seconds with "{MESSAGE}"')
            await asyncio.sleep(TIME_TO_WAIT)
            await channel.send(MESSAGE)
    except:
        pass