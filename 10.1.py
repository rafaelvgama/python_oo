class Televisao:
  def __init__(self):
    self.ligada = False
    self.canal = 2
    self.tamanho = 32
    self.marca = 'LG'

tv = Televisao()
print(f'Ligada? {tv.ligada}')
print(f'Canal: {tv.canal}')
print(f'Tamanho: {tv.tamanho}')
print(f'Marca: {tv.marca}')

print(10 * "=-" + "=")

tv_sala = Televisao()
tv_sala.ligada = True
tv_sala.canal = 4
print(f'Ligada? {tv_sala.ligada}')
print(f'Canal: {tv_sala.canal}')
print(f'Tamanho: {tv_sala.tamanho}')
print(f'Marca: {tv_sala.marca}')
