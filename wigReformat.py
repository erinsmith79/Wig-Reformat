[200~import os


os.chdir("/Users/erinsmith/Downloads")

def wigreformat(filename):
    chr=""
    f=open(filename, "r")
    outputFile=open("outputFile.txt", "w")
    for line in f:
        if line.startswith("track"):
            continue #  skip header
        if line.startswith("variableStep"):
            for term in line.rstrip().split():
                terms=term.split("=")
                if len(terms)==2 and terms[0]=="chrom":
                    chr=terms[1]
        else:
            vals=line.rstrip().split()
            if len(vals)==2:
                outputFile.write(f"{chr}\t{vals[0]}\t{vals[1]}\n")

    f.close()
    outputFile.close()

wigreformat("nucdata.wig")
