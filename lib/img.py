from PIL import Image
import os


def new_particle(output_file, x, y, r, g, b, size_tweak=15):
    """
    File sistemashi romelic mocemulia parametrad "output_file" shi wers Minecraftis particle brdzanebas romelic shedgeba mocemuli parametrebidan

    :param output_file: File Sistema romelshic motavsebulia tito frames funqciebi, umetesad gamoisaxeba rogorc frame0.mcfunction
    :param size_tweak: vcvlit rezolucias rom dzalzed didi ar mogvivides da minecraftis clientma chatvirtos kvelaferi, default: 15

    :param x: Fotos x axis ze mocemuli piqselis kordinati (x; ?)
    :param y: Fotos y axis ze mocemuli piqselis kordinati (?; y)

    :param r: Fotos x,y axis ze mocemuli piqselis witeli feris odenobis machvenebeli (0-255)
    :param g: Fotos x,y axis ze mocemuli piqselis mwvane feris odenobis machvenebeli (0-255)
    :param b: Fotos x,y axis ze mocemuli piqselis lurji feris odenobis machvenebeli (0-255)

    :return: None, Abrunebs arafers radganac chven ubralod parametr output_file shi vwert particles brdzanebas
    """
    output_file.write(
        f"particle minecraft:dust {r/255} {g/255} {b/255} 0.75 ^{x/size_tweak} ^{y/size_tweak} ^0 0 0 0 0 1 force @a\n")


def get_data(freimi, size_tweak=15):
    """
    Igebs informacias fotodan ris shedegadac chven shegvidzlia gamovikenot fotos piqselebis kordinatebi da aseve mati RGB machvenebeli

    :param freimi: Freimis sruli saxeli romelic motavsebulia umetesad "frames" foldershi, umetesad formatit frame0.png
    :param size_tweak: vcvlit rezolucias rom dzalzed didi ar mogvivides da minecraftma da serverma chatvirtos kvelaferi, default: 15
    :return: freimi, Abrunebs igive informacias rac parametri freimi sheicavs magram ".png" moshorebulia
    :return: cords, Igebs fotodan piqselis x,y da r,g,b informacias rogorc did masiur lists romelic shemdgom gamoikeneba rogorc "x, y, (r,g,b)" for i loopshi
    """
    image = Image.open(f"frames/{freimi}")  # extension shecvalet ig
    freimi = freimi.replace(".png", "")
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

    # es gatweaket tu mteli foto arspaundeba an racxa schirs, zedmetad mezareba ro tavisit datweakos eseni, mainc xelit gaketebuli sjobs
    new_size = (sigane // size_tweak, simagle // size_tweak)
    image = image.resize(new_size)

    sigane, simagle = image.size

    # image.show()

    data = list(image.getdata())

    # kordinatebs vedzebt rom mere qveda for loopshi gamovixot kordinatebi
    cords = [(x % sigane, x // sigane, val) for x, val in enumerate(data)]
    return freimi, cords


def make_file(freimi):
    """
    Aketebs datapackis funqcias risi shedegad shemdgom kodshi shegvedzleba informaciis chawera

    :param freimi: string variable romelic abrunebs romel frameze vimkofebit, umetesad gamoikofa formatit "frame0" sadac 0 waradgens romel frameze vart
    :return: output, Abrunebs File Sistemas datapackis funqciis romelshic shegvedzleba ragacis chawera (new_particle, eof_schedule)
    """
    if os.path.exists(f"{freimi}.mcfunction"):
        os.remove(f"{freimi}.mcfunction")  # tu arsebobs append ro ar uknas
    output = open(f"vid_funcs_output/{freimi}.mcfunction", "w")
    return output


def eof_schedule(amjamindelifreimi,output, shemdegifreimi) -> None:
    """
    Failis dasasrulshi vumatebt scoreboards da schedules radganac sheikmnas srulkofili animacia/video particlebit

    :param amjamindelifreimi: Tvlis romel frameze vimkofebit amjamad anu frame200 ze tu vart es ricxvi daabrunebs 200
    :param output: File Sistema romelshic motavsebulia tito frames funqciebi, umetesad gamoisaxeba rogorc frame0.mcfunction
    :param shemdegifreimi: Amjamindeli Frame-s momdevno frame anu tu vimkofebit parametr amjamindelifreimi shi 200 ze vutanabrebt am parametrs anu 201
    :return: amjamindelifreimi, amjamindelifreimi parametrs vumatebt 1 s da vabrunebt ukan
    """
    output.write("scoreboard players add @e[tag=fr] frames 1\n")
    #output.write(f"function fr:frame{shemdegifreimi}")
    output.write(f"schedule function fr:frame{shemdegifreimi} 0.2s")
    amjamindelifreimi += 1
    return amjamindelifreimi
