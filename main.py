import os
import discord

my_secret = os.environ['DC_TOKEN']
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game('APU BCC'))
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    guild = member.guild
    avatar = member.display_avatar.url
    welcome_channel = client.get_channel(865938416285384764)
    verify_channel = client.get_channel(992415598048985159)
    rules_channel = client.get_channel(992415645855662141)
    introduce_channel = client.get_channel(919920851095277598)
    embed = discord.Embed(title="APU BCC welcomes you! 🤗", description=f"🔰 To get started in your blockchain/crypto journey here, checkout {verify_channel.mention} and get verified as a member to get full access to the server.\n\n📄 Follow the rules of the server by checking out {rules_channel.mention} to know the Dos and Don'ts.\n\n🗣️ Introduce yourself to let everyone know who you are at {introduce_channel.mention}!", color=discord.Color.from_rgb(231, 227, 216))
    embed.set_thumbnail(url=avatar)
    await welcome_channel.send(f'Hello 👋 {member.mention} welcome to {guild.name}!', embed=embed)
try:
    client.run(my_secret)
except Exception as e:
    print(e)
