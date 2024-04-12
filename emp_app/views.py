from django.shortcuts import render, HttpResponse
from datetime import datetime
from . models import Employee,Department,Role
from django.db.models import Q 
# from . import templates

def home(request):
    return render(request,'index.html')


# Create your views here.

def all_emp(request):
    emps = Employee.objects.all()
    # print(emps)
    context={
        'emps':emps
    }

    # print(context)
    return render (request,'all_emp.html',context)


def add_emp(request):
    departments = Department.objects.all()
    
    context={
        'departments':departments
    }

    if (request.method =='POST'):
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        department =int(request.POST['department'])
        salary =int(request.POST['salary'])
        bonus =int(request.POST['bonus'])
        role =int(request.POST['role'])
        phone =int(request.POST['phone'])
        # hire_date =(request.POST['hire_date'])

        new_emp =Employee(first_name=first_name,last_name=last_name,dept_id=department,salary=salary,bonus=bonus,role_id=role,phone=phone,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee added successfully')
    elif (request.method=='GET'):
        return render (request,'add_emp.html',context)

def remove_emp(request,emp_id=0):

    if emp_id:
        try:
            employee_to_be_removed =Employee.objects.get(id=emp_id)
            employee_to_be_removed.delete()
            return  HttpResponse("Employee removed successfully")
        except:
            return HttpResponse("pls enter a valid employee id")
        
    emps =Employee.objects.all()
    context={
        'emps':emps
    }
    return render (request,'remove_emp.html',context)



def filter_emp(request):
    if(request.method=='POST'):
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        department=request.POST['department']
        role=request.POST['role']

        emps = Employee.objects.all()

        if first_name:
            emps = emps.filter(first_name__icontains =first_name)
        if last_name:
            emps = emps.filter(last_name__icontains =last_name)
        if department:
            emps = emps.filter(dept__name__icontains =department)
        if role:
            emps = emps.filter(role__name__icontains =role)

        context={
            'emps':emps
        }
        return render (request,'all_emp.html',context)


    return render (request,'filter_emp.html')

