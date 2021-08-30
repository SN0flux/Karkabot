import discord
import karkabot_command_text as kbc
import requests
from discord.ext import commands

class Dailies(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.group(invoke_without_command=True)
  async def daily(self, ctx):
    dailyParams = {'v': 'v=2019-05-16T00:00:00.000Z'}
    r = requests.get('https://api.guildwars2.com/v2/achievements/daily', params=dailyParams)
    response = r.json()
    pve = response['pve']
    wvw = response['wvw']
    fractals = response['fractals']
    pveAchievementList = getPVEAchievements(pve)
    wvwAchievementList = getWVWAchievements(wvw)
    fractalDailyList = getFractalDailies(fractals)
    
    dailyEmbed = embed=discord.Embed(
      title=f"Dailies", 
      description="Complete list of Today's Dailies", 
      color=0xFF5733)
    dailyEmbed.add_field(name="PVE", value='\n'.join(pveAchievementList),inline=False)
    dailyEmbed.add_field(name="WVW", value='\n'.join(wvwAchievementList),inline=False)
    dailyEmbed.add_field(name="Fractals", value='\n'.join(fractalDailyList),inline=False)

    await ctx.send(embed=dailyEmbed)

  @daily.command()
  async def pve(self, ctx):
    dailyParams = {'v': 'v=2019-05-16T00:00:00.000Z'}
    r = requests.get('https://api.guildwars2.com/v2/achievements/daily', params=dailyParams)
    response = r.json()
    pve = response['pve']
    pveAchievementList = getPVEAchievements(pve)
    dailyEmbed = embed=discord.Embed(
      title=f"PVE Dailies", 
      description="Today's PVE Dailies", 
      color=0xFF5733)
    dailyEmbed.add_field(name="PVE", value='\n'.join(pveAchievementList),inline=False)
    await ctx.send(embed=dailyEmbed)

  @daily.command()
  async def wvw(self, ctx):
    dailyParams = {'v': 'v=2019-05-16T00:00:00.000Z'}
    r = requests.get('https://api.guildwars2.com/v2/achievements/daily', params=dailyParams)
    response = r.json()
    wvw = response['wvw']
    wvwAchievementList = getWVWAchievements(wvw)
    dailyEmbed = embed=discord.Embed(
      title=f"WVW Dailies", 
      description="Today's WVW Dailies", 
      color=0xFF5733)
    dailyEmbed.add_field(name="WVW", value='\n'.join(wvwAchievementList),inline=False)
    await ctx.send(embed=dailyEmbed)

  @daily.command()
  async def fractals(self, ctx):
    dailyParams = {'v': 'v=2019-05-16T00:00:00.000Z'}
    r = requests.get('https://api.guildwars2.com/v2/achievements/daily', params=dailyParams)
    response = r.json()
    fractals = response['fractals']
    finalFractalList = getFractalDailies(fractals)
    dailyEmbed = embed=discord.Embed(
      title=f"Fractals", 
      description="Today's fractals", 
      color=0xFF5733)
    dailyEmbed.add_field(name="Fractals", value='\n'.join(finalFractalList),inline=False)
    await ctx.send(embed=dailyEmbed)

def setup(bot):
  bot.add_cog(Dailies(bot))

def getPVEAchievements(pveJson):
  achievementList = []
  for item in pveJson:
    for k, v in item.items():
      if k == 'level':
        if 'required_access' in item:
          req = item.get('required_access').get('condition')
          if req == 'HasAccess':
            achievementList.append(str(item['id']))
        elif v['max'] == 80:
          achievementList.append(str(item['id']))
  achieves = retrieveAchievements(achievementList)
  return achieves

def getWVWAchievements(wvwJson):
  achievementList = []
  for item in wvwJson:
    achievementList.append(str(item['id']))
  achieves = retrieveAchievements(achievementList)
  return achieves

def getFractalDailies(fractalsJson):
  fractalDailies = []
  finalFractalList = []
  for item in fractalsJson:
    fractalDailies.append(str(item['id']))
  fractals = retrieveAchievements(fractalDailies)
  for item in fractals:
    if "Recommended" in item or "Tier 4" in item:
      finalFractalList.append(item)
  return finalFractalList

def retrieveAchievements(achievementList):
  translatedAchievementList = []
  achievementListString = ','.join(achievementList)
  achieveParams = {'ids': achievementListString}
  r = requests.get('https://api.guildwars2.com/v2/achievements', params=achieveParams)
  achievementListJson = r.json()
  for item in achievementListJson:
    for k, v in item.items():
      if k == "name":
        translatedAchievementList.append(v)
  return translatedAchievementList