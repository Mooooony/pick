import mrcfile
for i in range(1,16):
        print(i)
        mrc = mrcfile.open(str(i)+".mrc")
        data = []
        data.append(mrc.data[70:582,70:582])
        data.append(mrc.data[70:582,652:1164])
        data.append(mrc.data[70:582,1234:1746])
        data.append(mrc.data[652:1164,70:582])
        data.append(mrc.data[652:1164,652:1164])
        data.append(mrc.data[652:1164,1234:1746])
        data.append(mrc.data[1234:1746,70:582])
        data.append(mrc.data[1234:1746,652:1164])
        data.append(mrc.data[1234:1746,1234:1746])
        for j in range(9):
                new = mrcfile.new(str(i)+'-'+str(j)+".mrc")
                new.set_data(data[j])
                new.close()
        mrc.close()
