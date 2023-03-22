from django.shortcuts import render,redirect
from django.contrib.auth import login , authenticate, logout
from django.contrib import messages
import psycopg2
from .models import EmployeeData
# Create your views here.


def Employee_details(request):
    stu = EmployeeData.objects.all()
    if request.method == 'POST':
        startdate = request.POST['fromdate']
        enddate = request.POST['todate']  
        stu_1 = EmployeeData.objects.filter(Date__lte=enddate, Date__gte=startdate)
        print(stu_1)
        return render(request,'index.html', {'stu_1': stu_1})
    return render(request,'data.html',{'stu':stu})

def user_login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            # Success, now let's login the user.
            return redirect(Employee_details)
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'login.html')

    


