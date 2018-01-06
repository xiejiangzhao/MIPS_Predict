OnebitLastPredict = 0
Predict_Time = 0
Fetch_Time = 0


def UpdateOnebitPredict(Predict):
    global OnebitLastPredict
    Fetch = False
    if Predict == OnebitLastPredict:
        Fetch = True
    OnebitLastPredict = Predict
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
    global OnebitLastPredict
    OnebitLastPredict=0
