from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import meettheteam





def demo(request):
    obj = place.objects.all()
    obj1 = meettheteam.objects.all()
    return render(request, "index.html", {'result': obj, 'res': obj1})

    # name = "india"
    # return render(request, "home.html", {'obj': name})
# def addition(request):
#     X=int(request.GET['num1'])
#     Y=int(request.GET['num2'])
#     res=X+Y
#     return render(request,"result.html",{'result':res})


# def demo(request):
#     return render(request, "home.html")

# def about(request):
#     return render(request,"about.html")
#
#
# def contact(request):
#     return render(request,"contact.html")
# def addition(request):
#     return render(request, "result.html")
