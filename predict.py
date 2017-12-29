from train import *
from data import *

mydata = dataProcess(512,512)

imgs_test = mydata.load_test_data()

myunet = myUnet()

model = myunet.get_unet()

model.load_weights('unet.hdf5')

imgs_mask_test = model.predict(imgs_test, verbose=1)
imgname = os.listdir("./test")
np.save('./results/imgs_mask_test.npy', imgs_mask_test)
for i in range(imgs_mask_test.shape[0]):
    img = imgs_mask_test[i]
    img = array_to_img(img)
    img.save("./results/%s"%(imgname[i]))


