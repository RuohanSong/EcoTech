from django.contrib.auth.models import AbstractUser
from django.db import models


class Member(AbstractUser):
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Member'


class SecurityQuestions(models.Model):
    QUESTION_CHOICES = [
        ('q1', 'What year did you enter college?'),
        ('q2', 'What year was your father born?'),
        ('q3', 'What is your mother\'s first name?'),
        ('q4', 'What was the name of your first pet?'),
        ('q5', 'What is the manufacturer of your first car?'),
        ('q6', 'How many pets have you had'),
        ('q7', 'Which city were you born in?'),
        ('q8', 'In which city did your parents meet?'),
        ('q9', 'What is your oldest sibling\'s first name?'),
        ('q10', 'In which city did you meet your spouse?'),
        ('q11', 'Which country did you go for the first travel abroad?'),
        ('q12', 'Which city did you go the first time you flew on a plane?'),
        ('q13', 'What is the name of the street where you grew up?'),
        ('q14', 'In which city did you grow up?'),
        ('q15', 'Which city were you in on the first day of 2024?'),
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



class UserProfile(models.Model):
    user = models.OneToOneField(Member, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
