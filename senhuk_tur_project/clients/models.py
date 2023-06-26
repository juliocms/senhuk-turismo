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
    name = models.TextField(max_length=100)
    mobile = models.IntegerField()
    email = models.TextField(max_length=100, null=False, default='DEFAULT VALUE')
    social_number = models.IntegerField()
    address = models.TextField(max_length=255)
    contact_1 = models.TextField(max_length=100)
    contact_1_mobile = models.IntegerField()
    contact_2 = models.TextField(max_length=100)
    contact_2_mobile = models.IntegerField()
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_FORM,
        default=NAO_INFORMAR,
    )
    # gender =  models.TextField(max_length=20)
    
    def __str__(self):
        return self.name
    