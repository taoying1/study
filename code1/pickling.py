import pickle
shoplistfile='shoplist.data'
shoplist=['apple','mango','carrot']
f=open(shoplistfile,'w')
pickle.dump(shoplist,f)
f.close()




