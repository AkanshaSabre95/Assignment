from django.db import models

class Note(models.Model):
    noteId = models.CharField(max_length=50,unique=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    