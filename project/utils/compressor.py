import re
from rcssmin import cssmin
from compressor.filters import CallbackOutputFilter


def compress(css, **kwargs):
    """
    Метод для исправления ошибки сжатия svg текста в scss - cssmin удаляет пробелы,
    что приводит к ошибки отображения svg в темплейте, тут же их предварительно 
    заменяем на %20
    """
    capture_svg = re.compile(r'url\("(data:image/svg.*?svg%3[Ee])\"\)')
    data_urls = re.findall(capture_svg, css)
    for data_url in data_urls:
        css = css.replace(data_url, data_url.replace(' ', '%20'))
    css = cssmin(css, **kwargs)
    return css


class CSSMinFilter(CallbackOutputFilter):
    """
    Переопределяем класс минифицирования для компрессора статики
    """
    callback = 'project.utils.compressor.compress'
