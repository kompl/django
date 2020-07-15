from django.core.paginator import Paginator
from blog.models import Post

def paginate(request, posts):
    paginator = Paginator(posts, 12)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''

    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''

    context={'page': page,
             'next_url': next_url,
             'prev_url': prev_url
    }
    return context
