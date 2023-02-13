from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Goal(models.Model):
    text = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): 
        self.text

class Person(models.Model): 
    gender = models.IntegerField()
    bmi = models.IntegerField()
    smoking = models.IntegerField()
    alcohol = models.IntegerField()
    stroke = models.IntegerField()
    phealth = models.IntegerField()
    mhealth = models.IntegerField()
    diffwalking = models.IntegerField()
    age = models.IntegerField()
    race = models.IntegerField()
    diabetes = models.IntegerField()
    pact = models.IntegerField()
    ghealth = models.IntegerField()
    sleep = models.IntegerField()
    asthma = models.IntegerField()
    kidney = models.IntegerField()
    skin = models.IntegerField()
    result = models.TextField(default='def')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1234)

    def getGender(self):
        if self.gender == 0:
            return "Male"
        return "Female"
    def getBmi(self):
        return self.bmi
    def getSmoking(self):
        return self.smoking==1
    def getAlcohol(self):
        return self.alcohol==1
    def getStroke(self):
        return self.stroke==1
    def getPhealth(self):
        return self.phealth
    def getMhealth(self):
        return self.mhealth
    def getDiffWalking(self):
        return self.diffwalking==1
    def getAge(self):
        age = self.age
        if age==0: return "18-24"
        elif age==1: return "25-29"
        elif age==2: return "30-34"
        elif age==3: return "35-39"
        elif age==4: return "40-44"
        elif age==5: return "45-49"
        elif age==6: return "50-54"
        elif age==7: return "55-59"
        elif age==8: return "60-64"
        elif age==9: return "65-69"
        elif age==10: return "70-74"
        elif age==11: return "75-79"
        else: return "80 or older"
    def getRace(self):
        race = self.race
        if race==0: return "White"
        elif race==1: return "Black"
        elif race==2: return "Hispanic"
        elif race==3: return "American Indian/Alaskan Native"
        elif race==4: return "Asian"
        else: return "Other"
    def getDiabetes(self):
        diabetes = self.diabetes
        if diabetes==3: return "Yes"
        elif diabetes==2: return "Yes (during pregnancy)"
        elif diabetes==1: return "No, borderline"
        else: return "No"
    def getPact(self):
        return self.pact==1
    def getGhealth(self):
        health = self.ghealth
        if health==0: return "Poor"
        elif health==1: return "Fair"
        elif health==2: return "Good"
        elif health==3: return "Very Good"
        else: return "Excellent"
    def getSleep(self):
        return self.sleep
    def getAsthma(self):
        return self.asthma==1
    def getKidney(self):
        return self.kidney==1
    def getSkin(self):
        return self.skin==1
    
    def getResult(self): 
        return self.result

    # def __str__(self):
    #     return self.result