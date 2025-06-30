import discord
from discord.ext import commands
from utils.channel_manager import ChannelManager

class ChannelCommands(commands.Cog):
    """Channel management commands"""
    
    def __init__(self, bot: commands.Bot, channel_manager: ChannelManager):
        self.bot = bot
        self.channel_manager = channel_manager
    
    @commands.command(name='channels', help='Gestionar canales donde el bot puede funcionar')
    async def manage_channels(self, ctx, action: str = 'list', channel_name: str | None = None):
        """Gestionar canales permitidos para el bot"""
        if not ctx.guild:
            await ctx.send("❌ Este comando solo funciona en servidores.")
            return
        
        guild_id = ctx.guild.id
        
        if action.lower() == 'list':
            await self._list_channels(ctx, guild_id)
        elif action.lower() == 'add':
            await self._add_channel(ctx, guild_id, channel_name)
        elif action.lower() == 'remove':
            await self._remove_channel(ctx, guild_id, channel_name)
        elif action.lower() == 'clear':
            await self._clear_channels(ctx, guild_id)
        else:
            await ctx.send("❌ Acción no válida. Usa: `list`, `add`, `remove`, o `clear`")
    
    async def _list_channels(self, ctx, guild_id: int):
        """List allowed channels"""
        guild_channels = self.channel_manager.get_guild_channels(guild_id)
        if not guild_channels:
            embed = discord.Embed(
                title="📋 Canales Permitidos",
                description="No hay canales configurados. El bot funciona en todos los canales.",
                color=0xffff00
            )
        else:
            channel_list = []
            for channel_name in guild_channels:
                # Buscar el canal por nombre
                channel_obj = discord.utils.get(ctx.guild.channels, name=channel_name)
                if channel_obj:
                    channel_list.append(f"• {channel_obj.mention} (`{channel_name}`)")
                else:
                    channel_list.append(f"• Canal no encontrado (`{channel_name}`)")
            
            embed = discord.Embed(
                title="📋 Canales Permitidos",
                description="\n".join(channel_list),
                color=0x00ff00
            )
        
        await ctx.send(embed=embed)
    
    async def _add_channel(self, ctx, guild_id: int, channel_name: str | None):
        """Add channel to allowed list"""
        if not channel_name:
            await ctx.send("❌ Debes proporcionar el nombre del canal.\nUso: `!channels add nombre-del-canal`")
            return
        
        # Verificar que el canal existe
        channel_obj = discord.utils.get(ctx.guild.channels, name=channel_name)
        if not channel_obj:
            await ctx.send(f"❌ No se encontró un canal llamado `{channel_name}` en este servidor.")
            return
        
        if self.channel_manager.add_allowed_channel(guild_id, channel_name):
            embed = discord.Embed(
                title="✅ Canal Agregado",
                description=f"El canal {channel_obj.mention} (`{channel_name}`) ahora está permitido para el bot.",
                color=0x00ff00
            )
        else:
            embed = discord.Embed(
                title="❌ Error",
                description="No se pudo guardar la configuración.",
                color=0xff0000
            )
        
        await ctx.send(embed=embed)
    
    async def _remove_channel(self, ctx, guild_id: int, channel_name: str | None):
        """Remove channel from allowed list"""
        if not channel_name:
            await ctx.send("❌ Debes proporcionar el nombre del canal.\nUso: `!channels remove nombre-del-canal`")
            return
        
        if self.channel_manager.remove_allowed_channel(guild_id, channel_name):
            embed = discord.Embed(
                title="✅ Canal Removido",
                description=f"El canal `{channel_name}` ya no está permitido para el bot.",
                color=0x00ff00
            )
        else:
            embed = discord.Embed(
                title="❌ Error",
                description="No se pudo guardar la configuración.",
                color=0xff0000
            )
        
        await ctx.send(embed=embed)
    
    async def _clear_channels(self, ctx, guild_id: int):
        """Clear all allowed channels"""
        if self.channel_manager.clear_guild_channels(guild_id):
            embed = discord.Embed(
                title="✅ Configuración Limpiada",
                description="El bot ahora funciona en todos los canales del servidor.",
                color=0x00ff00
            )
        else:
            embed = discord.Embed(
                title="❌ Error",
                description="No se pudo limpiar la configuración.",
                color=0xff0000
            )
        
        await ctx.send(embed=embed) 