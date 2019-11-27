from discord.ext import commands
import discord
from weather import Weatherday, Weatherdays, Current
from settings import TOKEN, WEATHER_URL, IMAGE_STORE_URL
import requests

bot = commands.Bot(command_prefix="sheila ")


@bot.command()
async def week(ctx):
    reference = Weatherdays(WEATHER_URL)

    weekly_embed = discord.Embed(title="Weather Report", color=0xDBE6FF)

    weekly_embed.set_author(
        name="Provided by Environment Canada", url="https://weather.gc.ca/"
    )

    weekly_embed.set_footer(text=f"Last updated {Current(WEATHER_URL).date}")

    for day in reference.days:
        report = Weatherday(day)
        weekly_embed.add_field(name=report.date(), value=report.info, inline=False)

    await ctx.send(embed=weekly_embed)


@bot.command()
async def current(ctx):
    reference = Current(WEATHER_URL)

    current_embed = discord.Embed(title="Current Weather", color=0xDBE6FF)

    image_number = reference.image.strip("https://weather.gc.ca/weathericons/").strip(
        ".gif"
    )

    current_embed.set_thumbnail(url="{}{}.jpg".format(IMAGE_STORE_URL, image_number))

    current_embed.set_footer(text=f"Last updated {reference.date}")

    details = {
        "Temperature": reference.temperature,
        "Condition": reference.condition,
        "Tendency": reference.tendency,
        "Wind": reference.wind,
        "Dew": reference.dew,
        "Visibility": reference.visibility,
        "Humidity": reference.humidity,
        "Pressure": reference.pressure,
    }

    for detail in details.items():
        current_embed.add_field(name=detail[0], value=detail[1], inline=True)

    current_embed.set_author(
        name="Provided by Environment Canada", url="https://weather.gc.ca/"
    )

    await ctx.send(embed=current_embed)


@bot.event
async def on_ready():
    print(f"Bot ready and logged in as {bot.user}.")


bot.run(TOKEN)