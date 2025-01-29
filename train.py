import tensorflow as tf
import numpy as np
import os


num_samples = 500
features = 20

data = np.random.rand(num_samples, features)
labels = np.random.randint(2, size=(num_samples, 1))


model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(features,)),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])


model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


model.fit(data, labels, epochs=10, batch_size=32)


if not os.path.exists("models"):
    os.makedirs("models")


model.save("models/trAIn_model.h5")
print("✅ AI model trained and saved successfully!")
