# -*- coding: utf-8 -*-

import yaml
import os
from copy import deepcopy

from django.db import models
from django.utils.functional import cached_property
from django.contrib.postgres.fields import ArrayField
from rest_framework import serializers

# Create your models here.



class ModelFactory(object):
    FIELD_TYPES = {
        'char': models.CharField,
        'int': models.IntegerField,
        'date': models.DateField,
    }
    FIELD_DEFAULTS = {
        'char': {
            'max_length': 255,
        }
    }
    FIELD_ATTRS = {
        'title': 'verbose_name',
        'id': 'db_column',
        'default': 'default',
        'blank': 'blank',
        'null': 'null',
        'max_length': 'max_length',
    }

    def __init__(self, definition):
        self.definition = definition

    @cached_property
    def models(self):
        models_classes = {}
        for name, definition in self.definition.items():
            name = name.capitalize()
            model_attrs = {
                '__module__': self.__module__,
                'Meta': type('Meta', (), {
                    'verbose_name': definition.get('title', name),
                    'app_label': self.__module__.split('.')[0],
                })
            }
            for field in definition.get('fields', []):
                field_type = field.pop('type')
                attrs = self.FIELD_DEFAULTS.get(field_type, {})
                attrs.update({self.FIELD_ATTRS.get(attr): value
                                    for attr, value in field.items()
                                    if attr in self.FIELD_ATTRS.keys()})
                model_attrs[field.get('id')]= self.FIELD_TYPES.get(field_type)(**attrs)
            models_classes[name] = type(name, (models.Model,), model_attrs)
        return models_classes

    @cached_property
    def serializers(self):
        models_serializers = {}
        for name, model in self.models.items():
            class_name = '%sSerializer' % name
            models_serializers[class_name] = type(class_name, (serializers.ModelSerializer,), {
                'Meta': type('Meta', (), {
                    'model': model,
                })
            })
        return models_serializers

    def model_serializer(self, model_name):
        return self.serializers.get('%sSerializer' % model_name)


generated_models = ModelFactory(yaml.load(open(os.path.join(os.path.dirname(__file__), 'models.yaml'))))
locals().update(generated_models.models)
locals().update(generated_models.serializers)

class Category(models.Model):
    name = models.CharField(u'Группа товара', max_length=64)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name=u'Группа')
    name = models.CharField(u'Название товара', max_length=128)
    price = models.DecimalField(u'Стоимость единицы, руб.', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Phone(models.Model):
    phone = models.CharField(max_length=255)
    users = ArrayField(base_field=models.IntegerField())


class Item(models.Model):
    STATUS_CHOICES = (
        (3, u'Не продан'),
        (7, u'Продан'),
        (5, u'Резерв'),
    )

    user_id = models.IntegerField()
    status = models.SmallIntegerField(choices=STATUS_CHOICES)