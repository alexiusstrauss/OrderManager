from django.contrib import admin

from .models import Agent, Commission, Order, OrderItem

admin.site.register(Agent)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Commission)
