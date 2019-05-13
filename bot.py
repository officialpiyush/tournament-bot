# tournament-bot
# Copyright (C) 2019 Piyush Bhangale

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import discord
from discord.ext import commands
import motor.motor_asyncio as amotor
import asyncio
import logging
import os

dbClient = amotor.AsyncIOMotorClient("mongodb://localhost:27017/")

bot = commands.Bot(command_prefix='t!')

bot.db= dbClient.client['tournament_bot']

extensions = ['cogs.settings','cogs.errors']
if __name__ == "__main__":
    for extension in extensions:
        bot.load_extension(extension)
        print(f"Loaded Cog {extension}")

@bot.event
async def on_ready():
    print(f"[BOT] Ready!")
    await bot.change_presence(activity = discord.Game(name='Tournaments'))

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)



bot.run(os.getenv("bottoken"))
