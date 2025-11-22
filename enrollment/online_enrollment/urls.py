from django.urls import path
from . import views

urlpatterns = [
    # ====MODELS====
    # path('student/', views.students),
    path('education/', views.education, name='education'),
    path('address/', views.address, name='address'),
    path('subject/', views.subject, name='subject'),
    path('family/', views.family, name='family'),
    # ====AUTHENTICATION====
    path('register/', views.register_user, name='register_user'),
    path('', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # ====EDIT====
    path('student/<int:pk>/edit/', views.edit_student, name='edit_student'),
    path('education/<int:pk>/edit/', views.edit_education, name='edit_education'),
    path('address/<int:pk>/edit/', views.edit_address, name='edit_address'),
    path('family/<int:pk>/edit/', views.edit_family, name='edit_family'),
    # ====STUDENT LIST====
    path('student-list/', views.student_list, name='student_list'),
    path('education-list/', views.education_list, name='education_list'),
    path('address-list/', views.address_list, name='address_list'),
    path('family-list/', views.family_list, name='family_list'),
    # STEP 1 (no ID = new student; with ID = go back to edit)
    path("add/student/", views.add_student_step1, name="add_student_step1"),
    path("add/student/<int:student_id>/", views.add_student_step1, name="add_student_step1_id"),
    path("add/address/<int:student_id>/", views.add_student_step2, name="add_student_step2"),
    path("add/education/<int:student_id>/", views.add_student_step3, name="add_student_step3"),
    path("add/family/<int:student_id>/", views.add_student_step4, name="add_student_step4"),
    path('student/delete/<int:pk>/', views.delete_student, name='delete_student'),
]