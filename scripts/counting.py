
countingchannels = {}
bot_user = None

@React.command()
async def countadd(ctx, channel: discord.TextChannel):
    global countingchannels
    global bot_user
    try:
        count = await ctx.bot.get_channel(channel.id).history(limit=1).flatten()
        count = int(count[0].content)
        bot_user = ctx.bot.user
    except:
        print(f"Failed to find count for channel {channel.name}")
    countingchannels[str(channel.id)] = str(count + 2)
    await channel.send(count + 1)


@React.listen()
async def on_message(message):
    global countingchannels
    global bot_user
    if str(message.channel.id) in countingchannels:
        if message.author != bot_user:
            if message.content.isdigit():
                count_test = int(countingchannels[str(message.channel.id)])
                if int(message.content) == count_test:
                    count = int(countingchannels[str(message.channel.id)])
                    count += 1
                    await message.channel.send(count)
                    count += 1
                    countingchannels[str(message.channel.id)] = str(count)