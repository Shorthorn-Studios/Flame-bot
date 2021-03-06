#    Flame Discord Bot
#    Copyright (C) 2019-2020  Edgewurth

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#----------------------
# IMPORTING COMMANDS
#----------------------
import discord
from discord.ext import commands
import random
import sys
import string
import time
from time import sleep
import datetime
from countDown import countDown
from countDown import flamebotTimers

#---------------------
# BOT SETUP
TOKEN = 'X' # Sets the Bot token
client = discord.Client() # DO NOT CHANGE
prefix = '&' # Sets the Bot's Prefix
version = '3'

#---------------------
# CHECK FOR COMMANDS
#---------------------
@client.event
async def on_message(message):
    # Call to countdown timer to see if we need to trigger any alerts
    #flamebotTimers.poll()
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    #------------------------#
    #    NEW COMMAND STYLE   #
    #------------------------#
    # 2020 Help Command
    if message.content.startswith(prefix + 'help'):
        print("[FLAME] Help Command Sent by" + str(message.author))
        args = message.content.split(" ")
        try:
            if args[1] == "clock":
                embed = discord.Embed(
                    title = 'Clock Command',
                    description = 'Shows you the current time.',
                    color = discord.Color.red()
                )
                embed.set_footer(text='Support Server: https://discord.gg/zRFpys7 \nWebsite: http://flamebot.rf.gd/ ')
                embed.add_field(name='Usage',value='``&clock``',inline=False)
            elif args[1] == "8ball":
                embed = discord.Embed(
                    title = 'Magic 8-Ball Command',
                    description = 'A fortune teller. Ask it a question and it will awnser it.',
                    color = discord.Color.red()
                )
                embed.set_footer(text='Support Server: https://discord.gg/zRFpys7 \nWebsite: http://flamebot.rf.gd/ ')
                embed.add_field(name='Usage',value='``&8ball <question>``',inline=False)
            elif args[1] == "rng":
                embed = discord.Embed(
                    title = 'Random Number Generator Command',
                    description = 'Generates a Number between X value and Y value.',
                    color = discord.Color.red()
                )
                embed.set_footer(text='Support Server: https://discord.gg/zRFpys7 \nWebsite: http://flamebot.rf.gd/ ')
                embed.add_field(name='Usage',value='``&rng <min-val> <max-val>``',inline=False)
            elif args[1] == "calc":
                embed = discord.Embed(
                    title = 'Basic Calculator Command',
                    description = 'Basic Calculator. Calculates something',
                    color = discord.Color.red()
                )
                embed.set_footer(text='Support Server: https://discord.gg/zRFpys7 \nWebsite: http://flamebot.rf.gd/ ')
                embed.add_field(name='Usage',value='``&calc <val> [method] <val>``',inline=False)
            elif args[1] == "calc":
                embed = discord.Embed(
                    title = 'Basic Calculator Command',
                    description = 'Basic Calculator. It calculates using addition (+), subtraction (-), division (/) or multiplication (*)',
                    color = discord.Color.red()
                )
                embed.set_footer(text='Support Server: https://discord.gg/zRFpys7 \nWebsite: http://flamebot.rf.gd/ ')
                embed.add_field(name='Usage',value='``&calc <val> [method] <val>``',inline=False)
            elif args[1] == "about":
                embed = discord.Embed(
                    title = 'About Command',
                    description = 'Gives you information on the bot.',
                    color = discord.Color.red()
                )
                embed.set_footer(text='Support Server: https://discord.gg/zRFpys7 \nWebsite: http://flamebot.rf.gd/ ')
                embed.add_field(name='Usage',value='``&about``',inline=False)
            elif args[1] == "help":
                embed = discord.Embed(
                    title = 'Help Command',
                    description = 'Sends an command list',
                    color = discord.Color.red()
                )
                embed.set_footer(text='Support Server: https://discord.gg/zRFpys7 \nWebsite: http://flamebot.rf.gd/ ')
                embed.add_field(name='Usage',value='``&help [optional command]``',inline=False)
            elif args[1] == "ping":
                embed = discord.Embed(
                    title = 'Ping Command',
                    description = 'Responds with the ping in milliseconds (ms).',
                    color = discord.Color.red()
                )
                embed.set_footer(text='Support Server: https://discord.gg/zRFpys7 \nWebsite: http://flamebot.rf.gd/ ')
                embed.add_field(name='Usage',value='``&about``',inline=False)
            elif args[1] == "avatar":
                embed = discord.Embed(
                    title = 'Avatar Command',
                    description = 'Sends an avatar of a specified user',
                    color = discord.Color.red()
                )
                embed.set_footer(text='Support Server: https://discord.gg/zRFpys7 \nWebsite: http://flamebot.rf.gd/ ')
                embed.add_field(name='Usage',value='``&avatar <user>``',inline=False)
            elif args[1] == "clear":
                embed = discord.Embed(
                    title = 'Clear Command',
                    description = 'Clears a set amount of messages',
                    color = discord.Color.red()
                )
                embed.set_footer(text='Support Server: https://discord.gg/zRFpys7 \nWebsite: http://flamebot.rf.gd/ ')
                embed.add_field(name='Usage',value='``&clear <amount>``',inline=False)
            elif args[1] == "include-ea": # These are commands for the Early Preview Users
                embed = discord.Embed(
                    title = 'Flame Command List',
                    description = 'Command Prefix: ``&``',
                    color = discord.Color.red()
                )
                embed.set_footer(text='Support Server: https://discord.gg/zRFpys7 \nWebsite: http://flamebot.rf.gd/ ')
                embed.add_field(name=':alarm_clock: Time :alarm_clock:',value='``clock``',inline=False)
                embed.add_field(name=':game_die: Fun :game_die:',value='``8ball``, ``rng``',inline=False)
                embed.add_field(name=':hammer_and_wrench: Utilities :hammer_and_wrench:',value='``calc``',inline=False)
                embed.add_field(name=':information_source: Information :information_source:',value='``about``, ``help``, ``ping``, ``avatar``',inline=False)
                embed.add_field(name=':hammer: Moderation :hammer:',value='``clear``',inline=False)
                if message.channel.id == "640258775684612166":
                    embed.add_field(name=':warning: Early-Access Users Only :warning:',value='``connect``,``disconnect``,``help``',inline=False)
            else:
                raise IndexError
        except IndexError:
            embed = discord.Embed(
                title = 'Flame Command List',
                description = 'Command Prefix: ``&``',
                color = discord.Color.red()
            )
            embed.set_footer(text='Support Server: https://discord.gg/zRFpys7 \nWebsite: http://flamebot.rf.gd/ ')
            embed.add_field(name=':alarm_clock: Time :alarm_clock:',value='``clock``',inline=False)
            embed.add_field(name=':game_die: Fun :game_die:',value='``8ball``, ``rng``',inline=False)
            embed.add_field(name=':hammer_and_wrench: Utilities :hammer_and_wrench:',value='``calc``',inline=False)
            embed.add_field(name=':information_source: Information :information_source:',value='``about``, ``help``, ``ping``, ``avatar``',inline=False)
            embed.add_field(name=':hammer: Moderation :hammer:',value='``clear``',inline=False)
            
        try:
            msg = ':incoming_envelope: I have sent an message with the commands to help you.'
            await client.send_message(message.author, embed=embed)
            await client.send_message(message.channel, msg)
        except:
            await client.send_message(message.channel, pmsg)
    #------------------------
    #    BOT INFO COMMANDS
    #------------------------
    
    # About Command
    if message.content.startswith(prefix + 'about'):
        print("[FLAME] About Command Sent")
        msg = 'Hello. My bot name is **Flame** and I am created by ``Edgewurth#1827``.\n I am in ' + str(len(client.servers)) + ' servers.\nDevelopment begun on the 1st September 2019.\nMy support discord is at https://discord.gg/Xb5asjm - join it if you need help.'
        await client.send_message(message.channel, msg)
    
    # Perms Command
    if message.content.startswith(prefix + 'perms'):
        print("[FLAME] About Command Sent")
        msg = ':incoming_envelope: I have sent an message with the permissions list.'
        pmsg = 'List of **Flame** permissions\n__``&clear``__\nThis Command Requires Manage Messages for the User and Bot.'
        try:
            args = message.content.split(" ")
            await client.send_message(message.author, pmsg)
            await client.send_message(message.channel, msg)
        except:
            msg = ':warning: ERROR: ``Unable to DM you the permissions list.``'
            await client.send_message(message.channel, msg)
            
            
    # Credits Commands
    if message.content.startswith(prefix + 'credits'):
        print("[FLAME] Credits Command Sent")
        try:
            args = message.content.split(" ")
            msg = ':incoming_envelope: I have sent an message with the credits.'
            pmsg = 'This is the list of people who have helped with the development of **Flame** in history or to the present.\n__Lead Developer__\nEdgewurth\n__Developers__\niycchan\nnicochulo2001\nRedDog2904\n__Tools Used__\nPython Language\nDiscord.PY\nHeroku\n__Special Thanks__\nCekko for setting up the discord support server\nAnd You for the Usage of this Bot!'
            await client.send_message(message.author, pmsg)
            await client.send_message(message.channel, msg)
        except:
            msg = ':warning: ERROR: ``Unable to DM you the credits list.``'
            await client.send_message(message.channel, msg)
                
        
    # Ping Command
    if message.content.startswith(prefix + 'ping'):
        timestampbef = datetime.datetime.now().timestamp()
        print("[FLAME] Ping Command Sent by ", message.author)
        msg = 'Pinging... Please Wait...'
        await client.send_message(message.channel, msg)
        timestampaft = datetime.datetime.now().timestamp()
        latency = timestampaft - timestampbef
        msg = 'Pong! The latency is ' + str(round(latency, 3)) + 'ms'
        await client.send_message(message.channel, msg)
    # Version Command
    if message.content.startswith(prefix + 'version'):
        msg = '__***FLAME***___\nVersion Siries: ' + version + '\nRunning Python: 3.6.8 with Discord.py as framework\nHosted on Heroku'
        await client.send_message(message.channel, msg)
    #------------------
    # MUSIC COMMANDS
    #------------------
    # Connect to Channel Command
    if message.content.startswith(prefix + 'connect'):
        if message.channel.id == "640258775684612166":
            print("[FLAME] Connect Command Sent")
            author = message.author
            channel = author.voice_channel
            await client.join_voice_channel(channel)
            msg = ':speaker: I have joined the voice channel you\'re in!'
            await client.send_message(message.channel, msg)
    # Disconnect to Channel Command - DISFUNCTIONAL
    if message.content.startswith(prefix + 'disconnect'):
        if message.channel.id == "640258775684612166":
            print("[FLAME] Disconnect Command Sent")
            server = message.server
            voice_client = client.voice_client_in(server)
            await voice_client.disconnect()
    # Play Command - DISFUNCTIONAL
    if message.content.startswith(prefix + 'play'):
        if message.channel.id == "640258775684612166":
            args = message.content.split(" ")
            url = args[1]
            server = message.server
            voice_client = client.voice_client_in(server)
            player = await voice_client.create_ytdl_player(url)
            players[server.id] = player
            player.start()
        print("[FLAME] Connect Command Sent")
        author = message.author
        channel = author.voice_channel
        await client.join_voice_channel(channel)
        msg = ':speaker: I have joined the voice channel you\'re in!'
        await client.send_message(message.channel, msg)
    # Disconnect to Channel Command - DISFUNCTIONAL
    if message.content.startswith(prefix + 'disconnect'):
        print("[FLAME] Disconnect Command Sent")
        server = message.server
        voice_client = client.voice_client_in(server)
        await voice_client.disconnect()
    # Play Command - DISFUNCTIONAL
    if message.content.startswith(prefix + 'play'):
        args = message.content.split(" ")
        url = args[1]
        server = message.server
        voice_client = client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
        players[server.id] = player
        player.start()
        player.start()
    #------------------
    # TIME COMMANDS
    #------------------
    # Current Time Command
    if message.content.startswith(prefix + 'clock'):
        print("[FLAME] Clock Command Sent")
        msg = datetime.datetime.now()
        await client.send_message(message.channel, msg)
            
    # Countdown Command
    if message.content.startswith(prefix + 'countdown'):
#        print("[FLAME] Countdown Command")
        args = message.content.split(" ")
        times = args[1]
        format = args[2]
 #      msg = 'Started a Timer of ' + times + format
        msg = 'Currently disabled'
        await client.send_message(message.channel, msg)
  #      client.loop.create_task(countdown_command(times, format))
    # TEST COMMAND
    if message.content.startswith(prefix + 'xtest'):
        args = message.content.split(" ")
        args.remove[0]
        msg = str(args)
        await client.send_message(message.channel, msg)
    #------------------
    # ADMIN COMMANDS
    #------------------ 
    # Warn
    if message.content.startswith(prefix + 'warn'):
        if message.author.server_permissions.kick_members:
            args = message.content.split(" ")
            username = args[1]
            reason = args[2]
            msg = 'Warned ' + str(discord.User.name) + ' for ' + str(reason)
            pmsg = 'You have been warned!\n**Reason: ' + reason
            await client.send_message(message.channel, msg)
            await client.send_message(discord.User(username).dm_channel, pmsg)
        else:
            msg = ':warning: ERROR: ``You do not have the permission "Kick Members"``'
            await client.send_message(message.channel, msg)
    # Clear
    if message.content.startswith(prefix + 'clear'):
        print("[FLAME] Clear Command")
        if message.author.server_permissions.manage_messages:
            msgs = []
            args = message.content.split(" ")
            amount = args[1]
            async for message in client.logs_from(message.channel, limit=int(amount) + 1):
                msgs.append(message)
            await client.delete_messages(msgs)
            await client.send_message(message.channel, ':wastebasket: Deleted ' + amount + ' messages')
        else:
            msg = ':warning: ERROR: ``You do not have the permission "Manage Messages"``'
            await client.send_message(message.channel, msg)
    #EMERGENCY        
    if message.content.startswith(prefix + 'clearx'):
        if message.author.server_permissions.manage_messages:
            try:
                msgs = []
                args = message.content.split(" ")
                amount = args[1]
                async for message in client.logs_from(message.channel, limit=int(amount) + 1):
                    msgs.append(message)
                    await client.delete_messages(msgs)
                await client.send_message(message.channel, 'Deleted ' + amount + ' messages')
            except IndexError:            
                msg = ':warning: ERROR: ``Value \'amount\' needs to be filled!``'
                await client.send_message(message.channel, msg)
            except:
                msg = ':warning: ERROR: ``Unknown Error``'
                await client.send_message(message.channel, msg) 
        else:
            msg = ':warning: ERROR: ``You do not have the permission "Manage Messages"``'
            await client.send_message(message.channel, msg)
    # Kick
    if message.content.startswith(prefix + 'kick'):
        if message.author.server_permissions.kick_members:
            args   = message.content.split(" ")
            userId = args[1]
            username = client.get_user_info(userId)
            await client.kick(username)
            msg = 'Kicked ' + args[1]
            await client.send_message(userId, msg)
        else:
            msg = ':warning: ERROR: ``You do not have the permission "Kick Members"``'
            await client.send_message(message.channel, msg)
    #------------------
    # UTILITIES
    #------------------
    # CALC Command
    if message.content.startswith(prefix + 'calc'):
        args   = message.content.split(" ")
        no1    = int(args[1])
        action = args[2]
        no2    = int(args[3])
        if action == '*':
            awns = no1 * no2
            msg = str(no1) + ' ' + str(action) + ' ' + str(no2) + ' = ' + str(awns) 
            await client.send_message(message.channel, msg)
        elif action == '/':
            awns = no1 / no2
            msg = str(no1) + ' ' + str(action) + ' ' + str(no2) + ' = ' + str(awns) 
            await client.send_message(message.channel, msg)
        elif action == '+':
            awns = no1 + no2
            msg = str(no1) + ' ' + str(action) + ' ' + str(no2) + ' = ' + str(awns) 
            await client.send_message(message.channel, msg)
        elif action == '-':
            awns = no1 - no2
            msg = str(no1) + ' ' + str(action) + ' ' + str(no2) + ' = ' + str(awns) 
            await client.send_message(message.channel, msg)
        else:
            msg = ':warning: ERROR: ``Value \'action\' needs to have an valid id from (* / + -)!``'
            await client.send_message(message.channel, msg)
        
    #------------------
    # USER COMMANDS
    #------------------
    # Avatar CMD
    if message.content.startswith(prefix + 'avatar'):
        try:
            if (message.mentions.__len__()>0):
                for user in message.mentions:
                    await client.send_message(message.channel, '>>> ' + user.avatar_url)
        except:
            await client.send_message(message.channel, '>>> ' + message.author.avatar_url)
    # User Info CMD
    
    #------------------
    # FUN COMMANDS
    #------------------
    # - RNG Command -
    if message.content.startswith(prefix + 'rng'):
        print("[FLAME] RNG Command Sent")
        args = message.content.split(" ")
        try:
            msg = random.randint(int(args[1]), int(args[2]))
            await client.send_message(message.channel, msg)
        except IndexError:
            msg = ':warning: ERROR: ``Values \'minval\' and \'maxval\' needs to be filled!``'
            await client.send_message(message.channel, msg)
        except:
            msg = ':warning: ERROR: ``Unknown Error``'
            await client.send_message(message.channel, msg)
    # 8-Ball Command Command x
    if message.content.startswith(prefix + '8ball'):
        print("[FLAME] 8Ball Command Sent")
        possible_responses = [
        'It is certain.',
        'It is decidedly so.',
        'Without a doubt.',
        'Yes - definitely.',
        'You may rely on it.',
        'As I see it, yes.',
        'Most likely.',
        'Outlook good.',
        'Yes.',
        'Signs point to yes.',
        'Reply Hazy, try again.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'Don\'t count on it.',
        'My reply is no.',
        'My sources say no',
        'Outlook not so good.',
        'Very doubtful.',
        'No.',
        ]
        await client.send_message(message.channel, random.choice(possible_responses))

    #---------------------
    # HIDDEN DEBUG CMDS
    #---------------------
    # NOTE: Only Ryan can access these
    if message.content.startswith(prefix + 'debug_token'):
        if message.author.id == "354512960250576896":
            await client.send_message(message.channel, TOKEN)
    if message.content.startswith(prefix + 'debug_announce'):
        if message.author.id == "354512960250576896":
            args = message.content.split(" ")
            msg  = '@everyone ' + args[1] 
            await client.send_message(discord.Object(id='609681917331243048'), msg)
    if message.content.startswith(prefix + 'debug_update_changelog'):
        if message.author.id == "354512960250576896":
            args = message.content.split(" ")
            msg  = str(args)
            await client.send_message(discord.Object(id='609681917331243048'), msg)
    if message.content.startswith(prefix + 'debug_getuserid'):
        args   = message.content.split(" ")
        userId = args[1]
        username = client.get_user_info(userId)
        msg = 'An name is ' + str(username)
        await client.send_message(message.channel, msg)
@client.event
async def countdown_command(times, format):
    await client.wait_until_ready()
 # Lets define our interval multipliers to start with (assuming 'tick' is in ms intervals).
    m = 60*1000     # 60 seconds to a minute
    h = int(m)*60   # 60 minutes to an hour
    d = int(h)*24   # 24 hours to a day
    w = int(d)*7    # 7 days to a week
    mo = int(w)*4    # 4 weeks to a 28 day month (for now - need some special handling for calendar months
   
    # Let's just set a zero duration value here for now. Will throw exception for incorrect time format later
    duration = 0
    if timeFormat == 'm':
            duration = int(m)*int(numberOfIntervals) # I'm playing safe by typecasting here
    if timeFormat == 'h':
            duration =  int(m)*int(numberOfIntervals)
    if timeFormat == 'd':
            duration = int(m)*int(numberOfIntervals)
    if timeFormat == 'w':
            duration = int(w)*int(numberOfIntervals)
    if timeFormat == 'mo':
            duration =  int(mo)*int(numberOfIntervals)
          
    
    
    
    ################################################################################
    # Deprecated Code
    ################################################################################
    #if format == 'm':
        ## Secs = Mins * 60
        #times = times * 60
    #elif format == 'h':
        ## Mins = H * 60
        #times = times * 60
        ## Secs = Mins * 60
        #times = times * 60
    #elif format == 'd':
        ## Day = H * 24
        #times = times * 24
        ## Mins = H * 60
        #times = times * 60
        ## Secs = Mins * 60
        #times = times * 60
    #elif format == 'mo':
        ## Month = D * 28
        #times = times * 28
        ## Day = H * 24
        #times = times * 24
        ## Mins = H * 60
        #times = times * 60
        ## Secs = Mins * 60
        #times = times * 60
    #times = int(times)
    
    
    
    
    ################################################################################
    # Give periodic reminders....disable for now
    # Also a lot of 'magic' numbers here.....need to remove to make code clearer
    ################################################################################
    #while times >= 0:
        #if times == 7200:
            #msg = '2 Hours Left'
            #await client.send_message(message.channel, msg)
        #elif times == 3600:
            #msg = '1 Hour Left'
            #await client.send_message(message.channel, msg)
        #elif times == 2700:
            #msg = '45 Minutes Left'
            #await client.send_message(message.channel, msg)
        #elif times == 1800:
            #msg = '30 Minutes Left'
            #await client.send_message(message.channel, msg)
        #elif times == 900:
            #msg = '15 Minutes Left'
            #await client.send_message(message.channel, msg)
        #elif times == 600:
            #msg = '10 Minutes Left'
            #await client.send_message(message.channel, msg)
        #elif times == 300:
            #msg = '5 Minutes Left'
            #await client.send_message(message.channel, msg)
        #elif times == 120:
            #msg = '2 Minutes Left'
            #await client.send_message(message.channel, msg)
        #elif times == 60:
            #msg = '1 Minute Left'
            #await client.send_message(message.channel, msg)
        #elif times == 30:
            #msg = '30 Seconds Left'
            #await client.send_message(message.channel, msg)
        #sleep(1)
        #times = times - 1
    #msg = '{0.author.mention}\'s Alarm is Rinning!'.format(message)
    #await client.send_message(message.channel, msg)
    
    #########################################################################################
    # End of mods take 1
    #########################################################################################
    
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name=prefix + 'help'))
    await client.change_status(game=discord.Game(name=prefix + 'help'))
    print("[FLAME] Bot Signed In and Started!")
client.run(TOKEN)
