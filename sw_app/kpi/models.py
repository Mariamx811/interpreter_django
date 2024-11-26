from django.db import models

# Create your models here.
class Kpi(models.Model):
    name = models.CharField(max_length=50,unique=True)
    expression = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.expression
    
class KpiAssetLink(models.Model):
    asset_id = models.IntegerField()
    kpi_id = models.ForeignKey(Kpi,on_delete=models.CASCADE)
    result = models.CharField(max_length=100)

    class Meta:
        unique_together = ('asset_id', 'kpi_id') 

    def __str__(self):
        return str(self.asset_id) + " : " + str(self.kpi_id)