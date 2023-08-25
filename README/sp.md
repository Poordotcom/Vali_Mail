# ValiMail - Biblioteca de Verificación de Correo Electrónico

ValiMail es una biblioteca diseñada para la verificación avanzada y efectiva de direcciones de correo electrónico.

## Características

- Verifica el formato y la validez de las direcciones de correo electrónico.
- Detecta si una dirección de correo electrónico existe en una base de datos filtrada.
- Soporta la verificación del dominio del correo electrónico.
- Soporta la comparación del correo electrónico con una lista negra.
- Integración con proveedores de servicios de correo electrónico populares.

## Instalación

Puedes instalar la biblioteca usando el siguiente comando:

```bash
pip install ValiMail


################################
#         Cómo Usar            #
################################

# Importa la biblioteca

from ValiMail import vali_mail, check_domain_name, check_if_known,is_dispose_email


# Usa las funciones de la biblioteca para verificar direcciones de correo electrónico

email = "example@email.com"
is_valid = vali_mail(email)
is_in_database = check_if_known(email)
is_valid_domain = check_domain_name(email)
is_dispose = is_dispose_email(email)

# Imprime los resultados

print(f"Is valid email: {is_valid}")
print(f"Is in database: {is_in_database}")
print(f"Has valid domain: {is_valid_domain}")
print(f"Is blacklisted: {is_dispose}")

#Se me agregaron los ejemplos en tiempo real en el archivo example.py
