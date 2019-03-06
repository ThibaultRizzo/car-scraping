from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from scraping.models import Car
from scraping.api.serializers import CarSerializer
from scraping.scraper.master_scraper import scrapAllWebsites


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def list(self, request):
        queryset = Car.objects.all()
        serializer = CarSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Car.objects.all()
        car = get_object_or_404(queryset, pk=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)


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
    vendor = 'Aramisauto'
    model_list = Car.objects.get_all_model(vendor)
    vendor_dict = {}
    vendor_list = []
    for model_dict in model_list:
        brand = model_dict["brand"]
        model_dict.pop("brand")
        model_dict["name"] = model_dict.pop("model")
        model_dict["size"] = Car.objects.get_number_of_model(
            model_dict["name"])

        if brand in vendor_dict.keys():
            vendor_dict[brand].append(model_dict)
        else:
            vendor_dict[brand] = [model_dict]
    for key, value in vendor_dict.items():
        vendor_list.append({"name": key, "children": value})
    return Response({"name": vendor, "children": vendor_list})


@api_view(['GET'])
def getVendorCount(request):
    return Response(Car.objects.get_car_count())
