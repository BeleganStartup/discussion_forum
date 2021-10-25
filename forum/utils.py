# Python
import uuid
# Django
from django.utils.text import slugify


def slugify_text(text):
    text = slugify(text)
    extra_text = str(uuid.uuid4())[0:8]
    return f"{text}-{extra_text}"
