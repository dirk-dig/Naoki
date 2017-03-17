import pylab as pl, numpy as np
import cPickle, gzip

mnist = cPickle.load(gzip.open("mnist.pkl.gz", "rb"))

start = 10
end = 15
for index in range (start, end + 1):

    a_digit = mnist[0][0][index]
    print mnist [0][1][index]

    arr= []
    for i in range(28):
        arr.append(a_digit[(i*28):(i*28)+28])

    pl.imshow(arr, interpolation= 'nearest', cmap='bone', origin='lower')
    pl.colorbar()

    ax= pl.gca()
    ax.invert_yaxis()

    pl.show()

