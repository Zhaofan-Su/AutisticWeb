import os
import glob
import numpy as np
from tensorflow import keras

# 使用Quick Draw 数据集, 有345个类别的约5千万张手绘图象
# 选择其中的100个分类进行训练

IMAGE_SIZE = 28


# 加载数据
def load_data(root, vfold_ratio=0.2, max_items_per_class=4000):
    all_files = glob.glob(os.path.join(root, '*.npy'))

    # 初始化变量
    x = np.empty([0, 784])
    y = np.empty([0])
    class_names = []

    # 加载每一个数据文件
    for idx, file in enumerate(all_files):
        data = np.load()
        data = data[0:max_items_per_class, :]
        labels = np.full(data.shape[0], idx)

        x = np.concatenate((x, data), axis=0)
        y = np.append(y, labels)

        class_name, ext = os.path.splitext(os.path.basename(file))
        class_names.append(class_name)
    data = None
    labels = None

    # 随机化数据集
    permutation = np.random.permutation(y.shape[0])
    x = x[permutation, :]
    y = y[permutation]

    # 分成训练集和测试集
    vfold_size = int(x.shape[0] / 100 * (vfold_ratio * 100))

    X_test = x[0:vfold_size, :]
    y_test = y[0:vfold_size]

    X_train = x[vfold_size:x.shape[0], :]
    y_train = y[vfold_size:y.shape[0]]

    return X_train, y_train, X_test, y_test, class_names


# 预处理数据
def preprocess_data(X_train, y_train, X_test, y_test, class_names):
    X_train = X_train.reshape(X_train.shape[0], IMAGE_SIZE, IMAGE_SIZE,
                              1).astype('float32')
    X_test = X_test.reshape(X_test.shape[0], IMAGE_SIZE, IMAGE_SIZE,
                            1).astype('float32')

    X_train /= 255.0
    X_test /= 255.0

    # 将种类向量转换为种类矩阵
    y_train = keras.utils.to_categorical(y_train, len(class_names))
    y_test = keras.utils.to_categorical(y_test, len(class_names))

    return X_train, y_train, X_test, y_test
