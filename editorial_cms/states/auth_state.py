import reflex as rx
from editorial_cms.services.auth_service import autenticar_usuario


class AuthState(rx.State):
    username: str = ""
    password: str = ""

    usuario_logueado: dict | None = None
    error: str = ""
    user_role: str = ""

    def login(self):
        usuario = autenticar_usuario(self.username, self.password)

        if not usuario:
            self.error = "Credenciales incorrectas"
            return

        # Guardar sesión
        self.usuario_logueado = {
            "id": usuario.id,
            "username": usuario.username,
            "rol": usuario.rol,
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

    # Variable reactiva segura
    @rx.var
    def username_actual(self) -> str:
        if self.usuario_logueado:
            return self.usuario_logueado.get("username", "")
        return ""

    # Obtener ID real desde sesión
    @rx.var
    def user_id(self) -> int | None:
        if self.usuario_logueado:
            return self.usuario_logueado.get("id")
        return None