from django.db import models
from DjangoUeditor.models import UEditorField 
# from DjangoUeditor.widgets import UEditorWidget

# Create your models here.

class Blog(models.Model):

    title = models.CharField(default='作品标题', max_length=50)
    date  = models.DateField()
    image = models.ImageField(default='default.png', upload_to='images/')
    text  = UEditorField(verbose_name=u'作品正文',width=600, height=300, imagePath="courses/ueditor/",filePath="courses/ueditor/", default='')


    def __str__(self):
        return self.title


    def short_text(self):
    	return self.text[:60] + '...'