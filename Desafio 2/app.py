from flask import Flask, render_template

app = Flask("__name__")

@app.route('/')
def Home():
    return render_template('/home.html', titulo='Home', previous='', next='Contato')

@app.route('/Contato')
def Contato():
    return render_template('/contato.html', titulo='Home', previous='', next='Quem_Somos')

@app.route('/Quem_Somos')
def Quem_Somos():
    return render_template('/quem_somos.html', titulo='Home', previous='Contato', next='Quem_Somos')

if __name__ == '__main__':
    app.run(debug=True)
