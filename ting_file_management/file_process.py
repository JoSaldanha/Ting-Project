import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if any(path_file in item for item in instance.queue):
        return instance

    content = txt_importer(path_file)
    if content is not None:
        new_dict = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(content),
            "linhas_do_arquivo": content
        }
        
        instance.enqueue({path_file: new_dict})
        sys.stdout.write(str(new_dict))
    
    return instance


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
