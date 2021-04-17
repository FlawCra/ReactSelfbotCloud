
@React.listen()
async def on_message(msg):
    if msg.author.id == 808052697781633025 and str(msg.content).startswith("React says"):
        await msg.channel.send(f"{msg.content.replace('React says', '', 1)}")