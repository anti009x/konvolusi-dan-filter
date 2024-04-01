matrixA = [[3,7,5,2,2],
          [9,5,5,8,3],
          [7,5,9,8,4],
          [5,1,6,3,4],
          [0,1,2,3,4],
          ]
matrixB = [[1,0,1],
            [2,0,2],
            [1,0,1],

           ]

def konklusi(x,y):
    result = [[sum(a*b for a,b in zip(rowA, colB)) 
              for colB in zip(*matrixA)] 
              for rowA in zip(*matrixB)]
    # matrixA*matrixB
    a = x
    b = y
    
    return result[a][b]

print(konklusi(2,3))
