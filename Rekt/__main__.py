from Bot import bot
from Config import configuration

token = configuration.discord.auth_token

if __name__ == "__main__":
    bot.run(token)
