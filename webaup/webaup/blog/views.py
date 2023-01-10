from blog import models
from wagtail.api.v2.views import BaseAPIViewSet
from blog.models import APIField
class blogViewSet(BaseAPIViewSet):

    model = models
    body_fields = BaseAPIViewSet.body_fields + ['introduction', 'image', 'body', 'subtitle', 'tags', 'date_published']