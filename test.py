import cv2
import numpy as np
import matplotlib.pyplot as plt


def testB():
    # 出力されたcsvを読み込むテスト
    x = np.loadtxt('data.csv', delimiter=',')
    plt.scatter(x[:,0], x[:,1])
    plt.show()
# testB()

def testA():
    img = np.zeros((100, 100), np.uint8)
    img[10:50, 20:60] = 1
    kernel = np.ones((3, 3), np.uint8)
    erosion = cv2.erode(img, kernel, iterations=1)
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

    plt.imshow(img)
    plt.show()
    plt.imshow(gradient)
    plt.show()

    while True:
        erosion = cv2.erode(erosion, kernel, iterations=1)
        plt.imshow(erosion)
        plt.show()

def testC():
    img = np.zeros((100, 100))
    img[10:50, 20:60] = 1
    dp = np.zeros((100, 100))
    # 初期化
    dp[:, :] = -1
    dp[np.where(img == 0)] = 0
    dx = [0, 0, 1,-1]
    dy = [1,-1, 0, 0]

    # マンハッタン距離
    # BEGIN
    i = 0
    while True:
        X, Y = np.where(dp == i)
        # もうマスがない
        if len(X) == 0:
            break
        for (x,y) in zip(X, Y):
            # 0の座標(x,y)
            print('brank', x, y)
            # 周囲をみて、まだ確定してないところがあればi+1で埋める
            for j in range(4):
                if 0 <= x+dx[j] < dp.shape[0] and 0 <= y+dy[j] < dp.shape[1] and dp[x+dx[j], y+dy[j]] == -1:
                    # 決まってない
                    dp[x+dx[j], y+dy[j]] = i + 1
        i += 1
    plt.imshow(dp), plt.title(i), plt.colorbar(), plt.show()
    # END

    tmp = img
    i = 1
    kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], np.uint8)
    while True:
        old = tmp.copy()
        tmp = cv2.erode(tmp, kernel, iterations=1)
        if len(np.where(tmp > 0)[0]) == 0:
            break
        dp[np.where(cv2.absdiff(old, tmp) > 0)] = i
        i += 1
    plt.imshow(dp), plt.colorbar(), plt.show()

    plt.imshow(img), plt.show()

testC()
