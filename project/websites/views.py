from django.shortcuts import render, HttpResponseRedirect
from .models import Website
from .forms import WebsiteForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

#def my_form(request):
#  if request.method == "POST":
#    form = WebsiteForm(request.POST)
#    if form.is_valid():
#      form.save()
#      messages.info(request, 'Your Website has been Indexed successfully!')
#      return HttpResponseRedirect('/website')
#  else:
#      form = WebsiteForm()
#  return render(request, 'websites/add.html', {'form': form})


@login_required
@csrf_exempt
def my_form(request):
    if request.method=="POST":
        form = WebsiteForm(data=request.POST)
        if form.is_valid():
            websitepost = form.save(commit=False)
            websitepost.website_author = request.user
            websitepost.save()
            obj = form.instance
            alert = True
            messages.info(request, 'Your Website has been Indexed successfully!')
            return render(request, 'websites/add.html',{'obj':obj, 'alert':alert})
    else:
        form= WebsiteForm()
    return render(request, 'websites/add.html', {'form':form})