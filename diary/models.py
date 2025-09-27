from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    """
    Модель для хранения записей в дневнике.
    Каждая запись привязана к автору, имеет заголовок, содержание и дату создания.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
