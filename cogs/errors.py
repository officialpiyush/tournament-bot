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

class ErrorCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commads.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error, commands.errors.CommandNotFound):
            await ctx.send("That command doesn't exist.")
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.send('This command cannot be used in private messages.')
        elif isinstance(error, commands.DisabledCommand):
            await ctx.send('Sorry. This command is disabled and cannot be used.')
        elif isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send(f"Not enough arguments supplied.")
            await ctx.send_help(ctx.command)
        elif isinstance(error, commands.errors.BadArgument):
            await ctx.send(f"Bad arguments supplied.")
            await ctx.send_help(ctx.command)
        elif isinstance(error, commands.errors.NotOwner):
            await ctx.send("This command is only for my master!!!!")
        elif isinstance(error, discord.errors.Forbidden):
            await ctx.send("I don't have enough permsissions to do that!")
        elif isinstance(error, commands.errors.MissingPermissions):
            await ctx.author.send("You don't have enough permissions to use this command!")
        else:
            raise

def setup(bot):
    bot.add_cog(ErrorCog(bot))
