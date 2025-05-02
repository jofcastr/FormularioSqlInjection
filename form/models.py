from django.db import models

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'
        managed = False
            
    def __str__(self):
        return f"{self.first_name} {self.last_name}"