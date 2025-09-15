from rest_framework import serializers
from .models import TransportOrder, Waypoint

class WaypointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waypoint
        fields = ['id', 'location', 'type']

class TransportOrderSerializer(serializers.ModelSerializer):
    waypoints = WaypointSerializer(many=True)

    class Meta:
        model = TransportOrder
        fields = ['id', 'order_number', 'customer_name', 'date', 'waypoints']

    def create(self, validated_data):
        waypoints_data = validated_data.pop('waypoints', [])
        order = TransportOrder.objects.create(**validated_data)
        for wp_data in waypoints_data:
            Waypoint.objects.create(order=order, **wp_data)
        return order
