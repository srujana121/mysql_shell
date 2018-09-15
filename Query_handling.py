import re
import sys
import numpy as np
from data_handling import reading_tables,reading_metadata
from display import project,error_handling

matrix_metadata=[]
simple_matrix_metadata=[]
data_matrix=[]
join=0
class Query_handling(object):

    def __init__(self,tables):
        self.tables=tables
        self.matrix_metadata=matrix_metadata
        self.simple_matrix_metadata=simple_matrix_metadata
        self.data_matrix=data_matrix
        self.join=join
    
    def query_processing(self,query):
        all_columns=[]
        join=0
        query=' '.join(query.split())
        #print query
        #if not 'from' in query:
         #   error_handling("Syntax Error: No Table Selected")
        split_from=query.split("from")
        if split_from!=['']:
            split_select = split_from[0].split('select')
            for s in split_select:
                if s=='':
                    split_select.remove('')
            if split_select==[' ']:
                error_handling("Syntax Error: No columns are selected from tables")

            #print split_select
            split_where=split_from[1].split('where')
            for s in split_where:
                if s=='':
                    split_where.remove('')
            #print split_where
            if 'where' in query and len(split_where)==1:
                error_handling("Syntax Error: Incorrect use of 'where' clause ")

            input_tables=split_where[0]
            self.matrix(input_tables)
            if len(split_where) > 1:
                if split_where[1]!=[]:
                    all_columns= self.where(split_where[1])
                    project(all_columns,self.matrix_metadata,split_select,input_tables,self.simple_matrix_metadata)
            else:
                all_columns=self.data_matrix
                project(all_columns,self.matrix_metadata,split_select,input_tables,self.simple_matrix_metadata)
                """"  print selected coulmns"""



    
    def matrix(self,input_tables):
        count=0
        input_tables=input_tables.strip()
        tables_list=input_tables.split(',')
        self.data_matrix=[]
        final_data_matrix=[]
        self.matrix_metadata=[]
        self.simple_matrix_metadata=[]
        for table in tables_list:
            table=table.strip()
            d=reading_tables(table)
            #print 'd'
            #print d
            if self.data_matrix== []:
                for row in d:
                    self.data_matrix.append(row)
                    final_data_matrix.append(row)
            else:
                count=0
                for row in d:
                    for r in self.data_matrix:
                        final_data_matrix.append(r+row)
                        count=count+1
            self.data_matrix=final_data_matrix
            final_data_matrix=[]
            #print count
        for table in tables_list:
            table=table.strip()
            k=self.tables[table]
            for column in k:
                self.simple_matrix_metadata.append(column)
                column=table+'.'+column
                self.matrix_metadata.append(column)
        #print self.data_matrix

    def where(self,conditions):
        conditions=conditions.strip( )
        l=conditions.split()
        check=-1
        if 'AND' in l:
            check=self.where_and(conditions)
        elif 'OR' in l:
            check=self.where_or(conditions)
        else:
            check=self.handle_conditions(conditions)
        return check

    def where_and(self,conditions):
        list_of_conditions=conditions.split('AND')
        check_1=self.handle_conditions(list_of_conditions[0])
        check_2=self.handle_conditions(list_of_conditions[1])
        required_rows=[]
        for row in check_1:
            for line in check_2:
                if row == line:
                    required_rows.append(row)
        return required_rows


    def where_or(self,conditions):
        list_of_conditions=conditions.split('OR')
        check_1=self.handle_conditions(list_of_conditions[0])
        check_2=self.handle_conditions(list_of_conditions[1])
        required_rows=[]
        for row in check_1:
            required_rows.append(row)
        for row in check_2:
            required_rows.append(row)
        for row in check_1:
            for line in check_2:
                if row == line:
                    required_rows.remove(row)
        return required_rows
    
        
    def handle_conditions(self,conditions):
        count=0
        conditions=conditions.strip()
        satisfying_rows=[]
        operator=''
        list_of_operators=['=','!=','>','>=','<','<=']
        for c in list_of_operators:
            if c in conditions:
                operator=c
        objects_to_verify=re.split(r"[=\>=\<=\<\>\!=]",conditions)
        for s in objects_to_verify:
            if s=='':
                objects_to_verify.remove('')
        if objects_to_verify[0] in self.matrix_metadata and objects_to_verify[1] in self.matrix_metadata:
            n1=self.matrix_metadata.index(objects_to_verify[0])
            n2=self.matrix_metadata.index(objects_to_verify[1])
            for row in self.data_matrix:
                if operator == '=':
                    operator='=='
                    join=-1
                statement=row[n1]+operator+row[n2]
                if eval(statement):
                    satisfying_rows.append(row)
                    count=count+1
        elif objects_to_verify[0] in self.simple_matrix_metadata and objects_to_verify[1] in self.simple_matrix_metadata:
            n1=self.simple_matrix_metadata.index(objects_to_verify[0])
            n2=self.simple_matrix_metadata.index(objects_to_verify[1])
            for row in self.data_matrix:
                if operator == '=':
                    operator='=='
                    join=-1
                statement=row[n1]+operator+row[n2]
                if eval(statement):
                    satisfying_rows.append(row)
                    count=count+1
        elif objects_to_verify[0] in self.matrix_metadata and objects_to_verify[1] not in self.matrix_metadata:
            n1=self.matrix_metadata.index(objects_to_verify[0])
            for row in self.data_matrix:
                if operator == '=':
                    operator='=='
                statement=row[n1]+operator+objects_to_verify[1]
                if eval(statement):
                    satisfying_rows.append(row)
                    count=count+1
        elif objects_to_verify[0] in self.simple_matrix_metadata and objects_to_verify[1] not in self.simple_matrix_metadata:
            n1=self.simple_matrix_metadata.index(objects_to_verify[0])
            for row in self.data_matrix:
                if operator == '=':
                    operator='=='
                statement=row[n1]+operator+objects_to_verify[1]
                if eval(statement):
                    satisfying_rows.append(row)
                    count=count+1
        return satisfying_rows   
