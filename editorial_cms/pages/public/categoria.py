import reflex as rx
from editorial_cms.services.category_service import obtener_categoria_por_slug
from editorial_cms.services.post_service import obtener_posts_por_categoria


@rx.page(route="/categoria/[slug]")
def categoria(slug: str):

    categoria = obtener_categoria_por_slug(slug)

    if not categoria:
        return rx.center(rx.heading("Categoría no encontrada"))

    posts = obtener_posts_por_categoria(categoria.id)

    return rx.container(
        rx.vstack(
            rx.heading(categoria.nombre),
            rx.foreach(
                posts,
                lambda post: rx.box(
                    rx.heading(post.titulo),
                    rx.link(
                        "Leer más",
                        href=f"/articulo/{post.slug}",
                        color="blue"
                    ),
                    rx.divider()
                )
            )
        )
    )