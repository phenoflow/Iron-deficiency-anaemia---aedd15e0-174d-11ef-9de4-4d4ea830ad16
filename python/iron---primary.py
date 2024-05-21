# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"D00..00","system":"readv2"},{"code":"18137","system":"readv2"},{"code":"35199","system":"readv2"},{"code":"9537","system":"readv2"},{"code":"6816","system":"readv2"},{"code":"21127","system":"readv2"},{"code":"27726","system":"readv2"},{"code":"31347","system":"readv2"},{"code":"19383","system":"readv2"},{"code":"15439","system":"readv2"},{"code":"55478","system":"readv2"},{"code":"36965","system":"readv2"},{"code":"19951","system":"readv2"},{"code":"4858","system":"readv2"},{"code":"20123","system":"readv2"},{"code":"57954","system":"readv2"},{"code":"795","system":"readv2"},{"code":"48338","system":"readv2"},{"code":"94528","system":"readv2"},{"code":"33420","system":"readv2"},{"code":"D50","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('iron-deficiency-anaemia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["iron---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["iron---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["iron---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
