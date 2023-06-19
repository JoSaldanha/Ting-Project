def exists_word(word, instance):
    results = []
    
    for file_data in instance.queue:
        occurrences = []
        
        lines = file_data.values()
        occurrences.append(lines)
        # for line_number, line in enumerate(lines, start=1):
        #     if word.lower() in line.lower():
        #         occurrences.append({"linha": line_number})
        
        # if occurrences:
        #     result = {
        #         "palavra": word,
        #         "arquivo": file_data["nome_do_arquivo"],
        #         "ocorrencias": occurrences
        #     }
        #     results.append(result)
    
    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
