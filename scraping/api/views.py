from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from scraping.models import Car
from scraping.api.serializers import CarSerializer
from scraping.scraper.master_scraper import scrapAllWebsites


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


@api_view(['GET'])
def scrap_websites(request):
    """ 
    Calls the process for scraping the websites
    """
    return Response(scrapAllWebsites())

    # if request.method == 'GET':
    #     cars = Car.objects.all()
    #     serializer = CarSerializer(cars, many=True)
    #     return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = CarSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getVendorTreemap(request):
    """
    Returns a JSON-like object to be used to create a treemap
    """
    vendor_list = ['aramisAuto', 'lacentrale', 'goodbuyauto.it']
    res = {}
    for vendor in vendor_list:
        res[vendor] = {"name": vendor, "children": getVendorNode(vendor)}
    return Response(res)


@api_view(['GET'])
def getVendorCount(request):
    return Response(Car.objects.get_car_count())


def getVendorNode(vendor):
    '''
    Get a list of all the models referred in DB and their count given vendor
    '''
    model_list = Car.objects.get_all_models(vendor)
    vendor_dict = {}
    vendor_list = []
    # For each model in list, we
    for model_dict in model_list:
        # Normalize the output object to get two fields name and size
        brand = model_dict["brand"]
        model_dict.pop("brand")
        model_dict["name"] = model_dict.pop("model")
        model_dict["size"] = Car.objects.get_number_of_model(
            model_dict["name"])

        # Organize the final response in specific fields per vendor
        if brand in vendor_dict.keys():
            vendor_dict[brand].append(model_dict)
        else:
            vendor_dict[brand] = [model_dict]
    for key, value in vendor_dict.items():
        vendor_list.append({"name": key, "children": value})
    return vendor_list
