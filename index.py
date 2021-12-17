import discord
from discord.ext import commands
import datetime
import calendar, time, os, subprocess


bot = commands.Bot(command_prefix = '*', description = "Hi")

print(datetime.datetime.now().strftime('%Y-%m-%d_%H:%M'))
print(calendar.weekday(2021, 12, 12))


subprocess.Popen("python notify.py")
def read():
    with open("tasks.txt", 'r') as file:
        filedata = file.read()
    return filedata

print(read())


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description = "JI hi Gi cHA", timestamp = datetime.datetime.utcnow(), color = discord.Color.green())
    embed.add_field(name = "Server Owner", value=f"{ctx.guild.owner}")
    await  ctx.send(embed=embed)

@bot.command()
async def hTask(ctx, title: str, time:str):
    embed = discord.Embed(title = title, description = "Hourly Task succesfully aded, time = " + time, color = discord.Color.green())
    await ctx.send(embed=embed)

    if read() == "":
        info = "h" + "*-*" + title + "*-*" + time + "*-*" + "NONE" + "*-*" + datetime.datetime.now().strftime('%Y-%m-%d_%H:%M')
    else:
        info = read() + "\n" + "h" + "*-*" + title + "*-*" + time + "*-*" + "NONE" + "*-*" + datetime.datetime.now().strftime('%Y-%m-%d_%H:%M')
    print(info)
    with open("tasks.txt", 'w') as file:
        file.write(info)

@bot.command()
async def dTask(ctx, title: str, time:str):
    embed = discord.Embed(title = title, description = "Daily Task succesfully aded, time = " + time, color = discord.Color.green())
    await ctx.send(embed=embed)

    if read() == "":
        info = "d" + "*-*" + title + "*-*" + time + "*-*" + "NONE" + "*-*"  + datetime.datetime.now().strftime('%Y-%m-%d_%H:%M')
    else:
        info = read() + "\n" + "d" + "*-*" + title + "*-*" + time + "*-*" + "NONE" + "*-*"  + datetime.datetime.now().strftime('%Y-%m-%d_%H:%M')
    print(info)
    with open("tasks.txt", 'w') as file:
        file.write(info)
    


@bot.command()
async def wTask(ctx, title: str, time:str, day: str):
    embed = discord.Embed(title = title, description = "Weekly Task succesfully aded, time = " + time, color = discord.Color.green())
    await ctx.send(embed=embed)

    if read() == "":
        info = "w" + "*-*" + title + "*-*" + time + "*-*" + day + "*-*" + datetime.datetime.now().strftime('%Y-%m-%d_%H:%M')
    else:
        info = read()  + "\n" + "w" + "*-*" + title + "*-*" + time + "*-*" + day + "*-*" + datetime.datetime.now().strftime('%Y-%m-%d_%H:%M')
    print(info)
    with open("tasks.txt", 'w') as file:
        file.write(info)


@bot.command()
async def mTask(ctx, title: str, time:str, day: str):
    embed = discord.Embed(title = title, description = "Montly Task succesfully aded, time = " + time, color = discord.Color.green())
    await ctx.send(embed=embed)

    if read() == "":
        info = "m" + "*-*" + title + "*-*" + time + "*-*" + day + "*-*" + datetime.datetime.now().strftime('%Y-%m-%d_%H:%M')
    else:
        info = read() + "\n" + "m" + "*-*" + title + "*-*" + time + "*-*" + day + "*-*" + datetime.datetime.now().strftime('%Y-%m-%d_%H:%M')
    print(info)
    with open("tasks.txt", 'w') as file:
        file.write(info)

    

@bot.command()
async def Task(ctx, title: str, time:str, date: str):
    embed = discord.Embed(title = title, description = "Task succesfully aded, time = " + time, color = discord.Color.green())
    await ctx.send(embed=embed)

    if read() == "":
        info = "t" + "*-*" + title + "*-*" + time + "*-*" + date + "*-*" + datetime.datetime.now().strftime('%Y-%m-%d_%H:%M')
    else:
        info = read() + "\n" + "t" + "*-*" + title + "*-*" + time + "*-*" + date + "*-*" + datetime.datetime.now().strftime('%Y-%m-%d_%H:%M')
    with open("tasks.txt", 'w') as file:
        file.write(info)

@bot.command()
async def list(ctx):
    embed = discord.Embed(title = "All tasks", description = read(), color = discord.Color.green())
    await ctx.send(embed = embed)
    rawtasks = read().split("\n")
    tasks = []
    i = 0
    for item in rawtasks:
        task = item.split("*-*")
        tasks.append(task)
        
    for item in tasks:
        i += 1
        embed = discord.Embed(title = "Task " + str(i), description = info, color = discord.Color.green())
        embed.add_field(name = "Title", value = item[1])
        
        if item[0] == 'h':
            embed.add_field(name = "Notifies", value = "Hourly")
            embed.add_field(name = "At", value = "the minute " + item[2])

        if item[0] == 'd':
            embed.add_field(name = "Notifies", value = "Daily")
            embed.add_field(name = "At", value = item[2])

        if item[0] == 'w':
            embed.add_field(name = "Notifies", value = "Weekly")
            day = item[3]
            txtday = ""
            if day == 0:
                txtday = "Monday"

            if day == 1:
                txtday = "Tuesday"

            if day == 2:
                txtday = "Wednesday"

            if day == 3:
                txtday = "Thursday"
            
            if day == 4:
                txtday = "Friday"
            
            if day == 5:
                txtday = "Saturday"
            
            if day == 6:
                txtday = "Sunday"
            
            embed.add_field(name = "At", value = item[2] + "every " + txtday)
            
        if item[0] == 'm':
            embed.add_field(name = "Notifies", value = "Monthly")
            embed.add_field(name = "At", value = item[2] + "every " + item[3])
            
        if item[0] == 't':
            embed.add_field(name = "Notifies", value = "Once")
            embed.add_field(name = "At", value = item[2] + " " + item[3])
        
        embed.add_field(name = "Task created", value = item[4])
        await ctx.send(embed = embed)
        
@bot.command()
async def remove(ctx, title):
    rawtasks = read().split("\n")
    tasks = []
    i = 0
    info = ""
    for item in rawtasks:
        task = item.split("*-*")
        tasks.append(task)
    
    for item in tasks:
        
        if item[1] == title:
            del rawtasks[i]
        
            #with open("tasks.txt", 'w') as file:
            #    file.write(str(rawtasks))
        i += 1
    for item in rawtasks:
        if info == "":
            info = item
        else: 
            info = info + "\n" + item
    
    with open("tasks.txt", 'w') as file:
        file.write(info)
    
    embed = discord.Embed(title = "Eliminated", description = "Task no longer on the list", color = discord.Color.green())
    await ctx.send(embed = embed)



                

    
@bot.event
async def stop(ctx):
    await ctx.send("stoped")


@bot.event
async def on_ready():
    print("El bot esta ready")


#bot.run(your discord bot TOKEN)
 