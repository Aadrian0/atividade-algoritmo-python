popula��oA=float(input("informe a popula��o da cidade A "))
popula��oB=float(input("informe a popula��o da cidade B "))
ano=0
taxa_crescimentoA=float(input("informe a taxa de crescimento da popula��o da cidade A "))
taxa_crescimentoB=float(input("informe a taxa de crescimento da popula��o da cidade B "))
while popula��oA < popula��oB:
	popula��oA+=round((popula��oA*taxa_crescimentoA)/100)
	popula��oB+=round((popula��oB*taxa_crescimentoB)/100)
	ano=ano+1

print("levar�",ano,"anos para popula��o da cidade A ser maior que a cidade B")
print("popula��oB-->",popula��oB,"habitantes")
print("popula��oA-->", popula��oA,"habitantes")