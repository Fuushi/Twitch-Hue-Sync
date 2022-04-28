print('Twitch plays philips hue')
print()
print('installing addons')
import traceback
import phue
from phue import Bridge
import pygame
from datetime import datetime
import random
import socket
import keyboard
from playsound import playsound
import threading
import time

#
port = 6667


print('///socket initialization')

tip = '192.168.1.237'
server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'minejjchasetwitch'
token = 
channel = '#volx' #minejjchasetwitch



b = Bridge(tip)

b.connect()

b.get_api()




delay = 600

starting_brightness = 200

b.set_light(8, 'on', True)



def PONG():
    sock.send(bytes('PONG :tmi.twitch.tv\r\n', 'UTF-8'))
    print("PONG SENT!")
    threading.Timer(300, PONG).start()


def key_lock():
    lissst = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                  'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1', '2', '3', '4', '5', '6' ,'7', '8', '9', '-', '=', '`', 'space')
    for char in lissst:
        keyboard.block_key(char)
    time.sleep(4) #change value later so i dont get fucked
    for char in lissst:
        keyboard.unblock_key(char)

def Errlog(Err):
    print(Err)
    #Log to file


def Keycheckcont(key):
    if keyboard.is_pressed(key) == True:
        return(True)
    else:
        return(False)


def Keycheckpress(key):
    keyID = 'bool' + str(key)
    try:
        if keyboard.is_pressed(key) == True:
            #print('a', globals()[keyID])
            if globals()[keyID] == True:
                globals()[keyID] = False
                #print('Keypress')
                return(True)
        else:
            globals()[keyID] = True
            #print('return')
            return(False)
    except:
        print('err')
        globals()[keyID] = True
        
def testfor(keyword, dataset):
    detect = ()
    if keyword == str(dataset):
        return(True)
    for i in range(len(dataset) - len(keyword)):
        dataset = str(dataset)
        temp = dataset[i:(i + len(keyword))]
        #print(temp)
        if str(temp) == keyword:
            print('command detected')
            return(True)   
    return(False)

def testforvalue(keyword, dataset, maxvalue):
    dataset = str(dataset)
    detect = ()
    for i in range(len(dataset) - len(keyword)):
        temp = dataset[i:(i + len(keyword))]
        if str(temp) == keyword:
            value = int(dataset[i + len(keyword):(i + len(keyword) + len(str(maxvalue)))])
            if value > maxvalue:
                value = int(maxvalue)
            print('command detected')
            return(True, value)   
    return(False, 1)
def hueControl(value):
    b.set_light((8, 5, 1, 6), 'on', True)
    b.set_light((8, 5, 1, 6), 'bri', 255)
    b.set_light((8, 5, 1, 6), 'sat', 255)
    b.set_light((8, 5, 1, 6), 'hue', value)
def satControl(value):
    b.set_light((8, 5, 1, 6), 'on', True)
    b.set_light((8, 5, 1, 6), 'bri', 255)
    b.set_light((8, 5, 1, 6), 'sat', value)
def shitman(time):
    for i in range(time):
        print('')

print('///')

epstien_didnt_kill_himself = True
while epstien_didnt_kill_himself:
    print('tick')
    try:
        sock.close()
    except:
        pass
    sock = socket.socket()
    sock.connect((server, port))
    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))
    resp = sock.recv(2048).decode('utf-8')
    print(resp)
    print()
    
    try:
        tempt2 = True
        timerBlock = 0
        game = True
        tick = False
        will_collide = False
        Block_posX = 5
        Block_posY = 1
        for i in range(10):
            #print('tick')
            t1 = datetime.now()
            tempt1 = str(t1)[18:26]#Tick tracking #increase tick speed
            if tempt1[2] == '1':
                if tempt2 == True:
                    tick = True
                    #print('Tick')
                    tempt2 = False
            if tempt1[2] == '2':
                tempt2 = True

            if tempt1[2] == '5':
                if tempt2 == True:
                    tick = True
                    #print('Tick')
                    tempt2 = False
            if tempt1[2] == '6':
                tempt2 = True

         #################################Twitch web socket
            Postdata = False
            dataset = [' ']
            resp = sock.recv(2048).decode('utf-8')

            #data recieved
            if response == "PING :tmi.twitch.tv":
                print("ping found")
            elif response[0] == 'P':
                print("ping[0] found")
                PONG()
            
            try:
                for i in range(len(resp)):
                    if i >= 1:
                        if str(resp)[i] == ':':
                            Postdata = True
                    try:
                        if Postdata == True:
                            dataset = str(dataset) + str(str(resp)[i])        
                    except:
                        pass
                dataset = dataset[6:len(dataset)]
                print(dataset)
                if dataset == "tmi.twitch.tv":
                    print("empty detected")
                elif dataset == "":
                    print("empty detected")
                playsound('tick.mp3')
                if testfor('!stop', dataset):
                    print('keystop detected')
                    t1 = threading.Thread(target=key_lock, args=())
                    t1.start()
                    #stop it
                    
                if testfor('!on', dataset):
                    b.set_light((8, 5, 1, 6), 'on', True)
                if testfor('!off', dataset):
                    b.set_light((8, 5, 1, 6), 'on', False)
                if testforvalue('sat', dataset, 255)[0] == True:
                    b.set_light((8, 5, 1, 6), 'sat', testforvalue('sat', dataset, 255)[1])
                if testforvalue('br', dataset, 255)[0] == True:
                    b.set_light((8, 5, 1, 6), 'bri', testforvalue('br', dataset, 255)[1])
                if testfor('!yellow', dataset):
                    hueControl(11000)
                if (testfor("!red", dataset)) == True:
                    hueControl(100)
                if testfor('!blue', dataset) == True:
                    hueControl(46000)
                if testfor('!purple', dataset) == True:
                    hueControl(49000)
                if testfor('!pink', dataset) == True:
                    hueControl(55000)
                if testfor('!green', dataset) == True:
                    hueControl(25000)
                if testfor('!orange', dataset) == True:
                    hueControl(5000)
                if testfor('!white', dataset) == True:
                    satControl(0)
                if testfor('!press', dataset) == True:
                    print('detected', dataset)
                    keyboard.press(dataset[7])
                
                if testforvalue('hue', dataset, 65000)[0] == True:
                    hueControl(testforvalue('hue', dataset, 65000)[1])
                if testfor('!rainbow', dataset) == True:
                    for i in range(8):
                        hueControl((i * 5000) + 1)
                        shitman(300)
                if testfor('!strobe', dataset) == True:
                     print('command detected')
                     b.set_light((8, 5, 1, 6), 'on', True)
                     shitman(300)
                     b.set_light((8, 5, 1, 6), 'off', False)
                     shitman(300)
                     b.set_light((8, 5, 1, 6), 'on', True)
                     shitman(300)
                     b.set_light((8, 5, 1, 6), 'off', False)
                     shitman(300)
                     b.set_light((8, 5, 1, 6), 'on', True)
                     shitman(300)
                     b.set_light((8, 5, 1, 6), 'off', False)
                     shitman(300)
                     b.set_light((8, 5, 1, 6), 'on', True)
            except Exception as error:
                print(error)
                pass

            tick = False

            try:
                t2 = datetime.now()
                t1 = float(str(t1)[18:26])
                t2 = float(str(t2)[18:26])
                t3 = (t2) - (t1)
                if t3 < 0:
                    t3 = float(0.0018560000000000798)
                t4 = 0.016 - t3
                pygame.time.wait(int(t4 * 5000))
     
            except:
                print('time err')
                pass
    except Exception as error:
        print(errore)
        sock.close()
        
sock.close()
