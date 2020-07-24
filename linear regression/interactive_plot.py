import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

X = pd.read_csv("../data/hard_work_pays_off_challenge_data/Linear_X_Train.csv").values
Y = pd.read_csv("../data/hard_work_pays_off_challenge_data/Linear_Y_Train.csv").values

theta = np.load("thetalist.npy")

plt.ion()
for i in range(30):
    y_hat = theta[i][0] + theta[i][1]*X
    plt.scatter(X,Y)
    plt.plot(X,y_hat,color='red')
    plt.draw()
    plt.pause(1)
    plt.clf()