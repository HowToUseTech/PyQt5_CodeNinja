import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have signed in successfully as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('o!help'):
        await message.channel.send('My name is C360 Order Bot! I take orders for this virtual restaurant! Please go to <#944189983068151808> for the menu and order something in <#944161441206910977> or <#944162295368548384>! My prefix is `o!`.')
    if message.content.startswith('o!pizza'):
        await message.channel.send('Ordered Pizza, please pay <@897003966024531989> 200 Coins.')
    if message.content.startswith('o!burger'):
        await message.channel.send('Ordered Burger, please pay <@897003966024531989> 36 Coins.')
    if message.content.startswith('o!fries'):
        await message.channel.send('Ordered French Fries, please pay <@897003966024531989> 29 Coins.')
    if message.content.startswith('o!coke'):
        await message.channel.send('Ordered Coke, please pay <@897003966024531989> 10 Coins.')
    if message.content.startswith('o!taco'):
        await message.channel.send('Ordered French Fries, please pay <@897003966024531989> 40 Coins.')
    if message.content.startswith('o!mdew'):
        await message.channel.send('Ordered Mountain Dew, please pay <@897003966024531989> 10 Coins.')
    if message.content.startswith('o!chicken'):
        await message.channel.send('Ordered Chicken, please pay <@897003966024531989> 110 Coins.')
    if message.content.startswith('o!tea'):
        await message.channel.send('Ordered Tea, please pay <@897003966024531989> 25 Coins.')
    if message.content.startswith('o!coffee'):
        await message.channel.send('Ordered Coffee, please pay <@897003966024531989> 25 Coins.')
    if message.content.startswith('o!bread'):
        await message.channel.send('Ordered Bread, please pay <@897003966024531989> 35 Coins.')
    if message.content.startswith('o!breadjam'):
        await message.channel.send('Ordered Bread with Jam, please pay <@897003966024531989> 36 Coins.')
    if message.content.startswith('o!sandwich'):
        await message.channel.send('Ordered Sandwich, please pay <@897003966024531989> 30 Coins.')
    if message.content.startswith('o!falooda'):
        await message.channel.send('Ordered Falooda, please pay <@897003966024531989> 27 Coins.')
client.run('oYQg0EhduDdXo3aHKtBib6TmzQpHwllN')