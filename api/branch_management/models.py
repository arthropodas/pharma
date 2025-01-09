from django.db import models
from user_management.models import UserData
# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=200)
    status = models.IntegerField(default=1)
    owner = models.ForeignKey(UserData, on_delete=models.CASCADE, related_name="branch_owner")
    pharmacist = models.ForeignKey(UserData, on_delete=models.CASCADE, null=True, blank=True, related_name="branch_staff")
    
    