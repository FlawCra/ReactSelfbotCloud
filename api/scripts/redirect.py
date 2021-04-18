@React.command()
async def redirect(ctx, *, url):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=int(json.load(open(f'./Themes/{json.load(open("config.json"))["theme"]}.json'))['embed_color'].replace('#', '0x'), 0), title='Redirect Checker')
        embed.set_thumbnail(url=json.load(open(f'./Themes/{json.load(open("config.json"))["theme"]}.json'))['embed_thumbnail_url'])
        embed.set_footer(text=json.load(open(f'./Themes/{json.load(open("config.json"))["theme"]}.json'))['embed_footer'], icon_url=json.load(open(f'./Themes/{json.load(open("config.json"))["theme"]}.json'))['embed_footer_url'])
        result = json.loads(requests.get(f"https://api.redirect-checker.net/?url={url}&timeout=5&maxhops=10&meta-refresh=1&format=json").text)
        for i in range(len(result['data'])):
            embed.add_field(name=f"__Redirect #{i + 1}__", value=f"{result['data'][i]['request']['info']['url']}", inline=False)
        await ctx.send(embed=embed, delete_after=json.load(open('config.json'))['delete_timeout'])
    except Exception as e:
        await ctx.send(f"Error: {e}")