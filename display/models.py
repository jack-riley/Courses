from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Validator(models.Manager):
    def validator (self,postData) :
        errors = {}
        if postData['new'] == "new":
            if len (postData['name']) < 5:
                errors['title'] = "Title should be at least two (2) characters"
    
            if len (postData['desc']) < 15:
                errors['desc'] = "Description is should be at least ten (15) characters"

            name = (Course.objects.filter(name=postData['name']))
            if name:
                errors['same_name'] = "Name already in use. Name cannot be a duplicate"
        
        if postData['new'] == "comm":
            if len (postData['comm']) < 1:
                errors['comm'] = "Comment must have text."
        
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Validator()


class Description(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, primary_key=True)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Validator()

class Comment(models.Model):
    comm = models.TextField()
    course = models.ForeignKey(Course, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Validator()
