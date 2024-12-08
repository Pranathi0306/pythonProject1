from django.shortcuts import render

# Create your views here.
def restauranthomepage(request):
    return render(request,'Restaurant/restauranthomepage.html')

def rrdarbar(request):
    return render(request,'Restaurant/rrdarbar.html')