# posts.management.commands.db_command

import os
from pathlib import Path
from dotenv import load_dotenv
from django.core.management.base import BaseCommand
from newsapi import NewsApiClient
from django.contrib.auth.models import User

from posts.models import BlogPost

BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path)


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **kwargs):
        newsapi = NewsApiClient(api_key=os.environ.get('NEWS_API_KEY'))

        top_headlines = newsapi.get_top_headlines(
            sources='bbc-news, cnn',
            language='en',
            page_size=100,
        )

        if top_headlines['status']=='ok':
            articles = top_headlines['articles']
            for i in range(len(articles)):

                # print(f"author: {articles[i]['author']}, cont: {articles[i]['content']}, title:{articles[i]['title']}, articles[i]['publishedAt']")
                
                user, created = User.objects.get_or_create(
                    username = articles[i]['author'],
                    password = f"{articles[i]['author']*3}"
                )

                if not created:
                    user.save()

                new_post, created = BlogPost.objects.get_or_create(
                    author=user, title=articles[i]['title'],
                    body=articles[i]['content'], image_url=articles[i]['urlToImage'], url=articles[i]['url'],
                    created_at=articles[i]['publishedAt'],
                    updated_at=articles[i]['publishedAt'],
                )

                if not created:
                    new_post.save()
                else:
                    break

