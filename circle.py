import cgitb, cgi
import math
import geo_funcs

# habilita a visualizacao de erros
cgitb.enable(display=0, logdir="./")

# instancia um form para receber dados do navegador
form = cgi.FieldStorage()

############ logica do script
# recebe o valor do raio do usuario
raio_ = float(form.getvalue('raio'))

# calcular area
area_circ = math.pi * R ** 2

############ HTML
title = "Círculo"
geo_funcs.print_header(title)
print("<h1>Círculo</h1><hr>")
print("<p>Raio: {:.1f}".format(raio_))
print("<p>Área do círculo: {:.1f}".format(area_circ))
print("<br><br>Clique <a href=\'../circulo.html\'>aqui</a> para novo cálculo.")
geo_funcs.print_footer()