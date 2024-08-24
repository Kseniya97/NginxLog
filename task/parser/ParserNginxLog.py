import logging
from datetime import datetime

from django.apps import apps


logger = logging.getLogger(__name__)

class ParserNginxLog:
    def __init__(self):
        pass

    def pars_date(self, json_data, info_model):
        """
        Parses JSON data and saves it to the database.

        :param json_data: List of JSON objects containing log data.
        :param model: Dictionary containing model information {'model': 'MyModel', 'app_label': 'myapp'}
        :return:
        """
        try:
            Model = apps.get_model(info_model['app_label'], info_model['model'])
            data_log_model = [Model(
                ip_adress=data['remote_ip'],
                data=datetime.strptime(data['time'], '%d/%b/%Y:%H:%M:%S %z'),
                http_method=data['request'].split(' ')[0],
                URI_request=data['request'].split(' ')[1],
                code_answer=data['response'],
                size_answer=data['bytes'],
            ) for data in json_data]

            Model.objects.bulk_create(data_log_model)
        except Exception as e:
            logger.error('Метод parse_date не может распарсить данные: {}'.format(e))
