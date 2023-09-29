class trafo():

    t = 5       # TEMPO CONSIDERADO NOS CÁLCULOS
    cosx = 0.92 # FATOR DE POTÊNCIA CONSIDERADO NOS CÁLCULOS

    def __init__(self, u1=0, u2=0, p=0, n1=0, n2=0, r1=0, r2=0):
        self.p = float(input("POTÊNCIA DO TRANSFORMADOR: "))
        self.u1 = float(input("TENSÃO NO PRIMÁRIO: "))
        self.u2 = float(input("TENSÃO NO SECUNDÁRIO: "))
        self.n1 = float(input("ESPIRAS NO PRIMÁRIO: "))
        self.n2 = float(input("ESPIRAS NO SECUNDÁRIO: "))
        self.r1 = float(input("RESISTÊNCIA NO ENROLAMENTO PRIMÁRIO: "))
        self.r2 = float(input("RESISTÊNCIA NO ENROLAMENTO SECUNDÁRIO: "))
        
    def alpha(self):
        alpha = self.u1 / self.u2
        print("\nRelação de Transformação: {:.3f}".format(alpha))
        if alpha < 1:
            print("\nTRANSFORMADOR ELEVADOR")
        elif alpha > 1:
            print("TRANSFORMADOR REBAIXADOR")
        else:
            print('\nTRANSFORMADOR ISOLADOR')
    
    def i1(self):
        global i1
        i1 = self.p / self.u1
        print("\nCorrente no Primário: {:.3f}A".format(i1))
        
    def i2(self):
        global i2
        i2 = self.p / self.u2
        print("Corrente no Secundário: {:.3f}A".format(i2))
        
    def f1(self): 
        global f1
        f1 = (self.u1 * trafo.t)/self.n1
        print("Fluxo Magnético no Primário: {:.3f}Wb".format(f1))
        
    def f2(self): 
        global f2 
        f2 = (self.u2 * trafo.t)/self.n2
        print("Fluxo Magnético no Secundário: {:.3f}Wb".format(f2))

    def k(self):
        k = f1 / f2
        print('Coeficiente de Acoplamento: {:.2f}'.format(k))

    def im(self):
        im = self.n1 * (f1 / i2)
        print('Impedância Mútua: {:.3f}H'.format(im))
    
    def p_s(self):
        global p_s
        p_s = self.u2 * trafo.cosx * i1
        print("Potência de Saída: {:.3f}VA".format(p_s))
        
    def p_cu(self):
        global p_cu
        p_cu = self.r1 * (i1**2) + self.r2 * (i2 ** 2)
        print("Perda Ohmica: {:.3f}VAR".format(p_cu))
        
    def red(self):
        red = ((p_s) / (p_s + p_cu))*100
        print("Rendimento: {:.3f}%".format(red))
        
    def p_fe(self):
        p_fe = (i1**2) * self.r2
        print("Perdas no Núcleo: {:.3f}VAR".format(p_fe))

