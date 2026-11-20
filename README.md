# LinGrapher (Linear Grapher)
Linear Grapher is a program that takes in data measurements and produces a graph in matplotlib alongside the relevant data analysis to produce the uncertainties and errors for said data. It is intended to be a program to automate the data analysis for my physics labs because I am WAY too lazy to do it myself.

## How it works
Linear Grapher is *supposed* to be a simple program(alas that's more or less subjective) where you input your data that you collected in the lab and wham-bam et voila, you have your graph and all the statistical analysis on said data that you need in the form of a .txt file produced after running the program(the graph is also saved as a png for easy integration into your report or whatever).

## How to use
First ensure that you have the latest version of python installed and the program installed to the cwd. Next, run it and pass the relevant command-line arguments for the data, uncertainties, x-axis label, y-axis label and the title of the graph. An example is given below:
```bash
python3 .\main.py --xreading 2,3,2,3 --xreading 4,4,4,4 --yreading 5,5,6 --yreading 7,7,3 --instrumentErrX 0.6 --instrumentErrY 1 --title Example --axisX XNew --axisY YNew
```

Ensure that the data you pass into the program is in the form of y=mx+c (a linear graph), so for instance with the pendulum equation T ≈ 2πsqrt(l/g), you would have the y-value data in the form of T^2 and the x-value data in the form of l, so that the gradient is (4π^2)/g. This assumes that you've done the relevant error propagation in order to arrange the equation in this way.

### Arguments
```--xreading``` - The following data is the readings for the "x-value" of a specific data point, can be multiple readings as long as each is separated by a comma.

```--yreading``` - The following data is the readings for the "y-value" of a specific data point, can be multiple readings as long as each is separated by a comma.

```--xtitle``` - The following value passed is the title for the graph, no need to surround with quotation marks as it is already read-in as a string.

```--axisX``` - The following value passed is the name of the x-axis for the graph.

```--axisY``` - The following value passed is the name of the y-axis for the graph.

```--instrumentErrX``` - The following value is the instrumental error for the x-values, it doesn't need to be input if the uncertainty via multiple readings is greater although the program already handles that.

```--instrumentErrY``` - The following value is the instrumental error for the y-values, it doesn't need to be input if the uncertainty via multiple readings is greater although the program already handles that.
