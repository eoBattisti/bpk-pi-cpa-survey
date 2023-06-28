from django.test import TestCase

from users.models import User

# Create your tests here.

class UserTestCase(TestCase):

  def test_create_user(self):
    user1 = User.objects.create(role=1)

    self.assertIsInstance(user1, User)
    self.assertEqual(user1.role , 1)


  def setUp(self):
    self.obj = User.objects.create(role=1)
    self.obj2 = User.objects.create(role=2)


  def test_edit_user(self):
    self.obj.role = 2
    self.obj.save()

    updated_user = User.objects.get(id=self.obj.id)

    self.assertEqual(self.obj.role, 2)


  def test_list_users(self):
    objects = User.objects.all()

    self.assertEqual(objects.count(), 2)
    self.assertEqual(objects[0].role,1)
    self.assertEqual(objects[1].role, 2)


  def test_delete_user(self):
    initial_count_of_current_objects = User.objects.count()

    self.obj2.delete()

    self.assertEqual(User.objects.count(), initial_count_of_current_objects-1)
    self.assertFalse(User.objects.filter(id=self.obj2.id).exists())