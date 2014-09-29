# -*- coding: utf-8 -*-

from django.utils import timezone
from rest_framework.test import APISimpleTestCase
from django.test.utils import override_settings
from django.conf import settings
from django.test import TestCase
from django.core.urlresolvers import reverse

from test_smyt import models

@override_settings(DATABASES = {
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
})
class ObjectsTest(TestCase):

    def setUp(self):
        super(ObjectsTest, self).setUp()
        self.maxDiff = None
        models.Users.objects.create(name='test', paycheck=70000, date_joined=timezone.now())
        models.Users.objects.create(name='test1', paycheck=90000, date_joined=timezone.now())
        models.Rooms.objects.create(department='test', spots=4)
        models.Rooms.objects.create(department='test1', spots=2)
        self.data = {
            reverse('objects', kwargs={'model': 'Users'}): {
                "fields": [{"editable": True, "required": True, "type": None, "name": "id", "title": "ID"},
                            {"editable": True, "required": False, "type": "text", "name": "name",
                             "title": u"Имя"},
                            {"editable": True, "required": False, "type": "number", "name": "paycheck",
                             "title": u"Зарплата"},
                            {"editable": True, "required": False, "type": "date", "name": "date_joined",
                             "title": u"Дата поступления на работу"}],
                "objects": list(models.Users.objects.values()),
            },
            reverse('objects', kwargs={'model': 'Rooms'}): {
                "fields": [{"editable": True, "required": True, "type": None, "name": "id", "title": "ID"},
                           {"editable": True, "required": False, "type": "text", "name": "department",
                            "title": u"Отдел"},
                           {"editable": True, "required": False, "type": "number", "name": "spots",
                            "title": u"Вместимость"}],
                "objects": list(models.Rooms.objects.values()),
            }}

    def test_list(self):
        for url, data in self.data.items():
            response = self.client.get(url)
            self.assertDictEqual(data, response.data)