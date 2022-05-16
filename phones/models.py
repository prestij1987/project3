from django.db import models


class Phone(models.Model):
        # TODO: Добавьте требуемые поля
        # id = models.IntegerField(Primary_key=True)
        name = models.TextField()
        price = models.IntegerField()
        image = models.TextField()
        release_date = models.DateField()
        lte_exists = models.BooleanField()
        slug = models.TextField()
