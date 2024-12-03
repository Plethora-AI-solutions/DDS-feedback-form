from django.db import models    
from datetime import datetime





class DDS_feedback(models.Model):

   question1 = models.IntegerField()
   question2 = models.IntegerField()
   question3 = models.IntegerField()
   question4 = models.IntegerField()
   question5 = models.IntegerField()
   question6 = models.IntegerField()
   question7 = models.IntegerField()
   question = models.CharField(max_length=240)











