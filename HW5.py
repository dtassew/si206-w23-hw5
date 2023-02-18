# Your name:
# Your student id:
# Your email:
# List who you have worked with on this homework:

import re, os, unittest

def read_file(filename):
    """ Return a list of the lines in the file with the passed filename """

    # Open the file and get the file object
    source_dir = os.path.dirname(__file__) #<-- directory name
    full_path = os.path.join(source_dir, filename)
    infile = open(full_path,'r', encoding='utf-8')

    # Read the lines from the file object into a list
    lines = infile.readlines()

    # Close the file object
    infile.close()

    # return the list of lines
    return lines

def create_names_dict(lines_list):
    """
    This function returns a dictionary with the keys being numbers, (1 - 10)
    and the values being a tuple made up of the first and last name from each biography subject
    """
    pass

def find_compound_words(lines_list):
    """
    This function finds all hyphenated compound words
    """
    pass

def find_long_words(lines_list):
    """
    This function finds all words between 12 and 20 letters (both inclusive) used in the text file 
    and returns a tuple. The first value should be a list of all long words found and the second value 
    should be the average length of those found words.
    """
    pass

def create_short_bios(lines_list):
    """
    This function returns a list containing the first sentence of each person’s bio.
    """
    pass

## Extra credit
def calculate_in_middle(mid, lines_list):
    """
    This function returns a count of the number of times a specified string appears
    in the text. The matched string should be in the middle of a word, not at 
    the start or end
    """
    pass

#Implement your own tests
class TestAllMethod(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_create_names_dict(self):
        pass

    def test_find_compound_words(self):
        pass

    def test_find_long_words(self):
        pass

    def test_create_short_bios(self):
        pass

    #Uncomment if working on Extra Credit
    #def test_calculate_in_middle(self):
    #    pass

def main():
    #Feel free run your functions here as well!    
    pass

if __name__ == '__main__':
    main()
    print()
    unittest.main(verbosity=2)