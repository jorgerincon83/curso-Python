print("proporcione los siguientes datos:")
nombre = input("proporcione el nombre:")
id = int(input("proporcione el   ID:"))
precio = float(input("proporcione el precio:"))
envioGratuito = input("Indica si el envio es gratuito (True/False):")

if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "Valor Incorrecto, debe ser True/False"    

print("nombre:", nombre)
print("id:", id)
print("precio:", precio)
print("envio gratuito?:", envioGratuito)        
