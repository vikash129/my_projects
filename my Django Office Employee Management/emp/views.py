from django.shortcuts import render , redirect , HttpResponse
from django.contrib.auth.models import User 
from django.views import View
from .models import *
import datetime
from django.db.models import Q 

class Index(View):
    def get(self , request):
        return render(request, 'emp/index.html')


class All_Emp(View):
    def get(self , request):
        return render(request, 'emp/view_all_emp.html' , {"employees"   : Employee.objects.all()})


class Add_Emp(View):
    def get(self , request):
        return render(request, 'emp/add_emp.html' , {'depts' : Department.objects.all() , 'roles' : Role.objects.all()})

    def post(self , request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])

        # print("-------------------------------", first_name , last_name , salary , bonus , phone , dept , role)

        Employee.objects.create( first_name= first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id = dept, role_id = role, hire_date = datetime.datetime.now())

        return redirect('all_emp')


class Remove_Emp(View):
    def get(self , request , emp_id = 0):
        if emp_id:
            Employee.objects.get(id =emp_id).delete()
            return redirect('all_emp')
        return render(request, 'emp/remove_emp.html' , {"emps" : Employee.objects.all()})


class Filter_Emp(View):
    def get(self , request):
        return render(request, 'emp/filter_emp.html')
    def post(self, request):
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']

        if not name:
            name = "#"
        if not dept:
            dept = "#"
        if not role:
            role = "#"


        empls = Employee.objects.filter( Q(first_name__icontains = name) | Q(last_name__icontains = name) | (Q(dept__name__icontains = dept)  | Q(role__name__icontains = role)) )
        return render(request, 'emp/view_all_emp.html' , {"employees"   : empls.all()})




