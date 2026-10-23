from time import time as getTime
from random import seed as randomSeed
from random import choice as randomChoice
from random import random
from random import randrange as randomRange
def genRoute(id : int, maxEndTime : int) -> str:
    startList = ["EntryLeft1","EntryLeft2","EntryLeft3","EntryRight1","EntryRight2","EntryRight3","EntryCentral1"]
    endList = ["ExitLeft1","ExitLeft2","ExitLeft3","ExitRight1","ExitRight2","ExitRight3","ExitCentral1"]
    start = randomChoice(startList)
    end = randomChoice(endList)
    while end[4:] == start[5:]: # Make sure it isn't making a U-Turn
        end = randomChoice(endList)
    endTime = randomRange(100, maxEndTime)
    rate = random()*0.7 # Define the rate with a maximum of 0.7
    red = randomRange(0,255)
    green = randomRange(0,255)
    blue = randomRange(0,255)
    routeString = f'    <flow id="f_{id}" begin="0.00" end="{endTime}" period="exp({rate})" color="{red},{green},{blue}" from="{start}" to="{end}"/>\n'
    return routeString

if __name__ == "__main__":
    currentTime = int(getTime())
    randomSeed(currentTime)
    with open(f"net{currentTime}.rou.xml","w") as netFile:
        xmlPrefix = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xmlFirstLine = '<routes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/routes_file.xsd">\n'
        xmlEndLine = '</routes>'
        netFile.write(xmlPrefix)
        netFile.write(xmlFirstLine)
        totalRoutes = randomRange(8,16)
        maxEndTime = 200
        for i in range(totalRoutes):
            netFile.write(genRoute(i,maxEndTime))
        netFile.write(xmlEndLine)