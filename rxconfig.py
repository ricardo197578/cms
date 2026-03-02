import reflex as rx

config = rx.Config(
    app_name="editorial_cms",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)