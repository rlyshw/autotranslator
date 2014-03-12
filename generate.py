import sys, argparse, csv, goslate, Translate

def translate(word, lang, api):
    if api == "goog":
        gs = goslate.Goslate()
        return gs.translate(str(word), str(lang))
    
def main(argv):
    inputfile = 'in.csv'
    outputfile = 'out.csv'
    lang = 'de'
    api = 'goog'
    
    print 'Input file is ', inputfile
    print 'Output file is ', outputfile
    try:
        with open(inputfile, 'rb') as infile:
            inreader = csv.reader(infile)
            with open(outputfile, 'wb+') as outfile:
                outwords = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL,
                                      delimiter=',')
                for row in inreader:
                    outwords.writerow([row[0],
                                       translate(row[0],lang, api)])
    except IOError as e:
        print 'cannot open', inputfile
        print e.strerror
if __name__ == "__main__":
   main(sys.argv[1:])
