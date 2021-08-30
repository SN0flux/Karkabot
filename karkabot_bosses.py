import discord
import karkabot_command_text as kbc
from discord.ext import commands

class Raid_Bosses(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.group(invoke_without_command=True, case_insensitive=True)
  async def bosses(self, ctx):
    await ctx.send("Provide a Wing and Boss for more information: **$bosses w1 vg**")

  #Raid Boss Groups
  @bosses.group(invoke_without_command=True, case_insensitive=True)
  async def w1(self, ctx):
    """Wing 1: Forsaken Thicket: Spirit Vale"""
    await ctx.send("Provide a boss for more information: **vg**, **spiritwoods**, **gorseval**, **sabetha**")    

  @bosses.group(invoke_without_command=True, case_insensitive=True)
  async def w2(self, ctx):
    """Wing 2: Forsaken Thicket: Salvation Pass"""
    await ctx.send("Provide a boss for more information: **slothasor**, **bandits**, **matthias**")   

  @bosses.group(invoke_without_command=True, case_insensitive=True)
  async def w3(self, ctx):
    """Wing 3: Forsaken Thicket: Stronghold of the Faithful"""
    await ctx.send("Provide a boss for more information: **escort**, **kc**, **castle**, **xera**")    

  @bosses.group(invoke_without_command=True, case_insensitive=True)
  async def w4(self, ctx):
    """Wing 4: Bastion of the Penitent"""
    await ctx.send("Provide a boss for more information: **cairn**, **overseer**, **samarog**, **deimos**")    

  @bosses.group(invoke_without_command=True, case_insensitive=True)
  async def w5(self, ctx):
    """Wing 5: Hall of Chains"""
    await ctx.send("Provide a boss for more information: **sh**, **river**, **statues**, **dhuum**")    

  @bosses.group(invoke_without_command=True, case_insensitive=True)
  async def w6(self, ctx):
    """Wing 6: Mythwright Gambit"""
    await ctx.send("Provide a boss for more information: **ca**, **twinlargos**, **qadim**")    

  @bosses.group(invoke_without_command=True, case_insensitive=True)
  async def w7(self, ctx):
    """Wing 7: The Key of Ahdashim"""
    await ctx.send("Provide a boss for more information: **gates**, **adina**, **sabir**, **qtp**")    

  #W1 Commands
  @w1.command()
  async def vg(self, ctx):
    """Vale Guardian"""
    await ctx.send(kbc.VG)

  @w1.command()
  async def spiritwoods(self, ctx):
    """Spirit Woods (Spirit Run)"""
    await ctx.send(kbc.SPIRITWOODS)

  @w1.command()
  async def gorseval(self, ctx):
    """Gorseval"""
    await ctx.send(kbc.GORSEVAL)

  @w1.command()
  async def sabetha(self, ctx):
    """Sabetha"""
    await ctx.send(kbc.SABETHA)

  #W2 Commands
  @w2.command()
  async def slothasor(self, ctx):
    """Slothasor"""
    await ctx.send(kbc.SLOTHASOR)

  @w2.command()
  async def bandits(self, ctx):
    """Prison Camp (Bandit Trio)"""
    await ctx.send(kbc.BANDITS)

  @w2.command()
  async def matthias(self, ctx):
    """Matthias Gabrel"""
    await ctx.send(kbc.MATTHIAS)

  #W3 Commands
  @w3.command()
  async def escort(self, ctx):
    """Siege the Stronghold (Escort)"""
    await ctx.send(kbc.ESCORT)

  @w3.command()
  async def kc(self, ctx):
    """Keep Construct"""
    await ctx.send(kbc.KEEPCONSTRUCT)

  @w3.command()
  async def castle(self, ctx):
    """Twisted Castle"""
    await ctx.send(kbc.TWISTEDCASTLE)

  @w3.command()
  async def xera(self, ctx):
    """Xera"""
    await ctx.send(kbc.XERA)

  #W4 Commands
  @w4.command()
  async def cairn(self, ctx):
    """Cairn The Indomitable"""
    await ctx.send(kbc.CAIRN)

  @w4.command()
  async def overseer(self, ctx):
    """Mursaat Overseer"""
    await ctx.send(kbc.OVERSEER)

  @w4.command()
  async def samarog(self, ctx):
    """Samarog"""
    await ctx.send(kbc.SAMAROG)

  @w4.command()
  async def deimos(self, ctx):
    """Deimos"""
    await ctx.send(kbc.DEIMOS)

  #W5 Commands
  @w5.command()
  async def sh(self, ctx):
    """Soulless Horror"""
    await ctx.send(kbc.SOULESSHORROR)

  @w5.command()
  async def river(self, ctx):
    """River of Souls"""
    await ctx.send(kbc.RIVEROFSOULS)

  @w5.command()
  async def statues(self, ctx):
    """Statues of Grenth"""
    await ctx.send(kbc.STATUES)

  @w5.command()
  async def dhuum(self, ctx):
    """Dhuum"""
    await ctx.send(kbc.DHUUM)

  #W6 Commands
  @w6.command()
  async def ca(self, ctx):
    """Conjured Amalgamate"""
    await ctx.send(kbc.CA)

  @w6.command()
  async def twinlargos(self, ctx):
    """Twin Largos"""
    await ctx.send(kbc.TWINLARGOS)

  @w6.command()
  async def qadim(self, ctx):
    """Qadim"""
    await ctx.send(kbc.QADIM)

  #W7 Commands
  @w7.command()
  async def gates(self, ctx):
    """Gates of Ahdashim"""
    await ctx.send(kbc.GATES)
  @w7.command()
  async def adina(self, ctx):
    """Cardinal Adina"""
    await ctx.send(kbc.ADINA)

  @w7.command()
  async def sabir(self, ctx):
    """Cardinal Sabir"""
    await ctx.send(kbc.SABIR)

  @w7.command()
  async def qtp(self, ctx):
    """Qadim The Peerless"""
    await ctx.send(kbc.QTP)

  @commands.command()
  async def cairncircles(self, ctx):
    """Cairn green circle rotation"""
    await ctx.send(kbc.CAIRNCIRCLES)

  @commands.command()
  async def lamp(self, ctx):
    """Q1 Lamp Paths"""
    await ctx.send(kbc.LAMP)

  @commands.command()
  async def svbuttons(self, ctx):
    """Spirit Vale button locations"""
    await ctx.send(kbc.SVBUTTONS)

  @commands.command()
  async def tcmap(self, ctx):
    """Twisted Castle Map"""
    await ctx.send(kbc.TCMAP)

  @commands.command()
  async def xeratank(self, ctx):
    """Xera Tanking Map"""
    await ctx.send(kbc.XERATANK)

def setup(bot):
  bot.add_cog(Raid_Bosses(bot))