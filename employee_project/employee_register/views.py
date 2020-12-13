from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def employee_list(requiest):
    context = {'employee_list':Employee.objects.all()}
    return render(requiest,"employee_register/employee_list.html",context)

def employee_form(requiest,id = 0):


    if requiest.method =="GET":
        # New EMP
        if id == 0:
            form= EmployeeForm()
        # View Edit Employee
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(requiest,"employee_register/employee_form.html",{'form':form})
    # POST REQUIEST
    else:
        if id ==0:
            form = EmployeeForm(requiest.POST)
        # UPDATE REQUIEST
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(requiest.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


def employee_delete(requiest,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')