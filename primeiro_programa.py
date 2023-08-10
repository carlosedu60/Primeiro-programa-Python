#tela de boas vindas
print("Hello World")
print("Seja bem vindo ao curso de Python")
print('')
print('xxxxxxxxxxxxxxxxxxxxxxx')
print('')

 
#Estruturas condicionais
MAIOR_IDADE = 18

idade = int(input("Informe sua idade: "))
    
if idade >= MAIOR_IDADE:
    print('Maior de idade, já pode tirar sua habilitação.')

if idade < MAIOR_IDADE:
    print('Menor de idade, Ainda não pode tirar sua habilitação.')
    
    
if idade >= MAIOR_IDADE:
    print('Já pode tirar sua habilitação.')
else:
    print('Ainda não pode tirar sua habilitação.')

