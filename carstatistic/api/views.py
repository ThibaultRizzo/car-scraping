from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from carstatistic.models import CarStatistic, CarStatisticTitle
from carstatistic.api.serializers import CarStatisticSerializer

from scraping.models import Car
import datetime


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarStatisticSerializer
    queryset = CarStatistic.objects.all()


@api_view(['GET'])
def get_highlighted_number(request):
    queryset = CarStatistic.objects.getLatestStats()
    serializer = CarStatisticSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_vendor_treemaps(request):
    """
    Returns a JSON-like object to be used to create a treemap
    """
    vendor_list = Car.objects.get_all_vendors()
    res = []
    for vendor in vendor_list:
        res.append({"name": vendor, "children": getVendorNode(vendor)})
    return Response({"name": "Treemap", "children": res})


@api_view(['GET'])
def get_boxplot(request):
    brand_list = Car.objects.get_all_brands()
    res = []
    for brand in brand_list:
        res.append(
            {"key": brand, "values": Car.objects.get_all_models_per_brand(brand, ['price'])})
    return Response(res)


def getVendorNode(vendor):
    '''
    Get a list of all the models referred in DB and their count given vendor
    '''
    model_list = Car.objects.get_all_models_per_vendor(vendor)
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
