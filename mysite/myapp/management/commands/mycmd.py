from django.core import management
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Generates DRF API Views and Serializers for a Django app'

    def add_arguments(self, parser):
        parser.add_argument('args', metavar='app_label', nargs='+', help='One or more application label.')

        parser.add_argument('-f', '--format', dest='format',
                            default='viewset',
                            help='view format: viewset(default), apiview, function, modelviewset'),

        parser.add_argument('-d', '--depth', dest='depth', default=0,
                            help='serialization depth'),

        parser.add_argument('--force', dest='force', action='store_true',
                            help='force overwrite files'),

        parser.add_argument('--serializers', dest='serializers',
                            action='store_true',
                            help='generate serializers only'),

        parser.add_argument('--views', dest='views', action='store_true',
                            help='generate views only'),

        parser.add_argument('--urls', dest='urls', action='store_true',
                            help='generate urls only'),

        parser.add_argument('--verbose', dest='verbose', action='store_true',
                            help='Print out logs of file generation'),

    def handle(self, *args, **options):
        management.call_command('generate', *args, **options)
