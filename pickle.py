import pickle
f=open("tst.pck","wb")
pickle.dump(12.3,f)
pickle.dump([1,2,3],f)
f.close()
