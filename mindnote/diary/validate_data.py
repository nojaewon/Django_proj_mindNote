from .models import Page
import random

def validate_pages():
    pages = Page.objects.all()
    for page in pages:
        page.score = random.randint(0,10)
        page.save()