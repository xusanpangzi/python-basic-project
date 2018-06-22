from random import random
import os
def printIntro():
    print("这个程序运行两个选手A和B的某种竞技比赛")
    print("这个程序需要A和B的能力值（0-1）")
def getinputs():
    a=eval(input("请输入选手A的能力值："))
    b=eval(input("请输入选手B的能力值："))
    n=eval(input("请输入模拟场次："))
    return a,b,n
def printsummary(winsA,winsB):
    n=winsA+winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A共获得{}场比赛，占比{:0.1%}".format(winsA,winsA/n))
    print("选手B共获得{}场比赛，占比{:0.1%}".format(winsB,winsB/n))
def gameover(a,b):
    return a==15 or b==15
def simonegame(probA,probB):
    scoreA,scoreB=0,0
    serving="A"
    while not gameover(scoreA,scoreB):
        if serving=="A":
            if random()<probA:
                scoreA+=1
            else:
                serving="B"
        else:
            if random()<probB:
                scoreB+=1
            else:
                serving="A"
    return scoreA,scoreB
def simNGames(n,probA,probB):
    winsA,winsB=0,0
    for i in range(n):
        scoreA,scoreB=simonegame(probA,probB)
        if scoreA>scoreB:
            winsA+=1
        else:
            winsB+=1
    return winsA,winsB

def main():
    printIntro()
    probA,probB,n=getinputs()
    winsA,winsB=simNGames(n,probA,probB)
    printsummary(winsA,winsB)
    os.system("pause")
main()
