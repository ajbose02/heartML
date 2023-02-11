from django.http import HttpResponseRedirect, Http404
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from django.shortcuts import render, get_object_or_404
from .models import Person

from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'Home.html') 

@login_required
def survey(request): 
    return render(request, 'ind.html')


def about(request): 
    return render(request, 'About.html')

# #create another view function for prediction without data in args
# @login_required
# def prediction(request) {

# }

@login_required
def prediction(request, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q):
    new_input = [[a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q]]
    data_path = 'heart_2020_cleaned.csv'
    healthData = pd.read_csv(data_path) 
    #healthData.drop('HeartDisease')
    healthData['AgeCategory'] = healthData['AgeCategory'].replace({'18-24':0,'25-29':1,'30-34':2,'35-39':3,'40-44':4,'45-49':5,'50-54':6,'55-59':7,'60-64':8,'65-69':9,'70-74':10,'75-79':11,'80 or older':12})
    healthData['Race'] = healthData['Race'].replace({'White':0, 'Black':1, 'Hispanic':2,'American Indian/Alaskan Native':3,'Asian':4,'Other':5})
    healthData['Smoking'] = healthData['Smoking'].replace({'No':0, 'Yes':1})
    healthData['AlcoholDrinking'] = healthData['AlcoholDrinking'].replace({'No':0, 'Yes':1})
    healthData['Stroke'] = healthData['Stroke'].replace({'No':0, 'Yes':1})
    healthData['DiffWalking'] = healthData['DiffWalking'].replace({'No':0, 'Yes':1})
    healthData['Sex'] = healthData['Sex'].replace({'Male':0, 'Female':1})
    healthData['PhysicalActivity'] = healthData['PhysicalActivity'].replace({'No':0, 'Yes':1})
    healthData['GenHealth'] = healthData['GenHealth'].replace({'Poor':0, 'Fair':1, 'Good': 2, 'Very good': 3, 'Excellent': 4})
    healthData['Asthma'] = healthData['Asthma'].replace({'No':0, 'Yes':1})
    healthData['KidneyDisease'] = healthData['KidneyDisease'].replace({'No':0, 'Yes':1})
    healthData['SkinCancer'] = healthData['SkinCancer'].replace({'No':0, 'Yes':1})
    healthData['Diabetic'] = healthData['Diabetic'].replace({'No':0, 'No, borderline diabetes': 1, 'Yes (during pregnancy)':2, 'Yes':3})
    healthData['HeartDisease'] = healthData['HeartDisease'].replace({'No':0, 'Yes': 1})
    feature_cols = ['Sex','BMI','Smoking', 'AlcoholDrinking', 'Stroke','PhysicalHealth', 'MentalHealth', 'DiffWalking','AgeCategory', 'Race', 'Diabetic', 'PhysicalActivity', 'GenHealth', 'SleepTime', 'Asthma', 'KidneyDisease', 'SkinCancer']
    X = healthData.loc[:, feature_cols]
    y = healthData.HeartDisease
    model = LogisticRegression(max_iter=10000)
    # fit model
    X_train , X_test, y_train, y_test = train_test_split(X,y,test_size=0.9,random_state=0)
    model.fit(X_train, y_train)
    result = ""
    subtext = ""
    new_output = model.predict(new_input)
    person = Person(new_input)
    print(person.getArray())
    print(new_output)
    # summarize input and output
    if(new_output == 1):
        result = "You are at risk for heart disease."
        subtext = "Although you are currently at risk, you can still reduce your chances by improving your health."
    else:
        result = "You are NOT at risk for heart disease."
        subtext = "Although you are currently not at risk, you can still reduce your chances by improving your health"
    context = {
        'result': result,
        'subtext': subtext
    } 
    return render(request, 'index.html', context)
