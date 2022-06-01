from click import command
import discord
from discord.ext import commands
import dotenv
import os


bot = commands.Bot(
    command_prefix="+",
    intents=discord.Intents.default(),
    description="First like!"
)


@bot.command()
async def react(ctx: commands.Context, channel: discord.TextChannel, message_id: int, *emojis: discord.PartialEmoji):
    """Reacts to a message with a set of emojis."""
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("This command is only available to admins.")
        return
    
    message: discord.Message = await channel.fetch_message(message_id)
    existing_reactions = {reaction.emoji.name: reaction for reaction in message.reactions}

    added, failed = set(), set()
    for emoji in emojis:
        try:
            # Add to existing reaction if one exists with same name
            reaction = existing_reactions.get(emoji.name, emoji)
            await message.add_reaction(reaction)
            added.add(str(emoji))
        except discord.errors.HTTPException:
            failed.add(str(emoji))

    if len(failed) == 0:
        description = "All emojis added successfully"
    else:
        description = "Some emojis could not be added - check they are in the server's emoji list or already added to the message."

    embed = discord.Embed(title="Reacted", description=description, color=0xC9B6D9)
    if len(added) > 0:
        embed.add_field(name="Reactions added", value=" ".join(added), inline=False)
    if len(failed) > 0:
        embed.add_field(name="Reactions failed", value=" ".join(failed), inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def unreact(ctx: commands.Context, channel: discord.TextChannel, message_id: int, *emojis: discord.PartialEmoji):
    """Removes reactions from a message."""
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("This command is only available to admins.")
        return

    message = await channel.fetch_message(message_id)
    existing_reactions = {reaction.emoji.name: reaction for reaction in message.reactions}

    removed = set()
    for emoji in emojis:
        if emoji.name in existing_reactions:
            await message.remove_reaction(existing_reactions[emoji.name], bot.user)
            removed.add(str(emoji))
    
    embed = discord.Embed(title="Unreacted", description="All emojis removed successfully", color=0xC9B6D9)
    embed.add_field(name="Reactions removed", value=" ".join(removed), inline=False)
    await ctx.send(embed=embed)


# Load environment variables from .env
dotenv.load_dotenv()
TOKEN = os.environ["BOT_TOKEN"]
bot.run(TOKEN)
