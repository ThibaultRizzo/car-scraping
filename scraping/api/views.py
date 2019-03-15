import csv
import datetime
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from scraping.models import Car
from scraping.api.serializers import CarSerializer
from scraping.scraper.master_scraper import scrapAllWebsites

from django.http import HttpResponse


class CustomResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'limit': self.page_size,
            'results': data
        })


class CarViewSet(viewsets.ModelViewSet):
    pagination_class = CustomResultsSetPagination
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def list(self, request):
        queryset = Car.objects.all()
        serializer = CarSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def recent_cars(self, request):
        recent_cars = Car.objects.all().order_by('-created')

        page = self.paginate_queryset(recent_cars)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_cars, many=True)
        return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Car.objects.all()
    #     car = get_object_or_404(queryset, pk=pk)
    #     serializer = CarSerializer(car)
    #     return Response(serializer.data)

    @action(detail=False)
    def get_car_csv(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="car_list_%s.csv"' % datetime.date.today()

        writer = csv.writer(response)
        fields_list = Car.get_fields()
        car_list = Car.objects.all().order_by(*fields_list)
        writer.writerow(fields_list)
        for car in car_list:
            row = []
            for field in fields_list:
                row.append(getattr(car, field))
            writer.writerow(row)
        return response


@api_view(['GET'])
def scrap_websites(request):
    """ 
    Calls the process for scraping the websites
    """
    return Response(scrapAllWebsites())
