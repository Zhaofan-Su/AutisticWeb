from utilits import load_data, preprocess_data
from model import define_model, train_and_validate

if __name__ == "__main__":
    # 下载数据
    # download()

    # 加载数据
    X_train, y_train, X_test, y_test, class_names = load_data('data')

    # 数据预处理
    # 模型使用规模为[N, 28, 28, 1]的批处理，输出规模为[N, 100]的概率
    X_train, y_train, X_test, y_test = preprocess_data(X_train, y_train,
                                                       X_test, y_test,
                                                       class_names)

    # 定义模型
    model = define_model(X_train.shape[1:])

    # 训练并测试模型
    model = train_and_validate(X_train, y_train, X_test, y_test, model)

    # 保存h5格式的模型
    model.save('quick_draw.h5')