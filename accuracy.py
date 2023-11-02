import preprocessing

class Accuracy():
    def __init__(self):
        super().__init__()

    def measure_accuracy(self,best_solution):
        point_threshold = best_solution[0][6]
        p = preprocessing.Preprocessor()
        initial_array = p.read('dataset.csv')
        input_array = initial_array[100000:]
        num_columns = len(input_array[0])
        num_rows = len(input_array)
        count = 0
        for i in range(len(input_array)):
            point = 0
            for j in range(len(best_solution) - 1):
                if (input_array[i][j + 3] < best_solution[0][j]):
                    point = point + 1
            if (point >= point_threshold):
                if (input_array[i][num_columns - 1] == 'TRUE'):
                    count = count + 1
            else:
                if (input_array[i][num_columns - 1] == 'FALSE'):
                    count = count + 1
        accuracy = count / num_rows
        print("Accuracy: ")
        print(accuracy)