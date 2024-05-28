from django.http import JsonResponse
from django.shortcuts import render
import requests

# Create your views here.
def customer_handler(request):
    url = 'http://34.16.96.114:8080/ver_clientes/'
    try:
        response = requests.get(url)
        response.raise_for_status()  
        datos = response.json()  
    except requests.exceptions.HTTPError as http_err:
        return JsonResponse({'error': f'HTTP error occurred: {http_err}'}, status=500)
    except Exception as err:
        return JsonResponse({'error': f'Other error occurred: {err}'}, status=500)

    
    return render(request, 'customers_data.html', {'clientes': datos["clientes"]})


def query_products(request, dni):
    url = f'http://34.173.229.142:8080/search/{dni}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        customer_products = response.json()
    except requests.exceptions.HTTPError as http_err:
        return JsonResponse({'error': f'HTTP error occurred: {http_err}'}, status=500)
    except Exception as err:
        return JsonResponse({'error': f'Other error occurred: {err}'}, status=500)
    
    return render(request, 'customer_product.html', {'datos_cliente': customer_products})


