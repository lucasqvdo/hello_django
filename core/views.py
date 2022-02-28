from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {}, de {} anos</h1>'.format(nome, idade))

def soma(request, valor1, valor2):
    resultado=valor1+valor2


    return HttpResponse('<h1> O resultado da soma de {} e {} é: {}'.format(valor1, valor2, resultado))


def div(request, valor1, valor2):
    resultado=valor1/valor2


    return HttpResponse('<h1> O resultado da divisão de {} e {} é: {}'.format(valor1, valor2, resultado))

def subtracao(request, valor1, valor2):
    resultado=valor1-valor2


    return HttpResponse('<h1> O resultado da subtração de {} e {} é: {}'.format(valor1, valor2, resultado))