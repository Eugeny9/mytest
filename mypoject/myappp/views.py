from django.shortcuts import render

from myappp.models import product
# Create your views here.
def indx(request):
    return render(request,"html1.html")

def index(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        new = product(name =data["name"],height = data["height"], width = data["width"], cost = data["cost"])
        new.save()
    return render(request, "vhod.html")

def card(request):
    data = product.objects.all()     
    return render(request, "card.html", {"res":data})

def titul(request):
    return render(request,"titul.html")