# -*- coding: utf-8 -*-

from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models.fields import CharField, IntegerField, DateField

from test_smyt.models import generated_models

class ObjectsView(ListAPIView):

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
                'objects': list(model.objects.values()),
                'fields': fields,
            }
            return Response(result, status=status.HTTP_200_OK)
        return Response(result, status=status.HTTP_400_BAD_REQUEST)


class CreateObjectView(CreateAPIView):

    def create(self, request, model, *args, **kwargs):
        self.serializer_class = generated_models.model_serializer(model)
        return super(CreateObjectView, self).create(request, *args, **kwargs)


class UpdateObjectView(UpdateAPIView):

    def update(self, request, model, *args, **kwargs):
        self.serializer_class = generated_models.model_serializer(model)
        self.model = generated_models.models.get(model)
        return super(UpdateObjectView, self).update(request, *args, **kwargs)



objects = ObjectsView.as_view()
create_object = CreateObjectView.as_view()
update_object = UpdateObjectView.as_view()
