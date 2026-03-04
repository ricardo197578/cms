import reflex as rx
from editorial_cms.services.auth_service import autenticar_usuario


class AuthState(rx.State):
    username: str = ""
    password: str = ""

    usuario_logueado: dict | None = None
    error: str = ""
    user_id: int = 0   # 👈 agregar esto
    user_role: str = ""   # 👈 AGREGA ESTA LÍNEA
    
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
        self.user_id = usuario.id   # 👈 guardar el id REAL
        return rx.redirect("/admin/dashboard")

    def logout(self):
        self.usuario_logueado = None
        return rx.redirect("/admin/login")

    def check_auth(self):
        # Protección de página
        if not self.usuario_logueado:
            return rx.redirect("/admin/login")

    # Variable reactiva segura
    @rx.var
    def username_actual(self) -> str:
        if self.usuario_logueado:
            return self.usuario_logueado.get("username", "")
        return ""