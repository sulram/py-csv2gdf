import csv
import util
from optparse import OptionParser

def main():
    parser = OptionParser(usage="usage: %prog [--input tweets.csv] [--output tweets_clean.txt] [--column tweet]",
                          version="%prog 1.0")
    parser.add_option("-i", "--input", dest="input", default="tweets.csv",
	    help="the input CSV file",)
    parser.add_option("-c", "--column", dest="column", default="tweet",
	    help="the CSV column to be cleaned and saved",)
    parser.add_option("-o", "--output", dest="output", default="tweets_clean.txt",
	    help="the output text file to be saved",)
    (options, args) = parser.parse_args()

    with open(options.output, "w") as my_output_file:
        with open(options.input, "r") as my_input_file:
            [my_output_file.write("".join(util.clean(row[options.column]))+'\n') for row in csv.DictReader(my_input_file)]
        my_output_file.close()

if __name__ == '__main__':
    main()