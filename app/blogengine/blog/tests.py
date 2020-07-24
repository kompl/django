from django.test import TestCase
from blog.models import Post, Tag


class PostModelCase(TestCase):
    def setUp(self):
        Post.objects.create(title='test-title', body='test-body')
        Tag.objects.create(title='test_tag')

    def test_title_label(self):

        test_post = Post.objects.first()

        field_label = test_post._meta.get_field('title').verbose_name
        field_max_length = test_post._meta.get_field('title').max_length
        field_db_index = test_post._meta.get_field('title').db_index

        self.assertEqual(field_label, 'title')
        self.assertEqual(field_max_length, 150)
        self.assertEqual(field_db_index, True)

    def test_body_label(self):

        test_post = Post.objects.first()

        field_label = test_post._meta.get_field('body').verbose_name
        field_blank = test_post._meta.get_field('body').blank

        self.assertEqual(field_label, 'body')
        self.assertEqual(field_blank, True)

    def test_date_pub_label(self):

        test_post = Post.objects.first()

        field_label = test_post._meta.get_field('date_pub').verbose_name
        field_auto_now_add = test_post._meta.get_field('date_pub').auto_now_add

        self.assertEqual(field_label, 'date pub')
        self.assertEqual(field_auto_now_add, True)

    def test_slug_label(self):
        test_post = Post.objects.first()

        field_label = test_post._meta.get_field('slug').verbose_name
        field_blank = test_post._meta.get_field('slug').blank
        field_max_length = test_post._meta.get_field('slug').max_length
        field_unique = test_post._meta.get_field('slug').unique


        self.assertEqual(field_label, 'slug')
        self.assertEqual(field_blank, True)
        self.assertEqual(field_max_length, 150)
        self.assertEqual(field_unique, True)


    def test_tags_label(self):

        test_tag = Tag.objects.first()
        test_post = Post.objects.first()

        test_post.tags.add(test_tag)

        field_label = test_post._meta.get_field('tags').verbose_name
        field_blank = test_post._meta.get_field('tags').blank
        tag_title = test_post.tags.first().title



        self.assertEqual(field_label, 'tags')
        self.assertEqual(field_blank, True)
        self.assertEqual(tag_title, 'test_tag')
