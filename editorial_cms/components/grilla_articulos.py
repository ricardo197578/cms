import reflex as rx  # Importa Reflex para construir componentes visuales.

from editorial_cms.states.public_state import PublicState  # Estado publico con eventos de carga/navegacion.
from editorial_cms.states.site_config_state import SiteConfigState  # Estado de configuracion de layout.


def _meta_articulo(post) -> rx.Component:  # Bloque reutilizable con fecha y enlace de lectura.
    return rx.hstack(  # Agrupa metadatos del articulo en horizontal.
        rx.text(  # Muestra fecha de publicacion.
            post["fecha_publicacion"],  # Fecha ya formateada desde el estado.
            font_size=rx.breakpoints(initial="xs", md="sm"),  # Tamano responsivo de la fecha.
            color="#94a3b8",  # Color secundario legible en fondo oscuro.
        ),
        rx.text("•", color="#64748b"),  # Separador visual entre fecha y enlace.
        rx.link(  # Enlace para navegar al detalle.
            "Leer más",  # Texto del enlace.
            href="/articulo/" + post.slug,  # Ruta dinamica por slug.
            on_click=PublicState.iniciar_carga_post,  # Activa estado de carga previa.
            font_size=rx.breakpoints(initial="xs", md="sm"),  # Tamano responsivo del enlace.
            color="#3b82f6",  # Color azul principal del enlace.
            _hover={"color": "#60a5fa"},  # Color al hover.
        ),
        spacing="2",  # Espacio entre elementos del meta.
        align="center",  # Alineacion vertical al centro.
    )


def _tarjeta_minimalista(post) -> rx.Component:  # Tarjeta para layout minimalista.
    return rx.vstack(  # Apila titulo, extracto y meta.
        rx.heading(  # Titulo del articulo.
            post.titulo,  # Titulo dinamico del post.
            size=rx.breakpoints(initial="4", md="5"),  # Tamano responsivo del titulo.
            color="#f8fafc",  # Color de alto contraste.
        ),
        rx.text(  # Extracto de contenido.
            post.contenido[:170] + "...",  # Corta contenido para preview.
            font_size=rx.breakpoints(initial="sm", md="md"),  # Tamano responsivo del extracto.
            color="#cbd5e1",  # Color secundario legible.
        ),
        _meta_articulo(post),  # Inserta bloque meta reutilizable.
        spacing="2",  # Espacio vertical entre elementos.
        align="start",  # Alinea contenido al inicio.
        width="100%",  # Ocupa todo el ancho disponible.
        padding_y="1.1em",  # Padding vertical interno.
        border_bottom="1px solid #1f2937",  # Separador inferior entre articulos.
    )


def _tarjeta_blog(post) -> rx.Component:  # Tarjeta para layout blog/clasico.
    return rx.box(  # Caja externa de la tarjeta.
        rx.vstack(  # Contenido vertical de la tarjeta.
            rx.cond(  # Renderiza imagen solo si existe.
                post.imagen_destacada,  # Condicion de imagen disponible.
                rx.image(  # Imagen destacada del articulo.
                    src=rx.get_upload_url(post.imagen_destacada),  # URL publica del archivo.
                    width="100%",  # Imagen a ancho completo.
                    height=rx.breakpoints(initial="180px", md="260px"),  # Alto responsivo.
                    object_fit="cover",  # Recorta para llenar caja sin deformar.
                    border_radius="12px",  # Bordes redondeados de la imagen.
                ),
            ),
            rx.heading(  # Titulo del articulo.
                post.titulo,  # Texto dinamico del titulo.
                size=rx.breakpoints(initial="4", md="5"),  # Escala tipografica responsiva.
                color="#f8fafc",  # Color de alto contraste.
            ),
            rx.text(  # Extracto de texto.
                post.contenido[:180] + "...",  # Preview recortado para lista.
                font_size=rx.breakpoints(initial="sm", md="md"),  # Tamano responsivo del extracto.
                color="#cbd5e1",  # Color secundario legible.
                line_height="1.65",  # Interlineado comodo para lectura.
            ),
            _meta_articulo(post),  # Meta reutilizable del articulo.
            spacing="3",  # Espacio vertical entre bloques.
            align="start",  # Alineacion de contenido al inicio.
            width="100%",  # VStack a ancho completo.
        ),
        padding=rx.breakpoints(initial="1.1em", md="1.4em"),  # Padding interno responsivo.
        border="1px solid #334155",  # Borde de tarjeta oscuro.
        border_radius="12px",  # Bordes redondeados de tarjeta.
        background="#0f172a",  # Fondo oscuro de la tarjeta.
        box_shadow="0 10px 24px rgba(2, 6, 23, 0.35)",  # Sombra para separacion visual.
        width="100%",  # Tarjeta a ancho completo dentro de la columna.
    )


def _tarjeta_revista(post) -> rx.Component:  # Tarjeta para layout revista/escenario.
    return rx.box(  # Caja externa de la tarjeta revista.
        rx.vstack(  # Contenido vertical interno.
            rx.cond(  # Muestra imagen solo cuando existe.
                post.imagen_destacada,  # Condicion de imagen disponible.
                rx.image(  # Imagen destacada.
                    src=rx.get_upload_url(post.imagen_destacada),  # URL publica de imagen.
                    width="100%",  # Ancho completo.
                    height="180px",  # Alto fijo para uniformidad de grilla.
                    object_fit="cover",  # Recorte centrado de la imagen.
                    border_radius="10px",  # Bordes redondeados de imagen.
                ),
            ),
            rx.heading(post.titulo, size="4", color="#fef3c7"),  # Titulo con tono editorial claro.
            rx.text(  # Extracto de contenido.
                post.contenido[:110] + "...",  # Recorte mas breve para formato revista.
                font_size="sm",  # Tamano compacto de texto.
                color="#fde68a",  # Color calido para contraste.
                line_height="1.6",  # Interlineado de lectura.
            ),
            _meta_articulo(post),  # Inserta metadatos de fecha y enlace.
            spacing="2",  # Espacio entre bloques internos.
            align="start",  # Alinea al inicio.
            width="100%",  # Ocupa todo el ancho de la celda.
        ),
        padding="1em",  # Padding interno uniforme.
        border="1px solid #a16207",  # Borde dorado oscuro.
        border_radius="12px",  # Radio de borde.
        background="#1f150a",  # Fondo oscuro calido.
        box_shadow="0 6px 16px rgba(0, 0, 0, 0.4)",  # Sombra media.
        width="100%",  # Ancho completo de tarjeta.
        _hover={"transform": "translateY(-2px)"},  # Leve elevacion en hover.
        transition="all 0.2s ease",  # Transicion suave.
    )


def _tarjeta_portal(post) -> rx.Component:  # Tarjeta para layout portal/boletin.
    return rx.box(  # Caja externa de tarjeta portal.
        rx.vstack(  # Contenido en bloque vertical.
            rx.cond(  # Muestra imagen solo si existe.
                post.imagen_destacada,  # Condicion de imagen cargada.
                rx.image(  # Imagen destacada de la tarjeta.
                    src=rx.get_upload_url(post.imagen_destacada),  # URL de imagen subida.
                    width="100%",  # Ancho completo de la tarjeta.
                    height=rx.breakpoints(initial="170px", md="210px"),  # Alto responsivo.
                    object_fit="cover",  # Ajuste de imagen por recorte.
                    border_radius="8px",  # Bordes redondeados de imagen.
                ),
            ),
            rx.heading(post.titulo, size="4", color="#dbeafe"),  # Titulo en azul claro.
            rx.text(  # Extracto del articulo.
                post.contenido[:140] + "...",  # Recorte intermedio para portal.
                font_size="sm",  # Tamano compacto.
                color="#bfdbfe",  # Color de texto secundario.
                line_height="1.6",  # Interlineado legible.
            ),
            _meta_articulo(post),  # Metadatos reutilizables.
            spacing="2",  # Espaciado interno.
            align="start",  # Alinea al inicio.
            width="100%",  # Ocupa ancho completo.
        ),
        padding="1em",  # Padding interior.
        border="1px solid #1d4ed8",  # Borde azul.
        border_radius="8px",  # Radio de borde moderado.
        background="#0b1324",  # Fondo oscuro del bloque.
        box_shadow="0 2px 8px rgba(0, 0, 0, 0.35)",  # Sombra sutil.
        width="100%",  # Tarjeta ocupa ancho de su columna.
    )


def grilla_articulos(posts) -> rx.Component:  # Renderiza tipo de grilla segun layout activo.
    return rx.cond(  # Primer nivel de decision por layout.
        (SiteConfigState.layout_publico == "blog") | (SiteConfigState.layout_publico == "clasico"),  # Layouts tipo lista vertical.
        rx.vstack(  # Contenedor vertical para blog/clasico.
            rx.foreach(posts, _tarjeta_blog),  # Recorre posts y renderiza tarjeta blog.
            spacing="4",  # Separacion entre tarjetas.
            width="100%",  # Ocupa ancho completo.
        ),
        rx.cond(  # Segundo nivel: layouts tipo revista.
            (SiteConfigState.layout_publico == "revista") | (SiteConfigState.layout_publico == "escenario"),  # Layouts con grilla de 3 columnas desktop.
            rx.grid(  # Grilla para revista/escenario.
                rx.foreach(posts, _tarjeta_revista),  # Recorre posts y renderiza tarjeta revista.
                columns=rx.breakpoints(initial="1", md="2", lg="3"),  # Cantidad de columnas responsiva.
                spacing="4",  # Espacio entre celdas.
                width="100%",  # Grilla a ancho completo.
            ),
            rx.cond(  # Tercer nivel: layouts tipo portal.
                (SiteConfigState.layout_publico == "portal") | (SiteConfigState.layout_publico == "boletin"),  # Layouts con 2 columnas desktop.
                rx.grid(  # Grilla para portal/boletin.
                    rx.foreach(posts, _tarjeta_portal),  # Recorre posts y renderiza tarjeta portal.
                    columns=rx.breakpoints(initial="1", md="2"),  # Columnas responsivas para portal.
                    spacing="4",  # Espaciado entre tarjetas.
                    width="100%",  # Grilla a ancho completo.
                ),
                rx.vstack(  # Fallback para minimalista.
                    rx.foreach(posts, _tarjeta_minimalista),  # Renderiza lista limpia minimalista.
                    spacing="0",  # Sin gap extra para look minimal.
                    width="100%",  # Ocupa ancho total.
                ),
            ),
        ),
    )
