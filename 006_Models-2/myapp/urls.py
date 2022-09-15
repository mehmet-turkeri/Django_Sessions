from django.urls import path
from .views import myapp, welcome

# '/myapp/' dan sonra
urlpatterns = [
    path('', myapp),
    path('welcome/', welcome),
    
]