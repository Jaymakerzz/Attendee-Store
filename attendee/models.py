import random
import string
from django.db import models

# Create your models here.


def generate_attendee_code():
    chars = string.ascii_uppercase + string.digits

    while True:
        code = "".join(random.choices(chars, k=8))
        if not Attendee.objects.filter(attendee_code=code).exists():
            return code


class Attendee (models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    attendee_code = models.CharField(max_length=8, editable=False,
                                     default=generate_attendee_code,
                                     unique=True
                                     )
    phone_number = models.CharField(max_length=13, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    organization = models.CharField(max_length=150, null=True, blank=True)
    role = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # class Meta:
    #     ordering = ['first_name']


class Attendee_photo(models.Model):
    attendee = models.OneToOneField(
        Attendee, on_delete=models.CASCADE, primary_key=True, related_name='photo')
    photo = models.ImageField(upload_to='attendee_photos/', null=True, blank=True)
    photo_uploaded_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['attendee']

    def __str__(self):
        return str(self.photo)


# class Attendee_poster(models.Model):
#     attendee = models.OneToOneField(
#         Attendee, on_delete=models.CASCADE, primary_key=True)
#     poster = models.FileField(upload_to='attendee_posters/')
#     poster_created_at = models.DateTimeField(auto_now=True)

#     def update_poster(self, new_poster):
#         if self.poster:
#             self.poster.delete(save=False)
#         self.poster = new_poster
#         self.save()
