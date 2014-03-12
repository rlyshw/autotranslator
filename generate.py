import sys, argparse, csv, goslate

def translate(word, lang, api):
    if api == "goog":
        gs = goslate.Goslate()
        return gs.translate(str(word), str(lang))
    
def main():
    inputfile = 'in.csv'
    outputfile = 'out.csv'
    langs = ['zh','de']
    api = 'goog'
    try:
        with open(inputfile, 'rb') as infile:
            inreader = csv.reader(infile)
            with open(outputfile, 'wb+') as outfile:
                outwords = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL,
                                      delimiter=',')
                for row in inreader:
                    for lang in langs:
                        row.append(translate(row[0],lang, api).encode('utf-8'))
                    outwords.writerow(row)
    except IOError as e:
        print 'cannot open', inputfile
        print e.strerror

if __name__ == "__main__":
   main()
