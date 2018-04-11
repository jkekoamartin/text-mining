import sys
import timeit

start = timeit.default_timer()


# Code written by James Martin

class Extractor:
    """
    This class contains the functions to parse a text and output a csv of numerical attribute.
    Keep a clean copy on hand, but we will be modifying this for different attributes as we progress.
    """

    # todo: stub
    def __init__(self, text, output):
        self.output = output

    def parse(self):
        pass

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
