# reproductor.py
# UNEFA Mérida
# Integrantes: yorbelysdavila, eislenp, ????
# Profesor: javierri
# Calificación
class reproductor:

#atributos
    nro_cancion=0
    nro_carpeta=False
    nro_volumen=0
    max_volumen=30
    cap_cd=3
    frecuencia_emisora=False
    portal_cerrado=False
    encendido=False
    nro_cd=0
    volumen=False
    reproducir_cancion=True
    sintonizar_dial=False
    reconocer_usb=False   

#metodos
def encender (self):
     if (self.encendido==False):
        self.encendido=true

def apagar (self):
     if (self.encendido==true):
        self.encendido=False

def abrir_porta (self):
     if (self.encendido and self.portal_cerrado==True):
               self.portal_cerrado=False
               print "portal abierto"

def cerrar_portal (self):
     if(self.encendido and self.portal_cerrado==False):
            self.portal_cerrado=True
            print "portal cerrado"

def reproducir (self):
     if (self.encendido and self.nro_cancion==true):
         self.nro_cancion=false
         print "reproduciendo cancion"
     else:
        print "error al reproducir cancion"

def volumen_reproductor (self):
     if (self.encendido and self.volumen==False):
              self.volumen=True
              print " subir volumen"
     else:
        print"bajar volumen"

def subir_volumen (self):
     if (self.volumen and self.encendido):
               if (self.nro_volumen < self.max_volumen):
                        self.nro_volumen=self.nro_volumen+1
                        print "sube",self.nro_volumen
               else:
                    print "no puede exceder volumen"
     else:
        print "error al subir volumen"

def bajar_volumen(self):
     if (self.volumen and self.encendido):
               if (self.nro_volum,en>0):
                        self.nro_volumen=self.nro_volumen -1
                        print"baja",self.nro_volumen
               else:
                   print "no puede bajar volumen"
     else:
          print"error al bajar volumen"

def anterio_cancion (self):
     if (self.encendido and self.reproducir_cancion==True):
               self.reproducir_cancion=False
               print "reproduciendo anterior cancion"

def siguiente_cancion (self):
      if (self.encendido and self.reproducir_cancion==True):
               self.reproducir_cancion=False
               print "reproduciendo siguiente cancion"

def pausar_cancion (self):
     if (self.encendido and self.reproducir_cancion==False):
              self.reproducir_cancion=True
              print "cancion en pausa"

def emisora(self):
    if (self.encendido and self.sintonizar_dial==True):
            self.sintonizar_dial=False
            print "sintonizando dial"
            
def emisora_am (self):
     if (self.encendido and self.frecuencia_emisora==True):
               self.frecuencia_emisora=False
               print "frecuencia am"
     else:
          print "no se encuentra emisora"

def emisora_fm (self):
     if (self.encendido and self.frecuencia_emisora==True):
              self.frecuencia_emisora=False
              print "frecuencia fm"
     else:
          print "error en frecuencia"
          
def usb(self):
    if (self.encendido and self.reconocer_usb==True):
             self.recocer_usb=False
             print "reconociendo usb"

def leer_usb (self):
      if (self.encendido and self.nro_carpetas==True):
                self.nro_carpetas=False
                print "examinando carpetas"
      else:
          print"no existe carpeta"

def selecionar (self, cd):
     if (cd<0 and cd>self.cap_cd):
            print "error de cd"
            return
     if (self.nro_cd > self.cap_cd):
            print "numero de cd excesivo"
            return
     if (self.nro_cd==0):
            print "seleccion incorreta, portal_cerrado"
            return
     self.abrir_portal()

#principal

a=reproductor()
a.encendido()

#reproducir
nro_cancion (2)
nro_cd(3)
