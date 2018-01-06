Predict_Time = 0
Fetch_Time = 0


class BPT:
    Predict_all = [None] * 16

    def __init__(self):
        for i in range(16):
            self.Predict_all[i] = 1

    def get_predict(self, history):
        return self.Predict_all[history]

    def update(self, history, change):
        self.Predict_all[history] += change
        if (self.Predict_all[history] < 0):
            self.Predict_all[history] = 0
        elif (self.Predict_all[history] > 3):
            self.Predict_all[history] = 3
        return
    def clear(self):
        for i in range(16):
            self.Predict_all[i] = 1


class BHT:
    History = [None] * 32
    BPT_all = [None] * 32

    def __init__(self):
        for i in range(32):
            self.History[i] = 0
        for i in range(32):
            self.BPT_all[i] = BPT()

    def clear(self):
        for i in range(32):
            self.History[i] = 0
        for i in range(32):
            self.BPT_all[i].clear()


LocalBranch = BHT()


def UpdateLocalPredict(Predict, PC):
    global LocalBranch
    Fetch = False
    PC %= 32
    PC_history = LocalBranch.History[PC]
    pre = LocalBranch.BPT_all[PC].get_predict(PC_history)
    if (Predict == 0) & (pre < 2):
        Fetch = True
        LocalBranch.BPT_all[PC].update(PC_history, -1)
    if (Predict == 1) & (pre > 1):
        Fetch = True
        LocalBranch.BPT_all[PC].update(PC_history, 1)
    if (Predict == 0) & (pre > 1):
        LocalBranch.BPT_all[PC].update(PC_history, -1)
    if (Predict == 1) & (pre < 2):
        LocalBranch.BPT_all[PC].update(PC_history, 1)
    LocalBranch.History[PC] = (LocalBranch.History[PC] << 1) % 4
    LocalBranch.History[PC] += Predict
    return Fetch


def Fetch_Increase():
    global Fetch_Time
    Fetch_Time += 1


def Predict_Increase():
    global Predict_Time
    Predict_Time += 1


def get_acu():
    global Predict_Time, Fetch_Time
    return Fetch_Time / Predict_Time

def clear_data():
    global Predict_Time,Fetch_Time,LocalBranch
    Predict_Time = 0
    Fetch_Time = 0
    LocalBranch.clear()
