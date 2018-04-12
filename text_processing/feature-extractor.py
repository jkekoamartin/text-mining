import sys
import timeit
import pandas as pd

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
        # read into dataframe
        text = pd.read_csv(self.text, header=None, delimiter=r".")

        nump_arr = text.as_matrix()

        for each in nump_arr:
            print(each)
    # we need to account for abbreviations, since we are using . as a delimiter


    # todo: stub
    def extract(self):
        pass

    # todo: stub
    def write(self):

        out = self.output

        out = open(out, 'w')

        # write sse
        out.write("\n")
        out.close()


def run():
    """
    runs parameters from command line
    """
    # get args
    text, output = sys.argv[1:]

    extractor = Extractor(text, output)

    print("Complete. Results written to " + "'" + output + "'")


def testing(text, output):
    """
    runs parameters defined in main method
    """
    extractor = Extractor(text, output)
    extractor.parse()


if __name__ == "__main__":
    # check correct length args
    # if no command line args, uses these parameters
    if len(sys.argv) == 1:
        testing("late_encounter.txt", "encounter_output.csv")
    elif len(sys.argv[1:]) == 2:
        print("Generating results")
        run()
    else:
        print("Invalid number of arguments passed. Please input: [text.txt output.csv]")

stop = timeit.default_timer()

print("Results in " + str(stop - start) + " seconds")
