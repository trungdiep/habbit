import logging
from django.utils.deprecation import MiddlewareMixin

log = logging.getLogger(__name__)

class ProcessViewMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        setattr(request, 'test', 'trung diep')
        return None