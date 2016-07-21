import sys
import ac
import acsys 

l_lapcount=0
lapcount=0
total = 0

def acMain(ac_version):
    global l_lapcount

    appWindow = ac.newApp("ACLapCounter")
    ac.setSize(appWindow, 200, 200)
    #ac.setTitle(appWindow, "LAP COUNTER")
    l_lapcount = ac.addLabel(appWindow, "Laps: 0");
    ac.setPosition(l_lapcount, 10, 30)

    bReset = ac.addButton(appWindow, "Reset")
    ac.setBackgroundOpacity(bReset, 100)
    ac.setFontSize(bReset, 14)
    ac.drawBorder(bReset, 1)
    ac.setSize(bReset, 60, 20)
    ac.setPosition(bReset, 85, 50)
    ac.addOnClickedListener(bReset, ResetLapsCount)
    ac.console("ACLapCounter::reset button setted")
    return "ACLapCounter"

def acUpdate(deltaT):
    global l_lapcount, lapcount, total
    laps = ac.getCarState(0, acsys.CS.LapCount)
    ac.console("ACLapCounter:: laps:{}  lapcount:{}".format(laps, lapcount))
    if laps > lapcount:
        lapcount = laps
        total = total + 1
        ac.setText(l_lapcount, "Laps: {}".format(total))

def ResetLapsCount(name, event):
    global total, l_lapcount
    total = 0
    ac.setText(l_lapcount, "Laps: {}".format(total))