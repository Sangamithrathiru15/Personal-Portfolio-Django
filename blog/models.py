from django.db import models

# Create your models here.
class Blogs(models.Model):
    title=models.CharField(max_length=50)
    pub_date=models.DateTimeField()
    body=models.TextField(max_length=550)
    blogimage=models.ImageField(upload_to='blogimage/')

    def __str__(self):
        #to display the description in the admin page
        return self.title

    def bodytext(self):
        #to just display the part of blog description
        return self.body[:100]


    def pubdateformat(self):
        #to display the date in the format like Mar 6 2019
        return self.pub_date.strftime('%b %e %Y')
    