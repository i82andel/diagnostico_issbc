# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 17:29:11 2021

@author: LuisAneri
"""

#!/usr/bin/env python
import bcEnfermedadesPulmonares as bcEnfermedades

conocimiento = bcEnfermedades

class MetodoCoberturaCausal():
    '''Método de cobertura causal para la tarea de diagnostico'''
    def __init__(self,fallos):
        self.fallos=fallos
        self.explicacion= ''
        self.diferencial=[]
        self.diagnostico=[]
        pass
    def obtenerConjuntoDiferencial(self):
        '''
        Obtiene el conjunto diferencial a partir de unos observables dados os fallos.
        
        @rtype:   list
        @return:  Conjunto de hipotesis compatible con los fallos.
        '''
        #Crear un conjunto diferencial con todos los fallos
        cc=CoberturaCausal(self.fallos)#Invoca la inferencia de cobertura causal
        self.diferencial=cc.execute()
 
        return self.diferencial
    def execute(self,tr=False):
        '''Ejecución del metodo de cobertura causal para la tarea de diagnostico.
        @rtype:   bolean
        @return:  Devuelve True si se ha realizado con éxito.
        '''
        self.explicacion+=u'Ejectutando cobertura causal. ' 
        #Se obtiene el conjunto diferencial invocando a la inferencia de cobertura causal
        cc=CoberturaCausal(self.fallos)

        self.diferencial=cc.execute()
        self.explicacion+=u'Se obtiene el conjunto diferencial: \n'

        for f in self.diferencial: #Va construyendo la explicación
            self.explicacion+=f.nombre+'\n'

        while len(self.diferencial)>0:#Mientras haya hipótesis que observar
            #Seleccionamos una hipotesis no seleccionada antes
            seleccionar=Seleccionar(self.diferencial)#Invoca a la inferencia de seleccionar
            hipotesis=seleccionar.execute()#Selecciona una hipótesis a ecaluar
            if tr:
                print ('hipotesis seleccionada', hipotesis)
                print ('======================')
            
            self.explicacion+=u'\nProbamos la  hipotesis de '
            self.explicacion+=hipotesis.nombre+'\n'
            if tr:            
                #print self.explicacion
                print()
                print ('antes de verificar', self.fallos,hipotesis)
                print ('hipotesis->',hipotesis.debePresentar)

            verifica=Verificar(self.fallos,hipotesis)#Con los fallos observados invoca la inferencia verificar
            verifica.execute(tr=tr)
            
            #print 'verifica.resultado=', verifica.resultado 
            if verifica.resultado==False:#Si el resultado de la verificación elimina la hipótesis del conjunto diferencial
                self.diferencial.remove(hipotesis)
                pass
            else:
                self.diagnostico.append(hipotesis)#Añade a la lista de diagnósticos compatibles la hipotesis
                self.diferencial.remove(hipotesis)#Suprime la hipótesis evaluada
            #Añadimos la justificación de verifica
            self.explicacion+=verifica.justificacion  #Añade a la justificación la justificación de la verificación
        pass
        if tr:
            print ('EL DIAGNOSTICO ES :',self.diagnostico)
        
        
     

class Inferencia():
    def __init__(self):
        pass
    def execute(self):
        pass
    
class CoberturaCausal(Inferencia):
    '''
    Se presenta una lista de fallos y proporciona una lista de posibles 
    hipotesis
    '''
    def __init__(self,fallos):
        Inferencia.__init__(self)
        self.fallos=fallos
        self.listaHipotesis=[]
    def execute(self):
        '''
         Mostrar todas las compatibles con los fallos. 
         Mejorar
        '''
        hipotesis= bcEnfermedades.hipotesis()
        self.listaHipotesis=hipotesis
        return hipotesis

        

class Seleccionar(Inferencia):
    '''
    Selecciona una hipotesis del conjunto diferencial
    '''
    def __init__(self,conjuntoDiferencial):
        Inferencia.__init__(self)
        self.conjuntoDiferencial=conjuntoDiferencial
    def execute(self):
        if len(self.conjuntoDiferencial)>0:
            return self.conjuntoDiferencial[0]
        else:
            return None
            

class Especificar(Inferencia):
   # Por desarrollar
    def __init__(self,lHipotesis):
        Inferencia.__init__(self)
        self.lHipotesis=lHipotesis
    def execute(self):
        if len(lHipotesis)>0:
            return lHipotesis[0]


class Obtener(Inferencia):
    #Por desarrollar
    def __init__(self,lHipotesis):
        Inferencia.__init__(self)
        self.lHipotesis=lHipotesis
    def execute(self):
        if len(lHipotesis)>0:
            return lHipotesis[0]    

   
class Verificar(Inferencia):
    '''
    Verifica si una hipótesis de averia es compatible con un conjunto de fallos.
    '''
    def __init__(self,fallos,hipotesis):
        Inferencia.__init__(self)
        self.fallos=fallos
        self.resultado=None
        self.hipotesis=hipotesis
        self.justificacion=''
    def execute(self,tr=False):
        #Eliminar aquellas hipotesis que no tengan todos los sintomas en debe de estar
        resultado=True
        if tr:
            print ('verificando la hipotesis:',self.hipotesis.nombre, self.hipotesis)
        for fh in self.hipotesis.debePresentar:#Cada fallo de la hipotesis debePresentar debe de estar en fallos
                                              # con sus valores aprepiados
             if tr:
                 print ('debe presentar:', fh,fh.nombre, fh.valor,'->',self.fallos)
                 print ('debe presentar:', (fh.nombre, fh.valor) ,'->',[(f.nombre,f.valor) for f in self.fallos])
              
             if not (fh.nombre in [f.nombre for f in self.fallos]):#Si el nombre del fallo de la hipótesis no está
                                                                   #en la lista de nombres de los fallos presentados
                                                                   #Construye la explicación
                 self.resultado=False
                 self.justificacion+=u'    No puede ser  '.encode(encoding='iso-8859-1')
                 self.justificacion+=self.hipotesis.nombre
                 self.justificacion+=u' porque deberia presentar el fallo '.encode(encoding='iso-8859-1')
                 self.justificacion+=fh.nombre+' \n'
                 #print type(f.valor)
                 if isinstance(fh.valor,bool):
                     self.justificacion+=str(fh.valor)+'\n'
                 elif isinstance(fh.valor,str):
                     self.justificacion+= fh.valor+'\n'
                 resultado=False
             else: #El nombre del fallo de la hipótesis está pero debe de coincidir los valores
                 falla=False #Bandera
                 for e in self.fallos:
                     if e.nombre==fh.nombre:#comprueba que coincide en valores
                         if  isinstance(fh.valor,list):#Si el valor del fallo de la hipótesis es de tipo lista
                             if not e.valor in fh.valor:#Comprueba que el valor del fallo presentado está en esa lista
                                 falla=True #El valor del fallo presentado no está en la lista
                                 break
                         else:#El valor del fallo de la hipótesis no es de tipo lista
                             if not e.valor==fh.valor:#Si no coincide los valores falla
                                 falla=True
                                 break
                        
                 if falla:#Si se ha fallado se añade a la justificación--->Mejorar
                     self.justificacion+=u'    No puede ser  '.encode(encoding='iso-8859-1')
                     self.justificacion+=self.hipotesis.nombre
                     self.justificacion+=u' porque deberia presentar el fallo '.encode(encoding='iso-8859-1')
                     self.justificacion+=fh.nombre+' \n con con valor apropiado.'
                     resultado=False
                     
             if resultado==False:#Si ha resultado fallida la verificación salimos de la verificación.
                 self.resultado=False
                 return (False,self.justificacion)
             else:
                 self.justificacion+=u' Puede ser  '.encode(encoding='iso-8859-1')+self.hipotesis.nombre+'.\n'
                 
                 
        #Eliminar aquellas hipotesis que tenga algun fallo en no debe tener
        for f in self.hipotesis.noPuedePresentar:
             if (f.nombre, f.valor) in [(e.nombre,e.valor) for e in self.fallos]:
                 self.resultado=False
                 self.justificacion+=u'    No puede ser  '.encode(encoding='iso-8859-1')
                 self.justificacion+=self.hipotesis.nombre
                 #self.justificacion+=f.nombre+' '
                 self.justificacion+=u' porque esta enfermedad no puede presentar el fallo '.encode(encoding='iso-8859-1')
                 self.justificacion+=f.nombre+' con valor '
                 if isinstance(f.valor,bool):
                     self.justificacion+=str(f.valor)+'\n'
                 elif isinstance(f.valor,str):
                     self.justificacion+= f.valor+'\n'                                 
                 resultado=False
        if resultado==False:
            self.resultado=False
            return (False,self.justificacion)

        self.resultado=True
        return (True,self.justificacion)
        
             
        
def diagnostico(hipotesis,fallos):
    
    
    if hipotesis=='PROSTATITIS':
        diagnostico='PROSTATITIS'
        justificacion = u'es una justificación'.encode(encoding='iso-8859-1')
        return (diagnostico,justificacion)
    else:
        return (None,None)

def identificaSignosSintomas(ltFallos):
    '''Identifica una lista de tuplas como signos y sintomas (fallos:atributo,valor)
    y compureba que son observables correctas de la base de conocimiento.
    '''
    obs=[]
    for tf in ltFallos:#Comprobar que cada fallo está en la base de conocimiento
        
        print (tf)
        ob=bcEnfermedades.creaObservable(tf)
        print (ob)
        if not ob==None:
            obs.append(ob)
        else:
            return None
    return obs 
    
 
    

if __name__ == '__main__':
    if False:
        dolorPerineal=bcEnfermedades.DolorPerineal(True)
        dolorLumbar=bcEnfermedades.DolorLumbar(True)
        cc=CoberturaCausal([dolorLumbar])
        cc.execute()
        for n in cc.listaHipotesis:
            print (n.nombre,n,n.debePresentar[0].nombre,n.debePresentar[0].valor)
        pass
    if False:
        dolorPerineal=bcEnfermedades.DolorPerineal(True)
        dolorLumbar=bcEnfermedades.DolorLumbar(True)
        mcc=MetodoCoberturaCausal([dolorPerineal,dolorLumbar])
        #diferencial=mcc.obtenerConjuntDiferencial()
        #print 'diferencial', diferencial
        mcc.execute()
        print ('Justificacion')
        print ('=============')
        print (mcc.explicacion)
        print ('Diagnostico: ',mcc.diagnostico)
        print ('fin')
    if False:
        fiebre=bcEnfermedades.Fiebre('alta')
        disuria=bcEnfermedades.Disuria(True)
        mcc=MetodoCoberturaCausal([fiebre, disuria])
        mcc.execute()
        print ('Justificacion')
        print ('=============')
        print (mcc.explicacion)
        print ()
        print ('Diagnostico: ' )
        for d in mcc.diagnostico:
            print (d.nombre)
        print ('fin')
    if True:
        #dolorLumbar=bcEnfermedades.creaObservable(('dolor lumbar','agudo'))
        #dolorLumbar=bcEnfermedades.DolorLumbar('agudo')
        #print 'el dolor lumbar es',dolorLumbar.valor
        #disuria=bcEnfermedades.Disuria(True)
        print()
        fiebre=bcEnfermedades.Fiebre('alta')
        disuria=bcEnfermedades.Disuria(True)
        mcc=MetodoCoberturaCausal([fiebre,disuria])
        mcc.execute(tr=False)
        print ('Justificacion')
        print ('=============')
        print (mcc.explicacion)
        print ()
        print ('Diagnostico: ' )
        for d in mcc.diagnostico:
            print ()
        print ('fin')
    if False:
        ls=identificaSignosSintomas([(u'fiebre','alta'),(u'dolor lumbar','alto')])
        print ('imprimiendo resultados',ls)
        
        
        
        
    

    
    
    