from helicopter.models import *

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contacts'},
]

class DataMixin:
    paginate_by = 5
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cats_selected' not in context:
            context['cat-selected'] = 0
        return context