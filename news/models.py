from django.db import models

# Create your models here.


class TypeNotification(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Notification(models.Model):
    name = models.CharField(max_length=150)
    type = models.ForeignKey(TypeNotification, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    file_content = models.FileField(upload_to='files', null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name