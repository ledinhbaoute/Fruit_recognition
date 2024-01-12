labels = [{'name':'dua_hau', 'id':1},{'name':'oi', 'id':2}]

ANNOTATION_PATH = 'D:/Private/Documents/Nam3/Xu_ly_anh/20110613_LeDinhBao_BTQuaTrinh_XuLyAnh/NhanDangTraiCay/NhanDangTraiCay/Tensorflow/workspace/annotations'

with open(ANNOTATION_PATH + '/label_map.pbtxt', 'w') as f:
    for label in labels:
        f.write('item { \n')
        f.write('\tname:\'{}\'\n'.format(label['name']))
        f.write('\tid:{}\n'.format(label['id']))
        f.write('}\n')
