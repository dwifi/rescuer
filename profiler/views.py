from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .forms import rform, tform, bform, aform
# Create your views here.
from .models import  membersform, teamform, bloodform, accidentform


def home(request):                                           #code for home index
    return render (request,"index.html")                     #end




def uraccident_details (request, pk):                       # A1 , link code con. to urls.py / model.py
    instance =  get_object_or_404(accidentform, pk=pk)          # A1 , link code con. to urls.py / model.py
    form=aform(request.POST or None, instance= instance)          # A1 , link code con. to urls.py / model.py
    context= {
        'form': form,
        'instance': instance,

    }
    return render (request, "accident_details.html", context)



def uraccidentform(request):
    form = aform(request.POST or None, request.FILES or None)
    if form.is_valid():
       content = form.save(commit=False)
       content.save()

    context = {
        "varform": form ,
        "team_list": teamform.objects.all(),

    }
    return render(request, "accidentform.html", context)


def uraccidentlist(request):                      #code for table

    query_list = accidentform.objects.all()  #code for table
    context = {                           #code for table
        'query_list': query_list,            #code for table
        'count': query_list.count(),        #code for total con. list.html

    }
    return render(request, "accidentlist.html", context)     #code for table con. list.html


def uraccident_delete(request, pk):                                 #delete code/  import 'redirect'
    instance = get_object_or_404(accidentform, pk=pk)
    instance.delete()
    return redirect('profiler:accident_list')


def uraccident_update(request, pk):
    instance = get_object_or_404(accidentform, pk=pk)
    form = aform(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "instance": instance,
        "varform": form,
        "team_list": teamform.objects.all(),
        "flag": True,


    }
    return render(request, "accidentform.html", context)








def urbloodform(request):
    form = bform(request.POST or None)
    print(request.POST.get('type'))
    if form.is_valid():
       content = form.save(commit=False)
       content.save()

    context = {
        "varform": form

    }
    return render(request, "bloodform.html", context)


def urbloodlist(request):                      #code for table

    query_list = bloodform.objects.all()  #code for table
    context = {                           #code for table
        'tittle': 'STUDENT LIST',         #code for table
        'query_list': query_list,            #code for table
        'count': query_list.count(),        #code for total con. list.html
        "blood_list":bloodform.objects.all() ,
        "flag": True,
    }
    return render(request, "teamlist.html", context)     #code for table con. list.html



def urblood_details (request, pk):                       # A1 , link code con. to urls.py / model.py
    instance =  get_object_or_404(bloodform, pk=pk)          # A1 , link code con. to urls.py / model.py
    form=bform(request.POST or None, instance= instance)          # A1 , link code con. to urls.py / model.py
    context= {
        'form': form,
        'instance': instance,

    }
    return render (request,"blood_details.html", context)



def urteamform(request):
    form = tform(request.POST or None )
    print(request.POST.get('firstname'))
    if form.is_valid():
       content = form.save(commit=False)
       content.save()

    context = {
        "varform": form

    }
    return render(request, "teamform.html", context)


def urteam_list(request):                      #code for table

    query_list = teamform.objects.all()  #code for table
    context = {                           #code for table
        'tittle': 'STUDENT LIST',         #code for table
        'query_list': query_list,            #code for table
        'count': query_list.count(),        #code for total con. list.html
        "team_list":teamform.objects.all() ,
        "flag": True,
    }
    return render(request, "teamlist.html", context)     #code for table con. list.html


def urteam_details (request, pk):                       # A1 , link code con. to urls.py / model.py
    instance =  get_object_or_404(teamform, pk=pk)          # A1 , link code con. to urls.py / model.py
    form=tform(request.POST or None, instance= instance)          # A1 , link code con. to urls.py / model.py
    context= {
        'form': form,
        'instance': instance,

    }
    return render (request,"teamdetails.html", context)



def urteam_delete(request, pk):                                 #delete code/  import 'redirect'
    instance = get_object_or_404(teamform, pk=pk)
    instance.delete()
    return redirect('profiler:team_list')



def urteam_update(request, pk):
    instance = get_object_or_404(teamform, pk=pk)
    form = tform(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "instance": instance,
        "varform": form,



    }
    return render(request, "teamform.html", context)




def urmembersform(request):
    form = rform(request.POST or None, request.FILES or None)     #add 'request.FILES or None' for image code
    if form.is_valid():
       instance = form.save(commit=False)
       instance.save()

    context = {
        "varform": form,
        "team_list": teamform.objects.all(),
        "blood_list": bloodform.objects.all(),

    }
    return render(request, "membersform.html", context)


def urmemformlist(request):                      #code for table

    query_list = membersform.objects.all()  #code for table
    context = {                           #code for table
        'tittle': 'STUDENT LIST',         #code for table
        'query_list': query_list,            #code for table
        'count': query_list.count(),        #code for total con. list.html
    }
    return render(request, "members_list.html", context)     #code for table con. list.html


def urmem_gridlist(request):                      #code for table

    query_list = membersform.objects.all()  #code for table
    context = {                           #code for table
        'tittle': 'STUDENT LIST',         #code for table
        'query_list': query_list,            #code for table
        'count': query_list.count(),        #code for total con. list.html
    }
    return render(request, "members_gridlist.html", context)     #code for table con. list.html


def urmemdetails (request, pk):                       # A1 , link code con. to urls.py / model.py
    instance =  get_object_or_404(membersform, pk=pk)          # A1 , link code con. to urls.py / model.py
    form=rform(request.POST or None, instance= instance)          # A1 , link code con. to urls.py / model.py
    context= {
        'form': form,
        'instance': instance,               #add   'instance': instance, for calling delete

    }
    return render (request,"members_details.html", context)       # A1 , link code con. to urls.py



def urmemformdelete(request, pk):                                 #delete code/  import 'redirect'
    instance = get_object_or_404(membersform, pk=pk)
    instance.delete()
    return redirect('profiler:memform_list')



def urmemform_update(request, pk):
    instance = get_object_or_404(membersform, pk=pk)
    form = rform(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "instance": instance,
        "varform": form,
        "team_list": teamform.objects.all(),
        "blood_list": bloodform.objects.all(),
        "flag": True,


    }
    return render(request, "membersform.html", context)

