import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!', intents=intents)




# Config section (change to your liking)

# Role names
Role1 = "Role 1"
Role2 = "Role 2"
Role3 = "Role 3"

# Emoji's used to react to message
Emoji1 = "🔴"
Emoji2 = "🟢"
Emoji3 = "🟣"

# Bot token
Token = "MTA1MzA4NzU0MTkxOTc1MjIzMg.GDZHNL.DyB3MPyZqkMV9TYV2fjU2E4WJTxs4HcUYB1KOo"








@client.command()
async def create_roles(ctx):
    # Create the three roles
    role1 = await ctx.guild.create_role(name=Role1)
    role2 = await ctx.guild.create_role(name=Role2)
    role3 = await ctx.guild.create_role(name=Role3)


@client.command()
async def ask_roles(ctx):

    # Get the message to delete
    message = ctx.message

    # Delete the message
    await message.delete()

    # Get the channel where the message will be sent
    channel = ctx.message.channel

    # Send the message with the emojis
    message = await channel.send("Which role do you want?")

    # Add the reactions to the message (u can change these)
    await message.add_reaction(Emoji1)
    await message.add_reaction(Emoji2)
    await message.add_reaction(Emoji3)

@client.event
async def on_reaction_add(reaction, user):
    # Check if the reaction is one of the emojis we added
    if str(reaction.emoji) == Emoji1:
        role = discord.utils.get(user.guild.roles, name=Role1)
    elif str(reaction.emoji) == Emoji2:
        role = discord.utils.get(user.guild.roles, name=Role2)
    elif str(reaction.emoji) == Emoji3:
        role = discord.utils.get(user.guild.roles, name=Role3)
    else:
        # If the reaction is not one of the emojis we added, do nothing
        return

    # Add the role to the user
    await user.add_roles(role)

client.run(Token)
