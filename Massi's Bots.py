import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
Owner = "261032113770463232"

@bot.event
async def on_ready() :
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))
    print('Ready to do some Deleten')

@bot.event
async def on_message(message):
    await bot.delete_message(message)

@bot.command(pass_context=True)
async def delete(ctx)
    await bot.delete_message
        await bot.delete_message


bot.run("NDE1NzA1ODQ2ODcwNDQxOTg3.DW51iA.0Imi5GWWrFkcuFLd57psI8NOa0Y")
