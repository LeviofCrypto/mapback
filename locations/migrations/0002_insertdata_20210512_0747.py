# Generated by Django 3.2.2 on 2021-05-12 07:47
from datetime import datetime, timezone

from django.db import migrations


def add_users(app_registry, schema_editor):
    User = app_registry.get_model('auth', 'User')
    new_users = [
        {
            'username': 'lowe',
            'password': 'password',
        },
        {
            'username': 'regular',
            'password': 'password'
        }
    ]
    for u in new_users:
        User.objects.create_user(**u)

def add_icons(app_registry, schema_editor):
    MarkerIcon = app_registry.get_model('locations', 'MarkerIcon')
    new_icons = [
        {
            "code_name": "bed",
            "humanreadable_name": "bed"
        },
        {
            "code_name": "bus",
            "humanreadable_name": "bus"
        },
        {
            "code_name": "coffee",
            "humanreadable_name": "coffee"
        },
        {
            "code_name": "cross",
            "humanreadable_name": "cross"
        },
        {
            "code_name": "crown",
            "humanreadable_name": "crown"
        },
        {
            "code_name": "globe",
            "humanreadable_name": "globe"
        },
        {
            "code_name": "hamburger",
            "humanreadable_name": "hamburger"
        },
        {
            "code_name": "house",
            "humanreadable_name": "house"
        },
        {
            "code_name": "mountain",
            "humanreadable_name": "mountain"
        },
        {
            "code_name": "ship",
            "humanreadable_name": "ship"
        },
        {
            "code_name": "shopping-bag",
            "humanreadable_name": "shopping bag"
        },
        {
            "code_name": "shopping-cart",
            "humanreadable_name": "shopping cart"
        },
        {
            "code_name": "subway",
            "humanreadable_name": "subway"
        },
        {
            "code_name": "swimmer",
            "humanreadable_name": "swimmer"
        },
        {
            "code_name": "train",
            "humanreadable_name": "train"
        },
        {
            "code_name": "tram",
            "humanreadable_name": "tram"
        },
        {
            "code_name": "tree",
            "humanreadable_name": "tree"
        },
        {
            "code_name": "important-building",
            "humanreadable_name": "important building"
        },
        {
            "code_name": "utensils",
            "humanreadable_name": "utensils"
        }
    ]
    for i in new_icons:
        MarkerIcon.objects.create(**i)

def add_significances(app_registry, schema_editor):
    MarkerSignificance = app_registry.get_model('locations', 'MarkerSignificance')
    User = app_registry.get_model('auth', 'User')
    owner1 = User.objects.get(username='lowe')
    new_signifs = [
        {
            'significance_label': 'Definitely visit',
            'hex_code': '00f000',
            'color_name': 'green'
        },
        {
            'significance_label': 'Maybe visit',
            'hex_code': 'f00000',
            'color_name': 'red'
        },
        {
            'significance_label': 'Camping spot',
            'hex_code': 'ffa500',
            'color_name': 'orange',
            'owner': owner1
        }
    ]
    for s in new_signifs:
        MarkerSignificance.objects.create(**s)

def add_locations(app_registry, schema_editor):
    Location = app_registry.get_model('locations', 'Location')
    MarkerSignificance = app_registry.get_model('locations', 'MarkerSignificance')
    MarkerIcon = app_registry.get_model('locations', 'MarkerIcon')
    User = app_registry.get_model('auth', 'User')
    new_locs = [
        {
            'place_name': 'Old home',
            'address': 'Hjortronvägen 22, Karlskoga',
            'latitude': 59.3103316,
            'longitude': 14.4888874,
            'description': 'This is where I grew up',
            'significance': MarkerSignificance.objects.get(
                significance_label='Definitely visit'
            ),
            'icon': MarkerIcon.objects.get(code_name='utensils'),
            'owner': User.objects.get(username='lowe')
        },
        {
            'address': 'Stortorget, Karlskrona',
            'latitude': 56.1611345,
            'longitude': 15.5849206,
            'description': 'There is a mediocre view of the square from here.',
            'significance': MarkerSignificance.objects.get(
                significance_label='Maybe visit'
            ),
            'icon': MarkerIcon.objects.get(code_name='house'),
            'owner': User.objects.get(username='regular')
        }
    ]
    for l in new_locs:
        Location.objects.create(**l)


def add_visitedgeopositions(app_registry, schema_editor):
    VisitedGeoPosition = app_registry.get_model('locations', 'VisitedGeoPosition')
    User = app_registry.get_model('auth', 'User')
    new_pos = [
        {
            'latitude': 59.3103316,
            'longitude': 14.4888874,
            'utc_timestamp': datetime(2002, 3, 2, 10, 3, 5, 340*1000, tzinfo=timezone.utc),
            'wall_clock_timestamp': datetime(2002, 3, 2, 11, 3, 5, 340*1000, tzinfo=timezone.utc),
            'owner': User.objects.get(username='lowe')
        },
        {
            'latitude': 59.3103336,
            'longitude': 14.4888894,
            'utc_timestamp': datetime(2002, 3, 2, 10, 4, 5, 340*1000, tzinfo=timezone.utc),
            'wall_clock_timestamp': datetime(2002, 3, 2, 11, 4, 5, 340*1000, tzinfo=timezone.utc),
            'owner': User.objects.get(username='lowe')
        },
    ]
    for p in new_pos:
        VisitedGeoPosition.objects.create(**p)

class Migration(migrations.Migration):
    dependencies = [
        ('locations', '0001_initial')
    ]

    add_funs = (
        add_users, 
        add_icons, 
        add_significances, add_locations,
        add_visitedgeopositions
    )

    operations = [migrations.RunPython(add_fun) for add_fun in add_funs]
