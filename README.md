# Oscar Ballot Competition
Determines winners of an Oscar Ballot competition

Requires python 2.7 to run

Requires as input a csv file with Oscar ballot entries with the following assumptions:
- First row is the header with each column's labels.
- First column is the timestamp
- Second column is the email address
- 24 Oscar categories 


It is recommended to create the Oscar Ballot through Google Forms, which can export the results into a csv file.

## Determining the winners
1. Copy and paste any row to the bottom of the spreadsheet.
2. Change the 'email' field of the new row to 'ANSWER'
3. For each field of the new 'ANSWER' row, find the actual winner from somewhere in that column of the spreadsheet
    and copy & paste it into the 'ANSWER' row field. It is important that the text matches EXACTLY.
4. In the cinema_people dict at the bottom of the code, input the computing id's and names of Cinema members.
    Ex: 
    ```
    { js8th : 'John Smith', mzw7af : 'Maurice Wong', ... }
    ```
5. Rename the csv spreadsheet to `ballot.csv` and put it in the same directory as this script.
6. Run: `python get_results.py` (Requires python 2.7)


A sample `ballot_sample.csv` is provided for reference.
