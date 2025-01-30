from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User


def hello(request):
    return HttpResponse("Hello, world!")


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email, password=password)
            return render(request, 'Loginify/success.html', {'username': user.username})
        except User.DoesNotExist:
            return render(request, 'Loginify/login.html', {'error': 'Invalid credentials!'})
    return render(request, 'Loginify/login.html')


@csrf_exempt
def user_create(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'Loginify/signup.html', {'error': 'Email already exists!'})

        user = User(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    return render(request, 'Loginify/signup.html')


def get_all_users(request):
    users = User.objects.all()
    user_data = [{"username": user.username, "email": user.email}
                 for user in users]
    return JsonResponse({"users": user_data})


def get_by_email(request, email):
    user = get_object_or_404(User, email=email)
    return JsonResponse({"user": {"username": user.username, "email": user.email}})


@csrf_exempt
def update_by_email(request, email):
    if request.method == 'POST':
        user = get_object_or_404(User, email=email)
        new_email = request.POST.get('email')
        new_pwd = request.POST.get('password')
        if new_email:
            user.email = new_email
        if new_pwd:
            user.password = new_pwd

        user.save()
        return JsonResponse({"message": "User updated successfully", "user": {"Email": user.email, "Password": user.password}})
    return JsonResponse({"message": "Invalid method"}, status=400)

@csrf_exempt
def del_by_email(request, email):
    if request.method == 'DELETE':
        user = get_object_or_404(User, email=email)
        user.delete()
        return JsonResponse({"message": f"User with email {email} deleted successfully"})
    return JsonResponse({"message": "Invalid method"}, status=400)
