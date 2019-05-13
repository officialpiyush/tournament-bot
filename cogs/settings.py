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

class SettingsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.db.settings

    @commands.group()
    async def settings(self, ctx):
        if ctx.invoked_subcommand is None:
            return

    @settings.command(name="vc-category", aliases=["vcc"])
    @commands.has_permissions(manage_guild=True)
    async def vccategory(self, ctx, category: discord.CategoryChannel):
        """Set The Category In Which VC's Would be created"""
        await self.db.find_one_and_update({
            {"_id": "config"},
            {"$set": {category: category.id}}}, upsert=True);

        await ctx.send(f"Sucessfully Set The category For Creating Voice Channels to `{category.name}`")

    @settings.command(name="channel")
    @commands.has_permissions(manage_guild=True)
    async def setchannel(Self,ctx,channel: discord.TextChannel):
        await self.db.find_one_and_update({
        {"_id": "config"},
        {"$set": {channel: channel.id}}},
        upsert=True
        )

        await ctx.send(f"{channel.mention} has been successfully set up for registerations")

    @settings.command(name="set_team_limit" , aliases=["stl" , "team-limit"])
    @commands.has_permissions(manage_guild=True)
    async def set_team_limit(self,ctx,size: int):
        await self.db.find_one_and_update({
        {"_id": "config"},
        {"$set": {"team_size": size}}},
        upsert=True
        )

        await ctx.send(f"`{size}` is the Limit Of Team Registerations Now")

        
def setup(bot):
    bot.add_cog(SettingsCog(bot))
