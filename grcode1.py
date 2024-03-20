import  discord
from discord.ext import commands
import asyncio
from typing import Optional
from discord import Interaction, Member
from datetime import datetime, timedelta
from grcode2 import Add_3days,Add_4days,find_next_Monday,find_next_Sunday,find_next_Tuesday,find_next_Wednesday,find_next_Thursday,find_next_Friday,find_next_Saturday,March21_5am,March21_3pm,March21_4pm,March21_7pm,March19_5am,March19_3pm,March19_4pm,March19_7pm,March19_8pm,March22_3pm,March23_3pm,March18_7pm,March18_8pm,March18_5pm,March22_7pm,March21_8pm,March22_4pm,March20_4pm,March20_3pm
from grcode2 import tuesday_Saturday,March22_7am,March18_6pm,March22_6pm
from grcode2 import monday_friday
from grcode2 import tuesday_friday
from grcode2 import find_next_day,wednesday_saturday,first_thursday_of_next_month,thursday_sunday,be_weekly_thurs,wednesday_sunday,monday_thursday
import os
from keep_alive import keep_alive
keep_alive()

bot = commands.Bot()


@bot.slash_command(name='warbandit',description='Show the servers of warbandit')
async def warbandit(ctx, max: int = None, x: int = None):

    if max is None and x is None:
        from datetime import datetime, timedelta
        import datetime
        embed=discord.Embed(title="WarBandits Servers Wipe Times" , description="Here you can find information for all of warbandit servers, including connection information and wipe schedule.\n > Global Blueprints\nBlueprints wipe once a month on the first Thursday of each month on the forced wipe",color=0xe10505)
        given_timestamp=March21_5am
        Add_4days(given_timestamp)
        embed.add_field(name=':flag_au: AU 2X Trio', value=f'Next Wipe:\n<t:{Add_4days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n172.111.33.16:28010\n#Wipe Schedule:\nEvery 4 Days @ 3PM AEDT```', inline=True)
        given_timestamp=March19_5am
        Add_3days(given_timestamp)
        embed.add_field(name=':flag_au: AU 3X Trio', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n172.111.33.22:28010\n#Wipe Schedule:\nEvery 3 Days @ 3PM AEDT```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        given_timestamp=March21_5am
        Add_3days(given_timestamp)
        embed.add_field(name=':flag_au: AU 3X Quad', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n172.111.33.34:28010\n#Wipe Schedule:\nEvery 3 Days @ 3PM AEDT```', inline=True)

        
        url='https://warbandits.gg/assets/media/images/WarBanditsLogo.png'
        embed.set_thumbnail(url=url)
        await ctx.respond(embed=embed)
        embed=discord.Embed(title='WarBandits Servers Wipe Times',description='Here you can find information for all of warbandit servers, including connection information and wipe schedule.\n>Global Blueprints\nBlueprints wipe once a month on the first Thursday of each month on the forced wipe',color=0xe10505)
        given_timestamp=March21_3pm
        Add_4days(given_timestamp)
        embed.add_field(name=':flag_eu: EU 2X Solo', value=f'Next Wipe:\n<t:{Add_4days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n45.88.230.125:28010\n#Wipe Schedule:\nEvery 4 Days @ 2PM UTC```', inline=True)
        given_timestamp=March22_3pm
        Add_4days(given_timestamp)
        embed.add_field(name=':flag_eu: EU 2X Duo', value=f'Next Wipe:\n<t:{Add_4days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n64.52.81.16:28010\n#Wipe Schedule:\nEvery 4 Days @ 2PM UTC```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        
        given_timestamp=March19_3pm
        Add_4days(given_timestamp)
        embed.add_field(name=':flag_eu: EU 2X Trio', value=f'Next Wipe:\n<t:{Add_4days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n209.237.141.7:28010\n#Wipe Schedule:\nEvery 4 Days @ 2PM UTC```', inline=True)
        given_timestamp=March22_3pm
        Add_4days(given_timestamp)
        embed.add_field(name=':flag_eu: EU 2X Quad', value=f'Next Wipe:\n<t:{Add_4days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n209.237.141.7:28010\n#Wipe Schedule:\nEvery 4 Days @ 2PM UTC```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        

        given_timestamp=March21_3pm
        Add_4days(given_timestamp)
        embed.add_field(name=':flag_eu: EU 2X Max 5', value=f'Next Wipe:\n<t:{Add_4days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n45.88.230.126:28010\n#Wipe Schedule:\nEvery 4 Days @ 2PM UTC```', inline=True)
        
        given_timestamp=March21_4pm
        Add_3days(given_timestamp)
        embed.add_field(name=':flag_eu: EU 3X Solo', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n45.88.230.58:28010\n#Wipe Schedule:\nEvery 3 Days @ 3PM UTC```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        

        given_timestamp=March19_3pm
        Add_3days(given_timestamp)
        embed.add_field(name=':flag_eu: EU 3X Duo', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n64.52.81.29:28010\n#Wipe Schedule:\nEvery 3 days @ 2PM UTC```', inline=True)
        
        given_timestamp=March21_4pm
        Add_3days(given_timestamp)
        embed.add_field(name=':flag_eu: EU 3X Trio', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n209.237.141.8:28010\n#Wipe Schedule:\nEvery 3 Days @ 3PM UTC```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
       
        given_timestamp=March22_4pm
        Add_3days(given_timestamp)
        embed.add_field(name=':flag_eu: EU 3X Quad', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n64.52.81.169:28010\n#Wipe Schedule:\nEvery 3 Days @ 3PM UTC```', inline=True)
        
        given_timestamp=March21_3pm
        Add_3days(given_timestamp)
        embed.add_field(name=':flag_eu: EU 3X Max 5', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n45.88.230.56:28010\n#Wipe Schedule:\nEvery 3 days @ 2PM UTC```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        
        find_next_Saturday()

        tuesday_Saturday()
        embed.add_field(name=':flag_eu: EU 5X Trio', value=f'Next Wipe:\n<t:{tuesday_Saturday("15:00")}:F>```md\n# IP For F1 Connect:\n64.52.81.21:28010\n#Wipe Schedule:\nTuesday And Saturday @ 2PM UTC```', inline=True)
        
        given_timestamp=March21_4pm
        Add_3days(given_timestamp)
        embed.add_field(name=':flag_eu: EU 5X Quad', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n45.88.230.57:28010\n#Wipe Schedule:\nEvery 3 days @ 3PM UTC```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        
        tuesday_friday()
        embed.add_field(name=':flag_eu: EU 5X NoBPs', value=f'Next Wipe:\n<t:{tuesday_friday("16:00")}:F>```md\n# IP For F1 Connect:\n209.237.141.74:28010\n#Wipe Schedule:\nTuesday And Friday @ 3PM UTC```', inline=True)
        
        embed.add_field(name=':flag_eu: Vanilla Trio', value=f'Next Wipe:\n<t:{find_next_day(5,"15:00")}:F>```md\n# IP For F1 Connect:\n64.52.81.22:28010\n#Wipe Schedule:\nEvery Saturday @ 2PM UTC```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        url='https://warbandits.gg/assets/media/images/WarBanditsLogo.png'
        embed.set_thumbnail(url=url)
        await ctx.respond(embed=embed)
        ######
        
        
        embed=discord.Embed(title='WarBandits Servers Wipe Times',description='Here you can find information for all of warbandit servers, including connection information and wipe schedule.\n>Global Blueprints\nBlueprints wipe once a month on the first Thursday of each month on the forced wipe',color=0xe10505)
        given_timestamp=March21_7pm
        Add_4days(given_timestamp)
        embed.add_field(name=':flag_us: US 2X Solo', value=f'Next Wipe:\n<t:{Add_4days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n199.231.233.113:28010\n#Wipe Schedule:\nEvery 4 Days @ 2PM EST```', inline=True)
        
        given_timestamp=March22_7pm
        Add_4days(given_timestamp)
        embed.add_field(name=':flag_us: US 2X Duo', value=f'Next Wipe:\n<t:{Add_4days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n199.231.233.118:28010\n#Wipe Schedule:\nEvery 4 Days @ 2PM EST```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        
        given_timestamp=March19_7pm
        Add_4days(given_timestamp)
        embed.add_field(name=':flag_us: US 2X Trio', value=f'Next Wipe:\n<t:{Add_4days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n199.231.233.36:28010\n#Wipe Schedule:\nEvery 4 Days @ 2PM EST```', inline=True)
        
        given_timestamp=March22_7pm
        Add_4days(given_timestamp)  
        embed.add_field(name=':flag_us: US 2X Quad', value=f'Next Wipe:\n<t:{Add_4days(given_timestamp) }:F>```md\n# IP For F1 Connect:\n199.231.233.74:28010\n#Wipe Schedule:\nEvery 4 Days @ 2PM EST```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        
        given_timestamp=March21_7pm
        Add_4days(given_timestamp)    
        embed.add_field(name=':flag_us: US 2X Max 5', value=f'Next Wipe:\n<t:{Add_4days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n205.178.177.86:28010\n#Wipe Schedule:\nEvery 4 Days @ 2PM EST```', inline=True)
        
        given_timestamp=March21_8pm
        Add_3days(given_timestamp)    
        embed.add_field(name=':flag_us: US 3X Solo', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n148.59.74.65:28010\n#Wipe Schedule:\nEvery 3 Days @ 3PM EST```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        
        given_timestamp=March21_7pm
        Add_3days(given_timestamp)  
        embed.add_field(name=':flag_us: US 3X Duo', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n199.231.233.114:28010\n#Wipe Schedule:\nEvery 3 Days @ 2PM EST```', inline=True)
        
        given_timestamp=March19_7pm
        Add_3days(given_timestamp)
        embed.add_field(name=':flag_us: US 3X Trio', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n199.231.233.76:28010\n#Wipe Schedule:\nEvery 3 Days @ 2PM EST```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        
        given_timestamp=March19_8pm
        Add_3days(given_timestamp)  
        embed.add_field(name=':flag_us: US 3X Quad', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n199.231.233.119:28010\n#Wipe Schedule:\nEvery 3 Days @ 3PM EST```', inline=True)
        
        given_timestamp=March21_8pm
        Add_3days(given_timestamp)  
        embed.add_field(name=':flag_us: US 3X Max 5', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n104.152.143.159:28010\n#Wipe Schedule:\nEvery 3 Days @ 3PM EST```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        
        
        embed.add_field(name=':flag_us: US 5X Trio', value=f'Next Wipe:\n<t:{tuesday_Saturday("19:00")}:F>```md\n# IP For F1 Connect:\n199.231.233.174:28010\n#Wipe Schedule:\nTuesday And Saturday @ 2PM EST```', inline=True)
        
        given_timestamp=March21_8pm
        Add_3days(given_timestamp)  
        embed.add_field(name=':flag_us: US 5X Quad', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n104.152.143.160:28010\n#Wipe Schedule:\nEvery 3 Days @ 3PM EST```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        
        
        embed.add_field(name=':flag_us: US 5X NoBPs', value=f'Next Wipe:\n<t:{monday_friday("20:00")}:F>```md\n# IP For F1 Connect:\n104.152.143.236:28010\n#Wipe Schedule:\nMonday And Friday @\n 3PM EST```', inline=True)
        embed.add_field(name=':flag_us: US 10X NoBPs', value=f'Next Wipe:\n<t:{tuesday_friday("19:00")}:F>```md\n# IP For F1 Connect:\n199.231.233.75:28010\n#Wipe Schedule:\nTuesday and Friday @ 2PM EST```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        await ctx.respond(embed=embed)



@bot.slash_command(name='werewolf',description='Show the servers of Werewolf')
async def werewolf(ctx, max: int = None, x: int = None):
    if max is None and x is None:
        embed=discord.Embed(title="Werewolf Gaming.co Servers Wipe Times" , description="Welcome to the Live Wipe countdown section. Here you will find all the wipe times & the count down to the next wipe!\n >Blueprints\nBlueprints wipe once a month on the first Thursday of each month on the forced wipe. This takes place at 19:00 UTC when Facepunch releases their Game Update. Maps will also wipe on BP Wipes.",color=0x0000FF)
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/LDefHIuhU2XNuYz3Jrzx_BwjDm_6ERp4dJJkIsdIKvY/https/i.imgur.com/p4Zm6Gy.gif?width=676&height=676")
        
        
        given_timestamp=March21_3pm
        embed.add_field(name='🐺 2x Trio', value=f'Next Wipe:\n<t:{Add_4days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n64.52.81.123:28017\n#Wipe Schedule:\nEvery 4 Days @ UTC  - \n14:00```', inline=True)
        given_timestamp=March22_4pm
        embed.add_field(name='🐺 3x Solo', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n45.88.230.129:28037\n#Wipe Schedule:\nEvery 3 Days @ UTC  - \n15:00```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        given_timestamp=March20_4pm
        embed.add_field(name='🐺 3x Duo', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n64.52.81.45:28027\n#Wipe Schedule:\nEvery 3 Days @ UTC  - \n15:00```', inline=True)
        given_timestamp=March21_3pm
        embed.add_field(name='🐺 3x Duo LARGE', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n45.88.230.132:28017\n#Wipe Schedule:\nEvery 3 Days @ UTC  - \n14:00```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        given_timestamp=March21_4pm
        embed.add_field(name='🐺 3x Trio', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n64.52.81.123:28027\n#Wipe Schedule:\nEvery 3 Days @ UTC  - 15:00```', inline=True)
        given_timestamp=March22_3pm
        embed.add_field(name='🐺 3x Trio LARGE', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n64.52.81.230:28037\n#Wipe Schedule:\nEvery 3 Days @ UTC  - 14:00```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        given_timestamp=March20_4pm
        embed.add_field(name='🐺 3x Quad', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n64.52.81.123:28037\n#Wipe Schedule:\nEvery 3 Days @ UTC  - 15:00```', inline=True)
        given_timestamp=March22_4pm
        embed.add_field(name='🐺 3x Max 5', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n45.88.230.129:28017\n#Wipe Schedule:\nEvery 3 Days @ UTC  - 15:00```', inline=True)

        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name='🐺 5x Weekly', value=f'Next Wipe:\n<t:{find_next_day(5,"15:00")}:F>```md\n# IP For F1 Connect:\n45.88.230.122:28017\n#Wipe Schedule:\nEvery Saturday @ UTC - 14:00```', inline=True)
        given_timestamp=March21_4pm
        embed.add_field(name='🐺 5x Solo', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n64.52.81.121:28037\n#Wipe Schedule:\nEvery 3 Days @ UTC  - 15:00```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        given_timestamp=March20_3pm
        embed.add_field(name='🐺 5x Duo', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n64.52.81.45:28017\n#Wipe Schedule:\nEvery 3 Days @ UTC  - 14:00```', inline=True)
        given_timestamp=March21_3pm
        embed.add_field(name='🐺 5x Duo LARGE', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n45.88.230.37:28015\n#Wipe Schedule:\nEvery 3 Days @ UTC  - 14:00```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        given_timestamp=March21_3pm
        embed.add_field(name='🐺 5x Trio', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n45.88.230.52:28017\n#Wipe Schedule:\nEvery 3 Days @ UTC  - 14:00```', inline=True)
        given_timestamp=March22_3pm
        embed.add_field(name='🐺 5x Trio LARGE', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n64.52.81.230:28027\n#Wipe Schedule:\nEvery 3 Days @ UTC  - 14:00```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        given_timestamp=March22_3pm
        embed.add_field(name='🐺 5x Quad', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n64.52.81.99:28017\n#Wipe Schedule:\nEvery 3 Days @ UTC  - 14:00```', inline=True)
        given_timestamp=March20_3pm
        embed.add_field(name='🐺 5x Max 5', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n64.52.81.121:28027\n#Wipe Schedule:\nEvery 3 Days @ UTC  - 14:00```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        given_timestamp=March22_4pm
        embed.add_field(name='🐺 5x No BPs', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\n64.52.81.45:28047\n#Wipe Schedule:\nEvery 3 Days @ UTC  - 15:00```', inline=True)
        embed.set_footer(text="🐺 Werwolf Gaming")
        await ctx.respond(embed=embed)

@bot.slash_command(name='templar',description='Show the servers of Templar')
async def templar(ctx, max: int = None, x: int = None):
    if max is None and x is None:
        embed=discord.Embed(title="TemplarGaming Servers Wipe Times (EU)" , description="Welcome to the Live Wipe countdown section. Here you will find all the wipe times & the count down to the next wipe!\n> Blueprints\nBlueprints wipe once a month on the first Thursday of each month on the forced wipe. This takes place at 19:00 UTC when Facepunch releases their Game Update. Maps will also wipe on BP Wipes.",color=0xFFFF00)
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/mbTbSkbzqvTPmcFURzICxwgP4o_jO0ZebFKTu0E9rUY/https/i.imgur.com/zptU9uj.png?format=webp&quality=lossless&width=559&height=559")

        embed.add_field(name=':flag_eu: 10x Max 6', value=f'Next Wipe:\n<t:{tuesday_Saturday("15:00")}:F>```md\n# IP For F1 Connect:\neu-10x-swift.templargaming.net\n#Wipe Schedule:\nEvery Tuesday & Saturday at 14:00 UK```', inline=False)
        given_timestamp=March22_3pm
        embed.add_field(name=':flag_eu: 10x Trio', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\neu-10x-swift-trio.templargaming.net\n#Wipe Schedule:\nEvery 3 Days at 14:00  UK ```', inline=False)
        
        embed.add_field(name=':flag_eu: 2x Duo', value=f'Next Wipe:\n<t:{find_next_day(5,"15:00")}:F>```md\n# IP For F1 Connect:\neu-2x-duo.templargaming.net\n#Wipe Schedule:\nEvery Saturday at 14:00 UK```', inline=False)
        await ctx.respond(embed=embed)
        embed=discord.Embed(title="TemplarGaming Servers Wipe Times (US)" , description="Welcome to the Live Wipe countdown section. Here you will find all the wipe times & the count down to the next wipe!\n> Blueprints\nBlueprints wipe once a month on the first Thursday of each month on the forced wipe. This takes place at 19:00 UTC when Facepunch releases their Game Update. Maps will also wipe on BP Wipes.",color=0xFFFF00)
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/mbTbSkbzqvTPmcFURzICxwgP4o_jO0ZebFKTu0E9rUY/https/i.imgur.com/zptU9uj.png?format=webp&quality=lossless&width=559&height=559")
        embed.add_field(name=':flag_us: 10x Max 8', value=f'Next Wipe:\n<t:{monday_friday("20:00")}:F>```md\n# IP For F1 Connect:\nus-10x-swift.templargaming.net\n#Wipe Schedule:\nEvery Monday & Friday at 15:00 US```', inline=False)
        await ctx.respond(embed=embed)
        embed=discord.Embed(title="TemplarGaming Servers Wipe Times (SEA)" , description="Welcome to the Live Wipe countdown section. Here you will find all the wipe times & the count down to the next wipe!\n> Blueprints\nBlueprints wipe once a month on the first Thursday of each month on the forced wipe. This takes place at 19:00 UTC when Facepunch releases their Game Update. Maps will also wipe on BP Wipes.",color=0xFFFF00)
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/mbTbSkbzqvTPmcFURzICxwgP4o_jO0ZebFKTu0E9rUY/https/i.imgur.com/zptU9uj.png?format=webp&quality=lossless&width=559&height=559")
        embed.add_field(name=':earth_asia: 10x Max 6', value=f'Next Wipe:\n<t:{tuesday_Saturday("19:00")}:F>```md\n# IP For F1 Connect:\nsea-10x-swift.templargaming.net\n#Wipe Schedule:\nEvery Tuesday & Saturday at 14:00 Singapore```', inline=False)
        given_timestamp=March22_7am
        embed.add_field(name=':earth_asia: 5x Quad', value=f'Next Wipe:\n<t:{Add_3days(given_timestamp)}:F>```md\n# IP For F1 Connect:\nsea-5x-quad.templargaming.net\n#Wipe Schedule:\nEvery 3 Days at 14:00 Singapore```', inline=False)
        await ctx.respond(embed=embed)


@bot.slash_command(name='atlas',description='Show the servers of Atlas')
async def atlas(ctx, max: int = None, x: int = None):
    if max is None and x is None:
        embed=discord.Embed(title="Atlas Servers Wipe Times (EU)", description="Welcome to the Live Wipe countdown section. Here you will find all the wipe times & the count down to the next wipe!\n> Blueprints\nBlueprints wipe once a month on the first Thursday of each month on the forced wipe. This takes place at 19:00 UTC when Facepunch releases their Game Update.",color=0x000000)
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/V8vP7bM7aXXHFxYWdO7FJ0_umULl9FBB6wd6Ah9SfJ0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1194236616164769874/877acbc35627627f7a64abdc790113f9.png?format=webp&quality=lossless&width=676&height=676")
        embed.add_field(name=':flag_eu: 10X', value=f'Next Wipe:\n<t:{monday_friday("18:00")}:F>```md\n# IP For F1 Connect:\n10x.atlasrust.uk:28010\n#Wipe Schedule:\nEvery Monday & Friday at 14:00 Londom```', inline=True)
        embed.add_field(name=':flag_eu: 2x Monthly', value=f'Next Wipe:\n<t:{first_thursday_of_next_month("20:00")}:F>```md\n# IP For F1 Connect:\n2xmonthly.atlasrust.uk:28010\n#Wipe Schedule:\nFirst Thursday every month 7pm Londom```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name=':flag_eu: 5X', value=f'Next Wipe:\n<t:{wednesday_saturday("17:00")}:F>```md\n# IP For F1 Connect:\n5x.atlasrust.uk:28010\n#Wipe Schedule:\nEvery Wednesday & Saturday at 4pm Londom```', inline=True)
        await ctx.respond(embed=embed)
        embed=discord.Embed(title="Atlas Servers Wipe Times (NA)", description="Welcome to the Live Wipe countdown section. Here you will find all the wipe times & the count down to the next wipe!\n> Blueprints\nBlueprints wipe once a month on the first Thursday of each month on the forced wipe. This takes place at 19:00 UTC when Facepunch releases their Game Update.",color=0x000000)
        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/JOEP6GrD1MqGxaN9k9ral1BGBFsu-ilEKZdM2ulypK0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1199545835793436762/df5c89e85a0a0bc159ac89682452ffcb.png?format=webp&quality=lossless&width=676&height=676")
        embed.add_field(name=':flag_na: 10X', value=f'Next Wipe:\n<t:{monday_friday("17:00")}:F>```md\n# IP For F1 Connect:\n10x.atlasrust.us:28015\n#Wipe Schedule:\nEvery Monday & Friday at 5pm Eastern Time```', inline=True)
        embed.add_field(name=':flag_na: 2X', value=f'Next Wipe:\n<t:{find_next_day(4,"16:30")}:F>```md\n# IP For F1 Connect:\nmain.atlasrust.us:28010\n#Wipe Schedule:\nEvery Friday at 4:30pm Eastern Time```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name=':flag_na: 5X', value=f'Next Wipe:\n<t:{tuesday_Saturday("17:00")}:F>```md\n# IP For F1 Connect:\n5x.atlasrust.us:28010\n#Wipe Schedule:\nEvery Tuesday & Saturday at 5pm Eastern Time```', inline=True)
        await ctx.respond(embed=embed)
@bot.slash_command(name='andysolam',description='Show the servers of Andysolam')
async def andysolam(ctx, max: int = None, x: int = None):
    if max is None and x is None:
        embed=discord.Embed(title="Andysolam Servers Wipe Times (EU)", description="Welcome to the Live Wipe countdown section. Here you will find all the wipe times & the count down to the next wipe!\n> Blueprints\nBlueprints wipe once a month on the first Thursday of each month on the forced wipe.",color=0x87CEEB)
        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/crjJD1MEKpZ5mJWOU1Li7IZ31oNxWJp22zuzpMoT54E/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/618951337324969988/81cfa2e086e62909a7b50c29df2b0ba6.png?format=webp&quality=lossless&width=559&height=559")
        
        embed.add_field(name=':flag_eu: 20x NoBPs Max8', value=f'Next Wipe:\n<t:{tuesday_Saturday("14:00")}:F>```md\n# IP For F1 Connect:\n20x.andysolam.eu\n#Wipe Schedule:\nEvery Tuesday and Saturday @ 3PM CET```', inline=True)
        embed.add_field(name=':flag_eu: 10x NoBPs MAIN Max6', value=f'Next Wipe:\n<t:{monday_friday("13:00")}:F>```md\n# IP For F1 Connect:\n10xnobps.andysolam.eu\n#Wipe Schedule:\nEvery Monday & Friday @ 2PM CET```', inline=True)
        
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name=':flag_eu: 10x Trio', value=f'Next Wipe:\n<t:{thursday_sunday("13:00")}:F>```md\n# IP For F1 Connect:\n10xtrio.andysolam.eu\n#Wipe Schedule:\nEvery Sunday & Thursday @ 2PM CET ```', inline=True)
        embed.add_field(name=':flag_eu: 10x SOLO', value=f'Next Wipe:\n<t:{wednesday_saturday("13:00")}:F>```md\n# IP For F1 Connect:\n10xsolo.andysolam.eu\n#Wipe Schedule:\nEvery Saturday & Wednesday @ 2PM CET ```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name=':flag_eu: 10X DUO', value=f'Next Wipe:\n<t:{wednesday_saturday("14:00")}:F>```md\n# IP For F1 Connect:\n10xduo.andysolam.eu\n#Wipe Schedule:\nEvery Saturday & Wednesday @ 3PM CET ```', inline=True)
        embed.add_field(name=':flag_eu: x1MILLION Max5', value=f'Next Wipe:\n<t:{tuesday_friday("14:00")}:F>```md\n# IP For F1 Connect:\nmillionx.andysolam.eu\n#Wipe Schedule:\nEvery Tuesday & Friday @ 1PM ET ```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        await ctx.respond(embed=embed)
        embed=discord.Embed(title="Andysolam Servers Wipe Times (US)", description="Welcome to the Live Wipe countdown section. Here you will find all the wipe times & the count down to the next wipe!\n> Blueprints\nBlueprints wipe once a month on the first Thursday of each month on the forced wipe.",color=0x87CEEB)
        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/crjJD1MEKpZ5mJWOU1Li7IZ31oNxWJp22zuzpMoT54E/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/618951337324969988/81cfa2e086e62909a7b50c29df2b0ba6.png?format=webp&quality=lossless&width=559&height=559")
        embed.add_field(name=':flag_us: 20x NoBPs Max8', value=f'Next Wipe:\n<t:{tuesday_Saturday("20:00")}:F>```md\n# IP For F1 Connect:\n20x.andysolam.us\n#Wipe Schedule:\nEvery Tuesday & Saturday @ 3PM ET ```', inline=True)
        embed.add_field(name=':flag_us: 10x NoBPs MAIN Max10', value=f'Next Wipe:\n<t:{monday_friday("20:00")}:F>```md\n# IP For F1 Connect:\n10xnobps.andysolam.us\n#Wipe Schedule:\nEvery Monday & Friday @ 3PM ET ```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name=':flag_us: 10x Trio', value=f'Next Wipe:\n<t:{thursday_sunday("20:00","18:00")}:F>```md\n# IP For F1 Connect:\n10xtrio.andysolam.us\n#Wipe Schedule:\nEvery Sunday @ 1PM ET & Friday @ Thursday @ 3PM ET ```', inline=True)
        embed.add_field(name=':flag_us: 10X DUO', value=f'Next Wipe:\n<t:{wednesday_saturday("21:30","19:00")}:F>```md\n# IP For F1 Connect:\n10xduo.andysolam.us\n#Wipe Schedule:\nEvery Wednesday @ 4.30PM ET & Friday @ Saturday @ 2PM ET ```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name=':flag_us: x1MILLION Max5', value=f'Next Wipe:\n<t:{tuesday_Saturday("20:00","18:00")}:F>```md\n# IP For F1 Connect:\nmillionx.andysolam.com\n#Wipe Schedule:\nEvery Tuesday @ 4PM ET & Friday @ Saturday @ 1PM ET```', inline=True)

        await ctx.respond(embed=embed)
        

@bot.slash_command(name='rustoria', description='Show the servers of Rustoria')
async def rustoria(ctx, max: int = None, x: int = None):
    if max is None and x is None :
        embed=discord.Embed(title="Rustoria Servers Wipe Times (EU)", description="Welcome to the Live Wipe countdown section. Here you will find all the wipe times & the count down to the next wipe!\n> Blueprints\nBlueprints wipe once a month on the first Thursday of each month on the forced wipe.",color=0xffa500)
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/R881YDPwczGA43F0L6banipsWGZZS8ECOWaf28nC4bs/https/files.rustoria.co/schaadt/39fff9b6-f6ae-40bf-8387-0e9f38f13599.png?format=webp&quality=lossless")
        
        embed.add_field(name=':flag_eu: Main', value=f'Next Wipe:\n<t:{find_next_day(3,"16:00")}:F>```md\n# IP For F1 Connect:\nmain.rustoria.uk:28010\n#Wipe Schedule:\nEvery Thursday @ 3PM UK```', inline=True)
        embed.add_field(name=':flag_eu: Medium', value=f'Next Wipe:\n<t:{be_weekly_thurs("16:00")}:F>```md\n# IP For F1 Connect:\nmedium.rustoria.uk:28010\n#Wipe Schedule:\nEvery Thursday @ 3PM UK (𝐁𝐢-𝐰𝐞𝐞𝐤𝐥𝐲)```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name=':flag_eu: Long', value=f'Next Wipe:\n<t:{first_thursday_of_next_month("20:00")}:F>```md\n# IP For F1 Connect:\nlong.rustoria.uk:28010\n#Wipe Schedule:\nFirst Thursday of every month(𝐌𝐨𝐧𝐭𝐡𝐥𝐲)```', inline=True)
        embed.add_field(name=':flag_eu: Small', value=f'Next Wipe:\n<t:{find_next_day(3,"16:00")}:F>```md\n# IP For F1 Connect:\nsmall.rustoria.uk:28010\n#Wipe Schedule:\nEvery Thursday @ 3PM UK```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name=':flag_eu: Mondays', value=f'Next Wipe:\n<t:{find_next_day(7,"16:00")}:F>```md\n# IP For F1 Connect:\nmon.rustoria.uk:28012\n#Wipe Schedule:\nEvery Monday @ 3PM UK```', inline=True)
        embed.add_field(name=':flag_eu: Low Pop', value=f'Next Wipe:\n<t:{first_thursday_of_next_month("20:00")}:F>```md\n# IP For F1 Connect:\nlowpop.rustoria.uk\n#Wipe Schedule:\nFirst Thursday of every month(𝐌𝐨𝐧𝐭𝐡𝐥𝐲)```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.set_footer(text='Rustoria eu')
        
        await ctx.respond(embed=embed)
        embed=discord.Embed(title="Rustoria Servers Wipe Times (US)", description="Welcome to the Live Wipe countdown section. Here you will find all the wipe times & the count down to the next wipe!\n> Blueprints\nBlueprints wipe once a month on the first Thursday of each month on the forced wipe.",color=0xffa500)
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/pY-MZJZ1lbamZnJCrDYhD1aonOH1taOlu17XOY77wIo/https/files.rustoria.co/schaadt/e83f2749-f80a-43aa-b3f5-1134133dda6e.png?format=webp&quality=lossless")
        embed.add_field(name=':flag_us: Main', value=f'Next Wipe:\n<t:{find_next_day(3,"20:00")}:F>```md\n# IP For F1 Connect:\nmain.rustoria.us:28010\n#Wipe Schedule:\nEvery Thursday @ 3PM EST```', inline=True)
        embed.add_field(name=':flag_us: Medium', value=f'Next Wipe:\n<t:{be_weekly_thurs("20:00")}:F>```md\n# IP For F1 Connect:\nmedium.rustoria.us:28010\n#Wipe Schedule:\nEvery Thursday @ 3PM EST (𝐁𝐢-𝐰𝐞𝐞𝐤𝐥𝐲)```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name=':flag_us: Long', value=f'Next Wipe:\n<t:{first_thursday_of_next_month("20:00")}:F>```md\n# IP For F1 Connect:\nlong.rustoria.us:28010\n#Wipe Schedule:\nFirst Thursday of every month(𝐌𝐨𝐧𝐭𝐡𝐥𝐲)```', inline=True)
        embed.add_field(name=':flag_us: Small', value=f'Next Wipe:\n<t:{find_next_day(3,"20:00")}:F>```md\n# IP For F1 Connect:\nsmall.rustoria.us:28010\n#Wipe Schedule:\nEvery Thursday @ 3PM EST```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name=':flag_us: Mondays', value=f'Next Wipe:\n<t:{find_next_day(7,"20:00")}:F>```md\n# IP For F1 Connect:\nmon.rustoria.us:28010\n#Wipe Schedule:\nEvery Monday @ 3PM EST```', inline=True)
        embed.add_field(name=':flag_us: Low Pop', value=f'Next Wipe:\n<t:{first_thursday_of_next_month("20:00")}:F>```md\n# IP For F1 Connect:\nlowpop.rustoria.us\n#Wipe Schedule:\nFirst Thursday of every month(𝐌𝐨𝐧𝐭𝐡𝐥𝐲)```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.set_footer(text='Rustoria us')
        
        await ctx.respond(embed=embed)
        embed=discord.Embed(title="Rustoria Servers Wipe Times (SEA)", description="Welcome to the Live Wipe countdown section. Here you will find all the wipe times & the count down to the next wipe!\n> Blueprints\nBlueprints wipe once a month on the first Thursday of each month on the forced wipe.",color=0xffa500)
        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/1RPCyBLQQLhPsfYuMwr8c-5LLGrq6_AvxRQSkqJcEEk/https/files.rustoria.co/schaadt/1e55c756-7717-4358-9b4d-833058503e90.png?format=webp&quality=lossless")
        embed.add_field(name=':earth_asia: Main', value=f'Next Wipe:\n<t:{find_next_day(3,"20:00")}:F>```md\n# IP For F1 Connect:\nmain.rustoria.asia:28010\n#Wipe Schedule:\nEvery Thursday @ 5PM AEST```', inline=True)
        embed.add_field(name=':earth_asia: Long', value=f'Next Wipe:\n<t:{first_thursday_of_next_month("20:00")}:F>```md\n# IP For F1 Connect:\nlong.rustoria.asia:28010\n#Wipe Schedule:\nFirst Thursday of every month(𝐌𝐨𝐧𝐭𝐡𝐥𝐲)```', inline=True)
        embed.set_footer(text='Rustoria sea')
        
        await ctx.respond(embed=embed)
        embed=discord.Embed(title="Rustoria Servers Wipe Times (EU,modded)", description="Welcome to the Live Wipe countdown section. Here you will find all the wipe times & the count down to the next wipe!\n> Blueprints\nBlueprints wipe once a month on the first Thursday of each month on the forced wipe.",color=0xffa500)
        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/jAZHpqpOYPhVZsIBRLf2HpFN4nXDHCi7tI1UPDfXrp0/https/files.rustoria.co/schaadt/21201522-c015-4f17-8d1c-aa0bb22bd352.png?format=webp&quality=lossless")
        embed.add_field(name=':flag_eu: 5X NoBPs Max8', value=f'Next Wipe:\n<t:{wednesday_sunday("17:00","12:00")}:F>```md\n# IP For F1 Connect:\nnobps.rustoria.uk:28010\n#Wipe Schedule:\nEvery Wednesday @4PM UK & Sunday @11AM UK```', inline=True)
        embed.add_field(name=':flag_eu: 10X NoBPs Max6', value=f'Next Wipe:\n<t:{tuesday_friday("13:00","13:00")}:F>```md\n# IP For F1 Connect:\n10x.rustoria.uk:28010\n#Wipe Schedule:\nEvery Tuesday & Monday @1PM UK```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name=':flag_eu: 3X NoBPs Max6', value=f'Next Wipe:\n<t:{monday_friday("13:00","13:00")}:F>```md\n# IP For F1 Connect:\n3x.rustoria.uk:28010\n#Wipe Schedule:\nEvery Friday & Monday @1PM UK```', inline=True)
        embed.add_field(name=':flag_eu: 2X Vanilla Max8', value=f'Next Wipe:\n<t:{monday_thursday("16:00","16:00")}:F>```md\n# IP For F1 Connect:\n2x.rustoria.uk:28010\n#Wipe Schedule:\nEvery Thursday & Monday @3PM UK```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.set_footer(text='Rustoria eu Modded')
        await ctx.respond(embed=embed)
        embed=discord.Embed(title="Rustoria Servers Wipe Times (US,modded)", description="Welcome to the Live Wipe countdown section. Here you will find all the wipe times & the count down to the next wipe!\n> Blueprints\nBlueprints wipe once a month on the first Thursday of each month on the forced wipe.",color=0xffa500)
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/itePonhJS_E-ah2Tkf3daptRMDaSFB9M7_aa14F1Hdc/https/files.rustoria.co/schaadt/71f1cb7a-0642-4d7a-a7de-433782be904c.png?format=webp&quality=lossless")
        embed.add_field(name=':flag_us: 5X NoBPs Max8', value=f'Next Wipe:\n<t:{wednesday_sunday("20:00","18:00")}:F>```md\n# IP For F1 Connect:\nnobps.rustoria.us:28010\n#Wipe Schedule:\nEvery Wednesday @3PM EST & Sunday @1PM EST```', inline=True)
        embed.add_field(name=':flag_us: 5x Trio', value=f'Next Wipe:\n<t:{tuesday_Saturday("20:00","18:00")}:F>```md\n# IP For F1 Connect:\ntrio5x.rustoria.us:28010\n#Wipe Schedule:\nEvery Tuesday @3PM EST & Saturday @1PM EST```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name=':flag_us: 10X NoBPs Max6', value=f'Next Wipe:\n<t:{tuesday_friday("22:00","22:00")}:F>```md\n# IP For F1 Connect:\n10x.rustoria.us:28010\n#Wipe Schedule:\nEvery Friday & Tuesday @5PM EST```', inline=True)
        embed.add_field(name=':flag_us: 3X NoBPs Max6', value=f'Next Wipe:\n<t:{monday_friday("20:00","20:00")}:F>```md\n# IP For F1 Connect:\n3x.rustoria.us:28010\n#Wipe Schedule:\nEvery Monday & Friday @3PM EST```', inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name=':flag_us: 2X Vanilla Max8', value=f'Next Wipe:\n<t:{monday_thursday("20:00","20:00")}:F>```md\n# IP For F1 Connect:\n2x.rustoria.us:28010\n#Wipe Schedule:\nEvery Monday & Thursday @3PM EST```', inline=True)
        embed.set_footer(text='Rustoria us Modded')
        await ctx.respond(embed=embed)





bot.run(token=os.environ.get('token'))
