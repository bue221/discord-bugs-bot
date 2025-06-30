import json
import os
from typing import Dict, List
from config import CHANNELS_CONFIG_FILE, DEFAULT_ALLOWED_CHANNEL

class ChannelManager:
    """Manager for allowed channels configuration"""
    
    def __init__(self):
        self.allowed_channels: Dict[str, List[str]] = {}
        self.load_config()
    
    def load_config(self) -> None:
        """Load allowed channels configuration from file"""
        try:
            if os.path.exists(CHANNELS_CONFIG_FILE):
                with open(CHANNELS_CONFIG_FILE, 'r') as f:
                    self.allowed_channels = json.load(f)
            else:
                self.allowed_channels = {}
        except Exception as e:
            print(f"Error loading channels config: {e}")
            self.allowed_channels = {}
    
    def save_config(self) -> bool:
        """Save allowed channels configuration to file"""
        try:
            with open(CHANNELS_CONFIG_FILE, 'w') as f:
                json.dump(self.allowed_channels, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving channels config: {e}")
            return False
    
    def is_channel_allowed(self, guild_id: int, channel_name: str) -> bool:
        """Check if a channel is allowed for bot usage by name"""
        guild_channels = self.allowed_channels.get(str(guild_id), [])
        return channel_name.lower() in [ch.lower() for ch in guild_channels]
    
    def add_allowed_channel(self, guild_id: int, channel_name: str) -> bool:
        """Add a channel to the allowed list by name"""
        guild_id_str = str(guild_id)
        if guild_id_str not in self.allowed_channels:
            self.allowed_channels[guild_id_str] = []
        
        if channel_name.lower() not in [ch.lower() for ch in self.allowed_channels[guild_id_str]]:
            self.allowed_channels[guild_id_str].append(channel_name)
            return self.save_config()
        return True
    
    def remove_allowed_channel(self, guild_id: int, channel_name: str) -> bool:
        """Remove a channel from the allowed list by name"""
        guild_id_str = str(guild_id)
        if guild_id_str in self.allowed_channels:
            # Remove by case-insensitive comparison
            self.allowed_channels[guild_id_str] = [
                ch for ch in self.allowed_channels[guild_id_str] 
                if ch.lower() != channel_name.lower()
            ]
            if not self.allowed_channels[guild_id_str]:
                del self.allowed_channels[guild_id_str]
            return self.save_config()
        return True
    
    def get_guild_channels(self, guild_id: int) -> List[str]:
        """Get allowed channels for a specific guild"""
        return self.allowed_channels.get(str(guild_id), [])
    
    def clear_guild_channels(self, guild_id: int) -> bool:
        """Clear all allowed channels for a guild"""
        guild_id_str = str(guild_id)
        if guild_id_str in self.allowed_channels:
            del self.allowed_channels[guild_id_str]
            return self.save_config()
        return True
    
    def setup_default_channels(self, guilds) -> None:
        """Setup default allowed channels for all guilds"""
        if not self.allowed_channels:
            for guild in guilds:
                self.allowed_channels[str(guild.id)] = [DEFAULT_ALLOWED_CHANNEL]
            self.save_config() 