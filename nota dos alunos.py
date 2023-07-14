nota1 = float(input("informe sua nota:"))
nota2 = float(input("informe sua nota:"))
nota3 = float(input("informe sua ultima nota:"))



media = (nota1+nota2+nota3) /3


if media >= 6:
    print ("Aprovado")
else:
   if media >= 5:
     print("conselho de classe")
   else:
     print("reprovado")

   
   
print("sua media foi: ", media ) 
