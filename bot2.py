import asyncio,discord,os
from discord.ext import commands
import random
import datetime
import time

bot = commands.Bot(command_prefix='~',status=discord.Status.online,help_command=None)

client = discord.Client()
logging_token = 0
#char_message = message.content
now_time = datetime.datetime.now()
logtext='str'
canuse = 0
past = 'str'
Now = 'str'
Excluded_Channel='sever_log'
random_cos = 0
wt = 0
chat_now ='str'
chat_past = 'str'
damage = 10000

@bot.event
async def on_ready():
    print('$ 다음으로 로그인합니다: ')
    print(bot.user.name)
    print('$ connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=None)
    print(f'$ 현 시각: {now_time}')

@bot.event
async def on_message(message):
    global logging_token
    global f
    global char_message
    global now_time
    global canuse
    global Now
    global past
    global random_cos
    global wt
    global chat_now
    global chat_past
    global damage
    msg = "<@{}>".format(message.author.id)
    if msg != '<@785114630434717726>':
        chat_past = chat_now
        chat_now = msg
    #    print(f'{chat_now} 챗나우 / {chat_past} 챗패스트')   

    #if msg!='<@404179080074887168>':
    #    print('관리자로 등록되지 않은 이용자의 접근이 차단되었습니다.')
    #    await message.channel.send('관리자 권한이 아닙니다. 봇 관리자에게 문의하여 주십시오')
    #    return
    #if message.author == client.user:
    #    return
    char_message = message.content
    if msg == '<@785114630434717726>': #봇
        canuse = 0
    if msg != '<@404179080074887168>' and msg != '<@333921998101020672>' and msg != '<@368794004399194114>': # 나 / 넥스형
        canuse = 0
        if msg != '<@785114630434717726>':
            if char_message == '~logging' or char_message == '~stop' or char_message == '~print log':
                await message.channel.send("관리자용 커맨드 접근 권한이 없으셔요. 관리자에게 확인 부탁드릴게요!")
    if msg == '<@404179080074887168>' or msg == '<@333921998101020672>' or msg == '<@368794004399194114>':
        canuse = 1
    if msg == '<@404179080074887168>':
        if char_message == '~kill':
            await message.channel.send("관리자의 명령에 따라 로코코의 작동이 일시 중단됩니다")
            time.sleep(10)
            await message.channel.send("다시 작동합니다!")
    #일반 유저용 커맨드
    if char_message == '~안녕 로코코' or char_message == '~안녕 로코코!' or char_message == '~로코코 안녕' or char_message == '~로코코 안녕!' or char_message == '~안녕' or char_message == '~안녕!':

        #사용 코드 줄에 따라 randint함수 2번 인자를 (-1) 조정하십시오
        random_cos = random.randint(1,3)
        print(f'안녕 - random_cos : {random_cos}')
        print(f'{msg}가 안녕 코드를 사용하였습니다.')

        if msg == '<@597063607041261568>':
            if random.randint(1,11) == 1:
                wt = 1 #백호 전용 루틴 작동.
                await message.channel.send(f'주인님 안녕하세요~! 우리들의 아이돌 {msg}님')

        if wt == 0:
            print('Normal code Activation')
            if random_cos == 1:
                await message.channel.send(f'안녕하세요~! {msg}님!')
            if random_cos == 2:
                await message.channel.send(f'반가워요! {msg}님!')
        wt = 0 #루틴 종료
    if char_message == '~로코코 몸통박치기':
        if chat_past == 'str':
            await message.channel.send('누가 먼저 말씀하신건지 모르겠어요...')
            await message.channel.send('(봇이 작동되자마자는 이 명령이 작동할수 없어요 ㅠ)')
        if chat_past != 'str':
            if chat_past == chat_now:
                await message.channel.send('정말 자신을 공격하시려구요....?')
            if chat_past != chat_now:
                damage = random.randint(1, 9999)
                await message.channel.send(f'이익! 쿵')
                await message.channel.send(f'{chat_past}님께서 {damage}만큼의 피해를 입으셨습니다....')
    
    if char_message == '~help' or char_message == '~도움말' or char_message == '~명령어':
        embed = discord.Embed(title="명령어", description="로코코에게 도움말을 요청하려면'~help, ~도움말, ~명령어 라고 말해주세요!'", color=0x62c1cc)
        embed.set_footer(text="~로코코 안녕, ~안녕 로코코, ~안녕\n저에게 인사를 해주시면 저도 답해드릴거에요! \n\n~로코코 몸통박치기\n방금 말씀하신 분에게 돌진해요! 1~9999사이의 데미지를 입어요\n주인님에겐 10분의 1의 확률로 이스터에그가 나와요!")
        await message.channel.send("로코코가 할수 있는 것들이에요!", embed=embed)
        if msg == '<@404179080074887168>' or msg == '<@333921998101020672>' or msg == '<@368794004399194114>':
            await message.channel.send("관리자 전용 명령어는 ~관리자 도움말 이라고 말해주시면 알려드릴게요!")

    if char_message == '~관리자 도움말':
        embed = discord.Embed(title="관리자용 로그 명령어", description="따로 등록된 관리자 분들이 사용하실수 있는 명령어들이에요!", color=0x62c1cc)
        embed.set_footer(text="~logging\n모든 말씀들을 전부 받아 적기 시작해요!\n따로 확인 가능하니 거짓말은 하지 말자구요!\n\n~stop\n노트를 덮고 그만 받아 적어요! 나중에 다른 명령어로 확인해볼수도 있어요\n\n~print log\n방금 받아적은 노트를 보여드려요!\n안타깝게도 제 노트는 2000자 뿐이라 이상이 되면 보여드릴수 없어요.\n(오류가 발생해요)")
        await message.channel.send("관리자용 로그 명령어들이에요!", embed=embed)
    #메시지 로그용 / 관리자 코드
    if canuse == 1:
        #cha = message.channel
        if char_message == '~logging':
            if logging_token == 1:
                await message.channel.send('이미 대화가 로깅중이에요!')
            if logging_token == 0:
                await message.channel.send('로깅을 시작할게요!')
                f = open("log.txt", 'a')
                logging_token = 1
                print('$system > logging_token : ', logging_token)

        if char_message == '~stop':
            if logging_token == 0:
                await message.channel.send('로깅 프로그램이 작동중이지 않아요')
            if logging_token == 1:
                await message.channel.send('로깅을 중단할게요!')
                f.close()
                logging_token = 0 
                print('$system > logging_token : ', logging_token)

        if char_message == '~print log':
            if logging_token == 1:
                await message.channel.send('강제로 로깅을 종료할게요....')
                logging_token = 0
            f.close()
            f = open("log.txt", 'r')
            logtext = f.read()
            await message.channel.send(logtext)
            print('$system > printing log........')
            f.close()


    if logging_token == 1 and char_message != '~stop':
        #메시지 로그 시작
        now = message.channel.name
        if now != Excluded_Channel:
            if now != past:
                f.write(now)
                f.write(" : \n")
                print('$system > change channel ( log )')
            f.write(now_time.strftime('20%y-%m-%d %H:%M:%S'))
            f.write(" / id: ")
            f.write(msg)
            f.write(" >> ")
            f.write(char_message)
            f.write('\n') #다음 줄을 위해 줄바꿈.
            #현 포맷 : id: <!@id>  >> text \n
            print(now_time, msg, ' > 로깅 내용: ',char_message)
            print(message.channel.name)
            past = now
             


#@bot.command(name='logging')
#@commands.has_role('진-무법자')
#async def log_start(ctx, pra_str):
#    if pra_str == 'prameter':
#        await ctx.send('파라메터를 인식하였습니다')
#        await ctx.send('대화 로깅을 시작합니다.')

#@log_start.error
#async def log_error(ctx, error):
#    await ctx.send("예외 처리 불가능한 오류가 발생하였습니다.")
#    await ctx.send("예상 : 파라메터를 지정하지 않으셨을 가능성이 높습니다.")

bot.run('Nzg1MTE0NjMwNDM0NzE3NzI2.X8zI-g.72lVMCz0sme24Oz1a-2oztWWB8o')