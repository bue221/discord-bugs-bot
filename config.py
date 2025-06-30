import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración del bot
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
COMMAND_PREFIX = '!'

# Archivo para almacenar configuración de canales
CHANNELS_CONFIG_FILE = 'channels_config.json'

# Canal por defecto permitido
DEFAULT_ALLOWED_CHANNEL = 'bugs-reporting'

# Verificar que el token existe
if not DISCORD_TOKEN:
    raise ValueError("❌ DISCORD_TOKEN no encontrado en el archivo .env")

print("✅ Configuración cargada correctamente")