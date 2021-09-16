from django.db import models

# Create your models here.

class garment(models.Model):
    pk_id_garment = models.AutoField(primary_key=True, null=False, blank=False)
    mark = models.CharField(max_length=50, null=False, blank=False)
    client = models.CharField(max_length=50, null=False, blank=False)
    size = models.CharField(max_length=50, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    discount = models.DecimalField(null=False, blank=False, max_digits=3, decimal_places=2)
    amount = models.IntegerField(null=False, blank=False)
    image = models.URLField(blank=False, null=False, default='https://imagizer.imageshack.com/img922/3096/5x1MLe.jpg')

    class Meta:
        verbose_name = 'id_garment'
        verbose_name_plural = 'id_garment'
        ordering = ['mark']

    def __str__(self):
        return "{0}".format(self.mark)


class mark(models.Model):
    pk_id_mark = models.AutoField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'id_mark'
        verbose_name_plural = 'id_mark'
        ordering = ['name']

    def __str__(self):
        return "{0}".format(self.name)
