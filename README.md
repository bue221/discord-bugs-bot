# 🐛 Bugs Bot

Bot de Discord modular para reportar y gestionar bugs de manera eficiente.

## 📁 Estructura del Proyecto

```
bugs-bot/
├── bot.py                 # Archivo principal del bot
├── config.py              # Configuración del bot
├── utils/                 # Utilidades y helpers
│   ├── __init__.py
│   └── channel_manager.py # Gestión de canales permitidos
├── commands/              # Comandos del bot
│   ├── __init__.py
│   ├── basic_commands.py  # Comandos básicos (ping, info)
│   ├── bug_commands.py    # Comandos de reporte de bugs
│   └── channel_commands.py # Gestión de canales
├── events/                # Eventos del bot
│   ├── __init__.py
│   └── bot_events.py      # Manejadores de eventos
├── pyproject.toml         # Dependencias y configuración
├── poetry.lock           # Lock file de dependencias
└── README.md             # Este archivo
```

## 🚀 Características

- **Modular**: Código organizado en módulos separados para fácil mantenimiento
- **Gestión de Canales**: Control sobre qué canales pueden usar el bot
- **Reporte de Bugs**: Sistema simple para reportar bugs
- **Configuración Persistente**: Los canales permitidos se guardan automáticamente
- **Canal por Defecto**: Funciona automáticamente en canales llamados "bugs-reporting"

## 🛠️ Instalación

1. **Clonar el repositorio**:

   ```bash
   git clone <url-del-repositorio>
   cd bugs-bot
   ```

2. **Instalar dependencias**:

   ```bash
   poetry install
   ```

3. **Configurar variables de entorno**:
   Crear un archivo `.env` en la raíz del proyecto:

   ```env
   DISCORD_TOKEN=tu_token_de_discord_aqui
   ```

4. **Ejecutar el bot**:
   ```bash
   poetry run python bot.py
   ```

## 📋 Comandos Disponibles

### Comandos Básicos

- `!ping` - Verificar latencia del bot
- `!info` - Información del bot

### Gestión de Canales

- `!channels list` - Mostrar canales permitidos
- `!channels add <nombre>` - Agregar canal permitido
- `!channels remove <nombre>` - Remover canal permitido
- `!channels clear` - Limpiar todos los canales permitidos

### Reporte de Bugs

- `!bug <descripción>` - Reportar un nuevo bug

## 🔧 Configuración de Canales

Por defecto, el bot solo funciona en canales llamados `bugs-reporting`. Para cambiar esto:

1. **Ver canales actuales**:

   ```
   !channels list
   ```

2. **Agregar un canal**:

   ```
   !channels add nombre-del-canal
   ```

3. **Remover un canal**:

   ```
   !channels remove nombre-del-canal
   ```

4. **Permitir todos los canales**:
   ```
   !channels clear
   ```

## 🏗️ Arquitectura Modular

### Módulos Principales

#### `utils/channel_manager.py`

- Clase `ChannelManager` para gestionar canales permitidos
- Persistencia de configuración en archivo JSON
- Validación de canales por nombre

#### `commands/`

- **`basic_commands.py`**: Comandos básicos del bot
- **`bug_commands.py`**: Comandos para reportar bugs
- **`channel_commands.py`**: Gestión de canales permitidos

#### `events/bot_events.py`

- Manejadores de eventos del bot
- Verificación de canales permitidos
- Respuestas automáticas

### Ventajas de la Modularización

1. **Separación de Responsabilidades**: Cada módulo tiene una función específica
2. **Mantenibilidad**: Fácil de modificar y extender
3. **Reutilización**: Los módulos pueden reutilizarse en otros proyectos
4. **Testabilidad**: Cada módulo puede probarse independientemente
5. **Escalabilidad**: Fácil agregar nuevas funcionalidades

## 🔄 Flujo de Trabajo

1. **Inicialización**: El bot carga la configuración de canales
2. **Verificación**: Cada mensaje se verifica contra canales permitidos
3. **Procesamiento**: Los comandos se procesan según el módulo correspondiente
4. **Persistencia**: Los cambios se guardan automáticamente

## 🐛 Reportar Bugs del Bot

Si encuentras un bug en el bot, puedes:

1. Usar el comando `!bug` en un canal permitido
2. Crear un issue en el repositorio
3. Contactar al desarrollador

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📞 Soporte

Para soporte, contacta al desarrollador o crea un issue en el repositorio.
