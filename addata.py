
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
from polls.models import Post

for i in range(20):
	newdata = Post(title = "我的標題{}".format(i+5),
		           body = "我的內文{}".format(i+5))
	newdata.save()