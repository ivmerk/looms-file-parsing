import pandas as pd
import numpy as np


class InputData:
    def __init__(self, file):
        try:
            self.file = file
            print(file.count)
            self.statsTable = pd.read_excel(file, usecols="A,D",  skiprows=4)
            self.headTable = pd.read_excel(
                file, index_col=0, nrows=2, usecols="A,B")
            self.stats = pd.DataFrame.to_numpy(self.statsTable)

        except:
            print(
                '.xlsx file not found or wrong format. Пожалуйста разместите правильный файл в директории inbox')
            exit(1)
