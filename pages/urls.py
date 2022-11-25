from django.urls import path 
from .views import * 

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('about/', About.as_view(), name = 'about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('reklama/', Reklama.as_view(), name="reklama"),
    path('team/', Team.as_view(), name = 'team'),

    path('<int:pk>/', ArticleDetailView.as_view(), name='post_detail'),
]