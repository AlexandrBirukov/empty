from .models import Counter


def extras(request):
    return {
        'page_counters': Counter.objects.approved(),
    }
