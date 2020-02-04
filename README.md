# py-data-tools

Some utility scripts and notebooks

### csv2gdf.py

Script to convert CSV files to GDF Gephi compatible format

```
python csv2gdf.py -f tweets.csv
```

### clean_tweets.py

Script to convert clean and output CSV column to a textfile

```
python clean_tweets.py [-i tweets.csv] [-o tweets_clean.txt] [-c tweet]
python clean_tweets.py [--input tweets.csv] [--output tweets_clean.txt] [--column tweet]
```

### dependencies

* Python 3.5
* [demoji](https://github.com/bsolomon1124/demoji)
* [gdf-formatter](https://github.com/GabrielTrettel/GDF_Formatter)
