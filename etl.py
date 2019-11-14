#libraries
import pandas as pd
import re
from sklearn.feature_extraction import text
from num2words import num2words
import time


class PropertyData:

    def __init__(self, column):
        self.address = pd.Series(column)

    def transformText(self):

        non_ascii = re.compile(r'[^\x00-\x7F]') # non ascii chraracters
        punctuations = re.compile(r'[^\w\s]') # punctuations i.e. non digits strings and spaces
        stop = text.ENGLISH_STOP_WORDS # get stop words using sklearn libray store in list stop

        # convert string to lower case, then remove non ascii characters, then remove punctuation marks and finaly remove last occurence duplicates
        address = self.address.str.lower().apply(lambda x: non_ascii.sub('', x)).apply(lambda x: punctuations.sub('', x)).apply(lambda x: self.remove_duplicates(x))

        # str.split() splits all words into an item in a list and uses white spaces as seperators
        address = address.str.split()

        # remove words that appear in stop words list
        address = address.apply(lambda x: [word for word in x if word not in stop])
        address = address.apply(lambda x: ' '.join(word for word in x))

        # convert ordinal numbers in string
        address = address.apply(lambda x: self.conv_ordinal(x))
        return address

    # function to remove duplicates
    def remove_duplicates(self,x):
        ''' reverses the string if the first word has a duplicate entry it is
            replaced with an empty string.
            designed to target instances like 21 BEECHFIELD WAY, CASTAHENY DUBLIN 15, DUBLIN
            and ignore instances like 183 DOORADOYLE PARK, DOORADOYLE ROAD, LIMERICK
            as targeting the latter may lead to a loss of important information
        '''
        text = x[::-1] # reverse the string
        duplicates = re.compile(r'^\b(\w+)\b(?=.*\b\1\b)')
        text = duplicates.sub('', text) # use regex to replace repeated word with empty string
        text = text[::-1] # reverse the string back to normal

        return text

    # function to convert ordinal numbers in address string to words
    def conv_ordinal(self,x):
        word = x.split()
        string_list = []

        for w in word:
            if bool(re.search('^(\d+(st|nd|rd|th))$', w)): # regex to search for an exact ordinal pattern in word
                number = int(w[:-2])
                w = num2words(number, ordinal=True)
            string_list.append(w)

        string_joined  = ' '.join(string_list)

        return string_joined

    def save_file(self, df, col, col_name):
        df[col_name] = col
        df.to_csv('new_properties.csv',index=False)


def main():

    start = time.time()

    properites_df = pd.read_csv("properties.csv")
    prop_addy = PropertyData(properites_df['Address'])
    address = prop_addy.transformText()

    print(str(len(address)) + " street addresses transformed" )

    prop_addy.save_file(properites_df, address, "Address")

    print("file saved as new_properties.csv")
    print("Process time: " + str(time.time() - start) + " seconds")


if __name__ == '__main__':
    main()
