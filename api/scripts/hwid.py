@React.command()
async def hwid(ctx):
    hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    print('HWID: ' + hwid)