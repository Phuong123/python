import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.utils.vis_utils import plot_model

# Define model using Sequential construct
model = Sequential()
model.add(Dense(1, input_dim=500))
model.add(Activation(activation='sigmoid'))
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

data = np.random.random((1000, 500))
labels = np.random.randint(2, size=(1000, 1))


score = model.evaluate(data,labels, verbose=0)
# print ("Before Training:", zip(model.metrics_names, score))
print ("Before Training:", list(zip(model.metrics_names, score)))

#print ([i for i in zip(model.metrics_names, score)])
model.fit(data, labels, epochs=10, batch_size=32, verbose=0)


score = model.evaluate(data,labels, verbose=0)
print ("After Training:", list(zip(model.metrics_names, score)))


plot_model(model, to_file='s1.png', show_shapes=True)

# Before Training: [('loss', 0.76832762384414677), ('acc', 0.50700000000000001)]
# After Training: [('loss', 0.67270196056365972), ('acc', 0.56299999999999994)]