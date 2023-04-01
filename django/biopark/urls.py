"""biopark URL Configuration."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from biopark import views


urlpatterns = [
    path("", views.InitialView.as_view(), name='initial'),
    path("home/", views.HomeView.as_view(), name='home'),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api/", include("biopark.api_urls")),
    path("eixos/", include("axis.urls")),
    path("eixos/listar/", views.EixosList.as_view()),
    path("perguntas/listagem/", views.PerguntasList.as_view(), name='ListagemPerguntas'),
    path("perguntas/cadastro/", views.PerguntasCad.as_view(), name='CadastroPerguntas'),
    path("avaliação/listagem/", views.AvaliacaoList.as_view(), name='ListagemAvaliacao'),
    path("avaliação/criar/", views.AvaliacaoCad.as_view(), name='CriarAvaliacao'),
    path("eixos/listagem/", views.EixosList.as_view(), name='ListagemEixos'),
    path("eixos/cadastro/", views.EixosCad.as_view(), name='CadastroEixos'),
    path("instituições/", views.Instituicao.as_view(), name='instituicao'),
    path("relatórios/", views.Relatorios.as_view(), name='relatorios'),
    path("importar/alunos/", views.ImportarAlunos.as_view(), name='alunos'),
    path("relatórios/professores/", views.ImportarProfessores.as_view(), name='professores')
]


handler400 = views.Handler400View.as_view()
handler403 = views.Handler403View.as_view()
handler404 = views.Handler404View.as_view()
handler500 = views.Handler500View.as_view()


if settings.DEBUG:
    # Getting media files for debug environment.
    urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns

    # Getting django-debug-toolbar assets.
    urlpatterns = [path('__debug__/', include('debug_toolbar.urls'))] + urlpatterns
