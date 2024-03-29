from django.db import models

# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class SyllabusUploader(models.Model):
    description = models.CharField(max_length=255, blank=True)
    syllabus = models.FileField(upload_to=user_directory_path)