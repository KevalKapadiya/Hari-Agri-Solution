from django.shortcuts import render, redirect
from accounts.models import *
from django.contrib import messages


# Create your views here.
def login(request):
    return render(request, 'login.html')


def register(request):
    
    
    from django.shortcuts import render, redirect
from .models import AgriUser

def register(request):
    if request.method == 'POST':
        print("Jay")
        full_name = request.POST['full_name']
        email = request.POST['email']
        mobile_no = request.POST['mobile_no']
        password = request.POST['password']
        address = request.POST['address']
        status = request.POST['status']
        amount_of_land = request.POST['amount_of_land']  # Make sure this is a valid decimal

        try:
            # Convert to decimal
            if not amount_of_land :
                pass
            #   # Convert string to float
            user = AgriUser.objects.create(
                full_name=full_name,
                email=email,
                mobile_no=mobile_no,
                address=address,
                status=status
            )
            if amount_of_land :
                amount_of_land = float(amount_of_land)
                user.amount_of_land = amount_of_land
            user.set_password(password)  # Hash the password
            user.save()
            messages.info(request, "Registration Completed Sucessfully")
            return redirect('/')  # Redirect after successful registration
        except Exception as e:
            # Handle the error when the conversion fails
            messages.info(request, e)
            return redirect('/register')

    return render(request, 'register.html')

        
    
    return render(request, 'register.html')
