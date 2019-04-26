from tensorflow.keras import layers
from tensorflow import keras
import tensorflow as tf

# 定义模型
# 使用3个卷积层和2个全连接层


def define_model(input_shape):
    model = keras.Sequential()
    # input_shape=X_train.shape[1:]
    model.add(
        layers.Convolution2D(
            16, (3, 3),
            padding='same',
            input_shape=input_shape,
            activation='relu'))
    model.add(layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(
        layers.Convolution2D(32, (3, 3), padding='same', activation='relu'))
    model.add(layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(
        layers.Convolution2D(64, (3, 3), padding='same', activation='relu'))
    model.add(layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(100, activation='softmax'))

    # 训练模型
    adam = tf.train.AdamOptimizer()
    model.compile(
        loss='categorical_crossentropy',
        optimizer=adam,
        metrics=['top_k_categorical_accuracy'])

    return model


# 训练模型
# 对模型进行5轮训练
# 将训练数据分为256批输入模型，并分离出10%作为验证集
def train_and_validate(X_train, y_train, X_test, y_test, model):
    # 训练、验证模型
    model.fit(
        x=X_train,
        y=y_train,
        validation_split=0.1,
        batch_size=256,
        verbose=2,
        epochs=5)

    # 测试模型
    score = model.evaluate(X_test, y_test, verbose=0)
    print("测试准确率：{:0.2f}%".format(score[1] * 100))

    return model
