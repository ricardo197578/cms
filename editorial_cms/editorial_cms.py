import reflex as rx

from editorial_cms.database import init_db
from editorial_cms.pages.admin.login import login
from editorial_cms.pages.admin.dashboard import dashboard
from editorial_cms.pages.index import index

init_db()

app = rx.App()

