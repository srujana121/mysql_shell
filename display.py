#!/usr/bin/python

from __future__ import division
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
        elif selected_col[0].find('sum')!=-1 or selected_col[0].find('average')!=-1 :
            n=len(selected_col[0])
            header=[]
            col=selected_col[0]
            header.append(col)
            col=col[4:n-1]
            k=0
            if col in matrix_metadata:
                k=matrix_metadata.index(col)
            elif col in simple_matrix_metadata:
                k=simple_matrix_metadata.index(col)
            l=[]
            sum_of_col=0
            count=0
            for row in all_columns:
                p=row[k]+'+'+'0'
                a=eval(p)
                sum_of_col+=a
                count+=1
            if selected_col[0].find('sum')!=-1:
                l.append(str(sum_of_col))
            else:
                l.append(str(sum_of_col/count))
            final_ans.append(l)
            print_data(header,final_ans)
        elif selected_col[0].find('max')!=-1 :
            n=len(selected_col[0])
            header=[]
            col=selected_col[0]
            header.append(col)
            col=col[4:n-1]
            print col
            k=0
            if col in matrix_metadata:
                k=matrix_metadata.index(col)
            elif col in simple_matrix_metadata:
                k=simple_matrix_metadata.index(col)
            l=[]
            max_of_col=-1000007
            for row in all_columns:
                p=row[k]+'>'+str(max_of_col)
                print p
                if eval(p):
                    max_of_col=int(row[k])
                    print 'max_of_col'
                    print max_of_col
            l.append(str(max_of_col))
            final_ans.append(l)
            print_data(header,final_ans)
        elif selected_col[0].find('min')!=-1 :
            n=len(selected_col[0])
            header=[]
            col=selected_col[0]
            header.append(col)
            col=col[4:n-1]
            print col
            k=0
            if col in matrix_metadata:
                k=matrix_metadata.index(col)
            elif col in simple_matrix_metadata:
                k=simple_matrix_metadata.index(col)
            l=[]
            min_of_col=1000007
            for row in all_columns:
                p=row[k]+'<'+str(min_of_col)
                print p
                if eval(p):
                    min_of_col=int(row[k])
                    print 'min_of_col'
                    print min_of_col
            l.append(str(min_of_col))
            final_ans.append(l)
            print_data(header,final_ans)
        


            
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


