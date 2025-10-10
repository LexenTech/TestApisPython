
import Credentials as cr

print("¡Conexión a Supabase exitosa!")


def leer_usuarios(tablename):
    # Leer todos los usuarios
    response = cr.supabase.table(f"{tablename}").select("*").execute()

    # Mostrar los resultados
    if response.data:
        for usuario in response.data:
            print(usuario)
    else:
        print("No se encontraron usuarios en la tabla.")

def crear_usuario(tablename, nombre, apellido_p, apellido_m, correo, telefono, rol_id, sucursal_id):
    response = cr.supabase.table(tablename).insert({
        "nombre": nombre,
        "apellidopaterno": apellido_p,
        "apellidomaterno": apellido_m,
        "correo": correo,
        "telefono": telefono,
        "passwordhash": "xxxxxcv",
        "rolid": rol_id,
        "sucursalid": sucursal_id
    }).execute()
    print("Usuario creado:", response.data)


def eliminar_usuario(tablename):
    # Leer usuarios primero
    print("----- LISTA DE USUARIOS -----")
    leer_usuarios(tablename)

    # Pedir ID a eliminar
    try:
        usuario_id = int(input("Ingresa el ID del usuario que deseas eliminar: "))
    except ValueError:
        print("Error: Debes ingresar un número válido.")
        return

    # Confirmar eliminación
    confirmar = input(f"¿Estás seguro de eliminar al usuario con ID {usuario_id}? (s/n): ").lower()
    if confirmar == 's':
        response = cr.supabase.table(tablename).delete().eq("id", usuario_id).execute()
        print("Usuario eliminado:", response.data)
    else:
        print("Eliminación cancelada.")

    # Mostrar usuarios después de la acción
    print("----- USUARIOS ACTUALIZADOS -----")
    leer_usuarios(tablename)

def actualizar_campo(tablename, usuario_id, columna, nuevo_valor):
    """
    Actualiza cualquier columna de un usuario en la tabla especificada.

    :param tablename: nombre de la tabla
    :param usuario_id: ID del registro a actualizar
    :param columna: nombre de la columna a modificar
    :param nuevo_valor: nuevo valor que se asignará
    """
    # Construir diccionario dinámico
    datos_actualizar = {columna: nuevo_valor}

    # Ejecutar actualización
    response = cr.supabase.table(tablename).update(datos_actualizar).eq("id", usuario_id).execute()

    if response.data:
        print(f"Registro actualizado correctamente: {response.data}")
    else:
        print("No se encontró el registro o no se pudo actualizar.")
