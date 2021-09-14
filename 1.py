import numpy as np
import time

start = time.time()

Mat1 = np.random.randint(10, size=(1000, 2000))
Mat2 = np.random.randint(10, size=(2000, 3500))

Mat3 = np.random.uniform(10, size=(1000, 2000))
Mat4 = np.random.uniform(10, size=(2000, 3500))

Result = [[0 for x in range(2000)] for y in range(3000)] 
# explicit for loops
for i in range(len(Mat1)):
    for j in range(len(Mat2[0])):
        for k in range(len(Mat2)):
            Result[i][j] += Mat1[i][k] * Mat2[k][j]


end = time.time()
print(Result“\n”)
print(end - start)
