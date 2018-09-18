#!/usr/bin/python

import sys
import re

from data_handling import reading_metadata
from Query_handling import Query_handling
from display import error_handling

query=""
def main():
    try:
        queries=str(sys.argv[1]).split(';')
        iput=str(sys.argv[1])
        queries = iput.split(';')
    except:
        error_handling('error : No query given')
    query_handling=Query_handling(reading_metadata('metadata.txt'))
    for query in queries:
        if query==' ':
            error_handling('error: No Query given')
        else:
            query=query.strip()
            if query!= " " :
                query_handling.query_processing(query)
            else:
                error_handling('error: No Query given')
    return 


main()
