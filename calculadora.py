import math
def suma(a,b):
    ar=a[0]+b[0]
    br=a[1]+b[1]
    return (ar,br)
def resta(a,b):
    ar=a[0]-b[0]
    br=a[1]-b[1]
    return (ar,br)
def producto(a,b):
    ar=((a[0]*b[0])+((a[1]*b[1])*-1))
    br=((a[0]*b[1])+(a[1]*b[0]))
    return (ar,br)
def division(a,b):
    ar=((a[0]*b[0]+a[1]*b[1])/(b[0]**2+b[1]**2))
    br=((b[0]*a[1]-a[0]*b[1])/(b[0]**2+b[1]**2))
    return (ar,br)
def modulo(a):
    r=((a[0]**2)+(a[1]**2))**0.5
    return r
def moduloDeUnVector(v):
    res=0
    for i in v:
        res+=modulo(i)
    return round(res,2)
def conjugado(a):
    ar=a[0]
    br=a[1]*-1
    return (ar,br)
def opuesto(a):
    ar=a[0]*-1
    br=a[1]*-1
    return (ar,br)
def cartesianasAPolares(a):
   theta=math.atan2(a[1],a[0])
   ar=(a[0]**2+a[1]**2)**5
   br=theta*(180/math.pi)
   return(ar,br)
def polaresACartesianas(a):
    h=a[0]
    alpha=a[1]*(math.pi/180)
    ar=h*math.cos(alpha)
    br=h*math.sin(alpha)
    return (ar,br)
def fase(a):
    ar=math.atan2(a[1],a[0])
    return (ar)
def adicionDeVectoresComplejos(a,b):
    res=[]
    if len(a)==len(b):
        for i in range(len(b)):
            res.append(suma(a[i],b[i]))
        return res
    else:
        raise "dimensiones invalidas"
def inverso(a):
    res=[]
    for i in range(len(a)):
        res.append(opuesto(a[i]))
    return res
def productoEscalar(a,b):
    ar=a[0]*b
    br=a[1]*b
    return (ar,br)
def escalarVector(a,b):
    res=[]
    for i in range(len(a)):
        res.append(productoEscalar(a[i],b))
    return res
def sumaDeMatrices(a,b):
    sol=[]
    for i in range(len(a)):
        res=[]
        for j in range(len(b)):
            res.append(suma(a[i][j],b[i][j]))
        sol.append(res)
    return sol
def inversaMatriz(a):
    sol=[]
    for i in range(len(a)):
        res=[]
        for j in range(len(a)):
            res.append(opuesto(a[i][j]))
        sol.append(res)
    return sol
def multiplicacionEscalarMatrices(a,b):
    for i in range(len(a)):
        res=[]
        for j in range(len(a)):
            res.append(productoEscalar(a[i][j],b))
    return [res]
def productoInternoDeVectores(a,b):
    aux = []
    res = [0,0]
    if len(a)==len(b):
        for i in range(len(a)):
           aux.append(producto(a[i],b[i]))
           res = suma(res,aux[i])
    return(res)
def traspuesta(a):
    res=[]
    for i in range(len(a[0])):
        t = []
        for j in range(len(a)):
            t.append(a[j][i])
        res.append(t)
    return res

def conjugadaMatriz(a):
    sol=[]
    for i in range(len(a)):
        res=[]
        for j in range(len(a)):
            res.append(conjugado(a[i][j]))
        sol.append(res)
    return sol
def vectorConjugado(v):
    final=[]
    for i in v:
        answer=conjugado(i)
        final.append(answer)
    return final
def adjunta(a):
    return (conjugadaMatriz(traspuesta(a)))
def multiplicacionMatices(m1,m2):
    sol = []
    for i in range(len(m1)):
        l = []
        for j in range(len(m2[0])):
            aux = (0,0)
            for k in range(len(m2)):
                sumas= producto(m1[i][k],m2[k][j])
                aux= suma(sumas,aux) 
    
            l.append(aux)
        sol.append(l)
    return (sol)
def vectorTranspuesto(vector):
    return vector
def vectorAdjunto(v):
    a=conjugado(v)
    b=vectorTranspuesto(a)
    return b
def productoDeDosVectores(v1,v2):
    respuesta=[]
    if len(v1)==len(v2):
        sol=(0,0)
        for i in range(len(v1)):
            sol=suma(final,multi(v1[i],v2[i]))
        return sol
def tensorVector(a,b):
    sol=[]
    for x in range(len(a)):
        for y in range(len(b)):
            sol.append(producto(a[x],b[y]))
    return sol

def tensorMatrices(a,b):
    sol=[]
    for i in range(len(a)):
        for j in range(len(b)):
             sol.append(tensorVector(a[i],b[j]))
    return sol
def potenciaCuadrada(num):
    return(producto(num,num))
def distanciaEntreDosVectores(a,b):
    res = []
    sol = [0,0]
    if len(a)==len(b):
        for i in range(len(a)):
            a.append(resta(a[i],b[i]))
        for j in range(len(res)):
            solucion = suma(solucion,potenciaCuadrada(res[j]))
    sol[0]=sol[0]**0.5
    return (sol)
def normaDeVector(a):
    sol = [0,0]
    for i in range(len(a)):
        sol = suma(sol,potenciaCuadrada(a[i]))
    sol[0]=sol[0]**0.5
    return(sol)
def esUnaHermitiana(m):
    if len(m) != len(m[0]):  raise ("La matriz no es cuadrada")
    return m == adjunta(m)
def esUnaUnitaria(m):
    if len(m) != len(m[0]):  raise ("La matriz no es cuadrada")
    i = [[(float(0),float(0)) for w in range(len(m))]for j in range(len(m))]
    for k in range(len(i)):
        i[k][k] = (float(1),float(0))
    return multiplicacionMatices(m,adjunta(m)) == multiplicacionMatices(adjunta(m),m) == i
def productoInternoEntreMatrices(m1,m2):
    adj = adjunta(m1)
    aux = multiplicacionMatices(adj,m2)
    res = (0,0)
    for i in range(len (aux)):
        res = suma(res,aux[i][i])
    return modulo(res)
def normaMatriz (m):
    return round(productoInternoEntreMatrices(m,m)**0.5,2)

#Ejercicio sistema cuantico de una particula en una linea

def probability(pos,vector):
    moduloAux=modulo(vector[pos])
    moduloVector=moduloDeUnVector(vector)
    probabilidad=(moduloAux/moduloVector)*100
    return round(probabilidad,2)
def transition(v1,v2):
    conjunto=vectorAdjunto(v2)
    sol=productoDeDosVectores(conjunto,v1)
    return sol  
