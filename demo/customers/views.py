from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/index.html', {'customers': customers})

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  # Redirect to a list view or another page
    else:
        form = CustomerForm()
    
    return render(request, 'customers/create.html', {'form': form})