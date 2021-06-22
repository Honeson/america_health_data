from django.shortcuts import render
import joblib
import pandas as pd


# Create your views here.
loaded_model = joblib.load('./models/logpredict.sav')

def index(request):
    context = {'a':1}
    return render(request, 'home.html', context)

def predict(request):
    if request.method == 'POST':
        factors = {}
        
        factors['Interest'] = request.POST.get('interest')
        factors['Credit'] = request.POST.get('credit')
        factors['Duration'] = request.POST.get('duration')
        factors['Income'] = request.POST.get('income')
        factors['Amount'] = request.POST.get('amount')
    df = pd.DataFrame({'x': factors}).transpose()
    prediction = loaded_model.predict(df)[0]
    prediction = bool(prediction)
    print("hhhfhhhhhhhhhhhhhhhhhhhhhh", prediction)
    message = ''
    if prediction:
        """I want all these below if there's a value for prediction, which is either 0 or 1"""
        if prediction==True:
            message = 'Congratulations!!! You can access loan now'
        else:
            message = 'You cannot access loan at this time'
        print("ggggggggggggggggggggggggggggg", prediction) #just what you asked
        print(type(prediction)) # to be sure it's an integer not bool
    context = {'prediction':prediction, 'message': message}
    return render(request, 'home.html', context)
