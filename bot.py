import discord
import os
from discord.ext import commands

status = ['Bep bop','.help']
bot_key = 'NzUzNzQ5MDcxNTMzMDQ3ODE5.X1qthg.8cGJzt9VfkRj8I1Y80iz5-1Dzi8'
PREFIX = 's!'

client = commands.Bot(command_prefix = PREFIX) # Command prefix example '.ping'
client.remove_command('help')

# Bot is ON message
@client.event	
async def on_ready():
	await client.change_presence(status=discord.Status.idle, activity=discord.Game('.help'))
	print('Bot is online.')


# Load, unload and refresh COGS
@client.command()
async def load(ctx, extension):
	# Load extensions from cog
	client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
	# Unload extensions from cog
	client.unload_extension(f'cogs.{extension}')


@client.command()
async def reload(ctx, extension):
	# Refresh cog extensions 
	client.unload_extension(f'cogs.{extension}')
	client.load_extension(f'cogs.{extension}')


@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        title=':clipboard: **Tabla de comandos** :clipboard:',
        description=f'**Prefijo:** {PREFIX}\n'
        			f'**Comandos para el usuario: **\n'
        			f'\n'
        			f':ping_pong: {PREFIX}ping - Latencia del servidor.\n'
        			f':8ball: {PREFIX}8ball [q] - Responde preguntas de si o no. \n'
        			f':level_slider: {PREFIX}random [x][y] - Numero random entre x e y.\n'
        			f':rainbow_flag: {PREFIX}gay [none/user] - Porcentaje de gay del usuario.\n'
        			f':eggplant:      {PREFIX}mide [None/user] - Cuanto le mide al usuario.\n',
    	colour = discord.Colour.blue())
    await ctx.send(embed=embed)


# Error message command
@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send(f'No existe ese comando. Mas info {PREFIX}help') 


# Loop through cogs folder, searchs for .py scripts
for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')


client.run(str(bot_key))