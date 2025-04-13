# 2) Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

lista = ["Python", "Java", "C++", "JavaScript"]

print("lista completa: ", lista)

#usando remove do lists
lista.remove("C++")
lista.append("Ruby")
print("lista sem o C++: usando o remove", lista)


# usando o pop em um for
lista2 = ["Python", "Java", "C++", "JavaScript"]

print("lista completa: ", lista2)

for l in lista2:
  if l == 'C++':
    lista2.remove(l)

lista2.append("Ruby") 

print("lista sem o C++: usando o um for", lista2)