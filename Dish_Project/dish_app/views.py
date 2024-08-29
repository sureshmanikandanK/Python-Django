from django.shortcuts import render
from .models import Dish
from .serializers import DishSerializer,DishDetailSerializer,DishImageSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status,parsers
from rest_framework.decorators import action


class DishViewset(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    parser_classes = (parsers.FormParser,parsers.MultiPartParser,parsers.FileUploadParser)

    def get_serializer_class(self):
        if self.action == 'list':
            return DishSerializer
        elif self.action == 'create':
            return DishSerializer
        elif self.action == 'upload_image':
            return DishImageSerializer
        return self.serializer_class
    @action(methods=['POST'],detail=True,url_path='upload_image')
    def upload_image(self,request,pk=None):
        Dish_objs=self.get_object()
        serializer = self.get_serializer(Dish_objs,data=request.data)
        if not serializer.is_valid():
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message': 'Invalid Data'
                })
        serializer.save()
        return Response({
                'status': status.HTTP_201_CREATED,
                'data': serializer.data,
                'message': 'Dish Image successfully'
            })


    def list(self, request):
        try:
            Dish_objs = Dish.objects.all()
            serializer = self.get_serializer(Dish_objs, many=True)
            return Response({
                'status': status.HTTP_200_OK,
                'data': serializer.data
            })
        except Exception as e:
            print(e)
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })

    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid():
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message': 'Invalid Data'
                })
            serializer.save()
            return Response({
                'status': status.HTTP_201_CREATED,
                'data': serializer.data,
                'message': 'Dish created successfully'
            })
        except Exception as e:
            print(e)
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })

    def update(self, request, pk=None):
        try:
            Dish_objs = self.get_object()
            serializer = self.get_serializer(Dish_objs, data=request.data, partial=False)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message': 'Invalid Data'
                })
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'data': serializer.data,
                'message': 'Dish Updated Successfully'
            })
        except Exception as e:
            print(e)
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })

    def partial_update(self, request, pk=None):
        try:
            Dish_objs = self.get_object()
            serializer = self.get_serializer(Dish_objs, data=request.data, partial=True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message': 'Invalid Data'
                })
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'data': serializer.data,
                'message': 'Dish Partially Updated Successfully'
            })
        except Exception as e:
            print(e)
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })

    def destroy(self, request, pk=None):
        try:
            Dish_objs = self.get_object()
            Dish_objs.delete()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Dish deleted successfully'
            })
        except Exception as e:
            print(e)
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })
