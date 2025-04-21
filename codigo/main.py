# IGNORE A BAGUNÇA

import discord
from discord.ext import commands, tasks
from discord import Embed, app_commands
import random
import datetime

intents = discord.Intents.all() #permissões
bot = commands.Bot(">", intents=intents)

VIDEOS = {
    "bomba": "./videos/oia as bomba.mp4",
    "100 reais": "./videos/100 reaais.mp4",
    "farm de buce-": "./videos/farm de buce-.mp4",
    "é mafia": "./videos/é mafia.mp4",
    "angu": "./videos/anguuu.mp4",
    "bom dia": "./videos/bom dia.mp4",
}

@bot.event
async def on_ready(): #evento que dispara quando o bot é inicializado
    mensagem_programada.start()
    sync = await bot.tree.sync() #sincroniza meus comandos de barra
    print(f"{len(sync)} comandos sincronizados")
    print(f"o {bot.user} ta on")


@bot.event
async def on_member_join(membro:discord.Member):
    canal = bot.get_channel(1363989205369356288)
    await canal.send(f"muito bom dia, {membro.mention}. todo  membro novo deve mandar 1000 v-bucks ao proprietário.")


#faz uma interface bonitinha usando o embed, não ficou tão organizado quanto eu queria, mas serve 🥸
@bot.tree.command(name="help", description="nem deus sabe o que ta acontecendo aqui 💩")
async def help(interaction:discord.interactions):
    embed = discord.Embed(
        title="ola galerinha, TALVEZ isso ajude",
        description="tem uns comando que da pra fazer aqui em baixo 👇",
        color=discord.Color.blurple()
    )
    embed.add_field(name="/fatos", value="mostra uns fatos, obvo")
    embed.add_field(name="/videos", value="da pra ver uns videozin funny")

    await interaction.response.send_message(embed=embed)


#usa a função choice do  app_commands pra escolher um fato aleatório dentro da lista 
@bot.tree.command(name="fatos", description="fatos.exe") 
async def fatos(interaction:discord.Interaction):
    respostas = ["O Bot-bom-dia é uma inegavel falha de criação...",
                 "Ser arrogante é como ser um elefante na africa, se alguem te der um tiro de bazuca você MORRE, amém 🙏",
                 "O brasil ta uma merda, ponto.",
                 "Eu não sei programar 👌",
                 ]
    await interaction.response.send_message(random.choice(respostas))


#mais uma vez usa o app_commands, agr ele coloca opções dentro do meu comando de barra
#e da um valor pra ele, quando seleciono uma opção, o codigo compara o valor com os nomes
#dos videos na minha lista     
@bot.tree.command(name="videos", description="Escolha um video, nengue")
@app_commands.choices(
    video=[
        app_commands.Choice(name="Bombas", value="bomba"),
        app_commands.Choice(name="Me empresta 100 reais?", value="100 reais"),
        app_commands.Choice(name="Farm de buce-", value="farm de buce-"),
        app_commands.Choice(name="É mafia", value="é mafia"),
        app_commands.Choice(name="Anguuu", value="angu"),
    ]
)
async def videos(interaction:discord.Interaction, video:app_commands.Choice[str]):
    caminho = VIDEOS.get(video.value)
    with open(caminho, "rb") as videos_maneiros:
        await interaction.response.send_message(file=discord.File(videos_maneiros))


#loopa um timer de 60 segundos até que os horários sejam condizentes, quando isso ocorre
#solta minha mensagem programada
@tasks.loop(seconds=60)
async def mensagem_programada():
    agora = datetime.datetime.now()

    if agora.hour==9 and agora.minute==0:    
        canal = bot.get_channel(1363999275977146479)
        caminho = VIDEOS.get("bom dia")
        mensagem = "BOM DIAAAAA (isso claramente não é um ataque ao bot bom-dia, ponto.)"

        with open(caminho, "rb") as video:
            await canal.send(content=mensagem, file=discord.File(video))


@bot.command()
async def ola(ctx: commands.Context):
    await ctx.send("saudações, perdedor")

bot.run("confidencial 🕵️")
