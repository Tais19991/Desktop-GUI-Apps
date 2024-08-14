class TextManager:

    def __init__(self, file_path: str):
        self.text_file = file_path
        self.text_list = []
        self.words_uploaded = []  # words showed for user
        self.user_words = []  # words entered by user

    def read_text_file(self) -> list:
        """Open, read, close text file and save list of words"""
        with open(self.text_file) as file:
            text = file.read()
            self.text_list = text.split()
        return self.text_list

    def get_clear_words(self, text: str) -> list:
        """Split text to words and clear words from symbols"""
        clear_words = []
        words = text.split()
        for word in words:
            clear_word = word.strip(",.:;()\"'?! ")
            clear_words.append(clear_word)

        return clear_words

    def get_user_text(self, text: str) -> None:
        """Get text entered by user, split and clear words, save to class variable"""
        self.user_words = self.get_clear_words(text)

    def get_example_text(self, text: str) -> None:
        """Get example text, split and clear words, add to class variable"""
        self.words_uploaded += self.get_clear_words(text)
        print(self.words_uploaded)

    def final_check_user_text(self) -> tuple:
        """Compare list of user words and list of uploaded example words
        Return total number of words, num of correct words, str of words with mistakes"""
        num_user_words = len(self.user_words)
        num_correct_user_words = 0
        words_with_mistakes = ''
        for index in range(0, num_user_words):
            if self.user_words[index] == self.words_uploaded[index]:
                num_correct_user_words += 1
            elif self.user_words[index] != self.words_uploaded[index]:
                words_with_mistakes += f"{self.words_uploaded[index]}   -   {self.user_words[index]}\n"

        if words_with_mistakes == "":
            words_with_mistakes = "No typo found"

        return num_correct_user_words, num_user_words, words_with_mistakes

    def reset_text_manager(self) -> None:
        """Reset class variables to initial state"""
        self.words_uploaded.clear()
        self.user_words.clear()
