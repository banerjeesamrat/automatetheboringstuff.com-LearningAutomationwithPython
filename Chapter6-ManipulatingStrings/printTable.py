'''

Write a function named printTable() that takes a list of lists of strings and
displays it in a well-organized table with each column right-justified. Assume
that all the inner lists will contain the same number of strings.

For example, the value could look like this:


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
             
Your printTable() function would print the following:


  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
  
Hint: Your code will first have to find the longest string in each of the
inner lists so that the whole column can be wide enough to fit all the strings.
You can store the maximum width of each column as a list of integers.
The printTable() function can begin with colWidths = [0] * len(tableData),
which will create a list containing the same number of 0 values as the number
of inner lists in tableData. That way, colWidths[0] can store the width of the
longest string in tableData[0], colWidths[1] can store the width of the longest
string in tableData[1], and so on. You can then find the largest value in the
colWidths list to find out what integer width to pass to the rjust() string
method.

'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(listoflists):
    # set column widths
    colWidths = [len(max(col, key=len)) for col in listoflists]
    # using list comprehension, len for length instead of last in ASCII order
    # print table
    for rownum in range(len(max(listoflists))):
        row = ''
        for col in range(len(listoflists)):
            row += listoflists[col][rownum].rjust(colWidths[col])+' '
        print(row)


printTable(tableData)
