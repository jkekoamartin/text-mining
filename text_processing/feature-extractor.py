import csv
import sys
import timeit
import re
import pandas as pd
from nltk.tokenize import sent_tokenize

start = timeit.default_timer()


# Code written by James Martin

class Extractor:
    """
    This class contains the functions to parse a text and output a csv of numerical attribute.
    Keep a clean copy on hand, but we will be modifying this for different attributes as we progress.
    """

    def __init__(self, text, output):
        self.text = text
        self.output = output

        self.sanitized_text = []
        self.output_array = []

    # todo: stub
    def parse(self):

        # todo: add splitting criteria

        with open(self.text, encoding="utf8") as f:
            content = f.readlines()
        # content = [x.strip() for x in content]

        tokenized_sent = sent_tokenize(content[0])

        sanitized_text = []


        for line in tokenized_sent:
            # control special characters here
            cleaned = re.sub("[“”‘’]", "", line)
            sanitized_text.append(cleaned)


        self.sanitized_text = sanitized_text

    # todo: stub
    def extract(self):

        # note that this removes last list (for some reason, we're getting the entire text appended to the end)
        for sentence in self.sanitized_text:
            temp = [get_sentence_length_char(sentence), get_sentence_length_word(sentence),
                    get_sentence_average_word_len(sentence)]
            self.output_array.append(temp)

        text = pd.DataFrame(self.output_array)

        print(text)

    # todo: stub
    def write(self):

        with open(self.output, 'w', newline='') as csvfile:
            fieldnames = ['sentence_length_char', 'sentence_length_word', 'average_word_length']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # excluding header for now
            # writer.writeheader()

            for line in self.output_array:
                writer.writerow({'sentence_length_char': line[0],
                                 'sentence_length_word': line[1],
                                 'average_word_length': line[2]})

        # out = self.output
        #
        # out = open(out, 'w')
        #
        # # write sse
        # for line in self.output_array:
        #     out.write(str(line) + "\n")
        #
        # out.close()


# non class helper methods
def get_sentence_length_char(sentence):
    return len(sentence) - sentence.count(' ')


def get_sentence_length_word(sentence):
    return len(sentence.split())


def get_sentence_average_word_len(sentence):
    words = sentence.split()
    return sum(len(word) for word in words) / len(words)


def run():
    """
    runs parameters from command line
    """
    # get args
    text, output = sys.argv[1:]

    extractor = Extractor(text, output)
    extractor.parse()
    extractor.extract()
    extractor.write()

    print("Complete. Results written to " + "'" + output + "'")


def testing(text, output):
    """
    runs parameters defined in main method
    """
    extractor = Extractor(text, output)
    extractor.parse()
    extractor.extract()
    extractor.write()


if __name__ == "__main__":
    # check correct length args
    # if no command line args, uses these parameters
    if len(sys.argv) == 1:
        testing("rawtext/californianstale.txt", "outputs/cali_output.csv")
    elif len(sys.argv[1:]) == 2:
        print("Generating results")
        run()
    else:
        print("Invalid number of arguments passed. Please input: [text.txt output.csv]")

stop = timeit.default_timer()

print("Results in " + str(stop - start) + " seconds")
