import discord
from discord.ext import commands
import datetime
import calendar, time

bot = commands.Bot(command_prefix = '*', description = "Hi")

def read():
    with open("tasks.txt", 'r') as file:
        filedata = file.read()
    return filedata

print(read())

print("loop")

@bot.event
async def on_ready():
    print("El bot esta ready")

@bot.command()
async def notify(ctx):
    await ctx.send("Notificando")
    notified = False

    while True:
        rawtasks = read().split("\n")
        tasks = []
        i = 0
        for item in rawtasks:
            task = item.split("*-*")
            tasks.append(task)
            i += 1
        for item in tasks:
            
            embed = discord.Embed(title = item[1], description = "Just notyficating @everyone", timestamp = datetime.datetime.utcnow(), color = discord.Color.blue())
            embed.add_field(name = "Task created", value = item[4])

            if item[0] == 'h':
                if item[2] == datetime.datetime.now().strftime('%M'):
                    if 1 >= int(datetime.datetime.now().strftime('%S')):
                        await ctx.send(embed=embed)
                        await ctx.send("@everyone")
                        break


            if item[0] == 'd':
                if item[2]== datetime.datetime.now().strftime('%H:%M'):
                    await ctx.send(embed=embed)
                    await ctx.send("@everyone")
                    break


            if item[0] == 'w':
                if item[2] == datetime.datetime.now().strftime('%H:%M'):
                    if item[3] == calendar.weekday(datetime.datetime.now().strftime('%Y'), datetime.datetime.now().strftime('%m'), datetime.datetime.now().strftime('%d')):
                        await ctx.send(embed=embed)
                        await ctx.send("@everyone")
                        break


            if item[0] == 'm':
                if item[2] == datetime.datetime.now().strftime('%H:%M'):
                    if item[3] == datetime.datetime.now().strftime('%d'):
                        await ctx.send(embed=embed)
                        await ctx.send("@everyone")
                        break


            if item[0] == 't':
                if item[2] == datetime.datetime.now().strftime('%H:%M'):
                    if item[3] == datetime.datetime.now().strftime('%Y-%m-%d'):
                        await ctx.send(embed=embed)
                        await ctx.send("@everyone")
                        break


#bot.run(your discord bot TOKEN)
    

