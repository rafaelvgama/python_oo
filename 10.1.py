# 10.1: Adicione atributos de tamanho e marca à classe Televisão.
# Crie dois objetos Televisão e atribua tamanhos e marcas diferentes.
# Depois, imprima o valor desses atributos de forma a confirmar
# a independência dos valores de cada instância (objeto).

class Televisao:
  def __init__(self):
    self.ligada = False
    self.canal = 2
    self.tamanho = 32
    self.marca = 'LG'

tv_quarto = Televisao()
tv_quarto.ligada = True
tv_quarto.canal = 10
tv_quarto.tamanho = 43
tv_quarto.marca = 'Sony'
print(f'Ligada? {tv_quarto.ligada}')
print(f'Canal: {tv_quarto.canal}')
print(f'Tamanho: {tv_quarto.tamanho}')
print(f'Marca: {tv_quarto.marca}')

print(10 * "=-" + "=")

tv_sala = Televisao()
tv_sala.ligada = True
tv_sala.canal = 4
tv_sala.tamanho = 55
tv_sala.marca = 'Samsung'
print(f'Ligada? {tv_sala.ligada}')
print(f'Canal: {tv_sala.canal}')
print(f'Tamanho: {tv_sala.tamanho}')
print(f'Marca: {tv_sala.marca}')
