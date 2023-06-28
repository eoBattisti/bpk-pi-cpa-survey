from django.test import RequestFactory, TestCase
from django.urls import reverse
from axis.models import Axle
from questions.models import Question
from axis.views import AxleUpdateView, AxleListView, AxleCreateView
from questions.views import QuestionsListView, QuestionsCreateView, QuestionsUpdateView

# Create your tests here.
class QuestionTestCase(TestCase):

  def test_create_question(self):
    # Cria a instância de Axis com os devidos atributos
    axis1 = Axle.objects.create(name="primeiro_eixo", description="eixo_primeira_desc")
    question1 = Question.objects.create(description="question_primeira_desc", axis=axis1)
    
    
    self.assertIsInstance(question1, Question) 
    self.assertEqual(question1.description, "question_primeira_desc") 
    self.assertEqual(question1.axis.name, "primeiro_eixo") 
  

  def setUp(self):
    self.factory = RequestFactory()
    self.obj = Axle.objects.create(name="test_axis", description="desc_to_be_updated")
    self.obj2 = Question.objects.create(description="first_one_to_be_listed", axis=self.obj)
    self.obj3 = Question.objects.create(description="second_one_to_be_listed", axis=self.obj)
    self.obj4 = Question.objects.create(description="third_one_to_be_listed", axis=self.obj)


  def test_list_questions(self):
    objects = Question.objects.all()

    self.assertEqual(objects.count(), 3)
    self.assertEqual(objects[0].description, "first_one_to_be_listed")
    self.assertEqual(objects[1].description, "second_one_to_be_listed")
    self.assertEqual(objects[2].description, "third_one_to_be_listed")

  
  def test_edit_question(self):
    self.obj2.description = "Updated_description"
    self.obj2.save()

    updated_question = Question.objects.get(id=self.obj2.id)

    self.assertEqual(updated_question.description, "Updated_description")


  def test_delete_question(self):
    initial_count_of_current_objects = Question.objects.count()

    self.obj2.delete()

    self.assertEqual(Question.objects.count(), initial_count_of_current_objects-1)
    self.assertFalse(Question.objects.filter(id=self.obj2.id).exists())
    

  def test_list_view_question(self):
    url = reverse("ListagemPerguntas")
    request = self.factory.get(url)
    response = QuestionsListView.as_view()(request)

    self.assertEqual(response.status_code, 200)
      
    self.assertContains(response, "third_one_to_be_listed")


  def test_create_view_question(self):
    self.obj1 = Axle.objects.create(name="axis_for_question", description="loren")
    url = reverse('CadastroPerguntas') 
    data = {'description': 'primeira_pergunta_teste', 'axis': self.obj1.id, 'answer_type': 1}
    request = self.factory.post(url, data)
    response = QuestionsCreateView.as_view()(request)

    self.assertEqual(response.status_code, 302)

    self.assertTrue(Question.objects.filter(description='primeira_pergunta_teste').exists())

  
  def test_update_view_question(self):
    url = reverse('questions:update', args=[self.obj3.id])
    data = {'id': self.obj3.id, 'description': 'updated object', 'axis': self.obj.id, 'answer_type': 1}
    request = self.factory.post(url, data)
    response = QuestionsUpdateView.as_view()(request, pk=self.obj3.id)

    self.assertEqual(response.status_code, 302)

    self.obj3.refresh_from_db()

    self.assertTrue(Question.objects.filter(description='updated object').exists())
    
    