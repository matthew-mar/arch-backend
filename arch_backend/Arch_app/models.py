from django.db import models
DATE_INPUT_FORMATS = ["%d.%m.%Y"]
# Create your models here.

class Period(models.Model):
    name = models.TextField(max_length=30, null=False)



class Style(models.Model):
    name = models.TextField(max_length=50, null=False)

    time = models.TextField(null=False,default="")

    distinctive_features = models.TextField(null=False,default="")

    basic_decorative_elements = models.TextField(null=False,default="")

    was_built = models.TextField(null=False,default="")

    example_name = models.TextField(null=False, max_length=50,default="")

    parent_id = models.IntegerField(null=True)

    slug = models.TextField(null=False, max_length=50,default="")

    period_id = models.ForeignKey(to=Period, null=True, on_delete=models.SET_NULL)





class StylePhoto(models.Model):

    link_to_picture = models.URLField(null=True)

    style_id = models.ForeignKey(to=Style, on_delete=models.CASCADE)


