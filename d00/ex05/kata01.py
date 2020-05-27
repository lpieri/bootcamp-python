if __name__ == "__main__":
    languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
        }
    for key, val in languages.items():
        toPrint = "{k} was created by {v}"
        print(toPrint.format(k=key, v=val))
