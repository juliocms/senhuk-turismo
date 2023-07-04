from django.db import models

class Client(models.Model):
    
    MASCULINO = "M"
    FEMININO = "F"
    OUTRO = "O"
    NAO_INFORMAR = "N"
    
    GENDER_FORM = [
        (MASCULINO, "masculino"),
        (FEMININO, "Feminino"),
        (OUTRO, "Outro"),
        (NAO_INFORMAR, "nao_informar"),
    ]
    
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100, null=False)
    mobile = models.IntegerField(null=False)
    email = models.TextField(max_length=100, null=False)
    social_number = models.IntegerField(null=False)
    address = models.TextField(max_length=255, null=False)
    birth_date = models.DateField(null=True, blank=True)
    description = models.TextField(max_length=255, null=True)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_FORM,
        default=NAO_INFORMAR,
        null=False
    )
    
    def __str__(self):
        return self.email
    