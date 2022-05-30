import cgitb, cgi
import geo_funcs

# habilita a visualizacao de erros
cgitb.enable(display=0, logdir="./")

# instancia um form para receber dados do navegador
form = cgi.FieldStorage()

############ logica do script
# recebe o valor do raio do usuario
base_ = float(form.getvalue('base'))
altura_ = float(form.getvalue('altura'))

# calcular area
area_ret = base_ * altura_

############ HTML
title = "Retângulo"
geo_funcs.print_header(title)
print("<h1>Retângulo</h1><hr>")
print("<p>Base: {:.1f}".format(base_))
print("<p>Altura: {:.1f}".format(altura_))
print("<p>Área do retângulo: {:.1f}".format(area_ret))
print("<br><br>Clique <a href=\'../retangulo.html\'>aqui</a> para novo cálculo.")
geo_funcs.print_footer()
