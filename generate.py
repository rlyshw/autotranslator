import sys, argparse, csv, goslate

def translate(word, target, detect, source, api):
    if api == "goog":
        gs = goslate.Goslate()
        if detect:
            return gs.translate(str(word), str(target), gs.detect(source))
        elif not detect:
            return gs.translate(str(word), str(target), source)

def main():
    inputfile = 'in.csv'
    outputfile = 'out.csv'
    langs = ['zh','de','fr']
    api = 'goog'
    try:
        with open(inputfile, 'rb') as infile:
            inputreader = csv.reader(infile)
            with open(outputfile, 'wb+') as outfile:
                outwords = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL,
                                      delimiter=',')
                for row in inputreader:
                    for lang in langs:
                        row.append(translate(row[0], lang, True,
                                   row[0], api).encode('utf-8'))
                    outwords.writerow(row)
    except IOError as e:
        print 'cannot open', inputfile
        print e.strerror

if __name__ == "__main__":
   main()
