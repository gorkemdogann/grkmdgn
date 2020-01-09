from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=100,verbose_name="Başlık")
    subtitle = models.CharField(max_length=100,verbose_name="Alt Başlık")
    content = RichTextField(verbose_name="İçerik")
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name="Kullanıcı"
    )

    def __str__(self):
        return self.title

    date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")

    image = models.ImageField(upload_to="images/", null=True,verbose_name="Fotograf Ekle")

    class Meta:
        ordering = ['-date']

def __str__(self):
    return self.title

