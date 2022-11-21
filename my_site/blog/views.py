from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "python-for-data-science",
        "image": "mountains.jpg",
        "author": "Ashraf Uddin",
        "date": date(2022, 11, 1),
        "title": "Python for Data Science",
        "excerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde, recusandae?",
        "content": """
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi nobis incidunt quaerat eos aut, unde repudiandae enim minima natus eveniet, laudantium facere, dolore fugiat explicabo quod quis sequi. Neque ad illum iste iusto nemo sed itaque delectus quis aperiam voluptate, tempora culpa, ipsum sapiente et ea labore enim. Dignissimos, ratione, atque incidunt molestias eligendi, consequatur distinctio dolore expedita mollitia similique aliquid. Dolore laborum pariatur voluptate, perferendis non unde facere iusto dolorem voluptates officia sint quis. Velit ipsam temporibus odio quis dolorem. Placeat aspernatur quo, dolore eum esse voluptatum culpa ex aliquam deleniti, nam adipisci perspiciatis minima sapiente pariatur ipsa. Unde!
        """,
    },
    {
        "slug": "python-for-data-visualize",
        "image": "woods.jpg",
        "author": "Ashraf Uddin",
        "date": date(2022, 11, 1),
        "title": "Python for Data Visualize",
        "excerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde, recusandae?",
        "content": """
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi nobis incidunt quaerat eos aut, unde repudiandae enim minima natus eveniet, laudantium facere, dolore fugiat explicabo quod quis sequi. Neque ad illum iste iusto nemo sed itaque delectus quis aperiam voluptate, tempora culpa, ipsum sapiente et ea labore enim. Dignissimos, ratione, atque incidunt molestias eligendi, consequatur distinctio dolore expedita mollitia similique aliquid. Dolore laborum pariatur voluptate, perferendis non unde facere iusto dolorem voluptates officia sint quis. Velit ipsam temporibus odio quis dolorem. Placeat aspernatur quo, dolore eum esse voluptatum culpa ex aliquam deleniti, nam adipisci perspiciatis minima sapiente pariatur ipsa. Unde!
        """,
    },
    {
        "slug": "python",
        "image": "coding.jpg",
        "author": "Ashraf Uddin",
        "date": date(2022, 11, 1),
        "title": "Python",
        "excerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde, recusandae?",
        "content": """
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi nobis incidunt quaerat eos aut, unde repudiandae enim minima natus eveniet, laudantium facere, dolore fugiat explicabo quod quis sequi. Neque ad illum iste iusto nemo sed itaque delectus quis aperiam voluptate, tempora culpa, ipsum sapiente et ea labore enim. Dignissimos, ratione, atque incidunt molestias eligendi, consequatur distinctio dolore expedita mollitia similique aliquid. Dolore laborum pariatur voluptate, perferendis non unde facere iusto dolorem voluptates officia sint quis. Velit ipsam temporibus odio quis dolorem. Placeat aspernatur quo, dolore eum esse voluptatum culpa ex aliquam deleniti, nam adipisci perspiciatis minima sapiente pariatur ipsa. Unde!
        """,
    },
    {
        "slug": "dart",
        "image": "mountains.jpg",
        "author": "Ashraf Uddin",
        "date": date(2022, 11, 1),
        "title": "Dart",
        "excerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde, recusandae?",
        "content": """
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi nobis incidunt quaerat eos aut, unde repudiandae enim minima natus eveniet, laudantium facere, dolore fugiat explicabo quod quis sequi. Neque ad illum iste iusto nemo sed itaque delectus quis aperiam voluptate, tempora culpa, ipsum sapiente et ea labore enim. Dignissimos, ratione, atque incidunt molestias eligendi, consequatur distinctio dolore expedita mollitia similique aliquid. Dolore laborum pariatur voluptate, perferendis non unde facere iusto dolorem voluptates officia sint quis. Velit ipsam temporibus odio quis dolorem. Placeat aspernatur quo, dolore eum esse voluptatum culpa ex aliquam deleniti, nam adipisci perspiciatis minima sapiente pariatur ipsa. Unde!
        """,
    }
]


def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
