from django.urls import path
from .views import another, user_id, index

urlpatterns = [

    # path('', another),
    #
    # # http://127.0.0.1:8000/users/<int:user_number>
    # path('<int:user_number>/', user_id, name='users'),
    # path('', index, name='first'),
]
