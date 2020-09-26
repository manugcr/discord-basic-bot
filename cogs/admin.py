import discord
from discord.ext import commands

class admin(commands.Cog):
	def __init__(self, client):
		self.client = client

	# Clear chat n+1 amount
	@commands.command()
	@commands.has_permissions(manage_messages = True)
	async def clear(self, ctx, amount = 5):
		await ctx.channel.purge(limit = amount + 1)


	commands.command()
	@commands.has_permissions(administrator = True)
	async def kick(self, ctx, user: discord.Member, *, reason=None):
		await user.kick(reason=reason)
		await ctx.send(f"{user} kicked.")	


def setup(client):
	client.add_cog(admin(client))