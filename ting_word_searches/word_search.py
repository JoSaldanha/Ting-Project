def exists_word(word, instance):
    results = [
        {
            "palavra": word,
            "arquivo": file_key,
            "ocorrencias": [
                {"linha": line_number}
                for line_number,
                line in enumerate(file_data["linhas_do_arquivo"], start=1)
                if word.lower() in line.lower()
            ]
        }
        for file_dict in instance.queue
        for file_key, file_data in file_dict.items()
        if any(word.lower()
               in line.lower() for line in file_data["linhas_do_arquivo"])
    ]

    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
