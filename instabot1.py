from instabot import Bot

# Inicia sesión en Instagram
bot = Bot()
bot.login(username="TU_USUARIO", password="TU_CONTRASEÑA")

# Obtiene listas de seguidores y seguidos
seguidores = bot.get_user_followers("TU_USUARIO")
seguidos = bot.get_user_following("TU_USUARIO")

# Identifica cuentas que sigues pero no te siguen de vuelta
no_te_siguen = [user for user in seguidos if user not in seguidores]

# Opcional: mostrar nombres de usuario en lugar de IDs
no_te_siguen_nombres = [bot.get_username_from_user_id(user) for user in no_te_siguen]

print("Cuentas que sigues y no te siguen de vuelta:")
for nombre in no_te_siguen_nombres:
    print(nombre)
