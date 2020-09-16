from discord.ext import commands
import os
import traceback
import requests

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
line_token = os.environ['LINE_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('hello')
    payload = {'message':'test'} # 通知させたいメッセージ
    headers = {'Authorization':'Bearer ' + line_token} # 発行したトークン
    r = requests.post('https://notify-api.line.me/api/notify', data=payload, headers=headers)


bot.run(token)
