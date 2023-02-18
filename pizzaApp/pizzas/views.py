from django.shortcuts import render,redirect
from .models import Pizza,Order
from .forms import PizzaForm

def home(request):
    return render(request, 'pizzas/home.html')


def pizzas(request):
    pizzas = Pizza.objects.all()
    
    context = {
        'pizzas': pizzas
    }
    return render(request, 'pizzas/pizzas.html', context)


def order_view(request, id):
    pizza = Pizza.objects.get(id=id)
    form = PizzaForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            order = form.save(commit=False)
            order.pizza = pizza
            order.user = request.user
            order.save()
            return redirect('home')
    context = {
        'pizza': pizza,
        'form': form
    }
    return render(request, 'pizzas/order.html', context)

def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    context = {
        'orders': orders,
        
    }
    return render(request, 'pizzas/my_orders.html',context)