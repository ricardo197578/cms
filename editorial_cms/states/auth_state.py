import reflex as rx
from editorial_cms.services.auth_service import autenticar_usuario
from editorial_cms.services.auth_service import obtener_rol_por_id


class AuthState(rx.State):
    username: str = ""
    password: str = ""

    usuario_logueado: dict | None = None
    user_role: str = ""
    error: str = ""

    class Config:
        persist = True  # 👈 esto activa persistencia del state completo

    def login(self):

        usuario = autenticar_usuario(self.username, self.password)

        if not usuario:
            self.error = "Credenciales incorrectas"
            return

        self.usuario_logueado = {
            "id": usuario.id,
            "username": usuario.username,
            "rol": usuario.rol
        }

        self.user_role = usuario.rol
        self.error = ""

        return rx.redirect("/admin/dashboard")

    def logout(self):
        self.usuario_logueado = None
        self.user_role = ""
        return rx.redirect("/admin/login")

    def check_auth(self):
        if not self.usuario_logueado:
            return rx.redirect("/admin/login")

        rol = self.rol_real

        if rol not in ["admin", "superadmin", "editor"]:
            return rx.redirect("/")

    @rx.var
    def username_actual(self) -> str:
        if self.usuario_logueado:
            return self.usuario_logueado.get("username", "")
        return ""

    @rx.var
    def user_id(self) -> int | None:
        if self.usuario_logueado:
            return self.usuario_logueado.get("id")
        return None
    
   

    @rx.var
    def rol_real(self) -> str:
        if not self.usuario_logueado:
            return ""
        user_id = self.usuario_logueado.get("id")
        return obtener_rol_por_id(user_id)