# !/usr/bin/env python3

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"

ft_tuple = ("Hello", "Bizkaia!")

ft_set.discard("tutu!")
ft_set.add("Urduliz!")

ft_dict["Hello"] = "42Urduliz!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)