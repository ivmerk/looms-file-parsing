import numpy as np
from datetime import datetime, timedelta

def getDelay(begin, end):

    try:
        return (str(datetime.strptime(end, '%d/%m/%Y %H:%M:%S') - datetime.strptime(begin, '%d/%m/%Y %H:%M:%S')))

    except:
        print(begin, end)


def isBreak(stats) -> int:

    try:
        count = 1
        while (True):
            if stats[0][1] == stats[1][1]:
                count += 1
                stats = np.delete(stats, 0, 0)
            else:
                return count

    except:
        print('Неправильный формат ячеек', stats[0][0])


def getPulseCount(minimalDelay, beginOfPulse, endOfPulse):
    delay = str(datetime.strptime(endOfPulse, '%d/%m/%Y %H:%M:%S') -
                datetime.strptime(beginOfPulse, '%d/%m/%Y %H:%M:%S'))
    return (minimalDelay * 60) / datetime.strptime(delay, '%H:%M:%S').second


def addDelay(totalDelay, beginOfDelay, endOfDelay):
    return totalDelay + (datetime.strptime(endOfDelay, '%d/%m/%Y %H:%M:%S') - datetime.strptime(beginOfDelay, '%d/%m/%Y %H:%M:%S'))
