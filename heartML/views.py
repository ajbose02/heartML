from django.http import HttpResponseRedirect, Http404
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from django.shortcuts import render, get_object_or_404
from .models import Person, Goal

from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'Home.html') 

@login_required
def survey(request): 
    return render(request, 'ind.html')

@login_required
def goals(request):
    goals = Goal.objects.filter(owner=request.user)
    context = {'goals': goals}
    return render(request, 'goals.html', context)
    
@login_required
def pred(request): 
    # people = Person.objects.filter(owner=request.user)
    result = Person.objects.filter(owner=request.user)[:1].get().getResult()
    split = str(result).split("|")
    res = split[0]
    subtext = split[1]
    context = {'result': res, 'subtext': subtext}
    
    return render(request, 'index.html', context)
   
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
    if(new_output == 1):
        result = "You are at risk for heart disease."
        subtext = "Although you are currently at risk, you can still reduce your chances by improving your health."
    else:
        result = "You are NOT at risk for heart disease."
        subtext = "Although you are currently not at risk, you can still reduce your chances by improving your health"
    
    res = result + "|" + subtext

    person = Person(gender=a,bmi=b,smoking=c,alcohol=d,stroke=e,phealth=f,mhealth=g,diffwalking=h,age=i,race=j,diabetes=k,pact=l,ghealth=m,sleep=n,asthma=o,kidney=p,skin=q, result=res, owner=request.user)
    person.save()

    goals = []
    descriptions = []

    #generating goals
    if(b>30):
        goals.append("BMI")
        d1 = "Your current BMI is " + str(b) + ". Ideally, you should target a BMI under 30 kg/m^2. In order to improve your BMI, exercise regularly and maintain a healthy diet."
        descriptions.append(d1)
    if(c==1):
        goals.append("Smoking")
        d2 = "Your current smoking habits contribute to your risk of develping heart disease. If you are addicted, get help by considering counseling."
        descriptions.append(d2)
    if(d==1): 
        goals.append("Alcohol")
        d3 = "Your current alcohol use contributes to your risk of developing heart disease. If you are addicted, get help by considering counseling."
        descriptions.append(d3)
    if(l==0):
        goals.append("Physical Activity")
        d4 = "Your lack of physical activity puts you at risk for heart disease. Aim for at least 150 min/week of aerobic activity/ Consider biking, swimming, and brisk walking."
        descriptions.append(d4)
    if(n<7):
        goals.append("Sleep")
        d5 = "You currently sleep " + str(n) + " hours per day. Lack of sleep increases your risk of heart disease, so target 7 hours of sleep every day. Prioritize your sleep by changing your daily routine."
        descriptions.append(d5)
    
    for i in range(len(goals)):
        goal = Goal(text = goals[i], description = descriptions[i], owner=request.user)
        goal.save()
        print("goal got saved")

    context = {
        'result': result,
        'subtext': subtext
    } 
    return render(request, 'index.html', context)
