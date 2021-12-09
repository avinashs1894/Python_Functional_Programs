'''
Created on 06-Dec-2021

@author: DELL
'''
def sum_of_three(n):
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            for k in range(j + 1, len(n)):
                if (n[i]+n[j]+n[k]) == 0:
                    print(n[i],"+",n[j], "+",n[k],"= 0")

n=[0, 1, -1, 2, -2, 3, -3, 4, ]
    
if __name__ == '__main__':
    sum_of_three(n)

