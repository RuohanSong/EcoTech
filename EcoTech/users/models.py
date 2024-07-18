from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Member(AbstractUser):
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Member'


class SecurityQuestions(models.Model):
    QUESTION_CHOICES = [
        ('q1', 'What is your favorite color?'),
        ('q2', 'What is your mother\'s first name?'),
        ('q3', 'What was the name of your first pet?')
    ]
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    security_question_1 = models.TextField(choices=QUESTION_CHOICES, max_length=255, blank=False, null=False)
    security_answer_1 = models.TextField(max_length=255, blank=False, null=False)
    security_question_2 = models.TextField(choices=QUESTION_CHOICES, max_length=255, blank=False, null=False)
    security_answer_2 = models.TextField(max_length=255, blank=False, null=False)
    security_question_3 = models.TextField(choices=QUESTION_CHOICES, max_length=255, blank=False, null=False)
    security_answer_3 = models.TextField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.member.username

    def get_question_text(self, question_code):
        return dict(self.QUESTION_CHOICES).get(question_code, question_code)

