from rest_framework.decorators import api_view
from rest_framework.response import Response

from scraping.models import Car


@api_view(['GET'])
def get_highlighted_number(request):
    return Response()


@api_view(['GET'])
def get_vendor_treemaps(request):
    """
    Returns a JSON-like object to be used to create a treemap
    """
    vendor_list = ['aramisAuto', 'lacentrale', 'goodbuyauto.it']
    res = {}
    for vendor in vendor_list:
        res[vendor] = {"name": vendor, "children": getVendorNode(vendor)}
    return Response(res)


@api_view(['GET'])
def get_boxplot(request):
    return Response()


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
