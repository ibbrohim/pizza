from django.db import models

# Create your models here.

class MainScrollModel(models.Model):
    image = models.ImageField(upload_to='main-scroll')
    title = models.CharField(max_length=50)
    info = models.CharField(max_length=250)
    discount = models.PositiveSmallIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.title
    class META:
        verbose_name =  'scroll'
        verbose_name_plural = 'scrolls'