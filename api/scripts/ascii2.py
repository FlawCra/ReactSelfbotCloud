
@React.command()
async def ascii2(ctx, font, *, text):
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}+&font=' + font).text
    if len('```' + r + '```') > 2000:
        return
    await ctx.send(f"```{r}```")
    
    #list of fonts: http://artii.herokuapp.com/fonts_list