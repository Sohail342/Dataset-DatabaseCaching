from django.db import models  

class Athlete(models.Model):     
    name = models.CharField(max_length=100)     
    age = models.IntegerField(null=True, blank=True)     
    country = models.CharField(max_length=100, null=True, blank=True)     
    year = models.IntegerField(null=True, blank=True)     
    closing_ceremony_date = models.DateField(null=True, blank=True)     
    sport = models.CharField(max_length=100, null=True, blank=True)     
    gold_medals = models.IntegerField(null=True, blank=True)    
    silver_medals = models.IntegerField(null=True, blank=True)    
    bronze_medals = models.IntegerField(null=True, blank=True)    
    total_medals = models.IntegerField(null=True, blank=True)     
    
    def __str__(self):         
        return self.name