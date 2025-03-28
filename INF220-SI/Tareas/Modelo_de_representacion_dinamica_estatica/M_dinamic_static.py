# Clase Automóvil con estructura estática
class AutomovilEstatico:
    """Clase que representa un automóvil usando una estructura estática."""

    def __init__(self, marca, modelo, anio):
        """Constructor que inicializa los atributos del automóvil."""
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    # Getters
    def get_marca(self):
        """Obtiene la marca del automóvil."""
        return self.marca

    def get_modelo(self):
        """Obtiene el modelo del automóvil."""
        return self.modelo

    def get_anio(self):
        """Obtiene el año del automóvil."""
        return self.anio

    # Setters
    def set_marca(self, marca):
        """Establece la marca del automóvil."""
        self.marca = marca

    def set_modelo(self, modelo):
        """Establece el modelo del automóvil."""
        self.modelo = modelo

    def set_anio(self, anio):
        """Establece el año del automóvil."""
        self.anio = anio

    def __str__(self):
        """Representación en cadena del automóvil."""
        return f"Automóvil Estático: Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}"


# Clase Automóvil con estructura dinámica
class AutomovilDinamico:
    """Clase que representa un automóvil usando una estructura dinámica."""

    def __init__(self, marca, modelo, anio):
        """Constructor que inicializa los datos del automóvil."""
        self.datos = {
            "marca": marca,
            "modelo": modelo,
            "anio": anio
        }

    # Getters
    def get_marca(self):
        """Obtiene la marca del automóvil."""
        return self.datos["marca"]

    def get_modelo(self):
        """Obtiene el modelo del automóvil."""
        return self.datos["modelo"]

    def get_anio(self):
        """Obtiene el año del automóvil."""
        return self.datos["anio"]

    # Setters
    def set_marca(self, marca):
        """Establece la marca del automóvil."""
        self.datos["marca"] = marca

    def set_modelo(self, modelo):
        """Establece el modelo del automóvil."""
        self.datos["modelo"] = modelo

    def set_anio(self, anio):
        """Establece el año del automóvil."""
        self.datos["anio"] = anio

    def __str__(self):
        """Representación en cadena del automóvil."""
        return f"Automóvil Dinámico: {self.datos}"


# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo con estructura estática
    auto_estatico = AutomovilEstatico("Honda", "Civic", 2019)
    print(auto_estatico)
    auto_estatico.set_modelo("Accord")
    print(auto_estatico)
    
    # Ejemplo con estructura dinámica
    auto_dinamico = AutomovilDinamico("Susuki", "Corolla", 2020)
    print(auto_dinamico)
    auto_dinamico.set_anio(2021)
    print(auto_dinamico)
    

