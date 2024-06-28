from django.urls import path
from . import views

app_name = 'polls'
# <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
# <li><a href="/polls/{{question.id}}/">{{question.question_text}}</a></li>
# app_name, specific 추가
urlpatterns = [
    path('', views.index, name='index'),
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]