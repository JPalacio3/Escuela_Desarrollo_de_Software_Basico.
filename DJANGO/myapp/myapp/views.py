from django.http import HttpResponse


def hola(request):
    numeros = [int(n) for n in request.GET['numeros'].split(',')]
    print(numeros)
    numerosOrd = sorted(numeros)

    return HttpResponse(str(numerosOrd))


def verificarEdad(requets, nombre, edad):
    if edad < 18:
        mensaje = f'Hola, {nombre}, No puede ingresar !'
    else:
        mensaje = f'Hola, {nombre}, puede ingresar !'

    return HttpResponse(mensaje)
