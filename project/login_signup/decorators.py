from django.http import HttpResponse
from django.shortcuts import render, redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('landing')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page.')

        return wrapper_func

    return decorator


def user_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'patient':
            return redirect('home')

        if group == 'pharmacy':
            return redirect('pharmacy-home')      
            
        if group == 'doctor':
            return view_func(request, *args, **kwargs)

        else:
            return redirect('login')

    return wrapper_function


def patient_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'doctor':
            return redirect('doctor-home')

        if group == 'pharmacy':
            return redirect('pharmacy-home')      
            
        if group == 'patient':
            return view_func(request, *args, **kwargs)

    return wrapper_function


def pharmacy_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'patient':
            return redirect('home')

        if group == 'doctor':
            return redirect('doctor-home')      
            
        if group == 'pharmacy':
            return view_func(request, *args, **kwargs)

    return wrapper_function
