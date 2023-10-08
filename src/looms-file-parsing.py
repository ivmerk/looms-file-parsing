import utils
import sys
import os
import pandas as pd
import numpy as np
import getAllStopping as gas
from datetime import datetime, timedelta
import constants
from inputData import InputData

file = ''
stats = []
headTable = pd.DataFrame()

try:
    file = f'{sys.argv[1]}'
    statsTable = pd.read_excel(file, usecols="A,D",  skiprows=4)
    headTable = pd.read_excel(file, index_col=0, nrows=2, usecols="A,B")
    stats = pd.DataFrame.to_numpy(statsTable)

except:
    print('.xlsx file not found or wrong format. Пожалуйста разместите правильный файл в директории inbox')
    exit(1)

input = InputData(file)

utils.checkRisultDir()

stats = utils.cleanArray(stats)

timeOfReportBegining = stats[0][0]
timeOfReportFinishing = stats[len(stats) - 1][0]
totalPeriod = utils.getDelay(timeOfReportBegining, timeOfReportFinishing)

resultItem = []

resultArr = gas.getAllStopping(stats)

resultArr = np.reshape(resultArr, (int(len(resultArr)/3), 3))

totalDelay = utils.getTotalDelay(resultArr, 2, 0)

totalDelay15minutes = utils.getTotalDelay(resultArr, 2)

resultArr = utils.getDelayFilteredArray(resultArr)

variable = utils.getDelayAmountByPeriods(
    resultArr, constants.CHECKING_PERIODS_BY_DEFAULT)

resultArr = utils.changeDelayFormateToString(resultArr)

resultArr = np.append(resultArr, ['Всего за период', '', str(totalPeriod)])
resultArr = np.append(
    resultArr, ['Всего простой', '', '{tDelay}%'.format(tDelay=str(int(totalDelay/totalPeriod*10000)/100))])
resultArr = np.append(
    resultArr, ['Всего простой больше заданного (15 минут по умолчанию) ', '', '{tDelay}%'.format(tDelay=str(int(totalDelay15minutes/totalPeriod*10000)/100))])

resultArr = np.reshape(resultArr, (int(len(resultArr)/3), 3))

resultDf = pd.DataFrame(resultArr)
resultDf = headTable._append(resultDf)

print(resultArr)
print(totalDelay/totalPeriod*100)
resultFile = f'./results/result_{file.replace(constants.DIRECTORY_FOR_INCOME, "")}'
resultDf.to_excel(resultFile)
