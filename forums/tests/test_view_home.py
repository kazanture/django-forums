from django.urls import reverse
from django.urls import resolve
from django.test import TestCase


from ..views import ForumListView
from ..models import Forum


class HomeTests(TestCase):
    def setUp(self):
        self.forum = Forum.objects.create(name='Django', description='Django forum.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, ForumListView)

    def test_home_view_contains_link_to_topics_page(self):
        forum_topics_url = reverse('forum_topics', kwargs={'pk': self.forum.pk})
        self.assertContains(self.response, 'href="{0}"'.format(forum_topics_url))