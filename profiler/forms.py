from django import forms
from .models import membersform, teamform,bloodform, accidentform


class rform(forms.ModelForm):
    class Meta:
        model = membersform
        fields = [
            "firstname",
            "lastname",
            "midname",
            "barangay",
            "birthdate",
            "age",
            "mobile",
            "team",
            "bloodtype",
            "civilstatus",
            "religion",
        ]


class tform(forms.ModelForm):
    class Meta:
        model = teamform
        fields = [
            "code",
            "name",

        ]


class bform(forms.ModelForm):
    class Meta:
        model = bloodform
        fields = [
            "code",
            "type",

        ]

class aform(forms.ModelForm):
    class Meta:
        model = accidentform
        fields = [
            "team_incharge",
            "name_of_victim",
            "address",
            "age",
            "place",
            "accident_type",
            "date",
            "time",

        ]
