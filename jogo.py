import turtle
import random

i=0               #contagem de quantas vezes os carros inimigos já apareceram
IniciarPausar = 0 #Se essa variável for 0, o jogo para, se for 1, o jogo inicia/continua
pontuacao = 0     #variável que controla a pontuação
quantidade = 60   #variável que controla a quantidade de Combustível
qtdAposColisao = 60

janela = turtle.Screen()                           #criação da janela
janela.bgcolor("gray")
janela.tracer(0)                                   #desligar a animação
janela.setup(900,700)

janela.addshape("imagens/carro_principal.gif")     #imagem do carro principal
janela.addshape("imagens/carro_roxo.gif")          #imagem do primeiro inimigo
janela.addshape("imagens/carro_rosa.gif")          #imagem do segundo inimigo
janela.addshape("imagens/combustivel.gif")         #imagem do combustível
janela.addshape("imagens/pista.gif")               #imagem da pista
janela.addshape("imagens/explosion.gif")           #imagem da explosão

pista = turtle.Turtle()                       #criação da pista 1
pista.shape("imagens/pista.gif")
pista.up()
pista.right(90)
pista.goto(0,400)

pista2 = turtle.Turtle()                       #criação da pista 2
pista2.shape("imagens/pista.gif")
pista2.up()
pista2.right(90)
pista2.goto(0,400)

carro = turtle.Turtle()                         #criação do carro
carro.up()
carro.shape("imagens/carro_principal.gif")
carro.goto(0,-240)

combustivel = turtle.Turtle()                   #criação do combustível
combustivel.up()
combustivel.shape("imagens/combustivel.gif")
combustivel.hideturtle()                   #para não aparecer no meio da tela no início

inimigo = turtle.Turtle()                       #criação do primeiro inimigo (carro roxo)
inimigo.up()
inimigo.shape("imagens/carro_roxo.gif")
inimigo.hideturtle()                       #para não aparecer no meio da tela no início

inimigo2 = turtle.Turtle()                      #criação do segundo inimigo (carro rosa)
inimigo2.up()
inimigo2.shape("imagens/carro_rosa.gif")
inimigo2.goto(10000,10000)                      #para não aparecer no meio da tela no início

explosao = turtle.Turtle()                      #criação da explosão
explosao.up()
explosao.shape("imagens/explosion.gif")
explosao.hideturtle()

pontos = turtle.Turtle()                        #criação do turtle dos pontos
pontos.up()
pontos.goto(260,280)
pontos.hideturtle()

pontosCombustivel = turtle.Turtle()            #criação do turtle da quantidade de combustível
pontosCombustivel.up()
pontosCombustivel.goto(260,260)
pontosCombustivel.hideturtle()

aperteEspaco = turtle.Turtle()
aperteEspaco.up()
aperteEspaco.goto(-210,100)
aperteEspaco.hideturtle()

def espaco():#quando apertar espaço, a variavel IniciarPausar atribui a 1 e os inimigos e os combustíveis se posicionam aleatoriamente
    global IniciarPausar
    IniciarPausar = 1
    carro.goto(0, -240)
    explosao.hideturtle()
    xCombustivel = random.randint(-200, 200)
    yCombustivel = random.randint(300, 301)
    combustivel.setposition(xCombustivel, yCombustivel)
    combustivel.showturtle()

    xInimigo = random.randint(-190,-40)
    yInimigo = random.randint(400, 460)
    inimigo.setposition(xInimigo, yInimigo)
    inimigo.showturtle()

    xInimigo2 = random.randint(40,190)
    yInimigo2 = random.randint(400,600)
    inimigo2.setposition(xInimigo2, yInimigo2)
    inimigo2.showturtle()

def direita():                       #O carro irá andar para "frente" - direita no caso
    carro.forward(20*IniciarPausar)
def esquerda():                      #O carro irá se mover para "trás" - esquerda no caso
    carro.backward(10*IniciarPausar)

def pistaDescer():  #coloquei 2 pistas para subirem para uma posição quando passar de -400 no eixo y
    pista.forward(5*IniciarPausar)  #pista desce de 5 em 5 pixels apenas quando IniciarPausar for 1
    if pista.ycor() <= -400:
        pista.goto(0,1000)

    pista2.forward(5*IniciarPausar) #pista 2 desce de 5 em 5 pixels apenas quando IniciarPausar for 1
    if pista2.ycor() <=-400:
        pista2.goto(0,900)

def combustivelDescer():
    y = combustivel.ycor()
    combustivel.sety((y - 7)*IniciarPausar)

def principal():
    global i
    y = inimigo.ycor()                #y é o ponto vertical do inimigo
    inimigo.sety((y - 7)*IniciarPausar)
    y2 = inimigo2.ycor()              #y2 é o ponto vertical do inimigo 2
    inimigo2.sety((y2 - 7)*IniciarPausar)
    if y <= -400:                     #se o inimigo sair totalmente da tela (passar de -400 do eixo y)
        y = random.randint(400,460)
        x = random.randint(-190,-25)
        inimigo.setposition(x,y)      #ele irá surgir dentro desses parâmetros de x e y
        i += 1                        #cada vez que os inimigos aparecem i soma + 1
        if i % 5 == 0:  #de 5 em cinco vezes que os inimigos aparecem, o combustível aparece
            yCombustivel = random.randint(500, 600)
            xCombustivel = random.randint(-200,200)
            combustivel.setposition(xCombustivel, yCombustivel)
            combustivelDescer()
    if y2 <= -400:                    #se o inimigo2 sair totalmente da tela (passar de -400 do eixo y)
        y2 = random.randint(400,600)
        x2 = random.randint(30,190)
        inimigo2.setposition(x2,y2)
    pistaDescer()
    pontuacaoAlcance()
    apertarEspaco()
    colisaoBorda()
    colisao()
    colisaoCombustivel()
    janela.update()
    janela.ontimer(principal,1000//60)
    janela.ontimer(combustivelDescer,1000//60)
    janela.ontimer(pistaDescer,1000//60)

def pontuacaoAlcance():   #A pontuação aumenta somando 0.25 quando o jogo esta rodando
    global pontuacao
    pontuacao +=0.25 *IniciarPausar
    if IniciarPausar == 0:
        pontuacao = 0
    pontos.clear()
    pontos.write(f"Pontuação: {pontuacao//1}", font=("Times New Roman", 15, "bold"))

def apertarEspaco():
    if IniciarPausar == 0:
        aperteEspaco.clear()
        aperteEspaco.write("Aperte espaço para iniciar!!!", font=("Century SchoolBook", 22, "bold"))
    else:
        aperteEspaco.clear()

def colisaoBorda():   #quando o carro bater na borda, ele explode e o jogo acaba
    global IniciarPausar
    global quantidade
    if carro.xcor() >= 200: #se o carro passar das bordas
        xCarro = carro.xcor()
        yCarro = carro.ycor()
        explosao.setposition(xCarro -10,yCarro)
        carro.setposition(xCarro-10, yCarro)
        explosao.showturtle()
        IniciarPausar = 0
        quantidade -= 10
    if carro.xcor() <= -200:
        xCarro = carro.xcor()
        yCarro = carro.ycor()
        explosao.setposition(xCarro + 10, yCarro)
        carro.setposition(xCarro + 10, yCarro)
        explosao.showturtle()
        IniciarPausar = 0
        quantidade -= 10

def colisao():     #quando o carro bate em outro, ele explode e o jogo acaba
    global IniciarPausar
    global quantidade
    dxPrimeiro = inimigo.xcor() - carro.xcor()   #diminuindo o x do inimigo 1 com o do carro
    dyPrimeiro = inimigo.ycor() - carro.ycor()   #diminuindo o y do inimigo 1 com o do carro
    if dxPrimeiro<=70 and dxPrimeiro>=-70 and dyPrimeiro<=128 and dyPrimeiro>=-128:
        xCarro = carro.xcor()
        yCarro = carro.ycor()
        explosao.setposition(xCarro, yCarro)
        explosao.showturtle()
        IniciarPausar = 0
        quantidade -= 10
    dxSegundo = inimigo2.xcor() - carro.xcor()   #diminuindo o x do inimigo 2 com o do carro
    dySegundo = inimigo2.ycor() - carro.ycor()   #diminuindo o y do inimigo 2 com o do carro
    if dxSegundo<=70 and dxSegundo>=-70 and dySegundo<=128 and dySegundo>=-128:
        xCarro = carro.xcor()
        yCarro = carro.ycor()
        explosao.setposition(xCarro, yCarro)
        explosao.showturtle()
        IniciarPausar = 0
        quantidade -= 10

def colisaoCombustivel():
    global quantidade
    global IniciarPausar
    global qtdAposColisao
    quantidade -= 0.03125 * IniciarPausar #a quantidade de combustivel vai diminuindo de 0,0625
    pontosCombustivel.clear()
    pontosCombustivel.write(f"Combustível: {quantidade // 1}", font=("Times New Roman", 15, "bold"))
    if quantidade <= 0:      #se a quantidade de combustível chegar a zero, o jogo para
        IniciarPausar = 0
        quantidade = qtdAposColisao
    dxC = combustivel.xcor() - carro.xcor()  #diminuindo o x do combustível com o do carro
    dyC = combustivel.ycor() - carro.ycor()  #diminuindo o y do combustível com o do carro
    if dxC<=50 and dxC>=-50 and dyC<=100 and dyC>=-100:
        combustivel.setposition(0,-600)
        quantidade +=15

janela.listen()
janela.onkeypress(direita, "Right")
janela.onkeypress(esquerda, "Left")
janela.onkeypress(espaco, "space")
principal()

janela.mainloop() #fazer com que a janela continue aberta