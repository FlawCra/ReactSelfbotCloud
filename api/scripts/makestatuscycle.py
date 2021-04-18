@React.command()
async def makestatuscycle(ctx, *, message):
	message_list = list(message)
	output = ""
	iteration = 1
	for letter in message_list:
		output = output + "".join(message_list[:iteration]) + "\n"
		try:
			if message_list[iteration] == " ":
				iteration += 2
			else:
				iteration += 1
		except:
			pass
		if iteration == len(message):
			break
	output = output + message + "\n"
	iteration = 1
	for letter in message_list:
		output = output + "".join(message_list[:len(message) - iteration]) + "\n"
		try:
			if message[len(message) - iteration - 1] == " ":
				iteration += 2
			else:
				iteration += 1
		except:
			pass
		if iteration == len(message):
			break
	await ctx.send(f"```\n{output}\n```")