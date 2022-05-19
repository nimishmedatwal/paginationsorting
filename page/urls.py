from django.urls import path,include


from page import views

urlpatterns = [
    path('',views.directory, name='directory')
]
