from django.core.validators import MinValueValidator
from django.db import models
from django.core.exceptions import ValidationError

# validators Member:
def valider_age(value):
    if value < 0 or value > 120:
        raise ValidationError("the age should be between 1 and 120.")

def validate_phone(value):
    if not value.isdigit():
        raise ValidationError("The phone number must contain only digits.")
    if len(value) != 8:
        raise ValidationError("The phone number must be exactly 8 digits long.")



class Member(models.Model):
    member_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(validators=[
        valider_age
    ])
    phone_number = models.CharField(max_length=8,
                                    validators=[validate_phone]
                                    )

    class Meta:
        db_table = 'club_member'

class Activity (models.Model):
    act_Code = models.IntegerField(primary_key=True)
    act_Name = models.CharField(max_length=255)
    monthly_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.0)]
    )
    capacity = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        db_table = 'club_activity'


class Inscription (models.Model):
    member_Id = models.ForeignKey(
        Member,
        on_delete=models.CASCADE
    )
    act_Code = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE
    )
    date_inscription = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'club_inscription'
        unique_together = ('member_Id', 'act_Code')


