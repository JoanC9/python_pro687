from discord.ext import commands
import discord 
#ctrl + ñ -> pip install y la primera palabra que esta importando 
#ctrl + shift + p -> python: select -> elegir otra version de discord

#los permisos por defecto del bot
intents = discord.Intents.default()
intents.message_content = True #es para darle permiso de que lea los mensajes

#cada vez que alguien quiera hablar con mi bot debe escribir primero el prefijo -> '$'
#intents = intents / los permisos del bot seran estos, son los que definimos en linea 7 y 8
bot  =  commands.Bot(command_prefix='$', intents=intents)

#event es algo que si o si va a pasar -> este ejecutandose imprime lo que tiene la funcion
@bot.event
async def listo(): #async = asincronico / en el momento -> porque es como decirle dame tiempo
                    #ya te doy la respuesto

    print(f'Mi bot {bot.user} esta nitidooo')

# $python -> para que funcione
@bot.command() #decorador que indica que la funcion de abajo sera un comando de discord
async def python(ctx): #lo que escriba el usuario se recibe como ctx = paquete o caja

    #await = esperame ya te ando enviando la respuesta / ctx = devolvemos la caja/ send = caja
    await ctx.send('Que mas panita')

#$saludo holacomoestas -> para que funcione
@bot.command() #, * = no importa la longitud del mensaje del usuario tu vas a recibir todo
async def saludo(ctx, *, mensaje:str):# -> que lo que envie el usuario lo vamos a tratar como un str

    #tratamiento del mensaje que envia el usuario .lower = todo lo pasamos a minuscula
    # strip = quitamos todos los espacios en blanco y unimos todo en una linea sin espacios
    mensaje = mensaje.lower().strip()

    if 'holacomoestas' in mensaje:

        await ctx.send('Todo bien vos')

    elif 'holapoawebonadocomotai' in mensaje:

        await ctx.send('muy bien')

    else:

        await ctx.send('Te me cuidas')

token = ''

bot.run(token)



