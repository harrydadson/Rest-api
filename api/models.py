from django.db import models


# Create your models here.
class Bucketlist(models.Model):
    #this class represents the bucketlist models
    name = models.CharField(max_length=200, blank=False, unique=True)
    owner = models.ForeignKey('auth.User',#django's default user
    related_name='bucketlists',
    on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        #return readable representation of databases
        return'{}'.format(self.name)
