import discord
from datetime import datetime
from Events import CheckedMessage
from Logging import logging


bot = discord.Client()


@bot.event
async def on_ready():
    logging.info(f"Online : {datetime.now().isoformat()}")


@bot.event
async def on_resumed():
    logging.info(f"Resumed : {datetime.now().isoformat()}")


@bot.event
async def on_error(event, *args, **kwargs):
    logging.debug(event, args, kwargs)


@bot.event
async def on_message(message):
    checkedMessage = CheckedMessage(message)
    logging.info(checkedMessage())


@bot.event
async def on_message_delete(message):
    logging.info(f"Deleted : {message}")


@bot.event
async def on_message_edit(before, after):
    logging.info(f"Changed : {before} -> {after}")
