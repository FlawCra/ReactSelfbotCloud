@React.listen()
async def on_message(message):
    if message.author.id == 270904126974590976:
        if (message.content.startswith('Type `') or message.content.startswith('Attack the boss by typing `')) and message.content.endswith('`'):
            await asyncio.sleep(3)
            await message.channel.send(((re.search('`(.+?)`', message.content).group(1)).encode('ascii', 'ignore')).decode('utf-8'))