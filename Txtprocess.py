import time,os
scale = 50
print("执行开始".center(scale//2,"-"))
start=time.perf_counter()
for i in range(scale+1):
    a='*'*i
    b='-'*(scale-i)
    c=(i/scale)*100
    dwr=time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]".format(c,a,b,dwr),end='')
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,'-'))
os.system("pause")