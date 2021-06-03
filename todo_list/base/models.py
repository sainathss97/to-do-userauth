from django.db import models
# importing inbuilt user models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank = True)
    #user = models.ForeignKey(User, on_delete=models.SET_NULL)
    title = models.CharField( max_length=5000)
    description = models.TextField(max_length = 5000,null=True,blank = True)
    complete =  models.BooleanField(default = False)
    create =  models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['complete']   
    