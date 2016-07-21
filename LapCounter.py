import sys
import ac
import acsys
import math
import serial
import syslog
import time

if platform.architecture()[0] == "64bit":
    sysdir=os.path.dirname(__file__)+'/stdlib64'
else:
    sysdir=os.path.dirname(__file__)+'/stdlib'
sys.path.insert(0, sysdir)
os.environ['PATH'] = os.environ['PATH'] + ";."

import ctypes

# variables globales
appWindow = 0
sharedMemoryLoaded = False
lapCount = 0
labelLapCount = 0
bReset = 0
appName = "LapCounter"


# Metodo principal
def acMain(ac_version):
	global appWindow, appName, labelLapCount, lapCount

	arduino.flush()

	# creo la app
	appWindow = ac.newApp(appName)

	lapCount = 0

	# establezco la configuración de la app
	ac.setSize(appWindow, 200, 200)
	ac.drawBorder(appWindow, 0)
	ac.setBackgroundOpacity(appWindow, 0)

	labelLapCount = ac.addLabel(appWindow, "Laps: 0")
	ac.setPosition(label_lapCount, 3, 30)

	bReset = ac.addButton(appWindow,"Reset")
    ac.setBackgroundOpacity(bReset, 0)
    ac.drawBorder(bReset, 0)
    ac.setSize(bReset, 30 * UiSize, 30 * UiSize)
    ac.setPosition(bReset, 85 * UiSize, 136 * UiSize)
    #ac.setBackgroundTexture(bReset,"content/gui/pitstop/repair_engine_OFF.png")
    ac.addOnClickedListener(bReset, ResetLapsCount)

	return appName

def acUpdate(deltaT):
	global labelLapCount, lapCount

	# ac.getCarState(0, acsys.CS.CurrentTyresCoreTemp)

	laps = ac.getCarState(0, acsys.CS.LapCount)

	if laps > lapCount:
		lapCount++
		ac.setText(label_lapCount, "Laps: {}".format(lapCount))

def acShutDown():
	texto = "no hago nada"

def ResetLapsCount(name, state):
	global lapCount

	lapCount = 0
	ac.setText(label_lapCount, "Laps: {}".format(lapCount))
