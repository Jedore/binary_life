from functools import wraps

from .models import BinaryLife


def add_total_views(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        bl = BinaryLife.objects.all().first()
        if bl:
            bl.views = bl.views + 1
            bl.save()
        else:
            bl = BinaryLife()
            bl.views = bl.views + 1
            bl.save()
        return func(*args, **kwargs)

    return wrapper
