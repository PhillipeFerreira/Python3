from maintrafo import trafo

trafo1 = trafo()

trafo1.alpha()
print('TRANSFORMADOR IDEAL')
trafo1.i1()
trafo1.i2()
trafo1.f1()
trafo1.f2()
trafo1.k()
trafo1.im()
print('\nTRANFORMADOR REAL\n')
trafo1.p_s()
trafo1.p_cu()
trafo1.red()
trafo1.p_fe()
print(f'Fator de Potência: {trafo.cosx}')
