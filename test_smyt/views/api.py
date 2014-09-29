# -*- coding: utf-8 -*-

from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models.fields import CharField, IntegerField, DateField

from test_smyt.models import generated_models

class ObjectsView(ListCreateAPIView):

    def list(self, request, model):
        types = {
            CharField: 'text',
            IntegerField: 'number',
            DateField: 'date',
        }
        result = {}
        if model in generated_models.models:
            model = generated_models.models.get(model)
            fields = []
            for field in model._meta.fields:
                fields.append({
                    'name': field.name,
                    'type': types.get(type(field)),
                    'title': field.verbose_name,
                    'required': field.blank,
                    'editable': field.editable,
                })
            result = {
                'objects': model.objects.values(),
                'fields': fields,
            }
            return Response(result, status=status.HTTP_200_OK)
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, model):
        self.serializer_class = generated_models.model_serializer(model)
        return super(ObjectsView, self).create(request)
        serializer = generated_models.model_serializer(model)(data=attrs)
        if serializer.is_valid():
            self.object = serializer.save(force_insert=True)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED,
                            headers=headers)
        return Response(None, status=status.HTTP_400_BAD_REQUEST)


objects = ObjectsView.as_view()
