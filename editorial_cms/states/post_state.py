import reflex as rx
from typing import List
from pathlib import Path
from uuid import uuid4
from editorial_cms.models.post import Post
from editorial_cms.models.category import Category
from editorial_cms.states.auth_state import AuthState
from editorial_cms.services.post_service import (
    crear_post,
    obtener_posts,
    obtener_posts_por_autor,
    eliminar_post,
    actualizar_post,
    obtener_post_por_id,
)
from editorial_cms.services.post_service import toggle_publicado
from editorial_cms.services.category_service import obtener_categorias


class PostState(rx.State):

    titulo: str = ""
    contenido: str = ""
    categoria_id: str = ""
    imagen_destacada: str = ""  # Nombre del archivo de imagen

    posts: List[Post] = []
    categorias: List[Category] = []
    editando_id: int | None = None

    # 🔹 PAGINACIÓN
    page: int = 1
    posts_per_page: int = 5
    busqueda: str = ""

    # 🔹 Setter para categoria_id que valida y parsea correctamente
    def set_categoria_id(self, value: str):
        """Captura el ID de categoría del select y lo valida"""
        if value:
            # Extrae solo números del valor en caso de que venga con referencias
            try:
                # Si viene como string puro (ej: "1"), lo asigna directamente
                if value.isdigit():
                    self.categoria_id = value
                else:
                    # Si viene vacío o inválido, lo limpiar
                    self.categoria_id = ""
            except:
                self.categoria_id = ""
        else:
            self.categoria_id = ""

    # 🔹 Cargar posts según rol
    async def cargar_posts(self):

        auth = await self.get_state(AuthState)

        # Admin → todos
        if auth.user_role == "admin":
            self.posts = obtener_posts()
            self.page = 1  # Resetear a primera página
            return

        # Editor → solo los suyos
        if auth.user_id:
            self.posts = obtener_posts_por_autor(auth.user_id)
            self.page = 1  # Resetear a primera página
        else:
            self.posts = []

    # 🔹 Cargar categorías disponibles
    async def cargar_categorias(self):
        self.categorias = obtener_categorias()

    # 🖼️ Subir imagen destacada
    async def subir_imagen(self, files: list[rx.UploadFile]):
        """Sube la imagen destacada del artículo."""
        if not files:
            print("✗ No hay archivos para subir")
            return
        
        try:
            archivo = files[0]
            if not archivo.filename:
                print("✗ El archivo no tiene nombre")
                return
            
            # Generar nombre único para evitar colisiones
            extension = Path(archivo.filename).suffix.lower()
            nombre_unico = f"img_{uuid4().hex}{extension}"
            
            # Obtener ruta de destino
            ruta_upload = Path(rx.get_upload_dir())
            ruta_upload.mkdir(parents=True, exist_ok=True)
            ruta_destino = ruta_upload / nombre_unico
            
            # Leer y guardar el archivo
            contenido = await archivo.read()
            ruta_destino.write_bytes(contenido)
            
            # Verificar que el archivo se guardó
            if ruta_destino.exists() and ruta_destino.stat().st_size > 0:
                self.imagen_destacada = nombre_unico
                print(f"✓ Imagen guardada: {nombre_unico}")
            else:
                print(f"✗ El archivo no se guardó correctamente")
        
        except Exception as e:
            print(f"✗ Error al subir imagen: {e}")
            import traceback
            traceback.print_exc()

    # 🔹 Crear post seguro
    async def guardar_post(self):

        if not self.titulo or not self.contenido or not self.categoria_id:
            return

        auth = await self.get_state(AuthState)

        if not auth.user_id:
            return

        try:
            categoria_id = int(self.categoria_id)
            crear_post(
                self.titulo, 
                self.contenido, 
                auth.user_id, 
                categoria_id,
                imagen_destacada=self.imagen_destacada or None
            )

            self.titulo = ""
            self.contenido = ""
            self.categoria_id = ""
            self.imagen_destacada = ""
            
            await self.cargar_posts()
        except (ValueError, TypeError):
            # Si no puedo convertir a int, no crees el post
            return

    # 🔹 Eliminar (solo admin)
    async def eliminar_post(self, post_id: int):

        auth = await self.get_state(AuthState)

        if auth.user_role != "admin":
            return

        eliminar_post(post_id)
        await self.cargar_posts()

    # 🔹 Preparar edición
    def set_editando(self, post_id: int):

        post = next((p for p in self.posts if p.id == post_id), None)

        if not post:
            return

        self.editando_id = post_id
        self.titulo = post.titulo
        self.contenido = post.contenido
        self.categoria_id = str(post.categoria_id) if post.categoria_id else ""
        self.imagen_destacada = post.imagen_destacada or ""

    # 🔹 Actualizar post con control por autor
    async def actualizar_post(self):

        if not self.editando_id:
            return

        auth = await self.get_state(AuthState)

        post = obtener_post_por_id(self.editando_id)

        if not post:
            return

        # Si no es admin, solo puede editar si es autor
        if auth.user_role != "admin":
            if post.autor_id != auth.user_id:
                return

        actualizar_post(
            self.editando_id, 
            self.titulo, 
            self.contenido,
            imagen_destacada=self.imagen_destacada or None
        )

        self.titulo = ""
        self.contenido = ""
        self.categoria_id = ""
        self.imagen_destacada = ""
        self.editando_id = None

        await self.cargar_posts()

    async def toggle_publicado(self, post_id: int):

        toggle_publicado(post_id)
        await self.cargar_posts()

    # 🔹 MÉTODOS DE PAGINACIÓN
    def pagina_anterior(self):
        if self.page > 1:
            self.page -= 1

    def siguiente_pagina(self):
        total_paginas = (len(self.posts_filtrados) + self.posts_per_page - 1) // self.posts_per_page
        if self.page < total_paginas:
            self.page += 1

    def set_busqueda(self, value: str):
        self.busqueda = value
        self.page = 1

    def limpiar_busqueda(self):
        self.busqueda = ""
        self.page = 1

    @rx.var
    def posts_filtrados(self) -> List[Post]:
        texto = self.busqueda.strip().lower()

        if not texto:
            return self.posts

        return [
            post
            for post in self.posts
            if texto in post.titulo.lower() or texto in post.contenido.lower()
        ]

    # 🔹 PROPIEDADES CALCULADAS
    @rx.var
    def puede_ir_atras(self) -> bool:
        return self.page > 1

    @rx.var
    def puede_ir_adelante(self) -> bool:
        total_paginas = (len(self.posts_filtrados) + self.posts_per_page - 1) // self.posts_per_page
        return self.page < total_paginas

    @rx.var
    def posts_paginados(self) -> List[Post]:
        start = (self.page - 1) * self.posts_per_page
        end = start + self.posts_per_page
        return self.posts_filtrados[start:end]
