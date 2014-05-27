from website.models import Event

def populate_footer(request):
    return {'events': Event.objects.all()}