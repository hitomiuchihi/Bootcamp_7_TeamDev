from django.db import models
from django.core.exceptions import ValidationError
import uuid


# Create your models here.
class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)

    def clean(self):
        if len(self.password) < 8:
            raise ValidationError('パスワードは8文字以上20文字以内で設定してください')
    
    def __str__(self):
        return f"user_id: {self.user_id}, name: {self.name}, email: {self.email}"

