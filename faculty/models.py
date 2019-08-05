from django.db import models
from django.urls import reverse


class courses(models.Model):
    cname = models.CharField(max_length=50)
    ccode = models.IntegerField(default=0)
    cnos = models.IntegerField(default=0)

    def __str__(self):
        return self.cname + "(" + str(self.ccode) +")"

class studentdata(models.Model):
    centre= models.CharField(max_length=50)
    sid= models.CharField(max_length=50)
    sname= models.CharField(max_length=40)
    skarma= models.IntegerField(default=200)
    course=models.ForeignKey(courses, on_delete=models.CASCADE)
    activity_1 = models.IntegerField(default=25 , verbose_name='Attendance')
    activity_2 = models.IntegerField(default=25 , verbose_name='Classroom participation')
    activity_3 = models.IntegerField(default=25 , verbose_name='Punctuality/ time management')
    activity_4 = models.IntegerField(default=25 , verbose_name='Personal hygiene/ Grooming')
    activity_5 = models.IntegerField(default=25 , verbose_name='Bed making')
    activity_6 = models.IntegerField(default=25 , verbose_name='Participation in Swachha Bharat/ Swadhaan')
    activity_7 = models.IntegerField(default=25 , verbose_name='Respect to teachers and others')
    activity_8 = models.IntegerField(default=25 , verbose_name='Ethics and values')
    flag1 = 0
    flag2 = 0
    flag3 = 0


    def save(self, *args ,**kwargs):
        self.skarma =self.activity_1 + self.activity_2  + self.activity_3  + self.activity_4  + self.activity_5  + self.activity_6  + self.activity_7  + self.activity_8
        super(studentdata, self).save(*args ,**kwargs)


    def get_absolute_url(self):
        if self.flag1 ==1:
            self.flag1=0
            return reverse('faculty:edit-edit')
        elif self.flag3 ==1:
            self.flag3 = 0
            return reverse('faculty:student-update')
        else:
            pass

    def __str__(self):
        return "Centre: " +self.centre +" Student ID: " +self.sid +" Name: " + self.sname +" Course: " + str(self.course) +" Karma Points: " + str(self.skarma)




