# IGNORE A BAGUNÇA

import discord
from discord.ext import commands, tasks
from discord import Embed, app_commands
import random
import asyncio
import datetime

intents = discord.Intents.all() #permissões
bot = commands.Bot(">", intents=intents)

roleta_jogo = {}

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


#devia ser crime usar programação pra fazer essa cagada aqui kkkkkkkkkkkkkkkkk
@bot.tree.command(name="ruby-chaan", description="me arrependo profundamente disso")
async def aiscream(interaction: discord.Interaction):
    await interaction.response.send_message("Ruby-chaaan! ^_^")
    await asyncio.sleep(1)
    await interaction.edit_original_response(content="Ruby-chaaan! ^_^ \nHaaaaayyy ヾ(≧▽≦\\*)o ")
    await asyncio.sleep(1.5)
    await interaction.edit_original_response(content="Ruby-chaaan! ^_^ \nHaaaaayyy ヾ(≧▽≦\\*)o \nNani ga sukii?? ")
    await asyncio.sleep(1.5)
    await interaction.edit_original_response(content="Ruby-chaaan! ^_^ \nHaaaaayyy ヾ(≧▽≦\\*)o \nNani ga sukii?? \nChocomin to! yori mo a-na-ta (\\*/ω＼*) ")
    await asyncio.sleep(0.5)
    await interaction.edit_original_response(content="Ruby-chaaan! ^_^ \nHaaaaayyy ヾ(≧▽≦\\*)o \nNani ga sukii?? \nChocomin to! yori mo a-na-ta (\\*/ω＼*) \n ")
    await asyncio.sleep(2)
    await interaction.edit_original_response(content="Ruby-chaaan! ^_^ \nHaaaaayyy ヾ(≧▽≦\\*)o \nNani ga sukii?? \nChocomin to! yori mo a-na-ta (\\*/ω＼*) \n \nAyumu-chaan! ^_^")
    await asyncio.sleep(1)
    await interaction.edit_original_response(content="Ruby-chaaan! ^_^ \nHaaaaayyy ヾ(≧▽≦\\*)o \nNani ga sukii?? \nChocomin to! yori mo a-na-ta (\\*/ω＼*) \n "
                                            "\nAyumu-chaan! ^_^ \nHaaaaaay (\\*^▽^\\*)")
    await asyncio.sleep(1.5)    
    await interaction.edit_original_response(content="Ruby-chaaan! ^_^ \nHaaaaayyy ヾ(≧▽≦\\*)o \nNani ga sukii?? \nChocomin to! yori mo a-na-ta (\\*/ω＼*) \n "
                                            "\nAyumu-chaan! ^_^ \nHaaaaaay (\\*^▽^\\*) \nNani ga sukiii?")
    await asyncio.sleep(1.5)    
    await interaction.edit_original_response(content="Ruby-chaaan! ^_^ \nHaaaaayyy ヾ(≧▽≦\\*)o \nNani ga sukii?? \nChocomin to! yori mo a-na-ta (\\*/ω＼*) \n "
                                            "\nAyumu-chaan! ^_^ \nHaaaaaay (\\*^▽^\\*) \nNani ga sukiii? \nSutoroberi fureivo! yori  mo  a-na-ta (✿◡‿◡)")
    

@bot.event
async def on_message(msg:discord.Message):
    if msg.author == bot.user:
        return
    
    if msg.content.lower() == "ruby chan!":
        aiscream = await msg.reply(content="Haaaaayyy ヾ(≧▽≦\\*)o ")
        await asyncio.sleep(1.5)
        await aiscream.edit(content="Haaaaayyy ヾ(≧▽≦\\*)o \nNani ga sukii?? ")
        await asyncio.sleep(1.5)
        await aiscream.edit(content="Haaaaayyy ヾ(≧▽≦\\*)o \nNani ga sukii?? \nChocomin to! yori mo a-na-ta (\\*/ω＼*) ")
        await asyncio.sleep(0.5)
        await aiscream.edit(content="Haaaaayyy ヾ(≧▽≦\\*)o \nNani ga sukii?? \nChocomin to! yori mo a-na-ta (\\*/ω＼*) \n ")
        await asyncio.sleep(2)
        await aiscream.edit(content="Haaaaayyy ヾ(≧▽≦\\*)o \nNani ga sukii?? \nChocomin to! yori mo a-na-ta (\\*/ω＼*) \n \nAyumu-chaan! ^_^")
        await asyncio.sleep(1)
        await aiscream.edit(content="Haaaaayyy ヾ(≧▽≦\\*)o \nNani ga sukii?? \nChocomin to! yori mo a-na-ta (\\*/ω＼*) \n "
                                                "\nAyumu-chaan! ^_^ \nHaaaaaay (\\*^▽^\\*)")
        await asyncio.sleep(1.5)    
        await aiscream.edit(content="Haaaaayyy ヾ(≧▽≦\\*)o \nNani ga sukii?? \nChocomin to! yori mo a-na-ta (\\*/ω＼*) \n "
                                                "\nAyumu-chaan! ^_^ \nHaaaaaay (\\*^▽^\\*) \nNani ga sukiii?")
        await asyncio.sleep(1.5)    
        await aiscream.edit(content="Haaaaayyy ヾ(≧▽≦\\*)o \nNani ga sukii?? \nChocomin to! yori mo a-na-ta (\\*/ω＼*) \n "
                                                "\nAyumu-chaan! ^_^ \nHaaaaaay (\\*^▽^\\*) \nNani ga sukiii? \nSutoroberi fureivo! yori  mo  a-na-ta (✿◡‿◡)")



#mini game de roleta russa altamente perigoso
@bot.tree.command(name="roleta_russa", description="muahahahah")
async def roleta_russa(interaction:discord.Interaction):
    embed = discord.Embed(
        title="Roleta Russa 🔫🐀",
        description="reaja com o emoji para participar",
        color=discord.Color.blurple()
    )
    await interaction.response.send_message(embed=embed)
    msg = await interaction.original_response()

    await msg.add_reaction("🔫")

    await asyncio.sleep(7)

    msg = await interaction.channel.fetch_message(msg.id) #pega a mensagem apos todas as atualizações

    #estou ficando louco, ponto.
    #lista os usuarios que reagiram a mensagem
    reaction = discord.utils.get(msg.reactions, emoji="🔫")
    players = []
    async for user in reaction.users():
        if not user.bot:
            players.append(user) 
    
    if not players:
        return await interaction.followup.send("seus cabeça de prego, me chamam pra nada é?")
    
    nomes = "\n".join(user.display_name for user in players)
    await interaction.followup.send(f"Aqui a lista dos pobres coitados:\n{nomes}")

    await asyncio.sleep(3)
    await interaction.channel.send("a bala ta no pente ☠️")

    await asyncio.sleep(3)
    
    #nesse bloco, gero um numero aleatorio pra ser a bala, e salvo tanto a bala, qnt os players que que reagiram, na variavel roleta_jogos
    #e uma lista de numeros disponiveis pra dar rolls. alem de uma nova "variavel", que vai armazenar a informação de se o player ja jogou
    #ou não, e tbm uma variavel pra dizer se o jogo esta rodando, como default começa com True
    bala = random.randint(1, 6)
    numeros_disponiveis = [1, 2 ,3 , 4 , 5, 6]
    
    #djabo dos inferno
    roleta_jogo[interaction.channel.id] = {
    'players': players,
    'bala': bala,
    'numeros_disponiveis': numeros_disponiveis,
    'ja_jogou': [],
    'ativo': True
}

    await interaction.channel.send("que começem os jogos 👿")
    await asyncio.sleep(2)
    await interaction.channel.send("podem dar rolls")

#comando novo de rolls, porem, só vai funcionar se o mini game estiver rolando
@bot.tree.command(name="rolls", description="rolas")
async def rolls(interaction:discord.Interaction):
    jogo = roleta_jogo.get(interaction.channel.id)

    #o ephemeral só faz com que o autor da interação receba a mensagem
    if not jogo or not jogo['ativo']:
        return await interaction.response.send_message("não tem nenhum jogo rolando", ephemeral=True)
        
    if interaction.user not in jogo["players"]:
        return await interaction.response.send_message("sai daqui vaicilão, ta nem jogando", ephemeral=True)
        
    if interaction.user in jogo['ja_jogou']:
        return await interaction.response.send_message("te acalma, precoce", ephemeral=True)
        
    if not jogo['numeros_disponiveis']:
        return await interaction.response.send_message("todos se safaram, o sossego esta restaurado", ephemeral=True)
        
    numero_player = random.choice(jogo['numeros_disponiveis'])
    jogo['numeros_disponiveis'].remove(numero_player) #remove o numero que ja foi sorteado, diminuindo a qnt de bala, aumentando a chance do prox se lasca
    jogo['ja_jogou'].append(interaction.user) # aplica o estado "ja jogou", ao autor da interação, assim ele n pode jogar dnv 
        
    await interaction.channel.send("roda a roleeeta, maria")
    await asyncio.sleep(2)
    await interaction.channel.send(f"{interaction.user.display_name} será vc atingido pela bala??!!")
    
    await asyncio.sleep(3)
    if numero_player == jogo['bala']:
        await interaction.channel.send("se fudeu kkkkkkkk, toma esse ban 😂")
        await interaction.guild.kick(interaction.user, reason="os guri cobraram")

        jogo['ativo'] = False
    else:
        await interaction.channel.send(f"sobreviveste, {interaction.user.display_name}. agradeça ao criador 🙏")

    await asyncio.sleep(1)
    #se todo mundo que estava inscrito ja jogou, mas sobraram chances, inclusive a bala, o jogo acaba
    if len(jogo['ja_jogou']) == len(jogo['players']) and jogo['numeros_disponiveis']:
        jogo['ativo'] = False
        return await interaction.channel.send("todos já jogaram, e ninguem morreu 😢, que inconveniente... \nentão cabo o jogo, ponto.")

    
    
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

bot.run("nada aqui")
