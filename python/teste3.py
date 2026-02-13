print("HELLO\n"*10)


end1 = "J"
end2 = "A"
end3 = "Y"
end4 = "C"
end5 = "E"
end6 = " "
end7 = "E"
end8 = " "
end9 = "V"
end10 = "I"
end11 = "K"
end12 = "T"
end13 = "O"
end14 = "R"

print(end1 + end2 + end3 + end4 + end5, end=" ") #esse , end=" " faz com que nao exista um \n pra o prox print
print(end7 + " ") #aqui isso nao ocorre
print(end9 + end10 + end11 + end12 + end13 + end14 + ".")

print(end1 + end2 + end3 + end4 + end5, end=" ") 
print(end7, end=" ") #aqui sim
print(end9 + end10 + end11 + end12 + end13 + end14 + ".")