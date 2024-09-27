from django.shortcuts import redirect

def student_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_student():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def admin_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_admin():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def mess_staff_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_mess_staff():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func
