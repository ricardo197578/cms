import reflex as rx

from editorial_cms.database import init_db
#Paginas admin
from editorial_cms.pages.admin.login import login
from editorial_cms.pages.admin.dashboard import dashboard
import editorial_cms.pages.admin.posts

from editorial_cms.pages.index import index 
import editorial_cms.models.post 
import editorial_cms.pages.public.articulos
import editorial_cms.pages.public.articulo
from editorial_cms.services.post_service import obtener_post_por_slug
import editorial_cms.models
from editorial_cms.pages.public.categoria import categoria

init_db()

app = rx.App()