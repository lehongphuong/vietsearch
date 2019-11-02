from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'), 

    # *******************************************************
    # begin Articles 
    path('insertAllDataFromJSON', views.insertAllDataFromJSON, name='insertAllDataFromJSON'),
    path('createDataArticles', views.createDataArticles, name='createDataArticles'),
    path('readDataArticles', views.readDataArticles, name='readDataArticles'),
    path('readManyDataArticles', views.readManyDataArticles, name='readManyDataArticles'),
    path('readAllDataArticles', views.readAllDataArticles, name='readAllDataArticles'),
    path('updateDataArticles', views.updateDataArticles, name='updateDataArticles'),
    path('deleteDataArticles', views.deleteDataArticles, name='deleteDataArticles'),
    path('deleteManyDataArticles', views.deleteManyDataArticles, name='deleteManyDataArticles'),
    path('searchDataArticles', views.searchDataArticles, name='searchDataArticles'), 
    # end Articles
    # *******************************************************  

    path('test', views.test, name='test'),
]
