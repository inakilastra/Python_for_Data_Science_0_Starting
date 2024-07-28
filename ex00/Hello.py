ft_list  = ["Hello", "tata!"]  # Lista
ft_tuple = ("Hello", "toto!")  # Tupla
ft_set   = {"Hello", "tutu!"}  # Conjunto
ft_dict  = {"Hello" : "titi!"} # Diccionario
#your code here
ft_list[1] = "World!"            # Modifico la lista
ft_tuple = ("Hello", "Bizkaia!") # No se puede modificar la tupla, creo una nueva tupla
ft_set.discard("tutu!")          # Elimino del conjunto
ft_set.add("Urduliz!")           # Agrego al conjunto
ft_dict["Hello"] = "42Urduliz!"  # Modifico la referencia "Hello" del diccionario

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
