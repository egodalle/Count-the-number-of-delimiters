def Count_Delimiter(input_file):

    lines = []
    delimiter_check = dict()
    
    with open(input_file) as f:
        lines = f.readlines()

    for rowdata in lines:
        no_of_delimiter = rowdata.count(",")

        if no_of_delimiter in delimiter_check:
            delimiter_check[no_of_delimiter] +=1
        else:
            delimiter_check[no_of_delimiter] = 1

    print ("No. of Delimiter","-","No. of Records")

    for i in delimiter_check:
        print(i,"-",delimiter_check[i])

input_file = 'C:/Python/Excess_Delimiter.csv'

Count_Delimiter(input_file)