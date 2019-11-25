import pymorphy2
morph = pymorphy2.MorphAnalyzer()

f = open(r"C:\Users\Elisaveta\Desktop\Coursework\2 level.txt", encoding = "UTF-8")
first_part = f.read()
f.close()

list1 = []
first_part = first_part.split()
for word in first_part:
    clean_word = word.strip("!.,?[]':;")
    clean_word = clean_word.replace('"', '').replace('?','').replace('!','').strip()
    list1.append(clean_word)

list_1 = []
for word in list1:
    p = morph.parse(word)[0]
    list_1.append(p.normal_form)



d = dict(zip(list1, list_1))
with open(r".\Lemmatized.txt", "w") as fw:
    for word in d:
        fw.write("{} \t {}\n".format(word, d[word]))

