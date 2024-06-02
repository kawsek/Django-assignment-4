from django.db import models
from category.models import CategoryModel
# Create your models here.
class TaskModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    categories = models.ManyToManyField(CategoryModel)
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
