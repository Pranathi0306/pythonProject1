from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.views import View

from .models import MenuItem,Category, OrderModel

# Create your views here.

class Order(View):
    def get(self, request, *args, **kwargs):
        Starters = MenuItem.objects.filter(category__name__contains='Starters')
        MainCourse = MenuItem.objects.filter(category__name__contains='MainCourse')
        Desserts = MenuItem.objects.filter(category__name__contains='Dessert')
        Beverages = MenuItem.objects.filter(category__name__contains='Beverages')

        context = {
            'Starters': Starters,
            'MainCourse': MainCourse,
            'Desserts': Desserts,
            'Beverages': Beverages,
        }

        return render(request, 'Customer/order.html', context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }

            order_items['items'].append(item_data)

            price = 0
            item_ids = []

        for item in order_items['items']:
            price += float(item['price'])
            item_ids.append(item['id'])

        order = OrderModel.objects.create(
            price=price,
            name=name,
            email=email,
            phone=phone,
        )
        order.items.add(*item_ids)

        context = {
            'items': order_items['items'],
            'price': price
        }

        return render(request, 'customer/order_confirmation.html', context)

def homepage(request):
    return render(request,'Customer/homepage.html')
def MainPage(request):
    return render(request,'Customer/MainPage.html')
def SignUpLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        print(pass2)
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'Customer/SignUp.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'Customer/SignUp.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'Customer/homepage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'Customer/SignUp.html')
    else:
        return render(request, 'Customer/SignUp.html')
def SignUpCall(request):
    return render(request, 'Customer/SignUp.html')

def SignInCall(request):
    return render(request, 'Customer/SignIn.html')

def SignInLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                messages.success(request, 'Login successful for Customer!')
                return redirect('customer:MainPage')

            elif len(username) == 4:
                messages.success(request, 'Login successful for Staff!')
                return redirect('delivery:Staff')

            else:
                messages.error(request, 'Login Failed!')
                return render(request, 'Customer/SignIn.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'Customer/SignIn.html')
    else:
        return render(request, 'Customer/SignIn.html')
def SignOut(request):
    auth.logout(request)
    return redirect('customer:HomePage')

def choosing(request):
    return render(request,'Customer/choosing.html')

def home123(request):
    return render(request,'Customer/home123.html')

def Cash(request):
    return render(request,'Customer/Cash.html')

def Online(request):
    return render(request,'Customer/Online.html')