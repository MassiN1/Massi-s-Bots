#Bot by @MassiBeast

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from discord.voice_client import VoiceClient
import random

bot = commands.Bot(command_prefix="!")
Owner = "261032113770463232"

@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))
    game = ("Massi's Bots")
    await bot.change_presence(game=discord.Game(name=game))

@bot.command(pass_context=True)
async def embed(ctx, *, msg: str = None):
    if msg == None:
        return discord.Embed(title="You didnt give me anything to say!")
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title=msg)
        await bot.say(embed=embed)
        print("Bot embed a users message")

@bot.command(pass_context=True)
async def Embed(ctx, *, msg: str = None):
    if msg == None:
        return discord.Embed(title="You didnt give me anything to say!")
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title=msg)
        await bot.say(embed=embed)
        print("Bot embed a users message")

@bot.command(pass_context=True)
async def game(ctx, *, msg: str = None):
        await bot.change_presence(game=discord.Game(name=msg))

@bot.command(pass_context=True)
async def Game(ctx, *, msg: str = None):
        await bot.change_presence(game=discord.Game(name=msg))

@bot.command(pass_context=True)
async def coin(ctx):
    choice = random.randint(1,2)
    if choice == 1:
        embed = discord.Embed(title="The coin landed on Heads! :cd:")
        await bot.say(embed=embed)
        print("Bot Played heads or tails")
    if choice == 2:
        embed = discord.Embed(title="The coin landed on Tails! :dvd:")
        await bot.say(embed=embed)
        print("Bot Played heads or tails")

@bot.command(pass_context=True)
async def Coin(ctx):
    choice = random.randint(1,2)
    if choice == 1:
        embed = discord.Embed(title="The coin landed on Heads! :cd:")
        await bot.say(embed=embed)
        print("Bot Played heads or tails")
    if choice == 2:
        embed = discord.Embed(title="The coin landed on Tails! :dvd:")
        await bot.say(embed=embed)
        print("Bot Played heads or tails")

@bot.command(pass_context=True)
async def person(ctx):
    await bot.say("⠀⠀⠀⠀⣠⣦⣤⣀")
    await bot.say("⠀⠀⠀⠀⢡⣤⣿⣿")
    await bot.say("⠀⠀⠀⠀⠠⠜⢾⡟")
    await bot.say("⠀⠀⠀⠀⠀⠹⠿⠃⠄")
    await bot.say("⠀⠀⠈⠀⠉⠉⠑⠀⠀⠠⢈⣆")
    await bot.say("⠀⠀⣄⠀⠀⠀⠀⠀⢶⣷⠃⢵")
    await bot.say("⠐⠰⣷⠀⠀⠀⠀⢀⢟⣽⣆⠀⢃")
    await bot.say("⠰⣾⣶⣤⡼⢳⣦⣤⣴⣾⣿⣿⠞")
    await bot.say("⠀⠈⠉⠉⠛⠛⠉⠉⠉⠙⠁")
    await bot.say("⠀⠀⡐⠘⣿⣿⣯⠿⠛⣿⡄")
    await bot.say("⠀⠀⠁⢀⣄⣄⣠⡥⠔⣻⡇")
    await bot.say("⠀⠀⠀⠘⣛⣿⣟⣖⢭⣿⡇")
    await bot.say("⠀⠀⢀⣿⣿⣿⣿⣷⣿⣽⡇")
    await bot.say("⠀⠀⢸⣿⣿⣿⡇⣿⣿⣿⣇")
    await bot.say("⠀⠀⠀⢹⣿⣿⡀⠸⣿⣿⡏")
    await bot.say("⠀⠀⠀⢸⣿⣿⠇⠀⣿⣿⣿")
    await bot.say("⠀⠀⠀⠈⣿⣿⠀⠀⢸⣿⡿")
    await bot.say("⠀⠀⠀⠀⣿⣿⠀⠀⢀⣿⡇")
    await bot.say("⠀⣠⣴⣿⡿⠟⠀⠀⢸⣿⣷")
    await bot.say("⠀⠉⠉⠁⠀⠀⠀⠀⢸⣿⣿⠁")
    await bot.say("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈")
    print ("Dotted person was shown")

@bot.command(pass_context=True)
async def Person(ctx):
    await bot.say("⠀⠀⠀⠀⣠⣦⣤⣀")
    await bot.say("⠀⠀⠀⠀⢡⣤⣿⣿")
    await bot.say("⠀⠀⠀⠀⠠⠜⢾⡟")
    await bot.say("⠀⠀⠀⠀⠀⠹⠿⠃⠄")
    await bot.say("⠀⠀⠈⠀⠉⠉⠑⠀⠀⠠⢈⣆")
    await bot.say("⠀⠀⣄⠀⠀⠀⠀⠀⢶⣷⠃⢵")
    await bot.say("⠐⠰⣷⠀⠀⠀⠀⢀⢟⣽⣆⠀⢃")
    await bot.say("⠰⣾⣶⣤⡼⢳⣦⣤⣴⣾⣿⣿⠞")
    await bot.say("⠀⠈⠉⠉⠛⠛⠉⠉⠉⠙⠁")
    await bot.say("⠀⠀⡐⠘⣿⣿⣯⠿⠛⣿⡄")
    await bot.say("⠀⠀⠁⢀⣄⣄⣠⡥⠔⣻⡇")
    await bot.say("⠀⠀⠀⠘⣛⣿⣟⣖⢭⣿⡇")
    await bot.say("⠀⠀⢀⣿⣿⣿⣿⣷⣿⣽⡇")
    await bot.say("⠀⠀⢸⣿⣿⣿⡇⣿⣿⣿⣇")
    await bot.say("⠀⠀⠀⢹⣿⣿⡀⠸⣿⣿⡏")
    await bot.say("⠀⠀⠀⢸⣿⣿⠇⠀⣿⣿⣿")
    await bot.say("⠀⠀⠀⠈⣿⣿⠀⠀⢸⣿⡿")
    await bot.say("⠀⠀⠀⠀⣿⣿⠀⠀⢀⣿⡇")
    await bot.say("⠀⣠⣴⣿⡿⠟⠀⠀⢸⣿⣷")
    await bot.say("⠀⠉⠉⠁⠀⠀⠀⠀⢸⣿⣿⠁")
    await bot.say("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈")
    await bto.add_reaction('')
    print ("Dotted person was shown")

@bot.command(pass_context=True)
async def ping(ctx):
    embed = discord.Embed(title=":ping_pong: Pong!")
    await bot.say(embed=embed)
    print ("User has pinged")

@bot.command(pass_context=True)
async def Ping(ctx):
    embed = discord.Embed(title=":ping_pong: Pong!")
    await bot.say(embed=embed)
    print ("User has pinged")

@bot.command(pass_context=True)
async def kms(ctx):
    embed = discord.Embed(title=":weary: :gun: GoodBye")
    await bot.say(embed=embed)
    print ("User killed themself")

@bot.command(pass_context=True)
async def Kms(ctx):
    embed = discord.Embed(title=":weary: :gun: GoodBye")
    await bot.say(embed=embed)
    print ("User killed themself")

@bot.command(pass_context=True)
async def steam(ctx):
    embed = discord.Embed(title="The bot maker's steam http://steamcommunity.com/id/MassiN1")
    await bot.say(embed=embed)
    print ("User got the creators steam details")

@bot.command(pass_context=True)
async def Steam(ctx):
    embed = discord.Embed(title="The bot maker's steam http://steamcommunity.com/id/MassiN1")
    await bot.say(embed=embed)
    print ("User got the creators steam details")

@bot.command(pass_context=True)
async def hi(ctx):
    embed = discord.Embed(title=":yum: Hey!")
    await bot.say(embed=embed)
    print ("User said hi")

@bot.command(pass_context=True)
async def Hi(ctx):
    embed = discord.Embed(title=":yum: Hey!")
    await bot.say(embed=embed)
    print ("User said hi")

@bot.command(pass_context=True)
async def hello(ctx):
    embed = discord.Embed(title=":yum: Hello!")
    await bot.say(embed=embed)
    print ("User said hello")

@bot.command(pass_context=True)
async def Hello(ctx):
    embed = discord.Embed(title=":yum: Hello!")
    await bot.say(embed=embed)
    print ("User said hello")

@bot.command(pass_context=True)
async def fortnite(ctx):
    embed = discord.Embed(title="here is the download link for Fortnite Battle Royale - https://www.epicgames.com/unrealtournament/download")
    await bot.say(embed=embed)
    print ("User requasted frotnite download link")

@bot.command(pass_context=True)
async def Fortnite(ctx):
    embed = discord.Embed(title="here is the download link for Fortnite Battle Royale - https://www.epicgames.com/unrealtournament/download")
    await bot.say(embed=embed)
    print ("User requasted frotnite download link")

@bot.command(pass_context=True)
async def rps_paper(ctx):
    choice = random.randint(0,6)
    if choice == 1:
        embed = discord.Embed(title="You chose Paper :page_facing_up: . I chose Paper :page_facing_up: . Its a Draw!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 2:
        embed = discord.Embed(title="You chose Paper :page_facing_up: . I chose Rock :full_moon: . You Win!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 3:
        embed = discord.Embed(title="You chose Paper :page_facing_up: . I chose Scissors :scissors: . I Win!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 4:
        embed = discord.Embed(title="You chose Paper :page_facing_up: . I chose Scissors :scissors: . I Win!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 5:
        embed = discord.Embed(title="You chose Paper :page_facing_up: . I chose Paper :page_facing_up: . Its a Draw!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 6:
        embed = discord.Embed(title="You chose Paper :page_facing_up: . I chose Rock :full_moon: . You Win!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")

@bot.command(pass_context=True)
async def Rps_paper(ctx):
    choice = random.randint(0,6)
    if choice == 1:
        embed = discord.Embed(title="You chose Paper :page_facing_up: . I chose Paper :page_facing_up: . Its a Draw!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 2:
        embed = discord.Embed(title="You chose Paper :page_facing_up: . I chose Rock :full_moon: . You Win!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 3:
        embed = discord.Embed(title="You chose Paper :page_facing_up: . I chose Scissors :scissors: . I Win!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
        print ("Paper vs Rock - Player Wins")
    if choice == 4:
        embed = discord.Embed(title="You chose Paper :page_facing_up: . I chose Scissors :scissors: . I Win!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 5:
        embed = discord.Embed(title="You chose Paper :page_facing_up: . I chose Paper :page_facing_up: . Its a Draw!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 6:
        embed = discord.Embed(title="You chose Paper :page_facing_up: . I chose Rock :full_moon: . You Win!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")

@bot.command(pass_context=True)
async def rps_rock(ctx):
    choice = random.randint(0,6)
    if choice == 1:
        embed = discord.Embed(title="You chose Rock :full_moon: . I chose Paper :page_facing_up: . I Win!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 2:
        embed = discord.Embed(title="You chose Rock :full_moon: . I chose Rock :full_moon: . Its a Draw!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 3:
        embed = discord.Embed(title="You chose Rock :full_moon: . I chose Scissors :scissors: . You Win!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 4:
        embed = discord.Embed(title="You chose Rock :full_moon: . I chose Scissors :scissors: . You Win!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 5:
        embed = discord.Embed(title="You chose Rock :full_moon: . I chose Paper :page_facing_up: . I Win!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 6:
        embed = discord.Embed(title="You chose Rock :full_moon: . I chose Rock :full_moon: . Its a Draw!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")

@bot.command(pass_context=True)
async def Rps_rock(ctx):
    choice = random.randint(0,6)
    if choice == 1:
        embed = discord.Embed(title="You chose Rock :full_moon: . I chose Paper :page_facing_up: . I Win!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 2:
        embed = discord.Embed(title="You chose Rock :full_moon: . I chose Rock :full_moon: . Its a Draw!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 3:
        embed = discord.Embed(title="You chose Rock :full_moon: . I chose Scissors :scissors: . You Win!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 4:
        embed = discord.Embed(title="You chose Rock :full_moon: . I chose Scissors :scissors: . You Win!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 5:
        embed = discord.Embed(title="You chose Rock :full_moon: . I chose Paper :page_facing_up: . I Win!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 6:
        embed = discord.Embed(title="You chose Rock :full_moon: . I chose Rock :full_moon: . Its a Draw!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")

@bot.command(pass_context=True)
async def rps_scissors(ctx):
    choice = random.randint(0,6)
    if choice == 1:
        embed = discord.Embed(title="You chose Scissors :scissors: . I chose Paper :page_facing_up: . You Win!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 2:
        embed = discord.Embed(title="You chose Scissors :scissors: . I chose Rock :full_moon: . I Win!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 3:
        embed = discord.Embed(title="You chose Scissors :scissors: . I chose Scissors :scissors: . Draw!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 4:
        embed = discord.Embed(title="You chose Scissors :scissors: . I chose Scissors :scissors: . Draw")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 5:
        embed = discord.Embed(title="You chose Scissors :scissors: . I chose Paper :page_facing_up: . You Win!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 6:
        embed = discord.Embed(title="You chose Scissors :scissors: . I chose Rock :full_moon: . I Win!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")

@bot.command(pass_context=True)
async def Rps_scissors(ctx):
    choice = random.randint(0,6)
    if choice == 1:
        embed = discord.Embed(title="You chose Scissors :scissors: . I chose Paper :page_facing_up: . You Win!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 2:
        embed = discord.Embed(title="You chose Scissors :scissors: . I chose Rock :full_moon: . I Win!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 3:
        embed = discord.Embed(title="You chose Scissors :scissors: . I chose Scissors :scissors: . Draw!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 4:
        embed = discord.Embed(title="You chose Scissors :scissors: . I chose Scissors :scissors: . Draw")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 5:
        embed = discord.Embed(title="You chose Scissors :scissors: . I chose Paper :page_facing_up: . You Win!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")
    if choice == 6:
        embed = discord.Embed(title="You chose Scissors :scissors: . I chose Rock :full_moon: . I Win!")
        await bot.say(embed=embed)
        print("Bot Played Rock Paper Scissors")

@bot.command(pass_context=True)
async def invite(ctx):
    embed = discord.Embed(title=":gear: https://discordapp.com/oauth2/authorize?client_id=415705846870441987&scope=bot&permissions=2146958591 :gear:")
    await bot.say(embed=embed)
    print ("User Requested Discord invite Link")

@bot.command(pass_context=True)
async def Invite(ctx):
    embed = discord.Embed(title=":gear: https://discordapp.com/oauth2/authorize?client_id=415705846870441987&scope=bot&permissions=2146958591 :gear:")
    await bot.say(embed=embed)
    print ("User Requested Discord invite Link")


@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's info on {}.".format(user.name), color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.add_field(name="Current Game", value=user.game)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
    print ("User requested a users info")

@bot.command(pass_context=True)
async def Info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's info on {}.".format(user.name), color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.add_field(name="Current Game", value=user.game)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
    print ("User requested a users info")

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here is the info about {}.".format(ctx.message.server.name), color=0x00ff00)
    embed.set_author(name="Massi Bots")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)
    print ("User requested the server info")

@bot.command(pass_context=True)
async def Serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here is the info about {}.".format(ctx.message.server.name), color=0x00ff00)
    embed.set_author(name="Massi Bots")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)
    print ("User requested the server info")

@bot.command(pass_context=True)
async def Help(ctx):
    embed = discord.Embed(name="Help Commands", description="Here is the commands for Massi Bots.", color=0x00ff00)
    embed.set_author(name="Massi Bots")
    embed.add_field(name="!Help", value="Shows all the commands for the Bot", inline=True)
    embed.add_field(name="!Hi/hello", value="Say hi to the Bot")
    embed.add_field(name="!Invite", value="Gives an invite link for the Bot", inline=True)
    embed.add_field(name="!Rps_(add R, P or S)", value="Do Rock Paper Scissors with the Bot", inline=True)
    embed.add_field(name="!Fortnite", value="Get the download link for Fortnite Battle Royale")
    embed.add_field(name="!Steam", value="Add the bot maker as a Steam Friend")
    embed.add_field(name="!Bff", value="Find out who the bots bestie is")
    embed.add_field(name="!Info", value="Shows the info of the mentioned user")
    embed.add_field(name="!Serverinfo", value="Shows info of the current server")
    await bot.say(embed=embed)
    print ("User requested all the commands")

@bot.command(pass_context=True)
@commands.has_role("Admin")
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya {}. Get the boot!".format(user.name))
    await bot.kick(user)
    print ("Admin kicked a user")

@bot.command(pass_context=True)
@commands.has_role("Admin")
async def Kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya {}. Get the boot!".format(user.name))
    await bot.kick(user)
    print ("Admin kicked a user")

@bot.command(pass_context=True)
@commands.has_role("Admin")
async def ban(ctx, user: discord.Member):
    await bot.say(":hammer_pick: {} got struck by the Banhammer!".format(user.name))
    await bot.ban(user)
    print ("Admin baned a user")

@bot.command(pass_context=True)
@commands.has_role("Admin")
async def Ban(ctx, user: discord.Member):
    await bot.say(":hammer_pick: {} got struck by the Banhammer!".format(user.name))
    await bot.ban(user)
    print ("Admin baned a user")

bot.run("NDE1NzA1ODQ2ODcwNDQxOTg3.DW51iA.0Imi5GWWrFkcuFLd57psI8NOa0Y")
