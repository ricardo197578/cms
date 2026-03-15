import reflex as rx  # Importa Reflex para crear estructuras de layout.
from editorial_cms.components.footer import footer  # Importa el footer global.

def layout(*children):  # Define un layout base para paginas publicas.
    return rx.box(  # Caja externa del layout.
        rx.vstack(  # Apila contenido y footer de forma vertical.
            *children,  # Inserta el contenido recibido por parametro.
            footer(),  # Agrega el footer al final de la pagina.
            width="100%",  # VStack a ancho completo.
            min_height="100vh",  # Altura minima igual al viewport.
            spacing="0",  # Sin separacion vertical extra.
        ),
        width="100%",  # Caja externa de ancho completo.
        background="var(--gray-1)",  # Fondo base del layout publico.
    )
