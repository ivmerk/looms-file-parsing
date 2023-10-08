from enum import Enum

DILAY_MIN_MINUTE = 15
DIRECTORY_FOR_INCOME = './inbox/'
DIRECTORY_FOR_RESULTS = './results'
CHECKING_PERIODS_BY_DEFAULT = [('06:00', '08:00'), ('18:00', '20:00')]


class ControllerStatus(Enum):
    STOP = '0'
    MISTAKE = 'Ошибка  255'
