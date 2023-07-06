import csv

# list of 'letters' by frequency
frequency_list = list('.etaoinshrdlcumwfgypbvkjxqz')
# print(l)

# dictionary of frequency map
dictionary = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0, "18": 0, "19": 0, "20": 0, "21": 0, "22": 0, "23": 0, "24": 0, "25": 0, "26": 0}

# ts = ""
# for k in range(27):
#     ts2 = '"{}": 0, '
#     ts = ts + ts2.format(k)
# print(ts)    

with open('messages.csv', newline='') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        for col in row:
            dictionary[col] = dictionary[col] + 1
    # sorted_dictionary = sorted(dictionary)
    sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    # for row in reader:
    #     for col in row:
    #         index = sorted_dictionary.index(col)
    #         print(frequency_list[index])

with open('messages.csv', newline='') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        ps = ""
        print(frequency_list)
        print(sorted_dictionary)
        print(dictionary)
        for col in row:
            for tup in sorted_dictionary:
                if tup[0] == col:
                    index = int(tup[0])
                    # print(index)
            ps = ps + frequency_list[index]
            # print(index)
            # print(frequency_list[index])
        print(ps)

