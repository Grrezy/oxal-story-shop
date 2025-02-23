from django.urls import path
from django.contrib.auth import views as auth_views
from .views import lista_produtos, adicionar_produto, detalhes_produto, login_view, logout_view, registro_view
from .views import dashboard


urlpatterns = [
    path('', lista_produtos, name='lista_produtos'),
    path('<str:categoria>/', lista_produtos, name='produtos_por_categoria'),
    path('adicionar/', adicionar_produto, name='adicionar_produto'),
    path('produto/<int:produto_id>/', detalhes_produto, name='detalhes_produto'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path("registro/", registro_view, name="registro_view"),
    path('dashboard/', dashboard, name='dashboard'),
     # Outras URLs
    path('senha/reset/', auth_views.PasswordResetView.as_view(template_name="produtos/password_reset.html"), name='password_reset'),
    path('senha/reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="produtos/password_reset_done.html"), name='password_reset_done'),
    path('senha/reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="produtos/password_reset_confirm.html"), name='password_reset_confirm'),
    path('senha/reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name="produtos/password_reset_complete.html"), name='password_reset_complete'),
]

