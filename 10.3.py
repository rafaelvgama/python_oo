# Modifique a classe Televisão de forma que se pedirmos para mudar 
# o canal para baixo, além do mínimo, ela vá para o canal máximo. Se mudarmos 
# para cima, além do canal máximo, que volte ao canal mínimo.

class Televisao:
  def __init__(self, canalInicio, canalMin, canalMax):
    self.ligada = False
    self.canal = canalInicio
    self.canalMin = canalMin
    self.canalMax = canalMax
    self.tamanho = 32
    self.marca = 'LG'

  def mudar_canal_para_baixo(self):
        if self.canal -1 >= self.canalMin:
            self.canal -= 1
        else:
            self.canal = self.canalMax

  def mudar_canal_para_cima(self):
      if self.canal + 1 <= self.canalMax:
          self.canal += 1
      else:
          self.canal = self.canalMin


tv = Televisao(99, 1, 99)
print(f'O canal inicial é {tv.canal}.')
print(f'O canal mínimo é {tv.canalMin}.')
print(f'O canal máximo é {tv.canalMax}.\n')

tv.mudar_canal_para_baixo()
print('Canal para baixo:')
print(f'O canal atual é {tv.canal}.\n')

tv.mudar_canal_para_cima()
tv.mudar_canal_para_cima()
tv.mudar_canal_para_cima()
print('Canal para cima:')
print(f'O canal atual é {tv.canal}.\n')

