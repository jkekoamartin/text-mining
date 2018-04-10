import sys
import timeit

start = timeit.default_timer()


# Code written by James Martin

class Extractor:
    """
    This class contains the functions to parse a text and output a csv of numerical attribute.
    Keep a clean copy on hand, but we will be modifying this for different attributes as we progress.
    """

    def __init__(self, text, output):
        self.output = output

    def parse(self):
        pass

    def extract(self):
        pass

    def write(self):

        out = self.output

        out = open(out, 'w')

        # write sse
        out.write("\n")
        out.close()


def run():
    # get args
    text, output = sys.argv[1:]

    extractor = Extractor(text, output)

    print("Complete. Results written to " + "'" + output + "'")


# this is used to run a data set with 2=> k <=10 and get the average of 10 runs for each k
def testing(text, output):
    extractor = Extractor(text, output)


if __name__ == "__main__":
    # check correct length args
    if len(sys.argv) == 1:
        testing("late_encounter.txt", "encounter_output.csv")
    elif len(sys.argv[1:]) == 2:
        print("Generating results")
        run()
    else:
        print("Invalid number of arguments passed. Please input: [text.txt output.csv]")

stop = timeit.default_timer()

print("Results in " + str(stop - start) + " seconds")
