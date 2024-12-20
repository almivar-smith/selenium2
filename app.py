from flask import Flask, request, render_template_string
import bleach  # Importar bleach para limpiar el HTML

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    # Inicializat variables
    result = ""
    error_message = ""
    number1 = ""
    number2 = ""
    
    if request.method == "POST":
        # Obtenir valors del formulario
        number1 = request.form.get("number1", "")
        number2 = request.form.get("number2", "")
        
        # Validació si los campos están buits 
        if not number1 or not number2:
            error_message = "¡Els 2 camps són obligatoris!"  # Minsatge d'error si, hi ha campss buits
        else:
            # Intentar convertir els valors a flot (decimal)
            try:
                number1 = float(number1)
                number2 = float(number2)
                # Realitzar la suma, si tot és válid
                result = number1 + number2
            except ValueError:
                # Si no son números válids, mostrar un error amb salto de línea
                error_message = "¡Si us plau! <br>només números válids!<br>Gràcies"
         
        # Sanitizar el missatje d'error para permetre només etiquetes HTML seguras (por ejemplo, <br>)
        error_message = bleach.clean(error_message, tags=['br'], strip=True)
    
    # HTML simple con los resultados
    return render_template_string("""
        <html>
            <head>
                <style>rom flask import Flask, request, render_template_string
import bleach  # Importar bleach para limpiar el HTML

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    # Inicializat variables
    result = ""
    error_message = ""
    number1 = ""
    number2 = ""
    
    if request.method == "POST":
        # Obtenir valors del formulario
        number1 = request.form.get("number1", "")
        number2 = request.form.get("number2", "")
        
        # Validació si los campos están buits 
        if not number1 or not number2:
            error_message = "¡Els 2 camps són obligatoris!"  # Minsatge d'error si, hi ha campss buits
        else:
            # Intentar convertir els valors a flot (decimal)
            try:
                number1 = float(number1)
                number2 = float(number2)
                # Realitzar la suma, si tot és válid
                result = number1 + number2
            except ValueError:
                # Si no son números válids, mostrar un error amb salto de línea
                error_message = "¡Si us plau! <br>només números válids!<br>Gràcies"
         
        # Sanitizar el missat
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f9;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                    }
                    .container {
                        text-align: center;
                        background-color: #fff;
                        padding: 30px;
                        border-radius: 10px;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                        width: 300px;
                    }
                    h2 {
                        margin-bottom: 20px;
                        color: #333;
                    }
                    input[type="text"] {
                        padding: 10px;
                        width: 80%;
                        margin: 10px 0;
                        font-size: 16px;
                        border: 1px solid #ccc;
                        border-radius: 5px;
                        text-align: center;
                    }
                    input[type="submit"] {
                        padding: 12px 20px;
                        font-size: 16px;
                        background-color: #4CAF50;
                        color: white;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        width: 80%;
                        margin-top: 10px;
                    }
                    input[type="submit"]:hover {
                        background-color: #45a049;
                    }
                    .result, .error {
                        margin-top: 20px;
                        font-size: 18px;
                    }
                    .error {
                        color: red;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h2>Calculadora de Suma</h2>
                    <form method="post">
                        <input type="text" id="number1" name="number1" placeholder="Número 1" value="{{ number1 }}"><br>
                        <input type="text" id="number2" name="number2" placeholder="Número 2" value="{{ number2 }}"><br>
                        <input type="submit" value="Calcular Suma"><br>
                    </form>
                    
                    {% if result %}
                        <div class="result">
                            <h3>Resultat: {{ result }}</h3>
                        </div>
                    {% endif %}
                    
                    {% if error_message %}
                        <div class="error">
                            <!-- Usamos 'safe' para permitir que el HTML (como <br>) se renderice correctamente -->
                            <h3>{{ error_message|safe }}</h3>
                        </div>
                    {% endif %}
                </div>
            </body>
        </html>
    """, result=result, error_message=error_message, number1=number1, number2=number2)

if __name__ == "__main__":
    app.run(debug=True)
