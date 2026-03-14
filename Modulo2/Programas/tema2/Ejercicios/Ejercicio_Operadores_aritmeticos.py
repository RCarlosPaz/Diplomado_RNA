def calcular_calorias(carbohidratos, proteinas, grasas):
    caloriasporcarbo = carbohidratos * 4
    caloriasporprote = proteinas * 4
    caloriasporgrasa = grasas * 9

    caloriastotales = caloriasporcarbo + caloriasporprote + caloriasporgrasa
    print("\nSimulador de Calculadora de Calorías\n")
    print("Calorias totales: ", caloriastotales)

    
calcular_calorias(10,40,5)
