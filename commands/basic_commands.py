import discord
from discord.ext import commands
from utils.channel_manager import ChannelManager

class BasicCommands(commands.Cog):
    """Basic bot commands"""
    
    def __init__(self, bot: commands.Bot, channel_manager: ChannelManager):
        self.bot = bot
        self.channel_manager = channel_manager
    
    @commands.command(name='ping', help='Verificar si el bot responde')
    async def ping(self, ctx):
        """Comando para verificar latencia del bot"""
        latency = round(self.bot.latency * 1000)
        await ctx.send(f'🏓 ¡Pong! Latencia: {latency}ms')
    
    @commands.command(name='info', help='Información del bot')
    async def info(self, ctx):
        """Mostrar información básica del bot"""
        embed = discord.Embed(
            title="🐛 Bot de Bugs",
            description="Bot básico para reportar y gestionar bugs",
            color=0x00ff00
        )
        embed.add_field(name="Servidores", value=len(self.bot.guilds), inline=True)
        embed.add_field(name="Usuarios", value=len(self.bot.users), inline=True)
        embed.add_field(name="Latencia", value=f"{round(self.bot.latency * 1000)}ms", inline=True)
        embed.add_field(name="Versión", value="1.0.0 Modular", inline=True)
        
        await ctx.send(embed=embed) 