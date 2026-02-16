def preparar_cafe(tipo, azucar=False, extra="ninguno"):
    # 1. TRADUCIR EL BOOLEANO
    # Si azucar es verdad, la etiqueta es "con azúcar"
    # Si no, la etiqueta es "sin azúcar"
    if azucar == True:
        txt_azucar = "con azúcar"
    else:
        txt_azucar = "sin azúcar"

    # 2. IMPRIMIR EL RESULTADO FINAL
    # Queremos que diga algo como: "Aquí tienes tu Latte, con azúcar y extra de Canela."
    print(f"Aquí tienes tu {tipo}, {txt_azucar} y extra de {extra}.")


# --- ZONA DE PRUEBAS (Descomenta para probar) ---
preparar_cafe("Espresso")                            
preparar_cafe("Latte", azucar=True)                  
preparar_cafe("Cappuccino", extra="Cacao", azucar=True)