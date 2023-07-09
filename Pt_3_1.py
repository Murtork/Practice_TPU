import functools
def find_average(listt):
    average= functools.reduce(lambda i, j: i + j, listt)/len(listt)
    return average

listt={1,3,5,7,9,111}
average=find_average(listt)
print("Среднее значение list_values ​​равно:" , average)
