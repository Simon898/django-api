# orders/management/commands/seed_orders.py
from django.core.management.base import BaseCommand
from orders.models import TransportOrder, Waypoint
from datetime import date

class Command(BaseCommand):
    help = 'Seed the database with sample transport orders'

    def handle(self, *args, **kwargs):
        TransportOrder.objects.all().delete()

        order1 = TransportOrder.objects.create(
            order_number='ORD001',
            customer_name='Simon',
            date=date(2025, 8, 21)
        )
        Waypoint.objects.create(order=order1, location='Boston', type='Delivery')

        order2 = TransportOrder.objects.create(
            order_number='ORD002',
            customer_name='Tomas',
            date=date(2025, 8, 22)
        )
        Waypoint.objects.create(order=order2, location='Chicago', type='Pickup')

        order3 = TransportOrder.objects.create(
            order_number='ORD003',
            customer_name='Ollie',
            date=date(2025, 8, 23)
        )
        Waypoint.objects.create(order=order3, location='Houston', type='Delivery')

        self.stdout.write(self.style.SUCCESS('Seeded sample transport orders'))
