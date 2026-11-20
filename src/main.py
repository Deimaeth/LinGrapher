###]-------------------------------------------------------------------------------------------------------;
# This program is written by Deimaeth                                                                      -
# License: BSD 2-Clause                                                                                    -
# It's in pretty sorry shape right now, but I'll work on fixes now, just wanted to get it done before labs -
###]-------------------------------------------------------------------------------------------------------;
import matplotlib.pyplot as plt
import math
import sys

def leastSquares(x:list, y:list) -> tuple:
        if len(x) != len(y):
            return ()
        else:
            # m formula: (n*sum(xy)-sum(x)sum(y))/(n*sum(x^2)-(sum(x))^2)
            # c formula: (sum(y)-m*sum(x))/(n)
            SigmaXY = 0
            SigmaX = 0
            SigmaXSquare = 0
            SigmaY = 0
            n = len(y)
            for i in range(0,len(y)):
                SigmaX += x[i]
                SigmaY += y[i]
                SigmaXSquare += pow(x[i],2)
                SigmaXY += x[i]*y[i]
            m = (n*SigmaXY-SigmaX*SigmaY)/(n*SigmaXSquare-(pow(SigmaX,2)))
            c = (SigmaY-m*SigmaX)/n
            return (m,c)

# takes in data points, calculate m&c, calculate delta m&c, plot graph, draw line of best fit and error bars
class LinGrapher:
    def __init__(self, x:list, y:list, deltaX, deltaY, xAxis:str, yAxis:str, title:str):
        if len(x) != len(y):
            return
        x_bar = list()
        y_bar = list()
        for i in range(0, len(x)):
            x_bar.append(sum(x[i])/len(x[i]))
            y_bar.append(sum(y[i])/len(y[i]))
        self.x = x_bar
        self.y = y_bar
        deltaXBar = list()
        deltaYBar = list()
        if len(x) < 10:
            for i in range(0,len(x)):
                deltaXBarI = ((max(x[i])-min(x[i]))/2)/math.sqrt(len(x[i]))
                deltaYBarI = ((max(y[i])-min(y[i]))/2)/math.sqrt(len(y[i]))
                deltaXBar.append(max(deltaXBarI, deltaX))
                deltaYBar.append(max(deltaYBarI, deltaY))
        else:
            for i in range(0,len(x)):
                sXSquare = 0
                sYSquare = 0
                for j in range(0,len(x[i])):
                    sXSquare += x[i]*x[i]
                for j in range(0,len(y[i])):
                    sYSquare += y[i]*y[i]
                deltaXBarI = (math.sqrt((1/len(x[i]))*(sXSquare)-self.x[i]*self.x[i]))/math.sqrt(len(x[i]))
                deltaYBarI = (math.sqrt((1/len(y[i]))*(sYSquare)-self.y[i]*self.y[i]))/math.sqrt(len(y[i]))
                deltaXBar.append(max(deltaXBarI, deltaX))
                deltaYBar.append(max(deltaYBarI, deltaY))
        self.deltaX = deltaXBar
        self.deltaY = deltaYBar
        self.xAxis = xAxis
        self.yAxis = yAxis
        self.title = title
    def calcLine(self) -> tuple:
        mc = leastSquares(self.x, self.y)
        mcUB = leastSquares([self.x[0], self.x[-1]], [self.y[0]-self.deltaY[0], self.y[-1]+self.deltaY[-1]])
        mcLB = leastSquares([self.x[0], self.x[-1]], [self.y[0]+self.deltaY[0], self.y[-1]-self.deltaY[-1]])
        # mc +- delMC = mc +- max(mcUB-mc, mc-mcLB)
        delMC = (max(abs(mcUB[0]-mc[0]),abs(mc[0]-mcLB[0])), max(abs(mcUB[1]-mc[1]),abs(mc[1]-mcLB[1])))
        return (mc, delMC)
    def plot(self, m, c):
        plt.scatter(self.x, self.y)
        mxc = self.x.copy()
        for i in range(0,len(mxc)):
            mxc[i] *= m
            mxc[i] += c
        plt.plot(self.x, mxc)
        plt.grid(True, color="green", linestyle="-", linewidth=0.5)
        plt.errorbar(self.x, self.y, xerr=self.deltaX, yerr=self.deltaY, fmt='o', color='blue', ecolor='gray', elinewidth=1.5, capsize=5)
        plt.title(self.title)
        plt.xlabel(self.xAxis)
        plt.ylabel(self.yAxis)
        plt.savefig(f"{self.title}GraphedResults.png", bbox_inches="tight", dpi=400)
        plt.show()
        plt.close()
        return
    def graph(self):
        mcDeltamc = self.calcLine()
        with open(f"{self.title}Results.txt", "wt") as results:
            results.write(f"m = {mcDeltamc[0][0]} +- {mcDeltamc[1][0]}\nc = {mcDeltamc[0][1]} +- {mcDeltamc[1][1]}\n")
            for i in range(0, len(self.x)):
                results.write(f"x +- Delta x = {self.x[i]} +- {self.deltaX[i]} : ")
                results.write(f"y +- Delta y = {self.y[i]} +- {self.deltaY[i]}\n")
        results.close()
        self.plot(mcDeltamc[0][0], mcDeltamc[0][1])

def main():
    if len(sys.argv) < 2:
        return
    x = list()
    xi = list()
    y = list()
    yi = list()
    delX = 0.0
    delY = 0.0
    xAxis = "X"
    yAxis = "Y"
    title = "Title"
    for i in range(1,len(sys.argv)):
        if sys.argv[i] == "--xreading":
            readingsX = sys.argv[i+1].split(',')
            for j in readingsX:
                xi.append(float(j))
            x.append(xi)
            xi = list()
        if sys.argv[i] == "--yreading":
            readingsY = sys.argv[i+1].split(',')
            for j in readingsY:
                yi.append(float(j))
            y.append(yi)
            yi = list()
        if sys.argv[i] == "--instrumentErrX":
            delX = float(sys.argv[i+1])
        if sys.argv[i] == "--instrumentErrY":
            delY = float(sys.argv[i+1])
        if sys.argv[i] == "--title":
            title = sys.argv[i+1]
        if sys.argv[i] == "--axisX":
            xAxis = sys.argv[i+1]
        if sys.argv[i] == "--axisY":
            yAxis = sys.argv[i+1]

    grph = LinGrapher(x, y, delX, delY, xAxis, yAxis, title)
    grph.graph()


if __name__ == "__main__":
    main()