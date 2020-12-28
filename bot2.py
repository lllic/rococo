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
testvar1 = 0
testvar2 = 0
errorc = 0
name = 'str'
hello_time = datetime.datetime.now()
hello_u = 0
fl = 0
it_ok = 0
str_len = 0
texttext = 'str'

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
    global testvar1
    global testvar2
    global errorc
    global name
    global hello_time
    global fl
    global it_ok
    global str_len
    hello_time = datetime.datetime.now()
    hello_time = hello_time.strftime('%H')
    msg = "<@{}>".format(message.author.id)
    if msg != '<@785114630435717726>':
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
    #################################################################################################
    #if msg == '<@785114630435717726>': #봇
    #    canuse = 0
    #if msg != '<@404179080074887168>' and msg != '<@333921998101020672>' and msg != '<@368794004399194114>': # 나 / 넥스형
    #    canuse = 0
    #    if msg != '<@785114630435717726>':
    #       if char_message == '~logging' or char_message == '~stop' or char_message == '~print log':
    #            await message.channel.send("관리자용 커맨드 접근 권한이 없으셔요. 관리자에게 확인 부탁드릴게요!")
    #if msg == '<@404179080074887168>' or msg == '<@333921998101020672>' or msg == '<@368794004399194114>':
    #    canuse = 1
    #if msg == '<@404179080074887168>':
    #    if char_message == '~kill':
    #        await message.channel.send("관리자의 명령에 따라 로코코의 작동이 일시 중단됩니다")
    #        time.sleep(10)
    #        await message.channel.send("다시 작동합니다!")
    #################################################################################################

    if msg == '<@785114630435717726>':
        canuse = 0
    elif msg != '<@404179080074887168>' and msg != '<@333921998101020672>' and msg != '<@368794004399194114>':
        canuse = 0
        if char_message == '~logging' or char_message == '~stop' or char_message == '~print log':
            await message.channel.send("관리자용 커맨드 접근 권한이 없으셔요. 관리자에게 확인 부탁드릴게요!")
    elif msg == '<@404179080074887168>' or msg == '<@333921998101020672>' or msg == '<@368794004399194114>':
        canuse = 1
    
    if msg == '<@404179080074887168>':
        if char_message == '~kill':
            await message.channel.send("관리자의 명령에 따라 로코코의 작동이 일시 중단됩니다")
            time.sleep(10)
            await message.channel.send("다시 작동합니다!")





    #일반 유저용 커맨드
    if char_message == '~안녕 로코코' or char_message == '~안녕 로코코!' or char_message == '~로코코 안녕' or char_message == '~로코코 안녕!' or char_message == '~안녕' or char_message == '~안녕!':

        #사용 코드 줄에 따라 randint함수 2번 인자를 (-1) 조정하십시오
        random_cos = random.randint(1,4)
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
            elif random_cos == 2:
                await message.channel.send(f'반가워요! {msg}님!')
            elif random_cos == 3:
                await message.channel.send(f'{msg}님! 부르셨나요?')
            # 아침 인사, 점심 인사(오늘 하루~), 저녁 인사
            elif random_cos == 4:
                hello_u = random.randint(1,3)
                if int(hello_time) > 2 and int(hello_time) < 7:
                    #새벽 (오전 3시~오전 6시)
                    if hello_u == 1:
                        await message.channel.send(f'새벽이에요 {msg}님!! 얼른 주무세요!!')
                    if hello_u == 2:
                        await message.channel.send(f'Zzz...(잠든것 같아요)')
                if int(hello_time) > 6 and int(hello_time) < 13:
                    #오전 (오전 7시~오전 12시)
                    if hello_u == 1:
                        await message.channel.send(f'반가워요! 좋은 아침이에요 {msg}님!')
                    if hello_u == 2:
                        await message.channel.send(f'안녕히 주무셨나요 {msg}님?')
                if int(hello_time) > 12 and int(hello_time) < 20:
                    #오후 (오후 1시~오후 7시)
                    if hello_u == 1:
                        await message.channel.send(f'안녕하세요! 좋은 하루 보내고 계신가요 {msg}님?')
                    if hello_u == 2:
                        await message.channel.send(f'안녕하세요! 오늘 하루도 서서히 끝나가고 있네요.. {msg}님')
                if int(hello_time) > 19 and int(hello_time) < 25 or int(hello_time) > 0 and int(hello_time) < 3 or int(hello_time) == 0:
                    #저녁 (오후 8시~오전 2시까지)
                    if hello_u == 1:
                        await message.channel.send(f'안녕하세요..! {msg}님! 로코코는 이제 자러 갈 시간이에요... ')
                    if hello_u == 2:
                        await message.channel.send(f'안녕하세요 {msg}님! 오늘 하루도 수고하셨어요')


        wt = 0 #루틴 종료
    if char_message == '~로코코 몸통박치기':
        if chat_past == 'str':
            await message.channel.send('누가 먼저 말씀하신건지 모르겠어요...')
            await message.channel.send('(봇이 작동되자마자는 이 명령이 작동할수 없어요 ㅠ)')
        else:
            if chat_past == chat_now:
                await message.channel.send('정말 자신을 공격하시려구요....?')
            if chat_past != chat_now:
                damage = random.randint(1, 9999)
                await message.channel.send(f'이익! 쿵')
                await message.channel.send(f'{chat_past}님께서 {damage}만큼의 피해를 입으셨습니다....')
    #####################################################################################
    #if char_message[0:7] == '~로코코 돌진':
    #    fl = 1
    #####################################################################################
    if char_message[0:8] == '~로코코 돌진 ':
        if char_message[0:12] != '~로코코 돌진 데미지 ':
            errorc = 0
            testvar1 = char_message.find('<')
            testvar2 = char_message.find('>')
            if testvar1 == -1 or testvar2 == -1:
                errorc = 1
            else:
                if testvar2 - testvar1  != 21 :
                    errorc = 1
                if char_message.find('@') != testvar1 + 1:
                    errorc = 1
                if char_message.find('!') != char_message.find('@') + 1:
                    errorc = 1
            if errorc == 0:
                name = '<@' + str(char_message[testvar1+3:testvar1+22])
                if msg == name:
                    await message.channel.send('정말 자신을 공격하시려구요.......?')
                if msg != name:
                    damage = random.randint(1, 9999)
                    name = char_message[testvar1+3:testvar1+22]
                    await message.channel.send('이익! 쿵')
                    await message.channel.send(f'<@{name}님께서 {damage}만큼의 피해를 입으셨습니다.....')
            else:
                await message.channel.send('명령어에 오류가 있는것 같아요... 다시 확인해주세요!')
        else:
            random_cos = random.randint(1,5)
            if random_cos == 4:
                random_cos = random.randint(1,3)
                if random_cos == 1:
                    await message.channel.send('사이좋게 지내야죠!')
                if random_cos == 2:
                    await message.channel.send('그러면 못써요!')
                if random_cos == 3:
                    await message.channel.send('그럴수는 없어요!')
            else:
                #돌진-데미지 섹터
                errorc = 0
                testvar1 = char_message.find('<')
                testvar2 = char_message.find('>')
                if testvar1 == -1 or testvar2 == -1:
                    errorc = 1
                else:
                    if testvar2 - testvar1  != 21 :
                        errorc = 1
                    if char_message.find('@') != testvar1 + 1:
                        errorc = 1
                    if char_message.find('!') != char_message.find('@') + 1:
                        errorc = 1
                if errorc == 0:
                    name = '<@' + str(char_message[testvar1+3:testvar1+22])
                    if msg == name:
                        await message.channel.send('정말 자신을 공격하시려구요.......?')
                    if msg != name:
                        #유저 코드 확인 완료
                        name = char_message[testvar1+3:testvar1+22]
                        damage = char_message[35:len(char_message)]
                        #로직 삽입 시작은 여기서..
                        str_len = len(char_message) - 35
                        for a in range(0, str_len):
                            #print(f'{a}({i[a+35]})는 {type(i[a+35])}입니다')

                            it_ok = 0

                            for b in range(0, 10):
                                #print(f'테스팅 {b}')
                                if str(char_message[a+35]) == str(b):
                                    #print('숫자입니다')
                                    it_ok = 1
                            if it_ok == 0:
                                print('숫자가 아닌 문자 존재')
                                it_ok = 2
                                break
                        if it_ok == 2:
                            print('오류')
                        else:
                            print('정상')
                            if len(char_message) <= 35:
                                await message.channel.send('명령어에 오류가 있는것 같아요... 확인 부탁드릴게요!')
                            else:
                                await message.channel.send('이익! 쿵')
                                await message.channel.send(f'<@{name}님께서 {damage}만큼의 피해를 입으셨습니다.....')
                else:
                    await message.channel.send('누구에게 하라는건지 잘 모르겠어요 ㅠ')
    
    elif char_message[0:7] == '~로코코 돌진':
        await message.channel.send('어떤 분께 하라는건지 잘 모르겠어요ㅠ')

    #####################################################################################
    #if fl == 1 :
    #    await message.channel.send('어떤 분께 하라는건지 잘 모르겠어요ㅠ')
    #    fl = 0
    #####################################################################################
        #
    #로코코 돌진 데미지 입력 명령어
    #if char_message[0:8] == '~로코코 돌진 데미지 ':
    #    errorc = 0
    #    testvar1 = char_message.find('<')
    #    testvar2 = char_message.find('>')
    #    if testvar1 == -1 or testvar2 == -1:
    #        errorc = 1
    #    else:
    #        if testvar2 - testvar1  != 21 :
    #            errorc = 1
    #        if char_message.find('@') != testvar1 + 1:
    #            errorc = 1
    #        if char_message.find('!') != char_message.find('@') + 1:
    #            errorc = 1
    #    if errorc == 0:
    #        name = '<@' + str(char_message[testvar1+3:testvar1+22])
    #        if msg == name:
    #            await message.channel.send('정말 자신을 공격하시려구요.......?')
    #        if msg != name:
    #            damage = char_message.find('>')
    #            name = char_message[testvar1+3:testvar1+22]
    #            await message.channel.send('이익! 쿵')
    #            await message.channel.send(f'<@{name}님께서 {damage}만큼의 피해를 입으셨습니다.....')
    #    else:
    #        await message.channel.send('명령어에 오류가 있는것 같아요... 다시 확인해주세요!')
    #if char_message[0:7] == '~로코코 돌진':
    #    await message.channel.send('어떤 분께 하라는건지 잘 모르겠어요ㅠ')
    texttext = "~로코코 안녕, ~안녕 로코코, ~안녕\n저에게 인사를 해주시면 저도 답해드릴거에요!\n주인님에겐 10분의 1의 확률로 이스터에그가 나와요! \n\n~로코코 몸통박치기\n방금 말씀하신 분에게 돌진해요! 1~9999사이의 데미지를 입어요\n\n~로코코 돌진 <@785114630435717726> (예시에요!)\n멘션하신 분한테 달려가서 돌진해요!\n\n~로코코 돌진 데미지 <@784645846752478852> 12345\n멘션하신 분한테 달려가서 돌진해요!\n다른 명령어와는 다르게 직접 데미지를 정하실수 있어요!\n명령어 특성상 멘션을 하고(@이름) 자동으로 띄어쓰기가 되니\n바로 데미지를 입력하시면 된답니다!\n(또 띄어쓰기를 하시면 제가 인식할수 없어요)"
    if char_message == '~help' or char_message == '~도움말' or char_message == '~명령어':
        embed = discord.Embed(title="명령어", description="로코코에게 도움말을 요청하려면'~help, ~도움말, ~명령어' 라고 말해주세요!", color=0x62c1cc)
        embed.set_footer(text=texttext)
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

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
