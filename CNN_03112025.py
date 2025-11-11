from tensorflow.keras import layers, models
from keras.preprocessing import image
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np

train_gen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_data = train_gen.flow_from_directory(
    'Animals/train',
    target_size=(128,128),
    batch_size=16,
    class_mode='binary',
    subset='training'
)

val_data = train_gen.flow_from_directory(
    'animals/train',
    target_size=(128,128),
    batch_size=16,
    class_mode='binary',
    subset='validation'
)

model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
history = model.fit(train_data, validation_data=val_data, epochs=5)

model.save('cnn_cat_dog_model.h5')
model = load_model('cnn_cat_dog_model.h5')

img_path = 'Animals/test/my_dog.jpg'
img = image.load_img(img_path, target_size=(128,128))
plt.imshow(img)
plt.axis('off')
plt.show()

img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

prediction = model.predict(img_array)

if prediction > 0.5:
    print("This is a Dog ")
else:
    print("This is a Cat ")