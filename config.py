import os

from dotenv import load_dotenv
from loguru import logger
load_dotenv()



class Config:
    # Load .env file
    if load_dotenv():
        logger.info("成功加载 .env 文件。")
    else:
        logger.warning("在项目的根目录中找不到 .env 文件，请确保已手动设置环境变量。")

    if os.getenv('FASTAPI_SERVER_URL') is not None:
        logger.warning(
            "环境变量 'FASTAPI_SERVER_URL' 已弃用，请从 .env 文件中移除该变量，并使用 'PORT' 环境变量代替。（默认值：PORT=8000）")
    else:
        logger.info("已成功加载环境变量到配置文件。")
    PORT = int(os.getenv('PORT') or 8000)
    Timeout = float((os.getenv('TIMEOUT')) or 60)
    Key = os.getenv('KEY')
    Key = list(map(str.strip, Key.split(','))) if Key else None
    Web_share = os.getenv('WEB_SHARE') or 'False'
    Proxy = os.getenv('PROXY')
    Proxy_Auth = os.getenv('PROXY_AUTH')
    if Proxy:
        logger.info(f"Proxy: {Proxy} enabled.")

    # telegram
    TELEGRAM = os.getenv('TELEGRAM')
    API_ID = int(os.getenv('API_ID') or -1)
    API_HASH = os.getenv('API_HASH')

    BOT_USERNAME = os.getenv('BOT_USERNAME')
    print(BOT_USERNAME)  # 打印变量的值
    BOT_USERNAME = BOT_USERNAME if BOT_USERNAME.startswith('@') else '@'+BOT_USERNAME
    print(os.getenv('BOT_USERNAME'))
    SESSION_NAME = os.getenv('SESSION_NAME')+'.session'
    SESSION_STRING = os.getenv('SESSION_STRING')
    # read session file if exists
    if os.path.exists(os.path.join('data',SESSION_NAME)) and not SESSION_STRING:
        with open(os.path.join('data',SESSION_NAME),'r') as f:
            SESSION_STRING = f.read().strip()
    TelegramGroupID = int(os.getenv('TELEGRAM_GROUP_ID') or -1)

    # discord
    Discord = os.getenv('DISCORD')
    DiscordClientBotToken = os.getenv('DISCORD_AUTH')
    DiscordChannelID = int(os.getenv('DISCORD_CHANNEL_ID') or -1)
    DiscordDalleBotID = int(os.getenv('DISCORD_DALLE_BOT_ID') or -1)

    # mkdir data/images if not exists
    os.makedirs(os.path.join('data', 'images'), exist_ok=True)

config = Config()