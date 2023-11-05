import numpy as np

class Preprocessor():
    def __init__(self):
        super().__init__()
    def read(self,filename):
        dtypes = np.dtype([
            ('id', 'U25'),
            ('time', float),
            ('tp', float),  # U25 for Unicode string of up to 25 characters
            ('cl', float),
            ('ph', float),
            ('redox', float),
            ('leit', float),
            ('trueb', float),
            ('cl2', float),
            ('fm', float),
            ('fm2', float),
            ('event', 'U25')
            ]
        )
        array = np.genfromtxt(filename, delimiter=',', dtype=dtypes, names=True)
        #array = np.genfromtxt('dataset.csv', delimiter=',')
        #print(array[0]['tp'])
        #print(array)
        return array
    def min_array(self,filename):
        array = self.read('dataset.csv')
        data_array = np.array(array)
        #print(data_array)
        num_columns = len(data_array[0])
        num_rows = len(data_array)
        #print(num_rows)
        min_values = []

        for i in range(3,num_columns-3):
            column_values = []
            for j in range(num_rows):
                column_values.append(data_array[j][i])

            column_values = np.array(column_values, dtype=float)
            min_value = np.nanmin(column_values)
            min_values.append(min_value)
        min_values.append(0)
        min_values_array = np.array(min_values)
        #print(min_values_array)
        return min_values_array
    def max_array(self,filename):
        array = self.read('dataset.csv')
        data_array = np.array(array)
        #print(array.max(axis=0))
        num_columns = len(data_array[0])
        num_rows = len(data_array)
        max_values = []

        for i in range(3, num_columns - 3):
            column_values = []
            for j in range(num_rows):
                column_values.append(data_array[j][i])

            column_values = np.array(column_values, dtype=float)
            max_value = np.nanmax(column_values)
            max_values.append(max_value)
        max_values.append(6)
        max_values_array = np.array(max_values)
        #print(max_values_array)
        return max_values_array
