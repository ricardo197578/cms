import reflex as rx
from typing import List
from editorial_cms.services.usuario_service import (
    listar_usuarios,
    crear_usuario,
    eliminar_usuario,
    cambiar_estado
)
from editorial_cms.models.usuario import Usuario


class UsuarioState(rx.State):

    usuarios: List[Usuario] = []

    username: str = ""
    email: str = ""
    password: str = ""
    rol: str = "autor"

    async def cargar_usuarios(self):
        self.usuarios = listar_usuarios()

    async def crear(self):
        crear_usuario(
            self.username,
            self.email,
            self.password,
            self.rol
        )
        await self.cargar_usuarios()

    async def eliminar(self, user_id: int):
        eliminar_usuario(user_id)
        await self.cargar_usuarios()

    async def toggle_activo(self, user_id: int, estado: bool):
        cambiar_estado(user_id, estado)
        await self.cargar_usuarios()