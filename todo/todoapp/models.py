from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{ self.text }'

    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = 'Todo'
        