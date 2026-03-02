import reflex as rx

@rx.page(
    route="/",
    on_load=lambda: rx.redirect("/admin/login")
)
def index():
    return rx.box()