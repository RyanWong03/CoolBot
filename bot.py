import discord, token_1, openai, asyncio, requests, json, random, phrases
from bs4 import BeautifulSoup
intents = discord.Intents.all()
client = discord.Client(intents=intents)

#make translator and dictionary function, and try to make so bot can join vc and talk from list of phrases
#maybe make two bots that can talk to each other
#use uptime robot to make bot run 24/7
@client.event
async def on_ready():
    # models = openai.Model.list()
    # with open("pricing.txt", "w") as f:
    #     # Loop through all the models
    #     for model in models["data"]:
    #         # Get the name of the model
    #         model_name = model["id"]
            
    #         # Get the price of the model
    #         try:
    #             price = model["price"]["usd"]
    #         except KeyError:
    #             price = "Not available"
            
    #         # Write the name and price to the file
    #         f.write(f"{model_name}: {price}\n")
    game = discord.Game("Black ops 3")
    await client.change_presence(status=discord.Status.online, activity=game)
    print(f"Logged in as {client.user}")
    channel_id = 1037100059373862912 #general in pro's server
    channel = await client.fetch_channel(channel_id)
    file = discord.File("pic.png")

    debate_channel = 1037132084310966282 #debate chnanel in pro's server
    debate = await client.fetch_channel(debate_channel)
    my_user_id = 318132313672384512
    user = await client.fetch_user(my_user_id)
    mention = user.mention
    # await channel.send("wake up")
    #await channel.send(f'Damn {mention}, ya out of luck kid')
    # await channel.send(file = file)

@client.event
async def on_message(message):
    if message.mentions and message.mentions[0] == client.user:
        await message.channel.send(random.choice(phrases.phrases))
    
client.run(token_1.DISCORD_TOKEN)