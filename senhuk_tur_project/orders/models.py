from django.db import models
from travels.models import Travel

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE, related_name="travel")
    id_sender = models.IntegerField(null=False)
    name = models.TextField(max_length=100, null=False)
    description = models.TextField(max_length=255, null=False)
    average_value = models.TextField(max_length=30, null=False)
    approximate_weight = models.TextField(max_length=10, null=False)
    approximate_size = models.TextField(max_length=10, null=False)
    recipient_data = models.TextField(max_length=10, null=False)
 
    def __str__(self):
        return f"{self.travel} | {self.name}"
