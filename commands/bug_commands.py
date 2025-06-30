import discord
from discord.ext import commands
from utils.channel_manager import ChannelManager

class BugCommands(commands.Cog):
    """Bug reporting commands"""
    
    def __init__(self, bot: commands.Bot, channel_manager: ChannelManager):
        self.bot = bot
        self.channel_manager = channel_manager
    
    @commands.command(name='bug', help='Reportar un bug')
    async def report_bug(self, ctx, *, descripcion: str = ''):
        """Comando básico para reportar bugs"""
        # Verificar si el canal está permitido
        if ctx.guild and not self.channel_manager.is_channel_allowed(ctx.guild.id, ctx.channel.name):
            await ctx.send("❌ Este comando no está permitido en este canal. Usa `!channels list` para ver canales permitidos.")
            return
        
        if not descripcion:
            await ctx.send("❌ Debes proporcionar una descripción del bug.\nUso: `!bug Tu descripción aquí`")
            return
        
        # Crear embed para el reporte
        embed = discord.Embed(
            title="🐛 Nuevo Bug Reportado",
            description=descripcion,
            color=0xff0000
        )
        embed.add_field(name="Reportado por", value=ctx.author.mention, inline=True)
        embed.add_field(name="Canal", value=ctx.channel.mention, inline=True)
        embed.add_field(name="Servidor", value=ctx.guild.name, inline=True)
        embed.timestamp = discord.utils.utcnow()
        
        await ctx.send("✅ Bug reportado exitosamente!", embed=embed)
        print(f"Bug reportado por {ctx.author}: {descripcion}") 