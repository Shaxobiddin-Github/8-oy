from django.db import models

# Create your models here.

class Klass(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Mexmonxona(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    yulduzlar = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Travel(models.Model):
    name = models.CharField(max_length=100)
    destination = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    klass = models.ForeignKey(Klass, blank=True, null=True, on_delete=models.CASCADE)
    mexmonxona = models.ForeignKey(Mexmonxona, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name