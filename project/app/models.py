from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone_number=models.CharField(max_length=12)
    description=models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
class Blogs(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    authorname=models.CharField(max_length=54)
    img=models.ImageField(upload_to='pictures',blank=True,null=True)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__(self):
        return self.title
