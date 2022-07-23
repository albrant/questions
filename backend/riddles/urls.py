from django.urls import path
from . import views

app_name = 'riddles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:riddle_id>/', views.detail, name='detail'),
    path('<int:riddle_id>/answer', views.answer, name='answer')
]
