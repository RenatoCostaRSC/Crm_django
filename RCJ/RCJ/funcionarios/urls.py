from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from RCJ.funcionarios import views as funcionarios_views

app_name = 'funcionarios'
urlpatterns = [
    #path('login/', LoginView.as_view(template_name='accounts/login.html'), name = 'login'),
    #path('login/', accounts_views.user_login, name='login'),
    #path('logout/', accounts_views.user_logout, name = 'logout'),
    path('lista_funcionarios/', funcionarios_views.list_funcionarios, name = 'lista_funcionario'),
    path('cadastrar_funcionario/', funcionarios_views.create_funcionario, name = 'cadastro_funcionario'),
    path('editar_funcionario/<int:pk>-<slug:slug>', funcionarios_views.edit_funcionario, name = 'editar_funcionario'),
    path('deletar_funcionario/<int:pk>-<slug:slug>', funcionarios_views.delete_funcionario, name = 'deletar_funcionario'),
    #path('admin/', admin.site.urls),
]
