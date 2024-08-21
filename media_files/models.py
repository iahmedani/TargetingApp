from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UploadLogs(models.Model):
    form_id = models.CharField(max_length=100)
    form_name = models.CharField(max_length=100)
    file_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    
    def __str__(self):
        return self.form_name
    
    class Meta:
        verbose_name_plural = 'Upload Logs'
        verbose_name = 'Upload Log'
