'''
##########INSTRUCTIONS###########
Assumed that the first row of the csv spreadsheet is the header/categories
First column is the timestamp, second column is the email address

1. Copy and paste any row to the bottom of the spreadsheet.
2. Change the 'email' field of the new row to 'ANSWER'
3. For each field of the new 'ANSWER' row, find the actual winner from somewhere in that column of the spreadsheet
    and copy & paste it into the 'ANSWER' row field. It is important that the text matches EXACTLY.
4. In the cinema_people hash below, and input the computing id's and names of Cinema members.
    Ex: { js8th : 'John Smith', mzw7af : 'Maurice Wong', ... }
5. Rename the csv spreadsheet to 'ballot.csv' and put it in the same directory as this script.
6. Run: "python get_results.py"
'''

import csv
import re
with open('ballot.csv', 'rU') as csvfile:
    creader = csv.reader(csvfile)
    count = 0
    results = {}
    first = True
    categories = [] #stores the first row of category names
    for row in creader:
        #skip the header
        if first:
            categories = row[2:len(row)]
            first = False
            continue
        #remove the timestamp column (first column)
        row = row[1:len(row)]
        #first row is email
        email = row[0]
        #map email to answer choices list (without email)
        results[email] = row[1:len(row)]
    #label the answer row as "ANSWER"
    answer = results['ANSWER']
    final_scores = []
    for key in results:
        if key == 'ANSWER':
            continue
        curr = results[key]
        #create a list with elements that match and get its length
        score = len([i for i, j in zip(answer, curr) if i == j])
        #strip @virginia.edu from username
        key = re.sub('@.*$', '', key)
        final_scores.append([key, score])
    final_scores = sorted(final_scores, key = lambda score: score[1])
    final_scores.reverse()
    for entry in final_scores:
        print entry[0] + "\t" + str(entry[1])
    print("\n\n")

    #print cinema committee scores
############## Cinema Committee Members ###################
    cinema_people = {
        'js8th' : 'John Smith',
        'mzw7af': 'Maurice Wong',
    }
    for entry in final_scores:
        name = entry[0]
        if name in cinema_people:
            print str(entry[1]) + "\t" + cinema_people[name]
