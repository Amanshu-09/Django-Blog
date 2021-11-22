from blog.views import category
from .models import *

def categories(request):
    cats = Post.objects.values('category').distinct()
    categories = []
    for dict in cats:
        for value in dict.values():
            categories.append(value)

    length = len(categories)
    middle_index = length//2
    categories1 = categories[:middle_index]
    categories2 = categories[middle_index:]

    return {
        'categories1': categories1,
        'categories2': categories2
    }