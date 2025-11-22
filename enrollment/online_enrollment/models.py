from django.db import models

# Create your models here.
class TestingDatabase(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}"

class StudentInformation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    student_id = models.IntegerField()
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        default=''
    )

    def __str__(self): # for showing names in the database
        return f"{self.last_name}, {self.first_name}"
    
    class Meta: # for making the data sorted alphabetically
        ordering = ["last_name"]

class Education(models.Model):
    student = models.ForeignKey(
        StudentInformation, 
        on_delete=models.CASCADE, 
        # related_name="educations",
        null=True,  # allow NULL in DB
        blank=True  # allow empty in forms
        )
    elementary = models.CharField(max_length=100)
    highschool = models.CharField(max_length=100)
    tertiary = models.CharField(max_length=100)
    achievements = models.CharField(max_length=100)
    year_graduated = models.IntegerField()
    
    def __str__(self): # for showing names in the database
        return f"{self.student}"
    
    class Meta:
        ordering = ['student']

class Adress(models.Model):
    student = models.ForeignKey(
        StudentInformation, 
        on_delete=models.CASCADE, 
        # related_name="educations",
        null=True,  # allow NULL in DB
        blank=True  # allow empty in forms
        )
    street = models.CharField(max_length=100)
    barangay = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    provice = models.CharField(max_length=100)
    zipcode = models.IntegerField()

    def __str__(self): # for showing names in the database
        return f"{self.student}"
    
    class Meta:
        ordering = ['student']
    
class Subject(models.Model):
    subject_code = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=100)
    time = models.CharField(max_length=20)
    room = models.CharField(max_length=10)
    units = models.IntegerField()

    def __str__(self): # for showing names in the database
        return f"{self.subject_code} - {self.subject_name}"
    
    class Meta:
        ordering = ['subject_code']

class FamilyBackground(models.Model):
    student = models.ForeignKey(
    StudentInformation, 
    on_delete=models.CASCADE, 
    # related_name="educations",
    null=True,  # allow NULL in DB
    blank=True  # allow empty in forms
    )
    mothers_name = models.CharField(max_length=100)
    # contact_no = models.IntegerField()
    mothers_contact = models.IntegerField(null=True)
    fathers_name = models.CharField(max_length=100)
    # contact_no = models.IntegerField()
    fathers_contact = models.IntegerField(null=True)
    guardian = models.CharField(max_length=100)

    def __str__(self): # for showing names in the database
        return f"{self.student}"
    
    class Meta:
        ordering = ['student']