from flask import Flask, render_template

app = Flask('__name__', static_folder='static')

@app.route("/")
def Home():
    return render_template('/Home.html', titulo='Final Stage', activehome='active')


@app.route('/Cadastro')
def Cadastro():
    return render_template('/Login/Cadastro.html', titulo='Cadastro')
@app.route('/Login')
def Login():
    return render_template('/Login/Login.html', titulo='Login')
@app.route('/RecupSenha')
def RecupSenha():
    return render_template('/Login/RecupSenha.html', titulo='Recuperar Senha')
@app.route('/ConfirmRecupSenha')
def ConfirmRecupSenha():
    return render_template('/Login/ConfirmRecupSenha.html', titulo='Confirmar Recuperação de Senha')
@app.route('/CadastroNovaSenha')
def CadastroNovaSenha():
    return render_template('/Login/CadastroNovaSenha.html', titulo='Cadastrar Nova Senha')
@app.route('/ConfirmNovaSenha')
def ConfirmNovaSenha():
    return render_template('/Login/ConfirmNovaSenha.html', titulo='Confirmar Nova Senha')


@app.route('/Contato')
def Contato():
    return render_template('/Contato/Contato.html', titulo='Contato', activecontato='active')
@app.route('/ConfirmContato')
def ConfirmContato():
    return render_template('/Contato/confirmContato.html', titulo='Confirmar Contato')


@app.route('/QuemSomos')
def QuemSomos():
    return render_template('/quemSomos.html', titulo='Quem Somos', activesomos='active')


@app.route('/Carrinho')
def Carrinho():
    return render_template('/Carrinho/Carrinho.html', titulo='Sacola')


@app.route('/PoliticadePrivacidade')
def PoliticadePrivacidade():
    return render_template('/privacidade.html', titulo='Política de Privacidade')
@app.route('/TermosdeUso')
def TermosdeUso():
    return render_template('/termos.html', titulo='Termos de Uso')
@app.route('/TrocaseDevolucoes')
def TrocaseDevolucoes():
    return render_template('/trocas.html', titulo='Trocas e Devoluções')


@app.route('/RespawnRoyale')
def RespawnRoyale():
    return render_template('/Products/respawnRoyale.html', titulo='Respawn Royale')
@app.route('/epicVictory')
def epicVictory():
    return render_template('/Products/epicVictory.html', titulo='Epic Victory')
@app.route('/infiniteQuest')
def infiniteQuest():
    return render_template('/Products/infiniteQuest.html', titulo='Infinite Quest')
@app.route('/mysticOdyssey')
def mysticOdyssey():
    return render_template('/Products/mysticOdyssey.html', titulo='Mystic Odyssey')
@app.route('/cosmicAura')
def cosmicAura():
    return render_template('/Products/cosmicAura.html', titulo='Cosmic Aura')
@app.route('/enchantedDream')
def enchantedDream():
    return render_template('/Products/enchantedDream.html', titulo='Enchanted Dream')





if __name__ == '__main__':
    app.run(debug=True)