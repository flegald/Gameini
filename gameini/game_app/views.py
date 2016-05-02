from __future__ import unicode_literals
from django.shortcuts import render


def placeholder(request):
    """Place holder view."""
    return render(request, 'placeholder.html')
