import sys

with open(sys.argv[1], "r") as f:
    data = f.readlines()

# exclude all lines that do not start with "|"
data = [line for line in data if line.startswith("|")]


def start_table():
    return "<table id='example' class='display'>\n<tbody>"


def add_header(line):
    especie, extrato, tempo_produtivo, sucessao, porte = line.split("|")[1:6]
    return f"<thead><tr>,<th>{especie}</th>,<th>{extrato}</th>,<th>{tempo_produtivo}</th>,<th>{sucessao}</th>,<th>{porte}</th></tr></thead>"


def start_body():
    return "<tbody>"


def translate_line(line):
    especie, extrato, tempo_produtivo, sucessao, porte = line.split("|")[1:6]
    return f"<tr><td>{especie}</td>,<td>{extrato}</td>,<td>{tempo_produtivo}</td>,<td>{sucessao}</td>,<td>{porte}</td></tr>"


def end_body():
    return "</tbody>"


def initialize_data_tables():
    return "<!-- Script para inicializar DataTables --><script>$(document).ready(function() {$('#example').DataTable();});</script>"


def end_table():
    return "</table>"


final_html = start_table()
final_html += add_header(data[0])
for line in data[2:]:
    final_html += translate_line(line)
final_html += end_body()
final_html += initialize_data_tables()
final_html += end_table()

print(final_html)
