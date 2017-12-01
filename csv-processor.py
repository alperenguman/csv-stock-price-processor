import csv
import datetime
import pdb
import collections

def getInputDescriptor():
     
    while True:
        filename = input("Please enter name of the file to be opened: ")
        
        try:
            file = open(filename + '.csv')
        except FileNotFoundError:
            continue
        
        return file     
        
def getDataList(file_object, column_number):
    reader = csv.reader(file_object)
    
    tupleslist = []
    
    for row in reader:
        tupleslist.append((row[0], row[column_number]))
        
    del tupleslist[0]
    
    return tupleslist

def averageData(list_of_tuples):
    result_list = []
    month_dict = collections.OrderedDict()

    for tuple in list_of_tuples:
        
        date = datetime.datetime.strptime(tuple[0], '%Y-%m-%d')
        new_format = datetime.datetime.strftime(date, '%m:%Y') 
        
        try: 
            month_dict[new_format].append(float(tuple[1]))
        except KeyError:
            month_dict[new_format] = []
            month_dict[new_format].append(float(tuple[1]))
       
    for key, value in month_dict.items():
        
        month_dict[key] = sum(month_dict[key])/len(month_dict[key])
        result_list.append((key, month_dict[key]))
        
    return result_list

def outputAverage(filename, average):
    file = open('data_' + str(filename) + '.txt', 'w')

    for tuple in average:
        file.write(str(tuple[0]) + ' '*8 + str(round(tuple[1], 2)) + '\n')

    file.close()

def main():
    file = getInputDescriptor()
    n = 1
    while n < 7:  
        outputAverage(n, (averageData(getDataList(file, n))))
        n += 1
        file.seek(0)
    print('Your CSV is processed.')

if __name__ == '__main__':
    main()
    