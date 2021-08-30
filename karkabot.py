import discord
from decouple import config
import random
import karkabot_command_text as kbc
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True

initial_extensions = ["karkabot_bosses", "karkabot_builds", "karkabot_dailies"]

DESCRIPTION = 'Karka Bot for skittering and assisting during GW2 Raids.'
bot = commands.Bot(command_prefix='$', description=DESCRIPTION, intents=intents, case_insensitive=True)

@commands.command(hidden=True)
async def load(extension_name : str):
  """Loads an extension."""
  try:
    bot.load_extension(extension_name)
  except (AttributeError, ImportError) as e:
    await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
    return
  await bot.say("{} loaded.".format(extension_name))

@commands.command(hidden=True)
async def unload(extension_name : str):
  """Unloads an extension."""
  bot.unload_extension(extension_name)
  await bot.say("{} unloaded.".format(extension_name))

@bot.command(hidden=True, aliases=['defMessage'])
async def defenseMessage(ctx):
  defSelectionInt = random.randrange(0, len(kbc.DEFMESSAGES))
  defSelection = kbc.DEFMESSAGES[defSelectionInt]
  defEmbed = discord.Embed(
    title=f"TT Defense (NOT BOSS SQUAD)",
    description=f"1. Lobby - {defSelection[0]}\n"
                f"2. Crimson - {defSelection[1]}\n"
                f"3. Amber - {defSelection[2]}\n"
                f"4. Cobalt - {defSelection[3]}\n"
                f"5. Condi - {defSelection[4]}\n"
                f"\n"
                f"6+. AFK - {defSelection[5]}", 
    color=0xFFFFFF)
  await ctx.send(embed=defEmbed)

@bot.command(hidden=True, aliases=['defRecruit'])
async def defenseRecruit(ctx):
  defEmbed = discord.Embed(
    title=f"TT Defense Recruitment",
    description=f"{kbc.DEFRECRUIT1}\n"
                f"\n"
                f"{kbc.DEFRECRUIT2}",
    color=0xFFFFFF)
  await ctx.send(embed=defEmbed)

@bot.event
async def on_member_join(member):
  """Says when a member joined."""
  guild = member.guild
  await guild.system_channel.send(kbc.NEWMEMBERMESSAGE.format(member, guild))


class KarkaHelpCommand(commands.MinimalHelpCommand):
  async def send_pages(self):
    destination = self.get_destination()
    e = discord.Embed(color=discord.Color.blurple(), description='')
    for page in self.paginator.pages:
      e.description += page
    await destination.send(embed=e)

bot.help_command = KarkaHelpCommand(no_category = 'General')

for extension in initial_extensions:
  bot.load_extension(extension)

bot.run(config('TOKEN'))