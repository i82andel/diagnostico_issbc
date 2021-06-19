# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 18:17:49 2021

@author: LuisAneri
"""
# Son los sintomas
class Observable():
    '''Definición genérica de una observable'''
    def __init__(self,nombre=None,tipo=None,valoresPermitidos=None,valor=None):
        #print 'observable->',valor
        self.nombre=nombre
        self.valor=valor
        self.tipo=tipo
        self.valoresPermitidos=valoresPermitidos
        
class TosSeca(Observable):
    def __init__(self,valor=None):
        #print valor
        nombre='Tos seca'
        tipo='multiple'
        valoresPermitidos=['leve','intenso']
        Observable.__init__(self,nombre,tipo,valoresPermitidos,valor) 
        
class TosFlema(Observable):
    def __init__(self,valor=None):
        nombre='Tos con flema'
        tipo='boleano'
        valoresPermitidos=None
        Observable.__init__(self,nombre ,tipo ,valoresPermitidos,valor)
        self.valor=valor
        
class Fiebre(Observable):
    def __init__(self,valor=None):
        nombre='fiebre'
        tipo='multiple'
        valoresPermitidos=['normal','alta','muy alta']
        Observable.__init__(self,nombre ,tipo ,valoresPermitidos,valor)
        self.valor=valor
        
class PerdidaOlfatoGusto(Observable):
    def __init__(self,valor=None):
        nombre='Perdida olfato o del gusto'
        tipo='boleano'
        valoresPermitidos=None
        Observable.__init__(self,nombre ,tipo ,valoresPermitidos,valor)
        self.valor=valor
        
class MoqueoNasal(Observable):
    def __init__(self,valor=None):
        nombre='Moqueo nasal'
        tipo='multiple'
        valoresPermitidos=['leve','intenso']
        Observable.__init__(self,nombre ,tipo ,valoresPermitidos,valor)
        self.valor=valor
        
class Estornudos(Observable):
    def __init__(self,valor=None):
        nombre='Estornudos'
        tipo='boleano'
        valoresPermitidos=None
        Observable.__init__(self,nombre ,tipo ,valoresPermitidos,valor)
        self.valor=valor

class DolorGarganta(Observable):
    def __init__(self,valor=None):
        nombre='Dolor de Garganta'
        tipo='multiple'
        valoresPermitidos=['normal','alta','muy alta']
        Observable.__init__(self,nombre ,tipo ,valoresPermitidos,valor)
        self.valor=valor

class DificultadRespirar(Observable):
    def __init__(self,valor=None):
        nombre='Dificultad para Respirar'
        tipo='boleano'
        valoresPermitidos=None
        Observable.__init__(self,nombre ,tipo ,valoresPermitidos,valor)
        self.valor=valor
          
class DolorCabeza(Observable):
    def __init__(self,valor=None):
        nombre='Dolor de cabeza'
        tipo='multiple'
        valoresPermitidos=['normal','alta','muy alta']
        Observable.__init__(self,nombre ,tipo ,valoresPermitidos,valor)
        self.valor=valor

class Diarrea(Observable):
    def __init__(self,valor=None):
        nombre='Diarrea'
        tipo='multiple'
        valoresPermitidos=['normal','alta','muy alta']
        Observable.__init__(self,nombre ,tipo ,valoresPermitidos,valor)
        self.valor=valor

# Aqui se tienen que adjuntar todos los sintomas a obs        
def observables():
    '''Devuelve la lista de observables de la BC
    '''
    obs=[]   
    obs.append(TosSeca())
    obs.append(TosFlema())
    obs.append(Fiebre())
    obs.append(PerdidaOlfatoGusto())
    obs.append(MoqueoNasal())
    obs.append(Estornudos())
    obs.append(DolorGarganta())
    obs.append(DificultadRespirar())
    obs.append(DolorCabeza())
    obs.append(Diarrea())

    return obs

# Esta funcion los instancia
def creaObservable(tp):
    '''Crea una instancia de un observable si la tupla coincide con la base de conocimiento
    . Si la observable es correcta devuelve una instancia de la observable.
    Corregir. Hay que mejorar esta función'''
    
    print(tp)
    if tp[0]==u'Tos seca':
        ob=TosSeca(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'Tos con flema':
        ob=TosFlema(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'fiebre':
        ob=Fiebre(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'Perdida olfato o del gusto':
        ob=PerdidaOlfatoGusto(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'Moqueo nasal':
        ob=MoqueoNasal(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'Estornudos':
        ob=Estornudos(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'Dolor de Garganta':
        ob=DolorGarganta(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'Dolor de cabeza':
        ob=DolorCabeza(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'Dificultad para Respirar':
        ob=DificultadRespirar(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'Diarrea':
        ob=Diarrea(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
        print (ob,ob.valoresPermitidos,tp[1])
        if tp[1] in ob.valoresPermitidos:
            ob.valor=tp[1]
            return ob
        else:
            print('no esta')
    return None
        
    
    

# Son las distintas enfermedades
class Enfermedad():
    '''Clase Enfermedad
    '''
    def __init__(self,nombre):
        self.nombre=nombre
        self.ayuda=u''

class Gripe(Enfermedad):
    def __init__(self):
        Enfermedad.__init__(self,nombre=u'Gripe')
        #Creamos instancias de observables
        tosSeca=TosSeca([u'leve',u'intenso'])
        tosFlema=TosFlema(True)
        fiebre=Fiebre(['normal','alta','muy alta'])
        perdidaOlfato=PerdidaOlfatoGusto(True)
        moqueoNasal = MoqueoNasal(['leve','intenso'])
        estornudos = Estornudos(True)
        dolorGaragnta = DolorGarganta(['normal','alta','muy alta'])
        dificultadRespirar = DificultadRespirar(True)
        dolorCabeza = DolorCabeza(['normal','alta','muy alta'])
        diarrea = Diarrea(['normal','alta','muy alta'])
        
        
        
        self.ayuda=u'Ayuda sobre Gripe'
        self.debePresentar =[tosSeca,fiebre,dolorCabeza]
        self.puedePresentar = [moqueoNasal,dolorGaragnta,diarrea]
        self.noPuedePresentar = [tosFlema,perdidaOlfato,estornudos,dificultadRespirar]
        self.ayuda=u'Ayuda sobre Gripe'
class Resfriado(Enfermedad):
    def __init__(self):
        Enfermedad.__init__(self,nombre=u'Resfriado')
        #Creamos instancias de observables
        tosSeca=TosSeca([u'leve',u'intenso'])
        tosFlema=TosFlema(True)
        fiebre=Fiebre(['normal','alta','muy alta'])
        perdidaOlfato=PerdidaOlfatoGusto(True)
        moqueoNasal = MoqueoNasal(['leve','intenso'])
        estornudos = Estornudos(True)
        dolorGaragnta = DolorGarganta(['normal','alta','muy alta'])
        dificultadRespirar = DificultadRespirar(True)
        dolorCabeza = DolorCabeza(['normal','alta','muy alta'])
        diarrea = Diarrea(['normal','alta','muy alta'])
        
        
        
        self.ayuda=u'Ayuda sobre Resfriado'
        self.debePresentar =[tosFlema,moqueoNasal,estornudos,dolorGaragnta]
        self.puedePresentar = [tosSeca]
        self.noPuedePresentar = [fiebre,perdidaOlfato,dificultadRespirar,dolorCabeza,diarrea]
        self.ayuda=u'Ayuda sobre Resfriado'

class COVID_19(Enfermedad):
    def __init__(self):
        Enfermedad.__init__(self,nombre=u'COVID_19')
        #Creamos instancias de observables
        tosSeca=TosSeca([u'leve',u'intenso'])
        tosFlema=TosFlema(True)
        fiebre=Fiebre(['normal','alta','muy alta'])
        perdidaOlfato=PerdidaOlfatoGusto(True)
        moqueoNasal = MoqueoNasal(['leve','intenso'])
        estornudos = Estornudos(True)
        dolorGaragnta = DolorGarganta(['normal','alta','muy alta'])
        dificultadRespirar = DificultadRespirar(True)
        dolorCabeza = DolorCabeza(['normal','alta','muy alta'])
        diarrea = Diarrea(['normal','alta','muy alta'])
        
        
        
        self.ayuda=u'Ayuda sobre COVID_19'
        self.debePresentar =[tosSeca,fiebre,perdidaOlfato]
        self.puedePresentar = [moqueoNasal,dolorGaragnta,dificultadRespirar,dolorCabeza]
        self.noPuedePresentar = [tosFlema,estornudos,diarrea]
        self.ayuda=u'Ayuda sobre COVID_19'

# Hay que añadir las enfermedades a lHp
def hipotesis():
    '''
    Posibles enfermedades o averías que pueden darse
    '''
    gri=Gripe()
    ap=Resfriado()
    tarj=COVID_19()
    
    lHp=[gri, ap, tarj]
    return lHp
        
    pass
