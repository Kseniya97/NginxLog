import json
from django.core.management.base import BaseCommand

from parser.ParserNginxLog import ParserNginxLog


class Command(BaseCommand):
    help = 'Parse log file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **options):
        file_path = options['file_path']

        if not self.is_valid_file(file_path):
            self.stdout.write(
                self.style.ERROR('This document format is not supported for reading. Use txt.'))
        else:
            with open(file_path, 'r') as file:
                data = file.readlines()
            json_objects = [json.loads(line) for line in data if line.strip()]
            pars_log = ParserNginxLog()
            pars_log.pars_date(json_objects, {'app_label': 'parser', 'model': 'LogModel'})
            pass

    def is_valid_file(self, file_path):
        """
       Check is valid file.

        :param file_path: str.
        :return: True/False
        """
        return file_path.endswith('.txt')
