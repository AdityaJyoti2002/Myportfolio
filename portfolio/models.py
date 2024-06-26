from django.db import models

# Create your models here.

# about model 
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"

    def __str__(self):
        return "About Me"

# service model 
class Service(models.Model):
    name = models.CharField(max_length= 100, verbose_name="Service name")
    description = models.TextField(verbose_name="About Service")
    link = models.TextField(verbose_name="link", null=True)

    def __str__(self):
        return self.name
    
# Recent work Models
class Recentwork(models.Model):
    title = models.CharField(max_length= 100, verbose_name="Work title")
    image = models.ImageField(upload_to="work")
    link = models.TextField(verbose_name="link", null=True)
    category = models.TextField(verbose_name="category", null=True)
    # description = models.TextField(verbose_name="about work")

    def __str__(self):
        return self.title
    
# client model
class Client(models.Model):
    name = models.CharField(max_length=100, null=True)
    pdf = models.FileField(upload_to="Clients", default="default.pdf")
    

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length= 100, verbose_name="Name")
    Email = models.CharField(max_length= 100, verbose_name="Email")
    subject = models.CharField(max_length= 100, verbose_name="Email")
    message = models.TextField(verbose_name="message", null=True)

    def __str__(self):
        return self.name