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
    results = []

    for file_dict in instance.queue:
        for file_name, file_data in file_dict.items():
            occurrences = [
                {"linha": line_number, "conteudo": line}
                for line_number,
                line in enumerate(file_data["linhas_do_arquivo"], start=1)
                if word.lower() in line.lower()
            ]
            if occurrences:
                results.append({
                    "palavra": word,
                    "arquivo": file_name,
                    "ocorrencias": occurrences
                })

    return results
