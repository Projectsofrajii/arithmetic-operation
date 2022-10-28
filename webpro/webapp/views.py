from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from operator import add
from .models import Arithmetic
from django.http import JsonResponse
from .serializers import Arithseri
# Create your views here.
class Arithmeticop(viewsets.ModelViewSet):

    def addition(self):
        inputA = self.request.GET('inputA')
        inputB = self.request.GET('inputB')
        if 'inputA' in self.request.GET and 'inputA' in self.request.GET:
            return JsonResponse(Arithmetic.objects.add(inputA + inputB))

    def subtraction(self):
        inputA = self.request.GET('inputA')
        inputB = self.request.GET('inputB')
        if 'inputA' in self.request.GET and 'inputA' in self.request.GET:
            return JsonResponse(Arithmetic.objects.sub(inputA + inputB))

    def multiplication(self):
        inputA = self.request.GET('inputA')
        inputB = self.request.GET('inputB')
        if 'inputA' in self.request.GET and 'inputA' in self.request.GET:
            return JsonResponse(Arithmetic.objects.mul(inputA + inputB))

    def division(self):
        inputA = self.request.GET('inputA')
        inputB = self.request.GET('inputB')
        if 'inputA' in self.request.GET and 'inputA' in self.request.GET:
            return JsonResponse(Arithmetic.objects.div(inputA + inputB))
