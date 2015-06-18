# coding=utf-8
import ujson as json
from django.core.management.base import BaseCommand
import requests
from project.home.models import CatPushDevice
from project.settings import GOOGLE_API_KEY, GCM_ENDPOINT


class Command(BaseCommand):
    help = 'Test push notifications for Sift'

    def handle(self, *args, **options):
        headers = {
            'UserAgent': "GCM-Server",
            'Content-Type': 'application/json',
            'Authorization': 'key=' + GOOGLE_API_KEY
        }

        push_recipients = CatPushDevice.objects.all()
        values = {
            "registration_ids": [x.token for x in push_recipients],
            "data": {"album": 7, "title": "Elmar Einasto"},
            "collapse_key": "message"
        }
        values = json.dumps(values)

        response = requests.post(url=GCM_ENDPOINT, data=values, headers=headers)

        print response
        print response.content

        push_recipients = CatPushDevice.objects.all()
        values = {
            "registration_ids": [x.token for x in push_recipients],
            "data": {"album": 8, "title": "Konstantin Kalamees"},
            "collapse_key": "message2"
        }
        values = json.dumps(values)

        response = requests.post(url=GCM_ENDPOINT, data=values, headers=headers)

        print response
        print response.content