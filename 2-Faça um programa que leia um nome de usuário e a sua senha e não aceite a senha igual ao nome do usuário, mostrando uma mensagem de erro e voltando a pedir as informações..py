2)
print("fa�a j� seu cadastro:")
usuario=str(input("usu�rio--> "))
senha=str(input("senha-->"))
while usuario==senha:
	print("ERRO: o usu�rio n�o pode ser igual a senha, tente novamente")
	usuario=str(input("usu�rio--> "))
	senha=str(input("senha-->"))
else:
	print("cadastrado efetuado com sucesso")
