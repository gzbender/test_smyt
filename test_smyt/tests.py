# -*- coding: utf-8 -*-


from rest_framework.renderers import JSONRenderer
from django.test.utils import override_settings
from django.test import TestCase
from django.core.urlresolvers import reverse
from django_dynamic_fixture import G, N
from django.db.models.fields import CharField, IntegerField, DateField

from test_smyt import models

def test_settings(fn):
    return override_settings(DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'test_smyt',
            'USER': 'smyt',
            'PASSWORD': 'somepass',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
        }
    })(fn)

@test_settings
class ModelsTest(TestCase):

    def test(self):
        for name, model in models.generated_models.models.items():
            serializer = models.generated_models.model_serializer(name)
            # create test
            obj = G(model)
            # update test
            new = N(model)
            for field in model._meta.get_all_field_names():
                if field != model._meta.pk.name and getattr(obj, field) != getattr(new, field):
                    setattr(obj, field, getattr(new, field))
            obj.save()



@test_settings
class ObjectsViewTest(TestCase):

    def setUp(self):
        super(ObjectsViewTest, self).setUp()
        self.maxDiff = None
        self.view_name = 'objects'

    def test_list(self):
        types = {
            CharField: 'text',
            IntegerField: 'number',
            DateField: 'date',
        }
        for name, model in models.generated_models.models.items():
            fields = []
            for field in model._meta.fields:
                fields.append({
                    'name': field.name,
                    'type': types.get(type(field)),
                    'title': field.verbose_name,
                    'required': field.blank,
                    'editable': field.editable,
                })
            # create 3 objects
            [G(model) for i in range(3)]
            data = {
                'objects': list(model.objects.values()),
                'fields': fields
            }
            url = reverse(self.view_name, kwargs={'model': name})
            response = self.client.get(url)
            self.assertDictEqual(data, response.data)


@test_settings
class CreateObjectViewTest(TestCase):

    def setUp(self):
        super(CreateObjectViewTest, self).setUp()
        self.maxDiff = None
        self.view_name = 'create_object'

    def test_create_object(self):
        for name, model in models.generated_models.models.items():
            serializer = models.generated_models.model_serializer(name)
            data = serializer(N(model)).data
            pk = model._meta.pk.name
            if pk in data:
                del data[pk]
            url = reverse(self.view_name, kwargs={'model': name})
            response = self.client.post(url, data)
            response_data = response.data
            if pk in response_data:
                del response_data[pk]
            self.assertDictEqual(data, response_data)


@test_settings
class UpdateObjectViewTest(TestCase):

    def setUp(self):
        super(UpdateObjectViewTest, self).setUp()
        self.maxDiff = None
        self.view_name = 'update_object'

    def test_create_object(self):
        jr = JSONRenderer()

        for name, model in models.generated_models.models.items():
            serializer = models.generated_models.model_serializer(name)
            obj = G(model)
            pk = model._meta.pk.name
            # PUT
            data = serializer(N(model)).data
            if pk in data:
                del data[pk]
            url = reverse(self.view_name, kwargs={'model': name, 'pk': obj.id})
            response = self.client.put(url, jr.render(data), content_type='application/json')
            response_data = response.data
            if pk in response_data:
                del response_data[pk]
            self.assertDictEqual(data, response_data)
            # PATCH
            orig_data = serializer(obj).data
            patch_data = {}
            for key, val in orig_data.items():
                if key != pk and val != data.get(key):
                    patch_data = {
                        key: val
                    }
                    data[key] = val
                    break
            response = self.client.patch(url, jr.render(patch_data), content_type='application/json')
            response_data = response.data
            if pk in response_data:
                del response_data[pk]
            self.assertDictEqual(data, response_data)
