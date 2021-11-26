from django.contrib import admin

from client.models import User
from .models import User, cart, delivery_agent, order, order_details

# Register your models here.
admin.site.register(User)
admin.site.register(order)
admin.site.register(order_details)
admin.site.register(cart)
admin.site.register(delivery_agent)