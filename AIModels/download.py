import urllib.request

# 下载数据集
f = open("used_classes.txt", "r")
classes = f.readlines()
f.close()
classes = [c.replace('\n', '').replace(' ', '_') for c in classes]

base_url = 'https://console.cloud.google.com/storage/browser/quickdraw_dataset/full/numpy_bitmap/'
for c in classes:
    cls_url = c.replace("_", "%20")
    path = base_url + cls_url + '.npy'
    urllib.request.urlretrieve(path, 'data/' + c + '.npy')
