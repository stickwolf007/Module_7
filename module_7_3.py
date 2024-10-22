class WordsFinder:
    def __init__(self, *file_names ):
        self.file_names  = file_names

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for j in text:
                    if j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        text = text.replace(j, '')
                words_in_text = text.split()
                all_words[file.name] = words_in_text
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        for name, i in self.get_all_words().items():
            if word in i:
                result[name] = i.index(word) + 1
            break
        return result

    def count(self,word):
        word = word.lower()
        result = {}
        for name, i in self.get_all_words().items():
            result[name] = i.count(word)
        return result

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))