from django.urls import path, include
from .views import another,  user_id

urlpatterns = [

    path('', another),

    # http://127.0.0.1:8000/users/<int:user_number>
    path('<int:user_number>/', user_id, name='users'),
]