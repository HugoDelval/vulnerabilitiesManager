#!/usr/bin/python
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
        (dirname, filename) = os.path.split(name)
        dirname = temp_directory + '/' + dirname
        archive_list.append(dirname + '/' + filename)
        zfile.extract(name, temp_directory)
    return archive_list


def floute_images(directory, blur_radius):
    for filename in os.listdir(directory):
        im = Image.open(directory + filename)
        myBlur = ImageFilter.GaussianBlur(radius=blur_radius)
        im = im.filter(myBlur)
        im.save(directory + filename)


def replace(word_directory, hash_find_replace):
    for file in os.listdir(word_directory):
        if file.startswith("header") or file == "document.xml":
            fh, abs_path = mkstemp()
            file_path = word_directory + file
            with open(abs_path, 'w') as new_file:
                with open(file_path) as old_file:
                    for to_search in hash_find_replace:
                        for line in old_file:
                            new_file.write(re.sub(to_search, hash_find_replace[to_search],
                                line.decode('ascii', 'ignore'), flags=re.IGNORECASE))
            os.close(fh)
            #Remove original file
            os.remove(file_path)
            #Move new file
            shutil.move(abs_path, file_path)


def process(inputfile, outputdirectory, blur_radius=17, hash_find_replace={}):
    temp_directory = outputdirectory + 'dossier_anonyme_' + inputfile.split('/')[-1]
    document_anonymise = outputdirectory + 'anonyme_' + inputfile.split('/')[-1]
    # on decompresse le docx dans un dossier, pour faire les modifs sur les photos tranquilement dans ce dossier
    archive_list = decompress(temp_directory, inputfile)

    # maintenant on attaque la modif des images
    floute_images(temp_directory + '/word/media/', blur_radius)
    # puis les find/replace
    if hash_find_replace:
        replace(temp_directory + '/word/', hash_find_replace)

    # puis on recompresse le tout en un fichier docx
    zout = zipfile.ZipFile(document_anonymise, "w", zipfile.ZIP_DEFLATED)
    for fname in archive_list:
        zout.write(fname, fname[len(temp_directory):])
    zout.close()
    # shutil.rmtree(temp_directory)


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
