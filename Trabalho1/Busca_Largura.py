from typing import List
class Torre(object):
    class Estado(object):
        def __init__(self):
            self.torre1 = []
            self.torre2 = []
            self.torre3 = []
            self.pai = None

        def copy(self):
            estado = Torre.Estado()
            estado.torre1 = self.torre1.copy()
            estado.torre2 = self.torre2.copy()
            estado.torre3 = self.torre3.copy()
            return estado
        
        def __repr__(self):
            return f'{self.torre1} | {self.torre2} | {self.torre3}'
    @property
    def estado_inicial(self):
            estado = Torre.Estado()
            estado.torre1 = [1,2,3,4,5]
            estado.torre2 = []
            estado.torre3 = []
            estado.pai = None
            return estado

    def solucao(self,estado):
            solucao_final = []
            while estado.pai is not None:
                solucao_final.append(estado)
                estado = estado.pai
            solucao_final.append(estado)
            return solucao_final.reverse()

    def funcao_objetivo(self,estado):
            return estado.torre3 == [5,4,3,2,1]

    def funcao_sucessora(self,estado):
        sucessores = []
        #acoes
        #1 tira do primeiro bota segundo
        #2 tira do primeiro bota terceiro
        #3 tira do segundo bota primeiro
        #4 tira do segundo bota terceiro
        #5 tira do terceiro bota primeiro
        #6 tira do terceiro bota segundo
        #criar um estado temporario para fazer as mudancas
        a1 = self.mover(estado,estado.torre1,estado.torre2,'1')
        a2 = self.mover(estado,estado.torre1,estado.torre3,'2')
        a3 = self.mover(estado,estado.torre2,estado.torre1,'3')
        a4 = self.mover(estado,estado.torre2,estado.torre3,'4')
        a5 = self.mover(estado,estado.torre3,estado.torre1,'5')
        a6 = self.mover(estado,estado.torre3,estado.torre2,'6')
        if a1: sucessores.append(a1)
        if a2: sucessores.append(a2)
        if a3: sucessores.append(a3)
        if a4: sucessores.append(a4)
        if a5: sucessores.append(a5)
        if a6: sucessores.append(a6)
        return sucessores

    def mover(self, estado_pai,source,target,acao):
        estado = estado_pai.copy()
        estado.pai = estado_pai
        estado.acao = acao
        if source:
            if not target or source[0] > target[0]:
                target.insert(0,source.pop(0))
                return estado
        return None

class Busca(object):
    def largura_busca(self,problema: Torre):
        borda = [problema.estado_inicial]
        repeat = []
        while True:
            if not borda:
                print('Falha ao encontrar solucao')
                return []
            repeat.append(borda)
            estado = borda.pop(0)
            for x in range(len(repeat)):
                for y in range(len(borda)):
                    if repeat[x] == borda[y]:
                        borda.remove(repeat[x])
            if problema.funcao_objetivo(estado):
                print('Solucao encontrada.')
                return problema.solucao(estado)
            x = problema.funcao_sucessora(estado)
            while x:
                borda.append(x.pop())
            print(estado)

    def profundidade_busca(self,problema: Torre):
        borda = [problema.estado_inicial]
        repeat = []
        while True:
            if not borda:
                print('Falha ao encontrar solucao')
                return []
            repeat.append(borda)
            estado = borda.pop()
            for x in range(len(repeat)):
                for y in range(len(borda)):
                    if repeat[x] == borda[y]:
                        borda.remove(repeat[x])
            if problema.funcao_objetivo(estado):
                print('Solucao encontrada.')
                return problema.solucao(estado)
            x = problema.funcao_sucessora(estado)
            while x:
                borda.insert(0,x.pop())
            print(estado)

    def custo_busca(self,problema: Torre):
        borda = [problema.estado_inicial]
        repeat = []
        while True:
            if not borda:
                print('Falha ao encontrar solucao')
                return []
            repeat.append(borda)
            borda.sort()
            estado = borda.pop(0)
            for x in range(len(repeat)):
                for y in range(len(borda)):
                    if repeat[x] == borda[y]:
                        borda.remove(repeat[x])
            if problema.funcao_objetivo(estado):
                print('Solucao encontrada.')
                return problema.solucao(estado)
            x = problema.funcao_sucessora(estado)
            while x:
                borda.append(x.pop())
            print(estado)

def main():
    problema = Torre()
    busca = Busca()
    solucao = busca.largura_busca(problema)
    print(solucao)
if __name__ == '__main__':
    main()