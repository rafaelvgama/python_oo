# 10.2: Atualmente, a classe Televisão inicializa o canal com 2.StopAsyncIteration
# Modifique a classe Televisão de forma a receber o canal inicial em seu construtor.


class Televisao:
  def __init__(self, canalInicial):
    self.ligado = False
    self.canal = canalInicial
  def muda_canal_para_baixo(self):
    if self.canal <= 0:
      self.canal 
  def muda_canal_para_cima(self):
    self.canal += 1

tv = Televisao(5)

print (f'O canal atual é o {tv.canal}.\n')
