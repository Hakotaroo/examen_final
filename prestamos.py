from abc import ABC, abstractmethod

#Herencia (clase)
class DetalleDisponibilidad(ABC):
    @abstractmethod
    def verificar_disponibilidad(self, detalle):
        pass

    @abstractmethod
    def actualizar_c(self, detalle):
        pass


class detalle_d(DetalleDisponibilidad):  
    def _init_(self):
        #Encapsulamiento
        self.__libros = ["Libro A", "Libro B"]  
    def verificar_disponibilidad(self, detalle):
        return detalle in self.__libros  #Polimorfismo
    

    def actualizar_c(self, detalle):
        try:#Manejo de errores
            self.__libros.remove(detalle)  
        except ValueError:
            print(f"Error: '{detalle}' no está en la lista.")

# Clase usuario
class usuario:  
    def _init_(self, nombre):
        self.__nombre = nombre  #Encapsulamiento
        self.__historial = []

    def actualizar_c(self, detalle):
        self.__historial.append(detalle)  

    def mostrar_historial(self):
        return self.__historial

#Clase para préstamos
class realizar_p:  
    def _init_(self, detalle_d, usuario):
        #Encapsulamiento
        self.__detalle_d = detalle_d  
        self.__usuario = usuario

    def realizar_p(self, detalle):
        if self.__detalle_d.verificar_disponibilidad(detalle):  # Polimorfismo
            try:
                self.__usuario.actualizar_c(detalle)
                self.__detalle_d.actualizar_c(detalle)
                print(f"Préstamo realizado: {detalle}")
            except Exception as e:  #Manejo de errores
                print(f"Error: {e}")
        else:
            print(f"El detalle '{detalle}' no está disponible.")

#Ejecución del sistema
if _name_ == "_main_":
    detalle_d_obj = detalle_d()
    usuario_obj = usuario("Juan Pérez")
    prestamo_obj = realizar_p(detalle_d_obj, usuario_obj)

    #Intentos de préstamo
    prestamo_obj.realizar_p("Libro A")
    prestamo_obj.realizar_p("Libro X")
    prestamo_obj.realizar_p("Libro A")

    #Mostrar historial
    print(f"Historial de préstamos: {usuario_obj.mostrar_historial()}")