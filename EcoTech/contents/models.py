from django.db import models
from users.models import Member


# Create your models here.

class Article(models.Model):
    CATEGORY_CHOICES = [
        ('clean_energy', 'Clean Energy'),
        ('sustainable_innovation', 'Sustainable Innovation'),
        ('agriculture', 'Agriculture'),
        ('green_living', 'Green Living'),
        ('climate', 'Climate'),
        ('eco_design', 'Eco Design'),
        ('animals', 'Animals'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    uploaded_by = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    document = models.FileField(upload_to='documents/', blank=True, null=True)  # For documents
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title

    def get_category_label(self):
        return dict(self.CATEGORY_CHOICES).get(self.category)


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.article}'
