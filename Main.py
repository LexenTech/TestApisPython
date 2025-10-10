
import Crud as c
import  ApisCrud




c.leer_usuarios('usuarios')


print("----- CREAR USUARIO -----")
"""
c.crear_usuario('usuarios',
               nombre="Juancho",
               apellido_p="Pérez",
               apellido_m="López",
               correo="Juancho.rojas@email.com",
               telefono="3312345678",
               rol_id=1,
               sucursal_id=2)

c.leer_usuarios('usuarios')
"""
print("----- Eliminar USUARIO -----")
#c.eliminar_usuario('usuarios')


tabla = "usuarios"


print("----- Actualizar USUARIO -----")
# Actualizar el correo del usuario con ID = 1
c.actualizar_campo(tabla, 1, "correo", "nuevo_correo@email.com")

# Actualizar el teléfono del usuario con ID = 2
c.actualizar_campo(tabla, 2, "telefono", "3398765432")
