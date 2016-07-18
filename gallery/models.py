from django.db import models

class Album(models.Model):

    title = models.CharField(max_length = 50)
    subtitle = models.CharField(max_length = 200)
    image = models.ImageField(upload_to ='images/photo-gallery')
    link = models.CharField(max_length = 200)

    published_date = models.DateTimeField(
            blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title