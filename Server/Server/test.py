from django.test import TestCase
from .models import User

class UserTestCase(TestCase):
	def setUp(self):
		User.objects.create(first_name="XYZ", last_name="PQR",email="xyz@gmail.com",username="xyzwu1928",
			password="xyzwu1928", total_upvotes_notes=3, total_downvotes_notes=1, 
			total_upvotes_assignments=4, total_downvotes_assignments=1)

	def testUser(self):
		user = User.objects.get(username="xyzwu1928",password="xyzwu1928")
		print(user.first_name)
		print(user.last_name)
		print(user.total_upvotes_assignments)
		print(user.total_downvotes_notes)
		self.assertEqual(user is not None, True)