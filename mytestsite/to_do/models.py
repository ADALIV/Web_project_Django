from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class WhatToDo(models.Model):
    def __str__(self):
        return self.text
    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1) # 하루 내로 작성된지 확인
    text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('data published')

class do_type(models.Model):
    todo = models.ForeignKey(WhatToDo, on_delete=models.CASCADE)
    priority = models.IntegerField(choices=models.IntegerChoices('Priority', [('low', 1), ('medium', 2), ('high', 3)]).choices, default=2)
    progress = models.CharField(max_length=10, choices=models.TextChoices('Progress', ['Done', 'Doing', 'DO!']).choices, default='Doing')