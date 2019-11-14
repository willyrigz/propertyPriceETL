# propertyPriceETL

An ETL script that reads the property.csv file and transforms it based on the following parameters
- Text should be lowercase
- Remove duplicates (last occurrence)
- Remove non-ascii characters
- Remove unwanted spaces, tabs or newlines
- Remove english stopwords and punctuation
- Convert ordinal numbers (e.g. from 1st, 2nd, 3rd to first, second, third)

The test_etl.py file applies unit testing to the script
