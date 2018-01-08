OnebitLastPredict = [0]*32
Predict_Time = 0
Fetch_Time = 0


def UpdateOnebitPredict(Predict,PC):
    PC%=32
    global OnebitLastPredict
    Fetch = False
    if Predict == OnebitLastPredict[PC]:
        Fetch = True
    OnebitLastPredict[PC] = Predict
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
    OnebitLastPredict=[0]*32
