class BPT:
    Predict_all = [None] * 16

    def __init__(self):
        for i in range(16):
            self.Predict_all[i] = 1

    def get_predict(self, history):
        return self.Predict_all[history]

    def update(self, history, change):
        self.Predict_all[history] += change
        if self.Predict_all[history] < 0:
            self.Predict_all[history] = 0
        elif self.Predict_all[history] > 3:
            self.Predict_all[history] = 3
        return


class BHT:
    History = [None] * 31
    BPT_all = [None] * 31

    def __init__(self):
        for i in range(31):
            self.History[i] = 0
        for i in range(31):
            self.BPT_all[i] = BPT()

    def clear(self):
        for i in range(31):
            self.History[i] = 0
        for i in range(31):
            self.BPT_all[i] = BPT()


test = BPT()
print(test.Predict_all[5])
