#import reflex as rx

#config = rx.Config(
#    app_name="editorial_cms",
#    plugins=[
#        rx.plugins.SitemapPlugin(),
#        rx.plugins.TailwindV4Plugin(),
#    ]
#)

#produccion
import reflex as rx
import os

config = rx.Config(
    app_name="editorial_cms",
    db_url=os.getenv("DATABASE_URL"),

    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)