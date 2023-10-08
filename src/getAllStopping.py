import utils
import numpy as np
import constants
from datetime import timedelta


def getAllStopping(stats):
    pulseCount = utils.getPulseCount(
        constants.DILAY_MIN_MINUTE, stats[0][0], stats[1][0])
    resultArr = np.array(['Время', 'Причина', 'Срок'], ndmin=2)
    totalDelay = timedelta()
    isStop = False
    isError = False

    print(constants.ControllerStatus.STOP.value,
          constants.ControllerStatus.MISTAKE.value)

    while len(stats) != 1:
        if stats[0][1] == constants.ControllerStatus.STOP.value:
            isStop = True
            stats = np.delete(stats, 0, 0)

        elif stats[0][1] != constants.ControllerStatus.STOP.value and stats[0][1] != constants.ControllerStatus.MISTAKE.value and stats[0][1] != '' and (isError or isStop):
            isError = False
            isStop = False
            resultItem = [stats[0][0], 'Остановка']
            while stats[0][1] != constants.ControllerStatus.STOP.value and stats[0][1] != constants.ControllerStatus.MISTAKE.value:
                stats = np.delete(stats, 0, 0)
            resultItem = np.append(
                resultItem, utils.getDelay(resultItem[0], stats[0][0]))
            resultArr = np.append(resultArr, resultItem)

        elif stats[0][1] == constants.ControllerStatus.MISTAKE.value:
            isError = True
            resultItem = [stats[0][0],
                          constants.ControllerStatus.MISTAKE.value]
            while stats[0][1] == constants.ControllerStatus.MISTAKE.value:
                stats = np.delete(stats, 0, 0)
            resultItem = np.append(
                resultItem, utils.getDelay(resultItem[0], stats[0][0]))
            resultArr = np.append(resultArr, resultItem)
        else:
            stats = np.delete(stats, 0, 0)

    return resultArr
