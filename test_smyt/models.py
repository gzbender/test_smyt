# -*- coding: utf-8 -*-

import yaml
import os

from django.db import models

# Create your models here.

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

def get_models_from_file(filename, module):
    models_classes = {}
    models_dict = yaml.load(open(filename))
    for name, definition in models_dict.items():
        name = name.capitalize()
        model_attrs = {}
        for field in definition.get('fields', []):
            field_type = field.pop('type')
            attrs = FIELD_DEFAULTS.get(field_type, {})
            attrs.update({FIELD_ATTRS.get(attr): value
                                for attr, value in field.items()
                                if attr in FIELD_ATTRS.keys()})
            model_attrs[field.get('id')]= FIELD_TYPES.get(field_type)(**attrs)
        model_attrs['Meta'] = type('Meta', (), {
            'verbose_name': definition.get('title', name),
            'app_label': module.split('.')[0],
        })
        model_attrs['__module__'] = module
        models_classes[name] = type(name, (models.Model,), model_attrs)
    return models_classes

generated_models = get_models_from_file(os.path.join(os.path.dirname(__file__), 'models.yaml'),
                                     'test_smyt.models')
locals().update(generated_models)