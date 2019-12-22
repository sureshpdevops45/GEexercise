import numpy
nArray = numpy.array(([21, 22, 23,25], [11, 22, 33,44], [43, 77, 89,78],[42, 74, 49,56]))
row = nArray[1] 
print('Contents of Row at Index 2 : ' , row)
column = nArray[:, 2] 
print('Contents of Column at Index 3 : ', column)
sub2DArr = nArray[1:3,1:3]
print(sub2DArr)
