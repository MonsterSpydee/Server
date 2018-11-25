from django.test import TestCase
from Server.models import User
from .models import POST
from Course_Branch.models import COURSE
from Course_Branch.models import BRANCH


class UserTestCase(TestCase):
	def setUp(self):
		User.objects.create(first_name="XYZ", last_name="PQR",email="xyz@gmail.com",username="xyzwu1928",
			password="xyzwu1928", total_upvotes_notes=3, total_downvotes_notes=1, 
			total_upvotes_assignments=4, total_downvotes_assignments=1)
		user = User.objects.get(username="xyzwu1928",password="xyzwu1928")
		BRANCH.objects.create(branch_id="CSE", branch_name="Computer Science and Engineering")
		branch = BRANCH.objects.get(branch_id="CSE")
		COURSE.objects.create(course_id="CSPE12", course_name="DAPA", branch=branch)
		course = COURSE.objects.get(course_id="CSPE12")
		POST.objects.create(author=user, course=course, num_upvotes=4, num_downvotes=1, 
			num_views=100, isNotes=False)

	def testUser(self):
		post = POST.objects.get(post_id=1)
		print(post.author.username)
		self.assertEqual(post is not None, True)