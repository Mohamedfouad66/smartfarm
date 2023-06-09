# sensors_api/sensors/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_temperature(request):
    # Code to read the DHT11 sensor and retrieve the temperature
    temperature = read_dht11_temperature()  # Implement this function to read the temperature

    # Return the temperature as JSON
    return JsonResponse({'temperature': temperature})

@csrf_exempt
def get_humidity(request):
    # Code to read the DHT11 sensor and retrieve the humidity
    humidity = read_dht11_humidity()  # Implement this function to read the humidity

    # Return the humidity as JSON
    return JsonResponse({'humidity': humidity})

@csrf_exempt
def get_soil_moisture(request):
    # Code to read the soil moisture sensor and retrieve the moisture level
    soil_moisture = read_soil_sensor()  # Implement this function to read the soil moisture

    # Return the moisture level as JSON
    return JsonResponse({'moisture': soil_moisture})

@csrf_exempt
def get_raindrop_status(request):
    # Code to read the raindrop sensor and retrieve the status
    raindrop_status = read_raindrop_sensor()  # Implement this function to read the raindrop sensor

    # Return the status as JSON
    return JsonResponse({'status': raindrop_status})

@csrf_exempt
def get_pir_status(request):
    # Code to read the PIR sensor and retrieve the status
    pir_status = read_pir_sensor()  # Implement this function to read the PIR sensor

    # Return the status as JSON
    return JsonResponse({'status': pir_status})




