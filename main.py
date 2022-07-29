import os
from discord.ext import commands
import requests
import json 
import random
import yoda

title = []
authors = []
url=[]


token = os.getenv('TOKEN')

bot = commands.Bot(command_prefix="$")
@bot.listen()
async def on_message(message):
  if message.author == bot.user:
    return

  if message.content == "Hello AwesomeBot!":
    await message.channel.send("Hello world!")

@bot.listen()
async def on_ready():
    print(f'Connected to Discord as {bot.user}!')
async def echo(ctx, *args):
  await ctx.send(" ".join(args))



@bot.command(name="e", help="Echoes provided text back to the channel")
async def echo(ctx, *args):
  await ctx.send(" ".join(args))


def get_quotes():
  response = requests.get("https://zenquotes.io/api/quotes")
  quotes = json.loads(response.text)
  return quotes


quotes = get_quotes()

def get_quote():
  quote = random.choice(quotes)
  quote = f"{quote['a']} said, \"{quote['q']}\""
  return(quote)

def yoda_ed():
  q = random.choice(quotes)
  q = f"{q['a']} said, \"{q['q']}\""
  q = yoda.translate(q)
  return(q)

def f_news(category):
    title = []
    authors = []
    url=[]
    y = str(category)
    news = y.lower()
    rlink = "https://api.nytimes.com/svc/topstories/v2/{}.json?api-key=hd5q5yjkU9uRgg5BsimIEYN6rmAuQN4O".format(news)
    response = requests.get(rlink)
    data = json.loads(response.text)
    new = data.get("results")
    for item in new:
      title.append(item.get("title"))
      authors.append(item.get("byline"))
      url.append(item.get("url"))
    half = title[:len(title)-10]
    result_list = '\n'.join(half)
    return(result_list)
  
def f_news2(category):
    title = []
    authors = []
    url=[]
    y = str(category)
    news = y.lower()
    rlink = "https://api.nytimes.com/svc/topstories/v2/{}.json?api-key=hd5q5yjkU9uRgg5BsimIEYN6rmAuQN4O".format(news)
    response = requests.get(rlink)
    data = json.loads(response.text)
    new = data.get("results")
    for item in new:
      title.append(item.get("title"))
      authors.append(item.get("byline"))
      url.append(item.get("url"))
    bottom = title[(len(title)-10):]
    result_list = '\n'.join(bottom)
    return(result_list)

def author(category, num):
    title = []
    authors = []
    url=[]
    y = str(category)
    news = y.lower()
    rlink = "https://api.nytimes.com/svc/topstories/v2/{}.json?api-key=hd5q5yjkU9uRgg5BsimIEYN6rmAuQN4O".format(news)
    response = requests.get(rlink)
    data = json.loads(response.text)
    new = data.get("results")
    for item in new:
      title.append(item.get("title"))
      authors.append(item.get("byline"))
      url.append(item.get("url"))
    return(authors[(num-1)])
def title(category, num):
    title = []
    authors = []
    url=[]
    y = str(category)
    news = y.lower()
    rlink = "https://api.nytimes.com/svc/topstories/v2/{}.json?api-key=hd5q5yjkU9uRgg5BsimIEYN6rmAuQN4O".format(news)
    response = requests.get(rlink)
    data = json.loads(response.text)
    new = data.get("results")
    for item in new:
      title.append(item.get("title"))
      authors.append(item.get("byline"))
      url.append(item.get("url"))
    return(title[(num-1)])
def url(category, num):
    title = []
    authors = []
    url=[]
    y = str(category)
    news = y.lower()
    rlink = "https://api.nytimes.com/svc/topstories/v2/{}.json?api-key=hd5q5yjkU9uRgg5BsimIEYN6rmAuQN4O".format(news)
    response = requests.get(rlink)
    data = json.loads(response.text)
    new = data.get("results")
    for item in new:
      title.append(item.get("title"))
      authors.append(item.get("byline"))
      url.append(item.get("url"))
    return(url[(num-1)])

@bot.command(name = "inspire", help = "Provides a randomly selected quote from the Internet.")
async def inspire(ctx, *args):
  await ctx.send(get_quote())

@bot.command(name = "yoda", help = "Provides a randomly selected quote from the Internet, but returns it in Yoda-istic style.")
async def yodac(ctx, *args):
  await ctx.send(yoda_ed())

@bot.command(name = "dailynews", help = "Provides today's hottest news and the website link. ")
async def r_news(ctx, *args):
  await ctx.send("What category of today's news is desired? ")
  userInput = await bot.wait_for("message")
  await ctx.send(f_news(userInput.content))
  await ctx.send("Do you want to preview more news? ")
  to_send = await bot.wait_for("message")
  if to_send.content == "yes":
    await ctx.send(f_news2(userInput.content))
  await ctx.send("Which of these appeal to you? Please return a number counting from the top of the list! ")
  us = await bot.wait_for("message")
  await ctx.send(title)
  us = int(us.content)
  await ctx.send(title(userInput.content,us))
  await ctx.send(author(userInput.content,us))
  await ctx.send(url(userInput.content,us))
  await ctx.send("Complete!")

  
  

bot.run(token)




