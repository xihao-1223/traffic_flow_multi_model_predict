from copy import deepcopy

import pandas as pd


class Pipe:
    data = None

    def __init__(self):
        pass

    def pipe(self, func):
        new_instance = deepcopy(self)
        data = func(new_instance.data)
        if data is not None:
            new_instance.data = data
        return new_instance

    def __add__(self, right_value):
        self.data.concate(right_value.data)
        return self


class DataPipe(Pipe):
    def __init__(self, data):
        self.data = data


class SeriesDataPipe(Pipe):
    def __init__(self, data, *args, **kwargs):
        self.data = pd.Series(data, *args, **kwargs)
