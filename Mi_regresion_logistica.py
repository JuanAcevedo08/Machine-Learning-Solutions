import math

horas = [1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 10]
aprobación = [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1]
b0 = 0
b1 = 0

def calculo_z(b0:int, b1:int, x:list):
    return [b0 + (b1 * v) for v in x]

def sigmoide(z:list):
    return [(1 / (1 + math.exp(-v))) for v in z]

def optimizacion(x: list, y: list, b0=0, b1= 0,lr=0.1, iteraciones=1000):
    for i in range(iteraciones):
        z = calculo_z(b0 , b1, x)
        p = sigmoide(z)

        errores = [p[j] - y[j] for j in range(len(y))]

        g0 = sum(errores) / len(y)
        g1 = sum([errores[j] * x[j] for j in range(len(y))]) / len(y)

        b0 -= lr * g0
        b1 -= lr * g1

    return [b0 , b1]

def aprobacion(name,tiempo_estudio):
    coefs = optimizacion(horas, aprobación)
    z = calculo_z(coefs[0], coefs[1], tiempo_estudio)
    p = sigmoide(z)

    for v in range(len(tiempo_estudio)):
        if p[v] > 0.5:
            print(f'El modelo predice que : {name[v]} puede aprobar el examen {tiempo_estudio[v]}. No es necesario el acompañamiento')
        else:
            print(f'El modelo predice que: {name[v]} No aprobará el examén debido a sus horas de estudio: {tiempo_estudio[v]}. solciitar acompañamiento ')

aprobacion(['María', 'juan', 'sofía', 'camila', 'gabriela', 'josé'], [1, 2, 3, 5, 6, 8])

