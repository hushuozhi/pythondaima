# 九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(j,i,i*j),end = '') # \t 空四个字符相当于tab键
    print()