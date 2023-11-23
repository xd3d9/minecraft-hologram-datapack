from PIL import Image
import os

fotos_saxeli = "marine" # extension ar ari sachiro

image = Image.open(f"{fotos_saxeli}.png") # extension shecvalet ig
'''
#ES FOTO ROM SHAVIA DAMNASHAVE ES KODIA
image = image.convert('L')
image = image.point( lambda p: 255 if p > 100 else 0 )
image = image.convert('1')
'''

# zogjer es sachiroa zogjer ara, tu foto amotrialebulia es nawili daakomentaret
# https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.transpose
image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

sigane, simagle = image.size

new_size = (sigane // 5, simagle // 5) # es gatweaket tu mteli foto arspaundeba an racxa schirs, zedmetad mezareba ro tavisit datweakos eseni, mainc xelit gaketebuli sjobs
image = image.resize(new_size)

sigane, simagle = image.size

#image.show()

data = list(image.getdata())

# kordinatebs vedzebt rom mere qveda for loopshi gamovixot kordinatebi
cords = [(x % sigane, x // sigane, val) for x, val in enumerate(data)]

if os.path.exists(f"{fotos_saxeli}.mcfunction"):
    os.remove(f"{fotos_saxeli}.mcfunction") # tu arsebobs append ro ar uknas
output = open(f"{fotos_saxeli}.mcfunction","w") 
for x, y, (r,g,b) in cords:
    output.write(f"particle minecraft:dust {r/255} {g/255} {b/255} 0.75 ^{x/15} ^{y/15} ^0 0 0 0 0 1 force @a\n") 
    #rogorc chans rgbs gamokeneba shesadzloaminecrafti tu mas 255 ze gavkoft
    #ik 15 zerovkof sigrdze da siganea mara sheidzlebaminecraftma daalimitos amitomac ise datovet ravacari an shegidzliat kide 20 ze gazardot, magas jobia new_size mixedot
    # an shegidzliat 90 ze gakot 15 an ramecifri da sanam 0.(x) ar izams da wesier periods tu damavickda ra kvia ar gamoixebs makamde echalichet ro datapackis zoma daiwios cuz 0.33333333333333333 da egremidis da iwevs
    #^^ an tu damavickda ro damrgvalebis racxa chavteno tkvenit gaaketet (0.1(6) -> 0.2)
print(f"datapackis funqcia sheikmna, shegidzliat naxot is {fotos_saxeli}.mcfunction shi, kordinatebis raodenoba {len(cords)}")