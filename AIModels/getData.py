from urllib import request

# 使用Quick Draw 数据集, 有345个类别的约5千万张手绘图象
# 选择其中的100个分类进行训练

# 下载数据集
def download():

  baseUrl = 'https://storage.googleapis.com/quickdraw_dataset/full/numpy_bitmap/'
  for c in classes:
