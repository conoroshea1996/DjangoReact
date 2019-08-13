from django.urls import path

from .views import ArcticleListView, ArticleDetailView

urlpatterns = [
    path('', ArcticleListView.as_view()),
    path('<pk>', ArticleDetailView.as_view())
]
