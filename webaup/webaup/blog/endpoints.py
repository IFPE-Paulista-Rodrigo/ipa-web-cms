from wagtail.api.v2.endpoints import BaseAPIEndpoint
from .models import models

class BlogAPIEndpoint(BaseAPIEndpoint):
    model  = models