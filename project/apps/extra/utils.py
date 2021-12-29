from django.core.mail import get_connection

from .models import EmailSettings, EmailLogger


def get_email_data():
    """
    Возвращает коннектор из базы данных для send_mail
    :return: connection, to_email
    """

    email_db = EmailSettings.objects.get()
    email_settings = {
        'host': email_db.host,
        'port': email_db.port,
        'username': email_db.email,
        'password': email_db.password,
        'use_tls': email_db.tls,
    }
    connection = get_connection(**email_settings)
    to_email = email_db.email
    return connection, to_email


def make_log(message):
    """
    Создание лога ошибки
    :return: объект созданного лога
    """
    log = EmailLogger.objects.create(message=message)
    return log
