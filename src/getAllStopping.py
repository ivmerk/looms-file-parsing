import utils
import numpy as np
import constants
from datetime import timedelta


def getAllStopping(stats):
    pulseCount = utils.getPulseCount(
        constants.DILAY_MIN_MINUTE, stats[0][0], stats[1][0])
    resultArr = np.array(['Время', 'Причина', 'Срок'], ndmin=2)
    totalDelay = timedelta()

    while len(stats) != 1:
        if stats[0][1] == '0':
            stats = np.delete(stats, 0, 0)

        elif stats[0][1] == '1':
            resultItem = [stats[0][0], 'Остановка']
            while stats[0][1] == '1':
                stats = np.delete(stats, 0, 0)
            resultItem = np.append(
                resultItem, utils.getDelay(resultItem[0], stats[0][0]))
            resultArr = np.append(resultArr, resultItem)

        elif stats[0][1] == 'Ошибка  255':
            resultItem = [stats[0][0], 'Ошибка  255']
            while stats[0][1] == 'Ошибка  255':
                stats = np.delete(stats, 0, 0)
            resultItem = np.append(
                resultItem, utils.getDelay(resultItem[0], stats[0][0]))
            resultArr = np.append(resultArr, resultItem)
    return resultArr