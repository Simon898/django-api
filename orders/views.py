from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TransportOrder
from .serializers import TransportOrderSerializer

class TransportOrderListCreateView(APIView):
    def get(self, request):
        queryset = TransportOrder.objects.all().prefetch_related('waypoints')

        # optional filters
        customer_name = request.query_params.get('customer_name')
        date = request.query_params.get('date')
        if customer_name:
            queryset = queryset.filter(customer_name__icontains=customer_name)
        if date:
            queryset = queryset.filter(date=date)

        serializer = TransportOrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransportOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransportOrderDetailView(APIView):
    def get(self, request, pk):
        try:
            order = TransportOrder.objects.prefetch_related('waypoints').get(pk=pk)
        except TransportOrder.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TransportOrderSerializer(order)
        return Response(serializer.data)
