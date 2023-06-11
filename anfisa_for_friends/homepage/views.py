from django.shortcuts import render


from ice_cream.models import IceCream


def index(request):
    template_name = 'homepage/index.html'
    ice_cream_list = IceCream.objects.select_related('wrapper').filter(
        category__is_published=True, is_published=True, is_on_main=True
    ).order_by('title')
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template_name, context)
