import transliterate

f = open(r".\Surnames russian.txt", "r", encoding = "UTF-8")
list1 = f.readlines()
f.close()
list_of_surnames = []
for w in list1:
    if w:
        list_of_surnames.append(w.strip())
        
list_of_surnames_english = []
for n in list_of_surnames:
    if n:
        name = transliterate.translit(n, reversed=True)
        list_of_surnames_english.append(name)
        

d = dict(zip(list_of_surnames, list_of_surnames_english))

with open(r".\Dictionary of surnames.txt", "w") as fw:
    for word in d:
        fw.write("{} \t {}\n". format(word, d[word]))

