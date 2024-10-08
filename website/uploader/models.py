from django.db import models

# Create your models here.

class videos(models.Model):
    title= models.CharField(max_length=255)
    v_file=models.FileField(upload_to='videos/') #stored in the videos/ directory within the media root.
    uploaded_at= models.DateTimeField(auto_now_add=True)
    processed_status= models.BooleanField(default=False)
    subtitles = models.JSONField(null=True,blank=True)

    def __str__(self):
     return self.title
    
#------------------------------------------------------------------------------
class Subtitle(models.Model):
   video= models.ForeignKey(videos,related_name='video_subtitles',on_delete=models.CASCADE)
   language= models.CharField(max_length=10)
   file= models.FileField(upload_to='subtitles/') #,default='subtitles/placeholder.srt')
   content = models.TextField()
   # timestamp = models.FloatField()
   start_time = models.FloatField(default=0.0)
   end_time = models.FloatField(default=0.0)

   def __str__(self):
      return f"{self.video.title} - {self.language} - {self.start_time} - {self.end_time}"

   # def __str__(self):
   #    return f"{self.video.title} - {self.language} - {self.timestamp}"


