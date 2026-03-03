import reflex as rx

from editorial_cms.database import init_db
from editorial_cms.pages.admin.login import login
from editorial_cms.pages.admin.dashboard import dashboard
from editorial_cms.pages.index import index
import editorial_cms.pages.admin.posts 
import editorial_cms.models.post 

init_db()

app = rx.App()

