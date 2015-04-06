#!/usr/bin/env python
import sched, time
import os
import subprocess
import random
from datetime import datetime

print "\n--------Animal Crossing Player--------"
print "All Songs are copyright Nintendo 2015."
print "\n"

path1 = os.getcwd() + "/songs/time"
path2 = os.getcwd() + "/songs/kk"

songlist = []
kklist = []

s = sched.scheduler(time.time, time.sleep)
n = 0

def checkSong():

    dirList1=os.listdir(path1)
    for timesong in dirList1:
        songlist.append(timesong)
    dirList2=os.listdir(path2)
    for kksong in dirList2:
        kklist.append(kksong)

def songTime(sc):

    if datetime.now().hour == 22 and datetime.today().weekday() == 5:
        y = random.randint(1,7)
        song = "songs/kk/" + kklist[y]
        songname = song[9:]
        songname = songname[:-4]
        print 'Now playing %s by K.K. Slider.' % songname
        play = subprocess.call(["afplay", song])

    else:
        global n
        x = datetime.now().hour
        song = "songs/time/" + songlist[x]
        if n == 0:
            print "It's currently %s o'clock." % x
        elif n == 1:
            print "It's currently %s o'clock. This song has played once." % x
        elif n == 2:
            print "It's currently %s o'clock. This song has played twice." % x
        else:
            print "It's currently %s o'clock. This song has played %s times." % (x, n)

        play = subprocess.call(["afplay", song])
        n += 1

    sc.enter(1, 1, songTime, (sc,))

checkSong()
s.enter(1, 1, songTime, (s,))
s.run()
