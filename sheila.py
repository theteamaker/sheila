from discord.ext import commands
import discord
from weather import Weatherday, Weatherdays, Current
from settings import TOKEN, WEATHER_URL, IMAGE_STORE_URL, SQL_DATABASE
import requests
from argument_constructor import argument_constructor
from search import get_search_data, refresh, cities, provinces
import time
from help_embeds import help_current, help_week, help_embed
from titlecase import titlecase
import numpy as np
import dataset

db = dataset.connect(SQL_DATABASE)
bot = commands.Bot(command_prefix="sheila ")
get_search_data()  # at startup, get the search data

table = db['servers']

@bot.command()
async def week(ctx, *, arg=""):
    default = table.find_one(server=str(ctx.guild.id))['default']
    
    if arg == "":
        constructed_argument = argument_constructor(default)
    else:
        constructed_argument = argument_constructor(arg)
    
    if constructed_argument == 404:  # returning an error for things not found
        msg = await ctx.send(
            "Something went wrong. try `sheila info current` for help with this command."
        )
        time.sleep(4)
        await msg.delete()
        return

    url = constructed_argument[1]
    province_name = constructed_argument[0]

    reference = Weatherdays(url)

    weekly_embed = discord.Embed(title=f"Weather Report for {province_name}", color=0xDBE6FF)

    weekly_embed.set_author(
        name="Provided by Environment Canada", url="https://weather.gc.ca/"
    )

    weekly_embed.set_footer(text=f"Last updated {Current(url).date}")

    for day in reference.days:
        report = Weatherday(day)
        weekly_embed.add_field(name=report.date(), value=report.info, inline=False)

    await ctx.send(embed=weekly_embed)


@bot.command()
async def current(ctx, *, arg=""):
    default = table.find_one(server=str(ctx.guild.id))['default']

    if arg == "":
        constructed_argument = argument_constructor(default)
    else:
        constructed_argument = argument_constructor(arg)

    if constructed_argument == 404:  # returning an error for things not found
        msg = await ctx.send(
            "Something went wrong. try `sheila info current` for help with this command."
        )
        time.sleep(4)
        await msg.delete()
        return

    url = constructed_argument[1]
    province_name = constructed_argument[0]

    reference = Current(url)

    today_text = Weatherday(Weatherdays(WEATHER_URL).days[0]).info

    current_embed = discord.Embed(
        title=f"Current Weather in {province_name}",
        description=today_text,
        color=0xDBE6FF,
    )

    image_number = reference.image.strip("https://weather.gc.ca/weathericons/").strip(
        ".gif"
    )

    current_embed.set_thumbnail(url="{}{}.jpg".format(IMAGE_STORE_URL, image_number))

    current_embed.set_footer(text=f"Last updated {reference.date}")

    details = reference.data

    for detail in details.items():
        current_embed.add_field(name=detail[0], value=detail[1], inline=True)

    current_embed.set_author(
        name="Provided by Environment Canada", url="https://weather.gc.ca/"
    )

    await ctx.send(embed=current_embed)


@bot.command(name="refresh")
async def searchrefresh(ctx):
    try:
        refresh()
        msg = await ctx.send(
            "The list of cities/provinces to index has been refreshed. (Keep in mind: you usually shouldn't ever need to use this.)"
        )
        time.sleep(4)
        await msg.delete()
    except:
        msg = await ctx.send(
            "For unknown reasons, the refresh has failed. Please report the issue at Sheila's GitHub page."
        )
        time.sleep(4)
        await msg.delete()

@bot.command()
async def info(ctx, arg=""):
    if arg == "":
        await ctx.send(embed=help_embed)

    arguments = {
        "current": help_current,
        "week": help_week,
    }

    for argument in arguments.items():
        if arg == argument[0]:
            await ctx.send(embed=argument[1])

@bot.command(name="cities")
async def cities_cmd(ctx, *, arg=""):
    if arg == "":
        return
    
    if arg.lower() in [province[1]["ID"].lower() for province in provinces.items()]:
        cities_list = []

        for city in cities[arg.upper()]:
            cities_list.append(titlecase(city))

        embeds = np.array_split(np.array(cities_list), 3)

        cities_embed = discord.Embed(
            title="Cities in {}".format(arg.upper()), 
            color=0xDBE6FF
        )


        for embed in embeds:
            text = ""
            for city in embed:
                text += "{}\n".format(city)
            cities_embed.add_field(
                name='Cities',
                value=text,
                inline=True
            )

        cities_embed.set_author(
        name="Provided by Environment Canada", url="https://weather.gc.ca/"
        )

        await ctx.send(embed=cities_embed)
    else:
        await ctx.send("Country code not found in database.")

@bot.command(name="set")
async def setdefault(ctx, *, arg=""):
    if arg == "":
        return

    server_id = ctx.guild.id
    default = arg

    if argument_constructor(default) == 404:
        await ctx.send("Invalid argument received - default couldn't be set.")
        return
    
    table_entry = table.find_one(server=str(server_id))
    
    if table_entry == None:
        table.insert(dict(server=str(server_id), default=arg))
        await ctx.send("**Success!** Default location has been stored.")
        return
    else:
        table.update(dict(server=str(server_id), default=arg), ['server'])
        await ctx.send("**Success!** Default location has been updated.")
        return
    
@bot.event
async def on_ready():
    print(f"Bot ready and logged in as {bot.user}.")

bot.run(TOKEN)
