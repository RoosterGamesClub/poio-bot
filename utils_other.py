import discord

def getDiscordColorFromString(color_str : str):
  if color_str == "" or color_str == "random":
    return discord.Color.random()

  if color_str == "default": return discord.Color.default()
  if color_str == "teal": return discord.Color.teal()
  if color_str == "dark_teal": return discord.Color.dark_teal()
  if color_str == "brand_green": return discord.Color.brand_green()
  if color_str == "green": return discord.Color.green()
  if color_str == "dark_green": return discord.Color.dark_green()
  if color_str == "blue": return discord.Color.blue()
  if color_str == "dark_blue": return discord.Color.dark_blue()
  if color_str == "purple": return discord.Color.purple()
  if color_str == "dark_purple": return discord.Color.dark_purple()
  if color_str == "magenta": return discord.Color.magenta()
  if color_str == "dark_magenta": return discord.Color.dark_magenta()
  if color_str == "gold": return discord.Color.gold
  if color_str == "dark_gold": return discord.Color
  if color_str == "orange": return discord.Color.orange
  if color_str == "dark_orange": return discord.Color.dark_orange
  if color_str == "brand_red": return discord.Color.brand_red()
  if color_str == "red": return discord.Color.red()
  if color_str == "dark_red": return discord.Color.dark_red()
  if color_str == "lighter_grey": return discord.Color.lighter_grey
  if color_str == "dark_grey": return discord.Color.dark_grey()
  if color_str == "light_grey": return discord.Color.light_grey()
  if color_str == "darker_grey": return discord.Color.darker_grey()
  if color_str == "og_blurple": return discord.Color.og_blurple()
  if color_str == "blurple": return discord.Color.blurple()
  if color_str == "dark_theme": return discord.Color.dark_theme()
  if color_str == "fuchsia": return discord.Color.fuchsia()
  if color_str == "yellow": return discord.Color.yellow()
  if color_str == "dark_embed": return discord.Color.dark_embed()
  if color_str == "light_embed": return discord.Color.light_embed()
  if color_str == "pink": return discord.Color.pink()
  
  return discord.Color.from_str(color_str)