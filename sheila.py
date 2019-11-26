from discord.ext import commands
import discord
from weather import days, Weatherday
from current import (
    date,
    img,
    condition,
    pressure,
    tendency,
    temperature,
    dew,
    humidity,
    wind,
    visibility,
)
from settings import TOKEN

bot = commands.Bot(command_prefix="sheila ")


@bot.command()
async def week(ctx):
    weekly_embed = discord.Embed(
        title="Weather Report", description=f"Last Updated {date}", color=0xDBE6FF
    )

    for day in days:
        report = Weatherday(day)
        weekly_embed.add_field(name=report.date(), value=report.info, inline=False)

    await ctx.send(embed=weekly_embed)


@bot.command()
async def current(ctx):
    current_embed = discord.Embed(
        title="Current Weather", description=f"Last Updated {date}", color=0xDBE6FF
    )
    current_embed.set_thumbnail(url=img)

    current_embed.add_field(name="Temperature", value=temperature, inline=True)
    current_embed.add_field(name="Condition", value=condition, inline=True)
    current_embed.add_field(name="Tendency", value=tendency, inline=True)
    current_embed.add_field(name="Wind", value=wind, inline=True)
    current_embed.add_field(name="Dew", value=dew, inline=True)
    current_embed.add_field(name="Visibility", value=visibility, inline=True)
    current_embed.add_field(name="Humidity", value=humidity, inline=True)
    current_embed.add_field(name="Pressure", value=pressure, inline=True)

    await ctx.send(embed=current_embed)


@bot.event
async def on_ready():
    print(f"Bot ready and logged in as {bot.user}.")


bot.run(TOKEN)
