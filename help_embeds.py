import discord

#current-specific embed help
help_current = discord.Embed(
        title=f"sheila current <provincial code> <city>",
        description="Neither parameters are case-sensitive. To find a list of cities within a province, type `sheila cities <provincial code>`.",
        color=0xDBE6FF,
    )

help_current.set_author(name="GitHub", url="http://github.com/theteamaker/sheila")

help_current.add_field(
    name="Provincial Codes",
    value="AB (Alberta)\nBC (British Columbia)\nMB (Manitoba)\nNB (New Brunswick)\nNL (Newfoundland)\nNT (Northwest Territories)\nNS (Nova Scotia)\nNU (Nunavut)\nON (Ontario)\nPE (Prince Edward Island)\nQC (Quebec)\nSK (Saskatchewan)\nYT (Yukon)",
    inline=False
)

#week-specific embed help
help_week = discord.Embed(
        title=f"sheila week <provincial code> <city>",
        description="Neither parameters are case-sensitive. To find a list of cities within a province, type `sheila cities <provincial code>`.",
        color=0xDBE6FF,
    )

help_week.set_author(name="GitHub", url="http://github.com/theteamaker/sheila")

help_week.add_field(
    name="Provincial Codes",
    value="AB (Alberta)\nBC (British Columbia)\nMB (Manitoba)\nNB (New Brunswick)\nNL (Newfoundland)\nNT (Northwest Territories)\nNS (Nova Scotia)\nNU (Nunavut)\nON (Ontario)\nPE (Prince Edward Island)\nQC (Quebec)\nSK (Saskatchewan)\nYT (Yukon)",
    inline=False
)

#general help embed
help_embed = discord.Embed(
    title="Sheila's Commands",
    description="designed by the super amateur but still cool teamaker.",
    color=0xDBE6FF
)

help_fields = {
    "current": "Displays the current weather in a given location.\n`sheila current` defaults to the specified default for the server.\n`sheila current <provincial code> <city>` displays information for other places.",
    "week": "Displays the weekly weather for a given location.\nCustom locations work in the same way as the current command.",
    "refresh": "Refreshes the map Sheila pulls from to get info. This should like, never be used, unless a new province gets added, ~~or Quebec finally leaves~~",
    "cities": "`cities <provincial_code>` outputs a list of cities in a province whose weather you can search for.",
    "set": "`set <provincial code> <city>` sets the default city to get the weather from for this server."
}

for help_field in help_fields.items():
    help_embed.add_field(
        name=help_field[0],
        value=help_field[1],
        inline=False
    )

help_embed.set_author(name="GitHub", url="http://github.com/theteamaker/sheila")