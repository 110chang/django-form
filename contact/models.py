from django.db import models

class Contact(models.Model):
    name = models.CharField('名前', max_length=255)
    kana = models.CharField('かな', max_length=255)
    email = models.CharField('メールアドレス', max_length=255)

    def __str__(self):
        return self.name
