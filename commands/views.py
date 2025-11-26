from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render

from .models import Command


@login_required
def home(request):
    query = request.GET.get('q', '').strip()
    tag = request.GET.get('tag', '').strip()
    level = request.GET.get('level', '').strip()

    commands = Command.objects.filter(user=request.user)

    if query:
        commands = commands.filter(
            Q(name__icontains=query)
            | Q(description__icontains=query)
            | Q(command__icontains=query)
        )

    if tag:
        commands = commands.filter(tag__icontains=tag)

    if level:
        commands = commands.filter(level=level)

    commands = commands.order_by('-updated_at', '-created_at')

    available_tags = (
        Command.objects.filter(user=request.user)
        .values_list('tag', flat=True)
        .distinct()
        .order_by('tag')
    )

    context = {
        'commands': commands,
        'query': query,
        'tag': tag,
        'level': level,
        'available_tags': available_tags,
    }

    return render(request, 'commands/home.html', context)
