from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

#str fonk. ekliyelim çünkü admin alanındaki
#isim olarak görünmesi için:
    def __str__(self):
        return self.name

