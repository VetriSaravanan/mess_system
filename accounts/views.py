from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, get_backends
from .forms import RegisterForm, CustomAuthenticationForm
from .decorators import student_required, admin_required, mess_staff_required
from .models import Student  # Import your Student model

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create the Student instance
            Student.objects.create(user=user)  # Create a Student for the new user
            
            # Explicitly assign the authentication backend
            backend = get_backends()[0]
            user.backend = f'{backend.__module__}.{backend.__class__.__name__}'

            login(request, user)  # Log the user in after registration

            # Redirect based on user role
            if user.is_student():
                return redirect('student_dashboard')
            elif user.is_admin():
                return redirect('admin_dashboard')
            else:
                return redirect('mess_dashboard')
        else:
            print(form.errors)
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})

# The rest of your views remain unchanged
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            backend = get_backends()[0]
            user.backend = f'{backend.__module__}.{backend.__class__.__name__}'
            login(request, user)

            # Redirect based on user role
            if user.is_student():
                return redirect('student_dashboard')
            elif user.is_admin():
                return redirect('admin_dashboard')
            else:
                return redirect('mess_dashboard')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@student_required
def student_dashboard(request):
    return render(request, 'students/student_dashboard.html')

@admin_required
def admin_dashboard(request):
    return render(request, 'admins/admin_dashboard.html')

@mess_staff_required
def mess_dashboard(request):
    return render(request, 'mess/mess_dashboard.html')

@student_required
def student_list(request):
    students = Student.objects.all()  # Fetch all students
    return render(request, 'accounts/student_list.html', {'students': students})

def no_permission(request):
    return render(request, 'accounts/no_permission.html')
