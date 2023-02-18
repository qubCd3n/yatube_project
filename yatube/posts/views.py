from django.http import HttpResponse


def index(request):
    return HttpResponse('Тут будет очень крутой дизайн главной страницы')

def group_posts(request, slug):
    return HttpResponse(f'А это у нас получается страничка для постов '
                        'отфильтрованных по группам.')