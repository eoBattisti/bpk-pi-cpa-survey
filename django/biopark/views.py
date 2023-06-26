"""Biopark views for Biopark Search project."""
from django.views.generic import TemplateView, RedirectView
from django.urls import reverse_lazy
from users.models import User


class InitialView(RedirectView):
    """
    Home page
    """
    def get_redirect_url(self, *args, **kwargs):
        user = User.objects.filter(pk=self.request.user.pk).first()

        if not user:
            return reverse_lazy("login")
        return reverse_lazy("home")


class HomeView(TemplateView):
    template_name = 'prepages/home/home.html'


class PerguntasList(TemplateView):
    """
    TemplateView de exemplo
    """
    template_name = 'prepages/perguntas/ListagemPerguntas.html'


class PerguntasCad(TemplateView):
    """
    TemplateView de exemplo
    """
    template_name = 'prepages/perguntas/CadastroPerguntas.html'


class ExamListView(TemplateView):
    """
    TemplateView de exemplo
    """
    template_name = 'prepages/avaliacao/ListagemAvaliacao.html'


class ExamCreateView(TemplateView):
    """
    TemplateView de exemplo
    """
    template_name = 'form/exams_editor.html'

class ExamUpdateView(TemplateView):
    """
    TemplateView de exemplo
    """
    template_name = 'form/exams_editor.html/<uuid:pk>'


class EixosList(TemplateView):
    """
    TemplateView de exemplo
    """
    template_name = 'prepages/eixos/ListagemEixos.html'


class EixosCad(TemplateView):
    """
    TemplateView de exemplo
    """
    template_name = 'prepages/eixos/CadastroEixos.html'


class Instituicao(TemplateView):
    """
    TemplateView de exemplo
    """
    template_name = 'prepages/instituicao/instituicao.html'


class Relatorios(TemplateView):
    """
    TemplateView de exemplo
    """
    template_name = 'prepages/relatorios/relatorios.html'


class ImportarAlunos(TemplateView):
    """
    TemplateView de exemplo
    """
    template_name = 'prepages/importar/alunos.html'


class ImportarProfessores(TemplateView):
    """
    TemplateView de exemplo
    """
    template_name = 'prepages/importar/professores.html'


class Handler400View(TemplateView):
    """
    Handler 400 view.
    """
    template_name = 'handler/400.html'


class Handler404View(TemplateView):
    """
    Handler 404 view.
    """
    template_name = 'handler/404.html'


class Handler500View(TemplateView):
    """
    Handler 500 view.
    """
    template_name = 'handler/500.html'


class Handler403View(TemplateView):
    """
    Handler 403 view.
    """
    template_name = 'handler/403.html'
