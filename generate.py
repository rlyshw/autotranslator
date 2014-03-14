import sys, argparse, csv, goslate

def translate(word, target, source, api):
    if api == "goog":
        gs = goslate.Goslate()
        return gs.translate(str(word), str(target), source)

def main():
    inputfile = 'in.csv'
    outputfile = 'out.csv'
    api = 'goog'
    with open(inputfile, 'rb+') as infile:
        inputreader = csv.reader(infile)
        langs = inputreader.next()
        with open(outputfile, 'wb+') as outfile:
            outwords = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)
            for row in inputreader:
                for l in range(1,len(langs)):
                    row.append(translate(row[0], langs[l],
                               langs[0], api).encode('utf-8'))
                outwords.writerow(row)

if __name__ == "__main__":
    main()
