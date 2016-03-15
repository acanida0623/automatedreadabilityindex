def main():
    ARI = 0
    while True:
        user_string = str(input("Please input the text you would like to find the ARI of: ")).lower()
        ari_string = User_String(user_string)
        ari_string.create_string_list()
        ari_string.get_characters()
        ari_string.get_sentences()
        ari_string.get_words()

        ARI = 4.71 * (ari_string.characters / ari_string.words) + 0.5 * (ari_string.words / ari_string.sentences) - 21.43

        print("The ARI index of the string is {ari}. ".format(ari=round(ARI,2)))



class User_String():
    def __init__(self,string):
        self.string = string
        self.string_list = []
        self.characters = 0
        self.words = 0
        self.sentences = 0
    def create_string_list(self):
        for x in range(len(self.string)):
            self.string_list.append(self.string[x])
    def get_characters(self):
        characters = 'abcdefghijklmnoqrstuvwxyz1234567890'
        character_list = [x for x in self.string_list if x in characters]
        self.characters = len(character_list)
    def get_words(self):
        spaces = ' '
        space_list = [x for x in self.string_list if x in spaces]
        self.words = len(space_list) + 1
    def get_sentences(self):
        periods = '.?!'
        period_list = [x for x in self.string_list if x in periods]
        self.sentences = len(period_list) + 1

main()


"""Score	Age	Grade Level
1	5-6	Kindergarten
2	6-7	First Grade
3	7-8	Second Grade
4	8-9	Third Grade
5	9-10	Fourth Grade
6	10-11	Fifth Grade
7	11-12	Sixth Grade
8	12-13	Seventh Grade
9	13-14	Eighth Grade
10	14-15	Ninth Grade
11	15-16	Tenth Grade
12	16-17	Eleventh grade
13	17-18	Twelfth grade
14	18-22	College"""
