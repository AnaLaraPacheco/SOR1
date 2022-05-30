import cgitb, cgi
import geo_funcs

# habilita a visualizacao de erros
cgitb.enable(display=0, logdir="./")

# instancia um form para receber dados do navegador
form = cgi.FieldStorage()

############ logica do script
# recebe os valores do usuario
base_menor = float(form.getvalue('base menor(b)'))
base_maior = float(form.getvalue('base maior(B)'))
altura_ = float(form.getvalue('altura'))

# calcular area
area_tra = (base_maior + base_menor) * altura_ / 2

############ HTML
title = "Trapézio"
geo_funcs.print_header(title)
print("<h1>Trapézio</h1><hr>")
print("<p>Base menor(b): {:.1f}".format(base_menor))
print("<p>Base maior(B): {:.1f}".format(base_maior))
print("<p>Altura: {:.1f}".format(altura_))
print("<p>Área do trapézio: {:.1f}".format(area_tra))
print("<br><br>Clique <a href=\'../trapézio.html\'>aqui</a> para novo cálculo.")
geo_funcs.print_footer()
