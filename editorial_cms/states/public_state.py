import reflex as rx
from typing import Optional, List, Dict, Any
from editorial_cms.models.post import Post
from editorial_cms.models.categoria_sidebar import CategoriaSidebar
from editorial_cms.services.post_service import obtener_recientes
from editorial_cms.models.post_public import PostPublic

from editorial_cms.services.post_service import (
    obtener_post_por_id,
    obtener_publicados,
    obtener_post_por_slug,
    obtener_posts_por_categoria_slug,
)

from editorial_cms.services.category_service import (
    obtener_categoria_por_slug,
    obtener_categorias_con_contador,
)

from editorial_cms.services.post_service import buscar_posts_por_titulo

from editorial_cms.services.post_service import buscar_posts
from editorial_cms.services.post_service import contar_posts
from urllib.parse import parse_qs, urlparse

class PublicState(rx.State):

    # 🔹 LISTADO GENERAL
    
    posts: List[PostPublic] = []

    # 🔹 DETALLE
    post_actual: Optional[Post] = None

    # 🔹 SIDEBAR TIPADO CORRECTAMENTE
    categorias_sidebar: List[CategoriaSidebar] = []

    # 🔹 FILTRADO POR CATEGORÍA
    posts_categoria: List[Post] = []
    nombre_categoria_actual: str = ""

    recientes: List[Post] = []
    # para buscar en bd por articulo
    busqueda: str = ""

    #estado para categoria activa
    
    categoria_activa: str = ""
    
    #paginacion
    page: int = 1
    per_page: int = 5

    total_posts: int = 0

    #propiedad computada para mostrar leyenda de resultado de busqueda
    @rx.var
    def mostrando_resultados(self)->bool:
        return bool(self.busqueda)
    
    #var para resaltar categoria activa
    @rx.var
    def hay_categoria_activa(self)->bool:
        return bool(self.categoria_activa)
    
     #VARIABLES COMPUTADAS 
    @rx.var
    def total_paginas(self) -> int:
        if self.total_posts == 0:
            return 1
        return (self.total_posts + self.per_page - 1) // self.per_page


    @rx.var
    def puede_ir_atras(self) -> bool:
        return self.page > 1


    @rx.var
    def puede_ir_adelante(self) -> bool:
        return self.page < self.total_paginas 
    
    # Construir url dinamicamente
    def construir_url(self):
            params = []

            if self.page > 1:
                params.append(f"page={self.page}")

            if self.busqueda:
                params.append(f"q={self.busqueda}")

            if self.categoria_activa:
                params.append(f"cat={self.categoria_activa}")

            if params:
                return "/articulos?" + "&".join(params)

            return "/articulos"
        


    # =========================
    # CARGAS
    # =========================
    async def cargar_recientes(self):
        self.recientes = obtener_recientes()

    async def cargar_publicados(self):
        posts_db = obtener_publicados()

        self.posts = [
            PostPublic(
                id=post.id,
                titulo=post.titulo,
                slug=post.slug,
                contenido=post.contenido,
                fecha_publicacion=post.fecha_publicacion.strftime("%d/%m/%Y"),
            )
            for post in posts_db
        ]

    async def cargar_categorias_sidebar(self):
        self.categorias_sidebar = obtener_categorias_con_contador()

    async def cargar_por_slug(self):
        slug = self.router.page.params.get("slug")

        if not slug:
            self.post_actual = None
            return

        self.post_actual = obtener_post_por_slug(slug)

    async def cargar_posts_por_categoria_slug(self):
        slug = self.router.page.params.get("slug")

        if not slug:
            self.posts_categoria = []
            self.nombre_categoria_actual = ""
            return

        categoria = obtener_categoria_por_slug(slug)

        if categoria:
            self.nombre_categoria_actual = categoria.nombre
            self.posts_categoria = obtener_posts_por_categoria_slug(slug)
        else:
            self.posts_categoria = []
            self.nombre_categoria_actual = ""

    # =========================
    # NAVEGACIÓN
    # =========================

    async def ver_post(self, post_id: int):
        try:
            post_id = int(post_id)
            self.post_actual = obtener_post_por_id(post_id)
            return rx.redirect("/articulo")
        except Exception:
            self.post_actual = None

    
    async def aplicar_filtros(self):

        self.total_posts = contar_posts(
            texto=self.busqueda,
            categoria_slug=self.categoria_activa,
        )

        posts_db = buscar_posts(
            texto=self.busqueda,
            categoria_slug=self.categoria_activa,
            page=self.page,
            per_page=self.per_page,
        )

        self.posts = [
            PostPublic(
                id=post.id,
                titulo=post.titulo,
                slug=post.slug,
                contenido=post.contenido,
                fecha_publicacion=post.fecha_publicacion.strftime("%d/%m/%Y"),
            )
            for post in posts_db
        ]

    
    async def set_busqueda(self, value: str):
        self.busqueda = value
        self.page = 1
        await self.aplicar_filtros()
        return rx.redirect(self.construir_url())
        

    async def set_categoria(self, slug: str):
        self.categoria_activa = slug
        self.page = 1
        await self.aplicar_filtros()
        return rx.redirect(self.construir_url())
        

    async def limpiar_busqueda(self):
        self.busqueda = ""
        self.page = 1
        await self.aplicar_filtros()
        return rx.redirect(self.construir_url())

    
    #METODO PARA CAMBIAR PAGINA
    async def siguiente_pagina(self):
        if self.page < self.total_paginas:
            self.page += 1
            await self.aplicar_filtros()
            return rx.redirect(self.construir_url())

    async def pagina_anterior(self):
        if self.page > 1:
            self.page -= 1
            await self.aplicar_filtros()
            return rx.redirect(self.construir_url())

    
    

    async def resetear_paginacion(self):

        url = self.router.url
        parsed = urlparse(url)
        query_dict = parse_qs(parsed.query)

        # PAGE
        try:
            self.page = int(query_dict.get("page", ["1"])[0])
        except:
            self.page = 1

        # BUSQUEDA
        self.busqueda = query_dict.get("q", [""])[0]

        # CATEGORIA
        self.categoria_activa = query_dict.get("cat", [""])[0]

        await self.aplicar_filtros()

        