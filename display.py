#!/usr/bin/python

import sys

def project(all_columns,matrix_metadata,split_select,input_tables,simple_matrix_metadata):
    #print 'all'
    #print all_columns
    header=[]
    final_ans=[]
    h=0
    index=[]
    selected_col=split_select[0].split(',')
    for col in selected_col:
        col=col.strip()
        if col not in matrix_metadata:
            if col not in simple_matrix_metadata:
                h=-11
                error_in=col
    
    if h==-11:
        selected_col[0]=selected_col[0].strip()
        if len(selected_col)==1 and  selected_col[0]== '*':
            print_data(matrix_metadata,all_columns)
        else:
            error_handling("No such columns exit in the given tables")
    else:
        for col in selected_col:
            col=col.strip()
            header.append(col)
            if col in matrix_metadata:
                index.append(matrix_metadata.index(col))
            else:
                index.append(simple_matrix_metadata.index(col))
        for row in all_columns:
            l=[]
            for n in index:
                l.append(row[n])
            final_ans.append(l)
        print_data(header,final_ans)

def error_handling(error):
    sys.stderr.write(error + '\n')
    quit(-1)

def print_data(header,ans):
    header_string='|'
    n=len(header)
    i=0
    for column in header:
        i+=1
        header_string+=column
        while(len(header_string)<i*13):
            header_string=header_string+' '
        header_string+='|  '
        if len(header_string)>i*13:
            header_string=header_string[:i*13]+'| '

    n=len(header_string.strip(' '))
    divider=''
    for i in range(n):
        divider+='-'
    print divider
    print header_string.strip(' ')
    print divider

    for row in ans:
        row_ans="|"
        i=0
        for l in row:
            row_ans+=l
            i+=1;
            while(len(row_ans)<i*13):
                row_ans=row_ans+' '
            row_ans+='|  '
            if len(row_ans)>i*13:
                row_ans=row_ans[:i*13]+'| '
        print row_ans.strip(' ')
    print divider


