from django.shortcuts import render

# Create your views here.
def deliveryhomepage(request):
    return render(request,'Delivery/deliveryhomepage.html')

