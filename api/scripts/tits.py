@React.command()
async def tits(ctx):
    blacklisted_words = ['redgifs', 'gifv']
    whitelisted_words = ['gif', 'png', 'jpg', 'jpeg']
    subreddits = ['boobs', 'tits', 'boobies', 'stacked', 'bigboobsgw', 'ghostnipples', 'hugeboobs']
    response = requests.get(f'https://www.reddit.com/r/{random.choice(subreddits)}/hot.json?limit=50', headers={'User-agent': ''})
    res = response.json()
    random_post = res['data']['children'][random.randint(0, 50)]
    post_title = random_post['data']['title']
    post_url = random_post['data']['url']
    post_permalink = random_post['data']['permalink']
    if any(word in post_url for word in blacklisted_words):
        await ctx.send(f'\uD83D\uDD1E `{post_title}`\n\n{post_url}\n\n\uD83D\uDC64 `Made by wizpizz`')
    elif any(word in post_url for word in whitelisted_words):
        embed = discord.Embed(title=post_title, url=f'https://www.reddit.com/{post_permalink}', color=0x202225)
        embed.set_image(url=post_url)
        embed.set_footer(text=f'Made by wizpizz')
        await ctx.send(embed=embed)
    else:
        await tits(ctx)