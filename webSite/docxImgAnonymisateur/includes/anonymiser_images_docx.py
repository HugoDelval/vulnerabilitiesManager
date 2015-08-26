# coding: utf8
from tempfile import mkstemp
import zipfile  # docx est au format zip
import os
import shutil  # operations fichiers
from PIL import Image, ImageFilter
import sys
import getopt
import re


def decompress(temp_directory, inputfile):
    zfile = zipfile.ZipFile(inputfile)
    archive_list = []
    for name in zfile.namelist():
        sous_dossiers_et_fichier = name.split('/')
        fin_absolute_path = ''
        for dossier in sous_dossiers_et_fichier:
            fin_absolute_path = os.path.join(fin_absolute_path, dossier)
        file_absolute_path = os.path.join(temp_directory, fin_absolute_path)
        archive_list.append(file_absolute_path)
        zfile.extract(name, temp_directory)
    return archive_list


def floute_images(directory, blur_radius):
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        im = Image.open(f)
        myBlur = ImageFilter.GaussianBlur(radius=blur_radius)
        im = im.filter(myBlur)
        im.save(f)


# TODO: 
# cette méthode ne semble pas stable sous windows, à débugger et modifier 
def replace(word_directory, hash_find_replace):
    for file in os.listdir(word_directory):
        if file.startswith("header") or file == "document.xml":
            fh, abs_path = mkstemp()
            file_path = word_directory + file
            with open(abs_path, 'w') as new_file:
                with open(file_path) as old_file:
                    for to_search in hash_find_replace:
                        for line in old_file:
                            # ça plante souvent ici à cause des encodages.. 
                            new_file.write(re.sub(to_search.decode('utf8'),
                                hash_find_replace[to_search].decode('utf8'),
                                line, flags=re.IGNORECASE))
            os.close(fh)
            #Remove original file
            os.remove(file_path)
            #Move new file
            shutil.move(abs_path, file_path)


"""
inputfile: chemin absolu vers le docx à anonymiser
outputdirectory: chemin absolu vers le dossier où ecrire le fichier anonyme
blur_radius: le facteur de flou
hash_find_replace: hash sous la forme {'mot à rechercher': 'mot à substituer'}
ROLE: ecrit un nouveau docx sous 'outputdirectory' en se basant sur le docx 'inputfile',
        en floutant les images et remplaçant les mots suivants hash_find_replace
"""
def process(inputfile, outputdirectory, blur_radius=17, hash_find_replace={}):
    # ex : /appli/includes/doc_anonyme/dossier_anonme_1.docx
    temp_directory = os.path.join(outputdirectory, 'dossier_anonyme_' + os.path.basename(inputfile))
    # ex : /appli/includes/doc_anonyme/anonyme_1.docx
    document_anonymise = os.path.join(outputdirectory, 'anonyme_' + os.path.basename(inputfile))
    # on decompresse le docx dans un dossier, pour faire les modifs sur les photos tranquilement dans ce dossier
    archive_list = decompress(temp_directory, inputfile)

    # maintenant on attaque la modif des images
    floute_images(os.path.join(os.path.join(temp_directory, 'word'), 'media'), blur_radius)
    # puis les find/replace
    if hash_find_replace:
        # TODO: 
        # cette méthode ne semble pas stable sous windows, à débugger et modifier 
        replace(os.path.join(temp_directory, 'word'), hash_find_replace)

    # puis on recompresse le tout en un fichier docx
    zout = zipfile.ZipFile(document_anonymise, "w", zipfile.ZIP_DEFLATED)
    for fname in archive_list:
        zout.write(fname, fname[len(temp_directory):])
    zout.close()
    shutil.rmtree(temp_directory)

######################################
# la suite est utile pour tester le script en ligne de commande
######################################
def error_input():
    print "Erreur, l'outil s'utilise comme suit : "
    print __file__ + ' -i <inputfile> -o <output_directory> [-b <blur_radius>]'
    print 'Note: blur_radius = 17 par default'
    sys.exit(2)


def main(argv):
    inputfile = ''
    outputdirectory = ''
    blur_radius = 17
    try:
        opts, args = getopt.getopt(argv, "hi:o:b:", ["ifile=", "odirectory="])
    except getopt.GetoptError:
        error_input()
    for opt, arg in opts:
        if opt == '-h':
            print "Utilisation de l'outil :"
            print __file__ + ' -i <inputfile> -o <output_directory> [-b <blur_radius>]'
            print 'Note: blur_radius = 17 par default'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputdirectory = arg
        elif opt in ("-b", "--blurradius"):
            blur_radius = int(arg)
    if inputfile == '' or outputdirectory == '' or blur_radius <= 0:
        error_input()
    process(inputfile, outputdirectory, blur_radius)


if __name__ == "__main__":
    main(sys.argv[1:])
