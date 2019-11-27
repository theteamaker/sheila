from discord.ext import commands
import discord
from weather import Weatherday, Weatherdays
from current import Current
from settings import TOKEN, WEATHER_URL, IMAGE_STORE_URL
import requests

bot = commands.Bot(command_prefix="sheila ")


@bot.command()
async def week(ctx):
    reference = Weatherdays(WEATHER_URL)

    weekly_embed = discord.Embed(
        title="Weather Report", 
        color=0xDBE6FF
        )

    weekly_embed.set_author(
        name="Provided by Environment Canada", 
        url="https://weather.gc.ca/"
    )

    weekly_embed.set_footer(
        text=f"Last updated {Current(WEATHER_URL).date}"
    )

    for day in reference.days:
        report = Weatherday(day)
        weekly_embed.add_field(
            name=report.date(), 
            value=report.info, 
            inline=False
        )

    await ctx.send(
        embed=weekly_embed
    )


@bot.command()
async def current(ctx):
    reference = Current(WEATHER_URL)

    current_embed = discord.Embed(
        title="Current Weather", 
        color=0xDBE6FF
    )

    image_number = reference.image.strip("https://weather.gc.ca/weathericons/").strip(
        ".gif"
    )

    current_embed.set_thumbnail(
        url="{}{}.jpg".format(IMAGE_STORE_URL, image_number)
    )

    current_embed.set_footer(
        text=f"Last updated {reference.date}"
    )

    current_embed.add_field(
        name="Temperature", 
        value=reference.temperature, 
        inline=True
    )

    current_embed.add_field(
        name="Condition", 
        value=reference.condition, 
        inline=True
    )

    current_embed.add_field(
        name="Tendency", 
        value=reference.tendency, 
        inline=True
    )

    current_embed.add_field(
        name="Wind", 
        value=reference.wind, 
        inline=True
    )

    current_embed.add_field(
        name="Dew", 
        value=reference.dew, 
        inline=True
    )

    current_embed.add_field(
        name="Visibility", 
        value=reference.visibility, 
        inline=True
    )

    current_embed.add_field(
        name="Humidity", 
        value=reference.humidity, 
        inline=True
    )

    current_embed.add_field(
        name="Pressure", 
        value=reference.pressure, 
        inline=True
    )

    current_embed.set_author(
        name="Provided by Environment Canada", 
        url="https://weather.gc.ca/"
    )

    await ctx.send(
        embed=current_embed
    )


@bot.event
async def on_ready():
    print(f"Bot ready and logged in as {bot.user}.")


bot.run(TOKEN)