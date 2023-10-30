# Exercício Python 25: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o
numero=[]
for i in range (0,6):
    num= int(input("Digite os numeros: "))
    if num % 2==0:
            numero.append (num)
            soma= sum (num) 
            print (soma)

