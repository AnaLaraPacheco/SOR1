import cgitb, cgi
import geo_funcs

# habilita a visualizacao de erros
cgitb.enable(display=0, logdir="./")

# instancia um form para receber dados do navegador
form = cgi.FieldStorage()

############ logica do script
# recebe o valor do lado do usuario
lado_ = float(form.getvalue('lado'))

# calcular area
area_quadrado = L ** 2

############ HTML
title = "Quadrado"
geo_funcs.print_header(title)
print("<h1>Quadrado</h1><hr>")
print("<p>Lado: {:.1f}".format(lado_))
print("<p>Área do quadrado: {:.1f}".format(area_quadrado))
print("<br><br>Clique <a href=\'../quadrado.html\'>aqui</a> para novo cálculo.")
geo_funcs.print_footer()