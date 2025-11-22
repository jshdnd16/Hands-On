from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentInformation, Education, Adress, Subject, FamilyBackground
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from .forms import StudentForm, EducationForm, AddressForm, FamilyForm
from django.contrib import messages


                # ====MODELS====
@login_required(login_url='login_user')
def education(request):
    education = Education.objects.all()
    return render(request, 'education.html', {'education':education})

@login_required(login_url='login_user')
def address(request):
    address = Adress.objects.all()
    return render(request, 'address.html', {'address':address})

@login_required(login_url='login_user')
def subject(request):
    subject = Subject.objects.all()
    return render(request, 'subject.html', {'subject':subject})

@login_required(login_url='login_user')
def family(request):
    family = FamilyBackground.objects.all()
    return render(request, 'family.html', {'family':family})


                # ====EDIT FUNCTION====
@login_required(login_url='login_user')
def edit_student(request, pk):
    student = get_object_or_404(StudentInformation, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student information updated.")
            return redirect('student_list')
        else:
            messages.error(request, "Failed to update student. Please fix the errors below.")
    else:
        form = StudentForm(instance=student)

    return render(request, 'edit_form.html', {'form': form})


@login_required(login_url='login_user')
def edit_education(request, pk):
    education = get_object_or_404(Education, pk=pk)

    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            messages.success(request, "Education details updated.")
            return redirect('education_list')
        else:
            messages.error(request, "Failed to update education. Please check the data.")
    else:
        form = EducationForm(instance=education)

    return render(request, 'edit_form.html', {'form': form})


@login_required(login_url='login_user')
def edit_address(request, pk):
    address = get_object_or_404(Adress, pk=pk)

    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            messages.success(request, "Address updated.")
            return redirect('address_list')
        else:
            messages.error(request, "Failed to update address. Check the data.")
    else:
        form = AddressForm(instance=address)

    return render(request, "edit_form.html", {"form": form})


@login_required(login_url='login_user')
def edit_family(request, pk):
    family = get_object_or_404(FamilyBackground, pk=pk)

    if request.method == 'POST':
        form = FamilyForm(request.POST, instance=family)
        if form.is_valid():
            form.save()
            messages.success(request, "Family background updated.")
            return redirect('family_list')
        else:
            messages.error(request, "Failed to update family background. Please fix the errors.")
    else:
        form = FamilyForm(instance=family)

    return render(request, 'edit_form.html', {'form': form})


                # ====ADD NEW STUDENT FUNCTION====
@login_required(login_url='login_user')
def add_student_step1(request, student_id=None):
    student = None

    if student_id:
        student = get_object_or_404(StudentInformation, id=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, "Student saved. Proceed to add address.")
            return redirect("add_student_step2", student.id)
        else:
            messages.error(request, "Failed to save student. Please fix the errors below.")
    else:
        form = StudentForm(instance=student)

    return render(request, "edit_form.html", {
        "form": form,
        "title": "Add Student",
        "student": student
    })


@login_required(login_url='login_user')
def add_student_step2(request, student_id):
    student = get_object_or_404(StudentInformation, id=student_id)
    address = Adress.objects.filter(student=student).first()

    if request.method == "POST":
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            address = form.save(commit=False)
            address.student = student
            address.save()
            messages.success(request, "Address saved. Proceed to add education.")
            return redirect("add_student_step3", student.id)
        else:
            messages.error(request, "Failed to save address. Please check the data.")
    else:
        form = AddressForm(instance=address)

    return render(request, "edit_form.html", {
        "form": form,
        "title": "Add Address",
        "student": student
    })


@login_required(login_url='login_user')
def add_student_step3(request, student_id):
    student = get_object_or_404(StudentInformation, id=student_id)
    education = Education.objects.filter(student=student).first()

    if request.method == "POST":
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            education = form.save(commit=False)
            education.student = student
            education.save()
            messages.success(request, "Education details saved. Proceed to add family background.")
            return redirect("add_student_step4", student.id)
        else:
            messages.error(request, "Failed to save education. Please check the data.")
    else:
        form = EducationForm(instance=education)

    return render(request, "edit_form.html", {
        "form": form,
        "title": "Add Education",
        "student": student
    })


@login_required(login_url='login_user')
def add_student_step4(request, student_id):
    student = get_object_or_404(StudentInformation, id=student_id)
    family = FamilyBackground.objects.filter(student=student).first()

    if request.method == "POST":
        form = FamilyForm(request.POST, instance=family)
        if form.is_valid():
            family = form.save(commit=False)
            family.student = student
            family.save()
            messages.success(request, "Family background saved. Student added successfully.")
            return redirect("student_list")
        else:
            messages.error(request, "Failed to save family background. Please check the data.")
    else:
        form = FamilyForm(instance=family)

    return render(request, "edit_form.html", {
        "form": form,
        "title": "Add Family Background",
        "student": student
    })


@login_required(login_url='login_user')
def delete_student(request, pk):
    student = get_object_or_404(StudentInformation, pk=pk)

    if request.method == 'POST':
        student.delete()   # CASCADE deletes all related records automatically
        messages.success(request, "Student record deleted.")
        return redirect('student_list')

    return render(request, 'confirm_delete.html', {'student': student})


                # ====LISTS FORM====
@login_required(login_url='login_user')
def student_list(request):
    students = StudentInformation.objects.all()
    return render(request, 'students.html', {'students': students})

@login_required(login_url='login_user')
def education_list(request):
    education = Education.objects.all()
    return render(request, 'education.html', {'education': education})

@login_required(login_url='login_user')
def address_list(request):
    address = Adress.objects.all()
    return render(request, 'address.html', {'address': address})

@login_required(login_url='login_user')
def family_list(request):
    family = FamilyBackground.objects.all()
    return render(request, 'family.html', {'family': family})


                # ====LOGIN/LOGOUT AND REGISTRATION FORM====
def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login_user')
        else:
            messages.error(request, "Registration failed. Please fix the errors.")
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form':form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully.")
                return redirect('dashboard')
        messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})


def logout_user(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login_user')

@login_required(login_url='login_user')
def dashboard(request):
    students = StudentInformation.objects.all()
    return render(request, 'students.html', {'students':students})

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully.")
            return redirect('student_list')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = StudentForm()
    return render(request, "add_student.html", {"form": form})