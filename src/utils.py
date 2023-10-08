import numpy as np
from datetime import datetime, timedelta
import os
import constants


def getDelay(begin, end):

    try:
        # return (str(datetime.strptime(end, '%d/%m/%Y %H:%M:%S') - datetime.strptime(begin, '%d/%m/%Y %H:%M:%S')))
        return (datetime.strptime(end, '%d/%m/%Y %H:%M:%S') - datetime.strptime(begin, '%d/%m/%Y %H:%M:%S'))

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


def checkRisultDir():
    if not os.path.exists(constants.DIRECTORY_FOR_RESULTS):
        os.mkdir(constants.DIRECTORY_FOR_RESULT)


def cleanArray(stats):
    while stats[len(stats) - 1][1] != '0' and stats[len(stats) - 1][1] != 'Ошибка  255':
        stats = np.delete(stats, len(stats) - 1, 0)
    return stats


def getDelayFilteredArray(stats, coloumn=2, delaySecs=15*60):
    dt = timedelta(seconds=delaySecs)
    i = 1
    while i < len(stats):
        if (stats[i][coloumn] < dt):
            stats = np.delete(stats, i, 0)
        else:
            i += 1
    return stats


def getTotalDelay(stats, coloumn=2, delaySecs=15*60):
    dt = timedelta(seconds=delaySecs)
    totalDelay = timedelta(0)
    i = 1
    while i < len(stats):
        if (stats[i][coloumn] > dt):
            totalDelay += stats[i][coloumn]
        i += 1
    return totalDelay


def getDelayAmountByPeriods(stats, periods, coloumnTime=0, colomnDelay=2):
    summaryDelaysBySchedule = timedelta(0)
    for period in periods:
        i = 1
        while i < len(stats):
            stopingTime = datetime.strptime(
                stats[i][coloumnTime], '%d/%m/%Y %H:%M:%S').strftime('%H:%M')
            if (stopingTime > period[0] and stopingTime < period[1]):
                summaryDelaysBySchedule += stats[i][colomnDelay]
            i += 1
    return summaryDelaysBySchedule


def changeDelayFormateToString(stats, coloumn=2):
    i = 1
    while i < len(stats):
        stats[i][coloumn] = str(stats[i][coloumn])
        i += 1
    return stats


def convertRowFromTimedeltaToStr(stats, row):
    pass
