"""Biopark views for Biopark Search project."""
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
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


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'prepages/home/home.html'





class PerguntasList(LoginRequiredMixin, TemplateView):
    """
    TemplateView de exemplo
    """
    login_url = reverse_lazy('login')
    template_name = 'prepages/perguntas/ListagemPerguntas.html'





class PerguntasCad(LoginRequiredMixin, TemplateView):
    """
    TemplateView de exemplo
    """
    login_url = reverse_lazy('login')
    template_name = 'prepages/perguntas/CadastroPerguntas.html'


    


class AvaliacaoList(LoginRequiredMixin, TemplateView):
    """
    TemplateView de exemplo
    """
    login_url = reverse_lazy('login')
    template_name = 'prepages/avaliacao/ListagemAvaliacao.html'

    


class AvaliacaoCad(LoginRequiredMixin, TemplateView):
    """
    TemplateView de exemplo
    """
    login_url = reverse_lazy('login')
    template_name = 'prepages/avaliacao/CriarAvaliacao.html'

    


class EixosList(LoginRequiredMixin, TemplateView):
    """
    TemplateView de exemplo
    """
    login_url = reverse_lazy('login')
    template_name = 'prepages/eixos/ListagemEixos.html'

    


class EixosCad(LoginRequiredMixin, TemplateView):
    """
    TemplateView de exemplo
    """
    login_url = reverse_lazy('login')
    template_name = 'prepages/eixos/CadastroEixos.html'

    


class Instituicao(LoginRequiredMixin, TemplateView):
    """
    TemplateView de exemplo
    """
    login_url = reverse_lazy('login')
    template_name = 'prepages/instituicao/instituicao.html'

    


class Relatorios(LoginRequiredMixin, TemplateView):
    """
    TemplateView de exemplo
    """
    login_url = reverse_lazy('login')
    template_name = 'prepages/relatorios/relatorios.html'

    


class ImportarAlunos(LoginRequiredMixin, TemplateView):
    """
    TemplateView de exemplo
    """
    login_url = reverse_lazy('login')
    template_name = 'prepages/importar/alunos.html'

    


class ImportarProfessores(LoginRequiredMixin, TemplateView):
    """
    TemplateView de exemplo
    """
    login_url = reverse_lazy('login')
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
