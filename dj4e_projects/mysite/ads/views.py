# Create your views here.
from .models import Ad
from .owner import *


class AdListView(OwnerListView):
    model = Ad


class AdDetailView(OwnerDetailView):
    model = Ad


class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ["title", "text", "price"]


class AdDeleteView(OwnerDeleteView):
    model = Ad


class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ["title", "text", "price"]
