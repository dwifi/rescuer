from django.contrib import admin
from .models import membersform, teamform, bloodform, accidentform
# Register your models here.



class membersformAdmin(admin.ModelAdmin):
    class Meta:
        model = membersform

admin.site.register(membersform, membersformAdmin)


class teamformAdmin(admin.ModelAdmin):
    class Meta:
        model = teamform

admin.site.register(teamform, teamformAdmin)



class bloodformAdmin(admin.ModelAdmin):
    class Meta:
        model = bloodform

admin.site.register(bloodform, bloodformAdmin)



class accidentformAdmin(admin.ModelAdmin):
    class Meta:
        model = accidentform

admin.site.register(accidentform, accidentformAdmin)