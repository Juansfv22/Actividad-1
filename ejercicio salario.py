horas_semana=48
pago_hora=5000
salario_bruto=int(horas_semana*pago_hora)
retencion_fuente=int(salario_bruto*0.125)
salario_neto=salario_bruto-retencion_fuente
print('El salario bruto por semana es de $',salario_bruto)
print('La retención en la fuente es de $',retencion_fuente)
print('El salario neto por semana es de $',salario_neto)
