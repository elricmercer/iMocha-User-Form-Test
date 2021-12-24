from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from id_form_app.models import User_Information


def UserForm(request):
    return render(request, "form_template.html")


def SaveUserData(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        postcode = request.POST.get('postcode')
        state = ""
        if postcode == 35000 or postcode == "35000":
            state = "Perak"
        elif postcode == 50000 or postcode == "50000":
            state = "Wilayah Persekutuan"
        elif postcode == 80000 or postcode == "80000":
            state = "Johor"
        try:
            userDetails = User_Information(name=name, dob=dob, address=address, postcode=postcode, state=state)
            userDetails.save()
            return HttpResponse("success")
        except:
            return HttpResponse("failed")
