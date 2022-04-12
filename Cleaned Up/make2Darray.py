import numpy
def main(input_num, input_array):
    num = 0
    
    for i in range(1,input_num):
        insert = []
        for l in range(1,input_num):
            insert.append(input_array[num])
            num+=1
        if(i == 1):
            TDArray =  numpy.array([insert])
        else:
            TDArray = numpy.append(TDArray, [insert],axis = 0)
    return TDArray