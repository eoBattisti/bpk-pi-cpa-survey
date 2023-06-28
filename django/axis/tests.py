from django.test import RequestFactory, TestCase
from django.urls import reverse
from axis.models import Axle
from users.models import User
from axis.views import AxleUpdateView, AxleListView, AxleCreateView

# Create your tests here.

# Setup
class AxleTestCase(TestCase):

  def test_create_axis(self):
    # Cria a instância de Axis com os devidos atributos
    axis1 = Axle.objects.create(name="primeiro_eixo", description="primeira_desc")
    axis2 = Axle.objects.create(name="segundo_eixo", description="segundo_eixo_desc")
    
    self.assertIsInstance(axis1, Axle) # verifica se a instância é do tipo Axle
    self.assertEqual(axis1.name, "primeiro_eixo") # verifica se o atributo name foi definido corretamente
    self.assertEqual(axis1.description, "primeira_desc") # verifica se o atributo description foi definido corretamente

    self.assertIsInstance(axis2, Axle)
    self.assertEqual(axis2.name, "segundo_eixo")
    self.assertEqual(axis2.description, "segundo_eixo_desc")


  def setUp(self):
    self.obj = Axle.objects.create(name="first_one_to_be_listed", description="desc_to_be_updated")
    self.obj2 = Axle.objects.create(name="second_one_to_be_listed", description="loren")
    self.obj3 = Axle.objects.create(name="third_one_to_be_listed", description="loren")
    self.obj4 = Axle.objects.create(name="forth_one_to_be_listed", description="loren")
    self.factory = RequestFactory()

  
  def test_edit_axis(self):
    self.obj.name = "i_got_updated"
    self.obj.description = "loren"
    self.obj.save()

    updated_axis = Axle.objects.get(id=self.obj.id)

    self.assertEqual(self.obj.name, "i_got_updated")
    self.assertEqual(updated_axis.description, "loren")

  
  def test_list_axis(self):
    objects = Axle.objects.all()

    self.assertEqual(objects.count(), 4)
    self.assertEqual(objects[0].name, "first_one_to_be_listed")
    self.assertEqual(objects[1].name, "second_one_to_be_listed")
    self.assertEqual(objects[2].name, "third_one_to_be_listed")
    self.assertEqual(objects[3].name, "forth_one_to_be_listed")

  
  def test_delete_axis(self):
    initial_count_of_current_objects = Axle.objects.count()

    self.obj.delete()

    self.assertEqual(Axle.objects.count(), initial_count_of_current_objects-1)
    self.assertFalse(Axle.objects.filter(id=self.obj.id).exists())

  
  def test_list_view_axis(self):
    url = reverse("ListagemEixos")  
    request = self.factory.get(url)
    response = AxleListView.as_view()(request)

    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "forth_one_to_be_listed")


  def test_create_view_axis(self):
      url = reverse("CadastroEixos")  
      data = {'name': 'create_view_test_object', 'description': 'loren'}
      request = self.factory.post(url, data)
      response = AxleCreateView.as_view()(request)

      self.assertEqual(response.status_code, 302)

      self.assertTrue(Axle.objects.filter(name='create_view_test_object').exists())


  def test_update_view_axis(self):
        url = reverse('axis:update', args=[self.obj3.id])
        data = {'id': self.obj3.id, 'name': 'updated object', 'description': 'loren'}
        request = self.factory.post(url, data)
        response = AxleUpdateView.as_view()(request, pk=self.obj3.id)

        self.assertEqual(response.status_code, 302)

        self.obj3.refresh_from_db()

        self.assertEqual(self.obj3.name, 'updated object')
  
