import discord
import random
from discord.ext import commands

class misc(commands.Cog):
	
	def __init__(self, client):
		self.client = client


	# Ping discord server with bot client
	@commands.command()
	async def ping(self, ctx):
		embed=discord.Embed(title='Pong! :ping_pong:',
							description=f'{round(self.client.latency * 1000)}ms' , 
							colour=discord.Colour.blue())
		await ctx.send(embed=embed)


	# 8ball Q&A style. Only yes or no questions.
	@commands.command(aliases = ['8ball'])
	async def ball8(self, ctx, *, question):
		responses = ["Es verdad.",
					 "Es asi, esta decidido.",
					 "Sin dudarlo.",
					 "Si, definitivamente.",
					 "Podes confiar en eso.",
					 "Por como lo veo, si.",
					 "Lo mas probable.",
					 "Tiene buena pinta.",
					 "Si.",
					 "Signs point to yes.",
					 "Respuesta confusa, pregunta mas tarde.",
					 "Preguntame mas tarde.",
					 "Mejor no te lo digo ahora.",
					 "No puedo saberlo en este momento.",
					 "Concentrate y pregunta devuelta..",
					 "No cuentes con eso.",
					 "No.",
					 "Mis conocimientos dicen que no.",
					 "No tiene buena pinta.",
					 "Muy poco probable."]
		embed = discord.Embed(title=f'{question} :8ball:',
							description=f'{random.choice(responses)}',
							colour=discord.Colour.blue())
		await ctx.send(embed=embed)


	# Random number between two integers.
	@commands.command(aliases=['random', 'rand'])
	async def random_num(self, ctx, start=0, end=1):
		max_num = int(max(start, end))
		min_num = int(min(start, end))

		embed = discord.Embed(title =f'Random ({min_num}, {max_num}) :level_slider:' ,
							description =f'{random.randint(min_num, max_num)}' ,
							colour = discord.Colour.blue())

		await ctx.send(embed=embed)

	@random_num.error
	async def random_error(self, ctx, error):
		await ctx.send('Tenes que especificar dos numeros.')
	

	# Gay rate 0-100%
	@commands.command(aliases=['gay', 'howgay'])
	async def gayrate(self, ctx, member: discord.Member = None):
		gaynum = random.randint(0, 100)
		if member == None:
			embed = discord.Embed(title = 'Gay rate :rainbow_flag:',
								description = f'{ctx.message.author.mention} es {gaynum}% gay.',
								colour = discord.Colour.blue())
			await ctx.send(embed=embed)
		else:
			embed = discord.Embed(title = 'Gay rate :rainbow_flag:',
								description = f'{member.mention} es {gaynum}% gay.',
								colour = discord.Colour.blue())
			await ctx.send(embed=embed)

	@gayrate.error
	async def gay_error(self, ctx, error):
		await ctx.send('Usuario incorrecto.')


	# Dick size 1-30cm
	@commands.command(aliases=['mide'])
	async def memide(self, ctx, member: discord.Member = None):
		size = random.randint(0, 30)
		if member == None:
			embed = discord.Embed(title='Me mide :eggplant:', 
								description=f'A {ctx.message.author.mention} le mide {size}cm',
								colour = discord.Colour.blue())
			await ctx.send(embed=embed)
		else:
			embed = discord.Embed(title = 'Le mide :eggplant:',
								description = f'A {member.mention} le mide {size}cm',
								colour = discord.Colour.blue())
			await ctx.send(embed=embed)

	@memide.error
	async def memide_erorr(self, ctx, error):
		await ctx.send('Usuario incorrecto.')

def setup(client):
	client.add_cog(misc(client))