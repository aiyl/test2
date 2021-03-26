import wikipediaapi

def categorymembers(categorymembers):
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧЪЬШЩЫЭЮЯ"
    count = 0
    first = 'А'
    list = []
    for c in categorymembers.values():
        char = c.title[0]
        if char in alphabet:
            if first != char:
                #print(first, ': ', count)
                list.append([first, count])
                first = char
                count = 1
            else:
                count += 1
    for i in range(len(list) - 1):
        for j in range(i+1, len(list)):
            if list[i][0] == list[j][0]:
                list[i][1] += list[j][1]
                list[j][1] = 0


    return list

if __name__ == '__main__':
    wiki_wiki = wikipediaapi.Wikipedia('ru')
    cat = wiki_wiki.page("Категория:Животные по алфавиту")
    list = categorymembers(cat.categorymembers)
    for i in range(len(list)):
        if list[i][1] != 0:
            print(list[i][0], ': ', list[i][1])
