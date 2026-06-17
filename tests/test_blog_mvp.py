import unittest

from blog import create_app
from blog.models import Post


class BlogMVPTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_homepage_is_available(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('WNBlog'.encode('utf-8'), response.data)

    def test_post_detail_is_available(self):
        with self.app.app_context():
            post = Post.query.first()
            self.assertIsNotNone(post)
            slug = post.slug

        response = self.client.get(f'/posts/{slug}')
        self.assertEqual(response.status_code, 200)

    def test_create_post_page_is_available(self):
        response = self.client.get('/admin/posts/new')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
