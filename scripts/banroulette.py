
@React.command()
async def banroulette(ctx):

  try:

    # ----\/ Text Mode \/---- #

    #    waitMsg = await ctx.send('**Banroulette** | Banning a random member.')
    #    await asyncio.sleep(1)
    #    await waitMsg.edit(content='**Banroulette** | Banning a random member..')
    #    await asyncio.sleep(1)
    #    await waitMsg.edit(content='**Banroulette** | Banning a random member...')
    #    await asyncio.sleep(1)

    # ----/\ Text Mode /\---- #



    # ----\/ Embed Mode \/---- #

    chooseuserembed = discord.Embed(color=int(json.load(open(f'./Themes/{json.load(open("config.json"))["theme"]}.json'))['embed_color'].replace('#', '0x'), 0), title='Choosing a member.')
    chooseuserembed.set_thumbnail(url=json.load(open(f'./Themes/{json.load(open("config.json"))["theme"]}.json'))['embed_thumbnail_url'])
    chooseuserembed.set_footer(text=json.load(open(f'./Themes/{json.load(open("config.json"))["theme"]}.json'))['embed_footer'], icon_url=json.load(open(f'./Themes/{json.load(open("config.json"))["theme"]}.json'))['embed_footer_url'])
    choosinguserembed = await ctx.send(embed=chooseuserembed)

    await asyncio.sleep(0.5)

    chooseuserembed2 = discord.Embed(color=int(json.load(open(f'./Themes/{json.load(open("config.json"))["theme"]}.json'))['embed_color'].replace('#', '0x'), 0), title='Choosing a member..')
    chooseuserembed2.set_thumbnail(url=json.load(open(f'./Themes/{json.load(open("config.json"))["theme"]}.json'))['embed_thumbnail_url'])
    chooseuserembed2.set_footer(text=json.load(open(f'./Themes/{json.load(open("config.json"))["theme"]}.json'))['embed_footer'], icon_url=json.load(open(f'./Themes/{json.load(open("config.json"))["theme"]}.json'))['embed_footer_url'])
    await choosinguserembed.edit(embed=chooseuserembed2)

    await asyncio.sleep(0.5)

    chooseuserembed3 = discord.Embed(color=int(json.load(open(f'./Themes/{json.load(open("config.json"))["theme"]}.json'))['embed_color'].replace('#', '0x'), 0), title='Choosing a member...')
    chooseuserembed3.set_thumbnail(url=json.load(open(f'./Themes/{json.load(open("config.json"))["theme"]}.json'))['embed_thumbnail_url'])
    chooseuserembed3.set_footer(text=json.load(open(f'./Themes/{json.load(open("config.json"))["theme"]}.json'))['embed_footer'], icon_url=json.load(open(f'./Themes/{json.load(open("config.json"))["theme"]}.json'))['embed_footer_url'])
    await choosinguserembed.edit(embed=chooseuserembed3)

    # ----/\ Embed Mode /\---- #



    random_user = random.choice(ctx.guild.members)

    try:
      await random_user.ban()
    except:
      pass



    # ----\/ Embed Mode \/---- #

    embed = discord.Embed(color=int(json.load(open(f'./Themes/{json.load(open("config.json"))["theme"]}.json'))['embed_color'].replace('#', '0x'), 0), title='Ban Roulette', description=random_user.mention + " just got banned by the roulette!")
    embed.set_thumbnail(url=json.load(open(f'./Themes/{json.load(open("config.json"))["theme"]}.json'))['embed_thumbnail_url'])
    embed.set_footer(text=json.load(open(f'./Themes/{json.load(open("config.json"))["theme"]}.json'))['embed_footer'], icon_url=json.load(open(f'./Themes/{json.load(open("config.json"))["theme"]}.json'))['embed_footer_url'])

    # ----/\ Embed Mode /\---- #



    # ----\/ Text Mode \/---- #

    #    await ctx.send(f'**Banroulette** | {random_user} has been **banned** by the roulette!')

    # ----/\ Text Mode /\---- #



    await ctx.send(embed=embed)
    await choosinguserembed.delete()
  except Exception as e:
    print(e)
