import discord
from discord.ext import commands
from config import DISCORD_TOKEN, COMMAND_PREFIX

# Import modules
from utils.channel_manager import ChannelManager
from commands.basic_commands import BasicCommands
from commands.bug_commands import BugCommands
from commands.channel_commands import ChannelCommands
from events.bot_events import BotEvents

async def setup_bot():
    """Setup and configure the bot"""
    # Configurar intents (permisos del bot)
    intents = discord.Intents.default()
    intents.message_content = True  # Necesario para leer contenido de mensajes

    # Crear instancia del bot
    bot = commands.Bot(
        command_prefix=COMMAND_PREFIX,
        intents=intents,
        description='Bot básico para reportar bugs 🐛'
    )

    # Initialize channel manager
    channel_manager = ChannelManager()

    # Add cogs
    await bot.add_cog(BasicCommands(bot, channel_manager))
    await bot.add_cog(BugCommands(bot, channel_manager))
    await bot.add_cog(ChannelCommands(bot, channel_manager))
    await bot.add_cog(BotEvents(bot, channel_manager))

    return bot

async def main():
    """Main function to run the bot"""
    try:
        print("🚀 Iniciando bot...")
        bot = await setup_bot()
        await bot.start(DISCORD_TOKEN or 'test')
    except Exception as e:
        print(f"❌ Error al iniciar el bot: {e}")

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
