import reflex as rx  # Importa Reflex para usar componentes de layout.


def content_container(*children):  # Crea un contenedor reutilizable para contenido principal.
    return rx.container(  # Componente container centrado.
        *children,  # Inyecta todos los componentes hijos recibidos.
        max_width="900px",  # Limita ancho maximo para mejorar legibilidad.
        width="100%",  # Ocupa todo el ancho disponible dentro del padre.
        margin="0 auto",  # Centra horizontalmente el container.
        padding_x=rx.breakpoints(initial="1em", md="1.5em", lg="2em"),  # Padding horizontal responsivo.
        padding_y=rx.breakpoints(initial="1.5em", md="2em", lg="2.5em"),  # Padding vertical responsivo.
    )
