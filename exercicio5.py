
string_recebe = str(input("Digite uma string: "))

print(string_recebe[2])

tamanho_str = len(string_recebe)
str_new = ""
for i in string_recebe:
    str_new = str_new + string_recebe[tamanho_str-1]
    tamanho_str = tamanho_str - 1
print(str_new)
