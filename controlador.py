from modelo.modeloCliente import Cliente
class Controlador:
    def __init__(self):
        #todo lo que sea composicion 
        #va en el costructor
        self.objCliente=Cliente()

    def agregarCliente(self, datoNombre):
        self.objCliente.guardar_cliente(datoNombre)

   # def modificarNombre(self):
       # datoNuevo= "YO"
       # self.objCliente.setNombre(self, datoNuevo)    

    def imprimirNombre(self):
        auxNombre= self.objCliente.getNombre()    
        self.objVista.mensaje(auxNombre)