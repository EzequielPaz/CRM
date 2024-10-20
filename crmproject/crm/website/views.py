from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddCustomerForm
from .models import Customer


def home(request):
    customers = Customer.objects.all()
    #Verificaion de inicio de sesion
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Has inciado sesion correctamente")
            return redirect('home')
        else:
            messages.success(request, "Hay un error")
            return redirect('home')
    else:
        return render(request, "home.html", {'customers':customers})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "Ha cerrado la sesion")
    return redirect('home')
    
def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Se ha registrado correctamente, Bienvenido!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Customer.objects.get(id=pk)
		return render(request, 'customer.html', {'customer_record':customer_record})
	else:
		messages.success(request, "Necesita primero inciar sesion para ver esto...")
		return redirect('home')
      
def delete_customer_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Customer.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Los datos del cliente han sido eliminados")
		return redirect('home')
	else:
		messages.success(request, "Debe inciar sesion primero")
		return redirect('home')
	
def add_customer(request):
	form = AddCustomerForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_customer = form.save()
				messages.success(request, "Cliente registrado exitosamente")
				return redirect('home')
		return render(request, 'add_customer.html', {'form':form})
	else:
		messages.success(request, "Debe inciar sesion primero")
		return redirect('home')

def update_customer(request, pk):
	if request.user.is_authenticated:
		current_record = Customer.objects.get(id=pk)
		form = AddCustomerForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Datos del cliente actualizados exitosamente!")
			return redirect('home')
		return render(request, 'update_customer.html', {'form':form})
	else:
		messages.success(request, "Debe inciar sesion primero")
		return redirect('home')