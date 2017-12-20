from django.db import models
from django.core.urlresolvers import reverse



# Create your models here.



def upload_location(instance, filename):                              #code for image field
    return "%s/%s" % (instance.id, filename)                        #end




class bloodform(models.Model):
    code = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

    def get_absolute_url(self):                                              # code for link/redirect con.to views.py
        return reverse('profiler:team_details', kwargs={'pk': self.pk})

class teamform(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):                                              # code for link/redirect con.to views.py
        return reverse('profiler:team_details', kwargs={'pk': self.pk})

class membersform(models.Model):
    members_image = models.ImageField(upload_to=upload_location,                 # code for image field
                                      blank=True, null=True,                     #
                                      height_field="members_height_field",       #
                                      width_field="members_width_field")         #
    members_height_field = models.IntegerField(default=0)                        #
    members_width_field = models.IntegerField(default=0)                         # end for image field

    firstname = models.CharField (max_length=100)
    lastname = models.CharField (max_length=100)
    midname = models.CharField (max_length=100)
    barangay = models.CharField (max_length=100)
    birthdate = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    age = models.CharField(max_length=2)
    mobile = models.CharField(max_length=13)
    team = models.ForeignKey(teamform)
    bloodtype = models.ForeignKey(bloodform)
    civilstatus = models.CharField(max_length=20)
    religion = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname + self.lastname

    def get_absolute_url(self):                                              # code for link/redirect con.to views.py
        return reverse('profiler:mem_details', kwargs={'pk': self.pk})    # end




class accidentform(models.Model):
    team_incharge = models.ForeignKey(teamform)
    name_of_victim = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    age = models.CharField(max_length=2)
    place = models.CharField(max_length=100)
    accident_type = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    time = models.CharField(max_length=10, null=True, blank=True)

    victims_image = models.ImageField(upload_to=upload_location,            # code for image field
                                      blank=True, null=True,                #
                                      height_field="victims_height_field",  #
                                      width_field="victims_width_field")    #
    victims_height_field = models.IntegerField(default=0)                   #
    victims_width_field = models.IntegerField(default=0)                     # end for image field


    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name_of_victim

    def get_absolute_url(self):                                              # code for link/redirect con.to views.py
        return reverse('profiler:my_vform_update', kwargs={'pk': self.pk})    # end