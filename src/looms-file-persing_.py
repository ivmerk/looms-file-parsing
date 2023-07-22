import utils
import sys
import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

DILAY_MIN_MINUTE = 15




file = ''
stats = []
headTable = pd.DataFrame()

try:
    file = f'{sys.argv[1]}'
    statsTable = pd.read_excel(file, usecols="A,D",  skiprows=4)
    headTable = pd.read_excel(file, index_col=0, nrows=2, usecols="A,B")
    stats = pd.DataFrame.to_numpy(statsTable)

except:
    print('.xlsx file not found or wrong format')
    exit(1)

if not os.path.exists('./results'):
    os.mkdir('./results')

while stats[len(stats) - 1][1] != '0':
    stats = np.delete(stats, len(stats) - 1, 0)
timeOfReportBegining = stats[0][0]
timeOfReportFinishing = stats[len(stats) - 1][0]
totalPeriod = utils.getDelay(timeOfReportBegining, timeOfReportFinishing)

resultArr = np.array(['Время', 'Причина', 'Срок'], ndmin=2)
resultItem = []
totalDelay = timedelta()
pulseCount = utils.getPulseCount(DILAY_MIN_MINUTE, stats[0][0], stats[1][0])


while len(stats) != 1:
    if stats[0][1] == '0':
        stats = np.delete(stats, 0, 0)

    elif stats[0][1] == '1':
        rowCount = utils.isBreak(stats)
        if rowCount > pulseCount:
            resultItem = [stats[0][0], 'Остановка',
                          utils.getDelay(stats[0][0], stats[rowCount-1][0])]
            resultArr = np.append(resultArr, resultItem)
            totalDelay = utils.addDelay(
                totalDelay, stats[0][0], stats[rowCount-1][0])
            print(totalDelay)
        stats = np.delete(stats, slice(0, rowCount), 0)

    elif stats[0][1] == 'Ошибка  255':
        rowCount = utils.isBreak(stats)
        if rowCount > pulseCount:
            resultItem = [stats[0][0], 'Ошибка  255',
                          utils.getDelay(stats[0][0], stats[rowCount-1][0])]
            resultArr = np.append(resultArr, resultItem)
            totalDelay = utils.addDelay(
                totalDelay, stats[0][0], stats[rowCount-1][0])
            print(totalDelay)
        stats = np.delete(stats, slice(0, rowCount), 0)

resultArr = np.append(resultArr, ['Всего за период', '', totalPeriod])
resultArr = np.append(resultArr, ['Простой составил', '', str(totalDelay)])

resultArr = np.reshape(resultArr, (int(len(resultArr)/3), 3))

resultDf = pd.DataFrame(resultArr)
resultDf = headTable._append(resultDf)
# totalDelay = getTolalDelay()


resultFile = f'./results/result_{file}'
resultDf.to_excel(resultFile)
print(resultFile, resultDf)
