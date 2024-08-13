import math
import random
from read_data import read_seqs

class MyModel:

    t_per = 0.5 # percentage of dataset devoted to training
    train_data = None
    test_data = None
    answers = None

    # the following function is a template for the final selection algorithm -> its arguments and return variables
    # TODO: for some reason this doesn't take self as an argument??? Don't know why.
    def _select_random_G(sequence):
        '''
        Takes a sequence with a missing symbol, returns complete sequence.
        Could change this to return only selected symbol, but that would require some extra code.
        '''
        # taken from our previous exploration of this dataset
        existing_g_symbols = ['G.29.52', 'G.29.30.52', 'G.H.29.52', 'G.29', 'G.27.30', 'G.27', 'G.29.51', 'G.27.30.52', 'G.29.23.52']

        for index, elem in enumerate(sequence):
            if elem == "G": sequence[index] = random.choice(existing_g_symbols)
        
        return sequence


    @staticmethod
    def _strip_non_G(dataset: dict):
        new_data = {}

        for key in dataset:
            seq = dataset.get(key)
            if "G" in seq: new_data[key] = seq

        return new_data
    
    
    def train_model(self):
        pass

    def test_model(self, selection_func=_select_random_G):
        correct_guess = 0

        for elem in self.test_data:
            my_guess = selection_func(self.test_data[elem])
            if my_guess == self.answers[elem]: correct_guess += 1

        accuracy = correct_guess / len(self.test_data)
        print(f"Accuracy: {accuracy*100:.2f}%")


    def __init__(self, dataset, answers, delete_non_G = False) -> None:

        if delete_non_G: dataset = self._strip_non_G(dataset)

        self.test_data = dict(list(dataset.items())[int(len(dataset)*self.t_per):])
        self.train_data = dict(list(dataset.items())[:int(len(dataset)*self.t_per)])

        self.answers = answers

        self.test_model()

if __name__ == "__main__":
    
    # for task 1.3, our model should predict the missing number after a G symbol (ex. G. -> G.25)
    task1 = read_seqs("data/znaki-sekwencje-20160604-analiza3.csv")
    complete_seqs = read_seqs("data/znaki-sekwencje-20160604-original.csv")

    # task1_train, task1_test = dict(list(task1.items())[len(task1)//2:]), dict(list(task1.items())[:len(task1)//2])
    model = MyModel(task1, complete_seqs, delete_non_G=True)
    pass