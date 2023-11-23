from lib.img import new_particle, get_data, make_file, eof_schedule
from lib.sisulelebi import loading, spinner

from fs import open_fs
from colorama import Style
freimebi = open_fs('./').listdir('/frames') # vxsnit frames folders rom amovixot kvela frame
amjamindelifreimi = 0

for freimi in freimebi:
    freimi, cords = get_data(freimi) # ar dagavickdet size_tweaks shecvla romelic aris meore parametri default 15 ia, example: get_data(freimi,30)

    output = make_file(freimi)
    for x, y, (r, g, b) in cords:
        new_particle(output, x, y, r, g, b) # get_data ze ra komentaric weria eg amasac exeba default 15 ia isev da example : new_particle(output, x, y, r, g, b, 30)
        # rogorc chans rgbs gamokeneba shesadzloa minecraftshi tu mas 255 ze gavkoft
        # ik 15 zerovkof sigrdze da siganea mara sheidzlebaminecraftma daalimitos amitomac ise datovet ravacari an shegidzliat kide 20 ze gazardot, magas jobia new_size mixedot
        # an shegidzliat 90 ze gakot 15 an ramecifri da sanam 0.(x) ar izams da wesier periods tu damavickda ra kvia ar gamoixebs makamde echalichet ro datapackis zoma daiwios cuz 0.33333333333333333 da egremidis da iwevs

    # vashorebt string "frame2" s "frames" rom gamovikenot shemdeg funqciebshi (loading, eof_schedule)
    clean_count = freimi.replace("frame", "")
    # vumatebt 1 s amjamindel frames rom gavigot romelia shemdegi frame
    next_Frame = int(clean_count)+1
    shemdegifreimi = str(next_Frame)  # ubralod string ad vakcevt tore errors

    amjamindelifreimi = eof_schedule(amjamindelifreimi,output, shemdegifreimi)
    frames_length = len(freimebi)

    print(f"{loading(amjamindelifreimi, frames_length)} {next(spinner)}{Style.RESET_ALL}", end='\r')
print("\nFramebis gaketeba dasrulda, shegidzliat moinaxulot isini vid_funcs_output foldershi")