from unet import *
from data import *

mydata = dataProcess(512,512)

imgs_test = mydata.load_test_data()

myunet = myUnet()

model = myunet.get_unet()

model.load_weights('unet.hdf5')

imgs_mask_test = model.predict(imgs_test, verbose=1)

np.save('../results/imgs_mask_test.npy', imgs_mask_test)
for i in range(imgs.shape[0]):
    img = imgs[i]
    img = array_to_img(img)
    img.save("../results/%d.jpg"%(i))

