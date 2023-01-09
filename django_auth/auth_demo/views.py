from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as authLogin, logout as authLogout, update_session_auth_hash
from django.contrib import messages
# Create your views here.


@login_required
def index(request):
    return render(request, 'auth_demo/index.html')


def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmPassword = request.POST.get("confirmPassword")

        if password != confirmPassword:
            messages.add_message(request, messages.ERROR,
                                 'Both Password should be same!')
            return redirect('register')

        create_user = User.objects.create_user(
            first_name=first_name, last_name=last_name, username=username, email=email, password=password)

        if create_user:
            user = authenticate(username=username, password=password)
            if user is not None:
                authLogin(request, user)
                messages.add_message(
                    request, messages.SUCCESS, 'Welcome' + first_name + ' ' + last_name)
                return redirect('index')

    return render(request, 'auth_demo/register.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            authLogin(request, user)
            messages.add_message(request, messages.SUCCESS,
                                 "Successfully Logged In.")
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Wrong Credentials')
            return redirect('login')

    return render(request, 'auth_demo/login.html')


@login_required
def logout(request):
    authLogout(request)
    return redirect('login')


@login_required
def change_password(request):
    if request.method == "POST":
        oldPassword = request.POST.get("oldPassword")
        password = request.POST.get("password")
        confirmPassword = request.POST.get("confirmPassword")

        if password != confirmPassword:
            messages.add_message(request, messages.ERROR,
                                 "Both Password should be Same")
            return redirect('change-password')
        else:
            password_match_found = request.user.check_password(oldPassword)
            if password_match_found:
                user = User.objects.get(username=request.user.username)
                user.set_password(password)
                user.save()
                update_session_auth_hash(request, user)
                messages.add_message(
                    request, messages.SUCCESS, "Password changed Successfully")
                return redirect("index")
            else:
                messages.add_message(
                    request, messages.ERROR, "Old Password didn't matched!")
                return redirect('change-password')

    return render(request, 'auth_demo/change-password.html')


# @login_required
# def change_password(request):
#     if request.method == "POST":
#         password = request.POST.get("password")
#         confirmPassword = request.POST.get("confirmPassword")
# # ********
#         if password == confirmPassword:
#             user = User.objects.get(username=request.user.username)
#             user.set_password(password)
#             user.save()
#             update_session_auth_hash(request, user)
#             return redirect("index")
# # ********
#     return render(request, 'auth_demo/change-password.html')


@login_required
def delete_account(request):
    if request.method == "POST":
        password = request.POST.get("password")

        password_match_found = request.user.check_password(password)
        if password_match_found:
            delete_success = User.objects.get(
                email=request.user.email).delete()
            if delete_success:
                messages.add_message(
                    request, messages.SUCCESS, "Your Account Deleted Successfully")
                return redirect('index')
            else:
                messages.add_message(
                    request, messages.ERROR, "Something went wrong")
                return redirect('delete-account')
        else:
            messages.add_message(request, messages.ERROR,
                                 "Your password didn't matched.")
            return redirect('delete-account')

    return render(request, 'auth_demo/delete-account.html')


# @login_required
# def delete_account(request):
#     User.objects.get(email=request.user.email).delete()
#     return redirect('index')
