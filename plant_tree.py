import numpy as np
import itertools
def detect(x):
    c_copy = x.copy()
    c_copy = c_copy.reshape(3,4)
    flag = 0 # ok
    for i in range(0,3):
        for j in range(0,4):
        
            try:
                tem = c_copy[i][j]*c_copy[i-1][j]*c_copy[i+1][j]
                if c_copy[i][j] == 1 and c_copy[i-1][j] == 1 and c_copy[i+1][j] == 1 and i-1>=0:
                    flag = 1 # no ok
            except:
                pass
            finally:
                try:
                    if c_copy[i][j] == 1 and c_copy[i][j-1] == 1 and c_copy[i][j+1] == 1 and j-1>=0:
                        flag = 1 # no ok
                except:
                    pass
                finally:
                    try:
                        if c_copy[i][j] == 1 and c_copy[i-1][j-1] == 1 and c_copy[i+1][j+1] == 1 and i-1>=0 and j-1>=0:
                            flag = 1
                    except:
                        pass
                    finally:
                        try:
                            if c_copy[i][j] == 1 and c_copy[i+1][j-1] == 1 and c_copy[i-1][j+1] == 1 and i-1>=0 and j-1>=0:
                                flag = 1
                        except:
                            pass
                        finally:
                            pass
    if flag == 0:
        return c_copy
    else:
        return -1


if __name__ == "__main__":

    dict1 = {}
    for count,i in enumerate(itertools.product([1,0],repeat= 12)):
        q = np.array(i)
        p = detect(q)
        dict1[count] = p
    dict1
    dict2 = {}

    def summ(x):
        if x == -1:
            return 0
        else:
            return x.sum()
    for keys,value in dict1.items():
        value = np.array(value)

        if value.any() == -1:
            pass
        else:
            temp = (value.sum())
        
        if temp > 6 and temp < 9:
            print(value)
