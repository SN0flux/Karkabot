import discord
import karkabot_command_text as kbc
from discord.ext import commands

class Raid_Builds(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.group(invoke_without_command=True, case_insensitive=True)
  async def builds(self, ctx):
    embed=discord.Embed(
      title=f"Build Professions", 
      description="The following professions and specs may have associated builds.\n Use **$builds <profession>** to view.", 
      color=0xFF5733)
    embed.add_field(name="Core", value='\n'.join(kbc.CORECLASSLIST), inline=True)
    embed.add_field(name="Elite 1", value='\n'.join(kbc.ELITE1LIST), inline=True)
    embed.add_field(name="Elite 2", value='\n'.join(kbc.ELITE2LIST), inline=True)
    await ctx.send(embed=embed)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def elementalist(self, ctx):
    embed = self.embedBuilder('Elementalist', kbc.ELEBUILDS)
    await ctx.send(embed=embed)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def tempest(self, ctx):
    embed = self.embedBuilder('Tempest', kbc.TEMPESTBUILDS)
    await ctx.send(embed=embed)

  @tempest.command(hidden=True)
  async def conditempest(self, ctx):
    """Condi Tempest"""
    await ctx.send(kbc.CONDITEMPEST)

  @tempest.command(hidden=True)
  async def healtempest(self, ctx):
    """Heal Tempest"""
    await ctx.send(kbc.HEALTEMPEST)

  @tempest.command(hidden=True)
  async def powertempest(self, ctx):
    """Power Tempest"""
    await ctx.send(kbc.POWERTEMPEST)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def weaver(self, ctx):
    embed = self.embedBuilder('Weaver', kbc.WEAVERBUILDS)
    await ctx.send(embed=embed)

  @weaver.command(hidden=True)
  async def condiweaver(self, ctx):
    """Condi Weaver"""
    await ctx.send(kbc.CONDIWEAVER)

  @weaver.command(hidden=True)
  async def hybridweaver(self, ctx):
    """Hybrid Weaver"""
    await ctx.send(kbc.HYBRIDWEAVER)

  @weaver.command(hidden=True)
  async def powerweaver(self, ctx):
    """Power Weaver"""
    await ctx.send(kbc.POWERWEAVER)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def engineer(self, ctx):
    embed = self.embedBuilder('Engineer', kbc.ENGINEERBUILDS)
    await ctx.send(embed=embed)

  @engineer.command(hidden=True)
  async def handkiteengineer(self, ctx):
    """Power DPS Scrapper"""
    await ctx.send(kbc.HANDKITEENGINEER)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def scrapper(self, ctx):
    embed = self.embedBuilder('Scrapper', kbc.SCRAPPERBUILDS)
    await ctx.send(embed=embed)

  @scrapper.command(hidden=True)
  async def healquickscrapper(self, ctx):
    """Heal Quickness Scrapper"""
    await ctx.send(kbc.HEALQUICKSCRAPPER)

  @scrapper.command(hidden=True)
  async def quickscrapper(self, ctx):
    """Quickness Scrapper """
    await ctx.send(kbc.QUICKNESSSCRAPPER)

  @scrapper.command(hidden=True)
  async def powerscrapper(self, ctx):
    """Power DPS Scrapper"""
    await ctx.send(kbc.POWERSCRAPPER)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def holosmith(self, ctx):
    embed = self.embedBuilder('Holosmith', kbc.HOLOSMITHBUILDS)
    await ctx.send(embed=embed)

  @holosmith.command(hidden=True)
  async def condiholo(self, ctx):
    """Power DPS Sword Holosmith"""
    await ctx.send(kbc.CONDIHOLO)

  @holosmith.command(hidden=True)
  async def powerswordholo(self, ctx):
    """Power DPS Sword Holosmith"""
    await ctx.send(kbc.POWERSWORDHOLO)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def guardian(self, ctx):
    embed = self.embedBuilder('Guardian', kbc.GUARDIANBUILDS)
    await ctx.send(embed=embed)

  @guardian.command(hidden=True)
  async def powerguardian(self, ctx):
    """Power Guardian"""
    await ctx.send(kbc.POWERGUARDIAN)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def dragonhunter(self, ctx):
    embed = self.embedBuilder('Dragonhunter', kbc.DRAGONHUNTERBUILDS)
    await ctx.send(embed=embed)

  @dragonhunter.command(hidden=True)
  async def powerdh(self, ctx):
    """Power Dragonhunter"""
    await ctx.send(kbc.POWERDH)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def firebrand(self, ctx):
    embed = self.embedBuilder('Firebrand', kbc.FIREBRANDBUILDS)
    await ctx.send(embed=embed)

  @firebrand.command(hidden=True)
  async def condifirebrand(self, ctx):
    """Condi Firebrand"""
    await ctx.send(kbc.CONDIFIREBRAND)

  @firebrand.command(hidden=True, aliases=['cqb'])
  async def condiquickbrand(self, ctx):
    """Condi Quickbrand"""
    await ctx.send(kbc.CQB)

  @firebrand.command(hidden=True)
  async def healbrand(self, ctx):
    """Healbrand w/ Quickness"""
    await ctx.send(kbc.HEALBRAND)

  @firebrand.command(hidden=True)
  async def bluetank(self, ctx):
    """Tank/Heal Firebrand"""
    await ctx.send(kbc.BLUETANK)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def mesmer(self, ctx):
    embed = self.embedBuilder('Mesmer', kbc.MESMERBUILDS)
    await ctx.send(embed=embed)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def chronomancer(self, ctx):
    embed = self.embedBuilder('Chronomancer', kbc.CHRONOMANCERBUILDS)
    await ctx.send(embed=embed)

  @chronomancer.command(hidden=True)
  async def purpletank(self, ctx):
    """Chronomancer Tank"""
    await ctx.send(kbc.PURPLETANK)

  @chronomancer.command(hidden=True)
  async def powerchrono(self, ctx):
    """Power Boon Chrono"""
    await ctx.send(kbc.POWERCHRONO)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def mirage(self, ctx):
    embed = self.embedBuilder('Mirage', kbc.MIRAGEBUILDS)
    await ctx.send(embed=embed)

  @mirage.command(hidden=True)
  async def staffmirage(self, ctx):
    """Condi Boon Mirage"""
    await ctx.send(kbc.CONDIBOONMIRAGE)

  @mirage.command(hidden=True)
  async def condimirage(self, ctx):
    """Condi DPS Mirage"""
    await ctx.send(kbc.CONDIDPSMIRAGE) 

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def necromancer(self, ctx):
    embed = self.embedBuilder('Necromancer', kbc.NECROBUILDS)
    await ctx.send(embed=embed)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def reaper(self, ctx):
    embed = self.embedBuilder('Reaper', kbc.REAPERBUILDS)
    await ctx.send(embed=embed)

  @reaper.command(hidden=True)
  async def powerreaper(self, ctx):
    """Power Reaper"""
    await ctx.send(kbc.POWERREAPER)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def scourge(self, ctx):
    embed = self.embedBuilder('Scourge', kbc.SCOURGEBUILDS)
    await ctx.send(embed=embed)

  @scourge.command(hidden=True)
  async def condiscourge(self, ctx):
    """Condi Scourge"""
    await ctx.send(kbc.CONDISCOURGE)

  @scourge.command(hidden=True)
  async def healscourge(self, ctx):
    """Heal Scourge"""
    await ctx.send(kbc.HEALSCOURGE)

  @scourge.command(hidden=True)
  async def pylonkitescourge(self, ctx):
    """Pylon Kite Scourge"""
    await ctx.send(kbc.PYLONKITESCOURGE)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def ranger(self, ctx):
    embed = self.embedBuilder('Ranger', kbc.RANGERBUILDS)
    await ctx.send(embed=embed)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def druid(self, ctx):
    embed = self.embedBuilder('Druid', kbc.DRUIDBUILDS)
    await ctx.send(embed=embed)

  @druid.command(hidden=True)
  async def condidruid(self, ctx):
    """Condi Druid"""
    await ctx.send(kbc.CONDIDRUID)

  @druid.command(hidden=True)
  async def healdruid(self, ctx):
    """Heal/Boon Druid"""
    await ctx.send(kbc.HEALDRUID)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def soulbeast(self, ctx):
    embed = self.embedBuilder('Soulbeast', kbc.SOULBEASTBUILDS)
    await ctx.send(embed=embed)

  @soulbeast.command(hidden=True)
  async def condisb(self, ctx):
    """Condi Soulbeast"""
    await ctx.send(kbc.CONDISOULBEAST)

  @soulbeast.command(hidden=True)
  async def handkitesb(self, ctx):
    """Handkite Soulbeast"""
    await ctx.send(kbc.HANDKITESB)

  @soulbeast.command(hidden=True)
  async def hybridsb(self, ctx):
    """Hybrid Soulbeast"""
    await ctx.send(kbc.HYBRIDSB)

  @soulbeast.command(hidden=True)
  async def powersb(self, ctx):
    """Power Soulbeast"""
    await ctx.send(kbc.POWERSB)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def revenant(self, ctx):
    embed = self.embedBuilder('Revenant', kbc.REVBUILDS)
    await ctx.send(embed=embed)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def herald(self, ctx):
    embed = self.embedBuilder('Herald', kbc.HERALDBUILDS)
    await ctx.send(embed=embed)

  @herald.command(hidden=True)
  async def handkiteherald(self, ctx):
    """Handkite Herald"""
    await ctx.send(kbc.HANDKITEHERALD)

  @herald.command(hidden=True)
  async def powerherald(self, ctx):
    await ctx.send(kbc.POWERHERALD)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def renegade(self, ctx):
    embed = self.embedBuilder('Renegade', kbc.RENEGADEBUILDS)
    await ctx.send(embed=embed)

  @renegade.command(hidden=True)
  async def alacren(self, ctx):
    """Power (Diviners) Alacren"""
    await ctx.send(kbc.POWERALAC)

  @renegade.command(hidden=True)
  async def condiren(self, ctx):
    """Condi DPS Renegade"""
    await ctx.send(kbc.CONDIREN)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def thief(self, ctx):
    embed = self.embedBuilder('Thief', kbc.THIEFBUILDS)
    await ctx.send(embed=embed)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def daredevil(self, ctx):
    embed = self.embedBuilder('Daredevil', kbc.DDBUILDS)
    await ctx.send(embed=embed)

  @daredevil.command(hidden=True)
  async def condidd(self, ctx):
    """Condi Daredevil"""
    await ctx.send(kbc.CONDIDAREDEVIL)

  @daredevil.command(hidden=True)
  async def powerdd(self, ctx):
    """Power Daredevil"""
    await ctx.send(kbc.POWERDAREDEVIL)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def deadeye(self, ctx):
    embed = self.embedBuilder('Deadeye', kbc.DEADEYEBUILDS)
    await ctx.send(embed=embed)

  @deadeye.command(hidden=True)
  async def qadimkitede(self, ctx):
    """Qadim Deadeye Kite"""
    await ctx.send(kbc.QADIMKITEDD)

  @deadeye.command(hidden=True)
  async def qtpkitede(self, ctx):
    """Qadim the Peerless Deadeye Kite"""
    await ctx.send(kbc.QTPKITEDAREDEVIL)

  @deadeye.command(hidden=True)
  async def rifledeadeye(self, ctx):
    await ctx.send(kbc.RIFLEDEADEYE)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def warrior(self, ctx):
    embed = self.embedBuilder('Warrior', kbc.WARBUILDS)
    await ctx.send(embed=embed)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def berserker(self, ctx):
    embed = self.embedBuilder('Berserker', kbc.BERSERKERBUILDS)
    await ctx.send(embed=embed)

  @berserker.command(hidden=True)
  async def condibanners(self, ctx):
    """Condi Banner Warrior"""
    await ctx.send(kbc.CONDIBANNERS)

  @berserker.command(hidden=True)
  async def powerbanners(self, ctx):
    """Power Banner Warrior"""
    await ctx.send(kbc.POWERBANNERS)

  @berserker.command(hidden=True)
  async def powerberserker(self, ctx):
    """Power DPS Berserker"""
    await ctx.send(kbc.POWERBERSERKER)

  @builds.group(invoke_without_command=True, hidden=True, case_insensitive=True)
  async def spellbreaker(self, ctx):
    embed = self.embedBuilder('Spellbreaker', kbc.SPELLBREAKERBUILDS)
    await ctx.send(embed=embed)

  @spellbreaker.command(hidden=True)
  async def handkitespellbreaker(self, ctx):
    await ctx.send(kbc.HANDKITESPELLBREAKER)

  @spellbreaker.command(hidden=True)
  async def powerbannerspellbreaker(self, ctx):
    await ctx.send(kbc.POWERBANNERSPELLBREAKER)

  def embedBuilder(self, prof, bList):
    t = "Elementalist"
    embed=discord.Embed(
      description=f"View one of the following builds by using **$builds {prof} <build>**", 
      color=0xFF5712)
    if bList:
      embed.add_field(name=f'{prof} builds', value='\n'.join(bList))
    else:
      embed.add_field(name="No builds available", value="Check back later, or try another command.")
    return embed

def setup(bot):
  bot.add_cog(Raid_Builds(bot))