html_code = '''
<!DOCTYPE html>
<html lang="es">
...
</html>
'''

# Extraer el contenido CSS dentro de las etiquetas <style>
start_tag = '<style>'
end_tag = '</style>'
start_index = html_code.find(start_tag) + len(start_tag)
end_index = html_code.find(end_tag)
css_content = html_code[start_index:end_index].strip()

# Crear un nuevo archivo CSS externo
file_name = 'styles.css'
with open(file_name, 'w') as css_file:
    css_file.write(css_content)

print(f"Archivo {file_name} generado exitosamente.")
