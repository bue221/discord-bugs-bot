import discord
from discord.ext import commands
from utils.channel_manager import ChannelManager
from config import COMMAND_PREFIX, DEFAULT_ALLOWED_CHANNEL

class BotEvents(commands.Cog):
    """Bot event handlers"""
    
    def __init__(self, bot: commands.Bot, channel_manager: ChannelManager):
        self.bot = bot
        self.channel_manager = channel_manager
    
    @commands.Cog.listener()
    async def on_ready(self):
        """Bot ready event"""
        # Setup default channels if none exist
        if not self.channel_manager.allowed_channels:
            self.channel_manager.setup_default_channels(self.bot.guilds)
        
        print(f'🎸 ¡Bot conectado como {self.bot.user}!')
        print(f'ID del bot: {self.bot.user.id if self.bot.user else "No hay usuario conectado"}')
        print(f'Conectado a {len(self.bot.guilds)} servidores')
        print('Bot listo para usar!')
        print(f'Canal por defecto: {DEFAULT_ALLOWED_CHANNEL}')
        
        # Cambiar estado del bot
        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening, 
                name="reportes de bugs | !help"
            )
        )
    
    @commands.Cog.listener()
    async def on_message(self, message):
        """Message event handler"""
        # Ignorar mensajes del propio bot
        if message.author == self.bot.user:
            return
        
        # Verificar si el canal está permitido (solo para servidores)
        if message.guild and not self.channel_manager.is_channel_allowed(message.guild.id, message.channel.name):
            # Permitir comandos de configuración en cualquier canal
            if not message.content.startswith(f'{COMMAND_PREFIX}channels'):
                return
        
        # Respuesta automática a "hola"
        content = message.content.lower()
        if 'hola' in content or 'hello' in content or 'hi' in content:
            await message.reply('¡Hola! 👋 Soy tu bot de bugs 🐛. Usa `!help` para ver qué puedo hacer.')
        
        # IMPORTANTE: Permitir que los comandos funcionen
        await self.bot.process_commands(message)
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """Command error handler"""
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f"❌ Comando no encontrado. Usa `{COMMAND_PREFIX}help` para ver comandos disponibles.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"❌ Faltan argumentos. Usa `{COMMAND_PREFIX}help {ctx.command}` para ver el uso correcto.")
        else:
            await ctx.send("❌ Ocurrió un error inesperado.")
            print(f"Error: {error}") 