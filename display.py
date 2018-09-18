#!/usr/bin/python

from __future__ import division
import sys
import collections 

def project(all_columns,matrix_metadata,split_select,input_tables,simple_matrix_metadata):
    header=[]
    final_ans=[]
    h=0
    index=[]
    selected_col=split_select[0].split(',')
    #print selected_col
    #print matrix_metadata
    #print simple_matrix_metadata

    for col in selected_col:
        col=col.strip()
        if col not in matrix_metadata:
            if col not in simple_matrix_metadata:
                h=-11
                error_in=col
            else:
                col_count=collections.Counter(simple_matrix_metadata)
                if col_count[col]>1:
                    error_handling('ERROR: Multiple columns exist with give column name '+ col)
    
    if h==-11:
        selected_col[0]=selected_col[0].strip()
        if len(selected_col)==1 and  selected_col[0]== '*':
            print_data(matrix_metadata,all_columns)
        else:
            header=[]
            l=[]
            for inputs in selected_col:
                inputs=inputs.strip()
                if inputs.find('sum')!=-1 or inputs.find('max')!=-1 or inputs.find('min')!=-1 or inputs.find('average')!=-1:
                    n=len(inputs)
                    if inputs.find('average')!=-1:
                        col=inputs[8:n-1]
                    else:
                        col=inputs[4:n-1]
                    index=0
                    if col in matrix_metadata:
                        index=matrix_metadata.index(col)
                        header.append(inputs)
                    elif col in simple_matrix_metadata:
                        index=simple_matrix_metadata.index(col)
                        header.append(inputs)
                    else:
                        error_handling('ERROR: No such column exist')
                    
                    if inputs.find('sum')!=-1:
                        required_ans=sum_of_data(index,all_columns,1)
                        l.append(str(required_ans))
                    elif inputs.find('max')!=-1:
                        required_ans=max_of_data(index,all_columns)
                        l.append(str(required_ans))
                    elif inputs.find('min')!=-1:
                        required_ans=min_of_data(index,all_columns)
                        l.append(str(required_ans))
                    elif inputs.find('average')!=-1:
                        required_ans=sum_of_data(index,all_columns,0)
                        l.append(str(required_ans))
                else:
                    error_handling('ERROR: No such column exist')
            final_ans.append(l)
            print_data(header,final_ans)
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
    #sys.stderr.write(error + '\n')
    print error
    quit(-1)

def sum_of_data(index,all_columns,check):
    l=[]
    sum_of_col=0
    count=0
    for row in all_columns:
        p=row[index]+'+'+'0'
        a=eval(p)
        sum_of_col+=a
        count+=1
    if check == 1:
        k=sum_of_col
        return k
    else:
        return sum_of_col/count

def max_of_data(index,all_columns):
    l=[]
    max_of_col=-1000007
    for row in all_columns:
        p=row[index]+'>'+str(max_of_col)
        if eval(p):
            max_of_col=int(row[index])
    return max_of_col
def min_of_data(index,all_columns):
    l=[]
    min_of_col=1000007
    for row in all_columns:
        p=row[index]+'<'+str(min_of_col)
        if eval(p):
            min_of_col=int(row[index])
    return min_of_col

def print_data(header,ans):
    header_string='|'
    n=len(header)
    i=0
    for column in header:
        i+=1
        header_string+=column
        while(len(header_string)<i*16):
            header_string=header_string+' '
        header_string+='|  '
        if len(header_string)>i*16:
            header_string=header_string[:i*16]+'| '

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
            while(len(row_ans)<i*16):
                row_ans=row_ans+' '
            row_ans+='|  '
            if len(row_ans)>i*16:
                row_ans=row_ans[:i*16]+'| '
        print row_ans.strip(' ')
    print divider


