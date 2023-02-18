from django.urls import path
from .views import home,pizzas,order_view,my_orders


urlpatterns = [
    
    path('',home,name='home' ),
    path('pizzas/',pizzas,name='pizzas' ),
    path('pizzas/<int:id>',order_view,name='order' ),
    path('my_orders/',my_orders,name='my_orders' ),
]