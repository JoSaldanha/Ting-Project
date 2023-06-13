import sys
import os


def txt_importer(path_file):
    if os.path.splitext(path_file)[1] != ".txt":
        sys.stderr.write("Formato inválido")
    try:
        with open(path_file, 'r') as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines]
        return lines
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
