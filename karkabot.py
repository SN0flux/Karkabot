import discord
from decouple import config
import requests, random, asyncio, datetime
import karkabot_command_text as kbc
from discord.ext import commands
import os

intents = discord.Intents.all()
intents.members = True

initial_extensions = ["karkabot_bosses", "karkabot_builds", "karkabot_dailies"]

DESCRIPTION = 'Karka Bot for skittering and assisting during GW2 Raids.'
bot = commands.Bot(command_prefix='$', description=DESCRIPTION, intents=intents, case_insensitive=True)


def next_wednesday(d):
    days_ahead = 2 - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

## FIX THIS FOR YEARS, VALID ONLY 2023
def get_com_emboldened(week_number):
  week_number = week_number%7
  if week_number == 0:
    com = "w7"
    emb = "w6"
    return com, emb
  elif week_number == 1:
    com = "w1"
    emb = "w7"
    return com, emb
  elif week_number == 2:
    com = "w2"
    emb = "w1"
    return com, emb
  elif week_number == 3:
    com = "w3"
    emb = "w2"
    return com, emb
  elif week_number == 4:
    com = "w4"
    emb = "w3"
    return com, emb
  elif week_number == 5:
    com = "w5"
    emb = "w4"
    return com, emb
  elif week_number == 6:
    com = "w6"
    emb = "w5"
    return com, emb

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

@bot.command(hidden=True, aliases=['quaggan'])
async def randomQuaggan(ctx):
  r = requests.get('https://api.guildwars2.com/v2/quaggans')
  response = r.json()
  quagganSelectionInt = random.randrange(0, len(response))
  await ctx.send(f"https://static.staticwars.com/quaggans/{response[quagganSelectionInt]}.jpg")

@bot.command(hidden=True)
async def raidEvent(ctx, wing_list):
  user = ctx.author
  roles = user.roles
  for role in roles:
    if role.Permissions.administrator:
      # Find next wednesday
      start_date=next_wednesday(datetime.datetime.now().astimezone())
      start_date=start_date.replace(hour=19, minute=0)
      end_date=start_date.replace(hour=22)
      raid_channel = discord.utils.get(ctx.guild.channels, name="Raiding")
      raid_schedule_channel=discord.utils.get(ctx.guild.channels, name="raid-scheduling")

      #Get CoM and Emboldened
      week_num = start_date.isocalendar()[1]
      com, emb = get_com_emboldened(week_num)

      event_description=(f'Karka Council Raidsday Agenda:'
        f'\nRaids: {wing_list}'
        f'\nCall of the Mists: {com}'
        f'\nEmboldened: {emb}'
      )

      raid_event = await ctx.guild.create_scheduled_event(
        name="Raidsday", 
        start_time=start_date,
        privacy_level="GUILD_ONLY",
        channel=raid_channel,
        end_time=end_date, 
        description=event_description, 
        reason=None
      )

      await raid_schedule_channel.send(raid_event.url)


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

async def setup():
  for extension in initial_extensions:
    await bot.load_extension(extension)

asyncio.run(setup())
bot.run(config('TOKEN'))