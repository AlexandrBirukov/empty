from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
import os


@deconstructible
class FileExtValidator(object):
    message = _(
        "File extension '%(extension)s' is not allowed. "
        "Allowed extensions are: '%(allowed_extensions)s'."
    )
    code = 'invalid_extension'

    def __init__(self, allowed_extensions=None, max_size=None, message=None, code=None):
        self.allowed_extensions = allowed_extensions  # Допустимые расширения
        self.max_size = max_size  # Максимальный размер
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):

        # Проверяем допустимое расширение загружаемого файла
        extension = os.path.splitext(value.name)[1][1:].lower()
        if self.allowed_extensions is not None and extension not in self.allowed_extensions:
            raise ValidationError(
                self.message,
                code=self.code,
                params={
                    'extension': extension,
                    'allowed_extensions': ', '.join(self.allowed_extensions)
                }
            )

        # Проверяем размер загружаемого файла
        file_size = len(value)
        if self.max_size and file_size > self.max_size:
            message = _('Превышен размер загружаемого файла')
            raise ValidationError(message)

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.allowed_extensions == other.allowed_extensions and
            self.message == other.message and
            self.code == other.code
        )
