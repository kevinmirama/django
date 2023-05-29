from django.http import JsonResponse
from .models import Contacto
from django.shortcuts import render
import requests
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


def buscar_actualizar_contacto(request):
    # Verificar si el método de la solicitud es POST
    if request.method == 'POST':
        # Obtener el correo electrónico y el nombre de la solicitud
        email = request.POST.get('email')
        nombre = request.POST.get('nombre')
        # Intentar encontrar un contacto con el correo electrónico dado
        contacto = Contacto.objects.filter(email=email).first()
        # Si se encuentra un contacto
        if contacto:
            # Actualizar el nombre del contacto
            contacto.nombre = nombre
            contacto.save()
            # Devolver una respuesta JSON indicando que el contacto fue actualizado
            return JsonResponse({'mensaje': 'Contacto actualizado'})
        else:
            # Si no se encuentra un contacto, crear uno nuevo con el correo electrónico y el nombre dados
            Contacto.objects.create(email=email, nombre=nombre)
            # Devolver una respuesta JSON indicando que se creó un nuevo contacto
            return JsonResponse({'mensaje': 'Contacto creado'})
    else:
        # Si el método de la solicitud no es POST, devolver una respuesta JSON indicando que el método no está permitido
        return JsonResponse({'mensaje': 'Método no permitido'})


def mostrar_formulario(request):
    return render(request, 'plantilla.html')

def crear_o_actualizar_hubspot(email, nombre):
    # Construir la URL para la API de HubSpot utilizando el correo electrónico y la clave de API de HubSpot
    url = f"https://api.hubapi.com/contacts/v1/contact/createOrUpdate/email/{email}/?hapikey={settings.HUBSPOT_API_KEY}"
    # Crear los datos para enviar a la API de HubSpot
    data = {
        "properties": [
            {"property": "email", "value": email},
            {"property": "firstname", "value": nombre}
        ]
    }
    # Enviar una solicitud POST a la API de HubSpot con los datos
    response = requests.post(url, json=data)


# Crear una ruta /webhook para recibir un webhook que llegara por una petición POST
@csrf_exempt
def webhook(request):
    # Verificar si el método de la solicitud es POST
    if request.method == 'POST':
        # Obtener los datos del cuerpo de la solicitud
        data = request.body
        # Procesar los datos recibidos
        # Devolver una respuesta JSON indicando que el webhook fue recibido
        return JsonResponse({'mensaje': 'Webhook recibido'})
    else:
        # Si el método de la solicitud no es POST, devolver una respuesta JSON indicando que el método no está permitido
        return JsonResponse({'mensaje': 'Método no permitido'})
