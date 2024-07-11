class Univariate():
    def quanQual(dataset):
      quan=[]
      qual=[]

      for colName in dataset.columns:
        #print(colName)
        if(dataset[colName].dtype=='O'):
          #print(colName)
          qual.append(colName) 
        else:
          #print(colName)
          quan.append(colName)
      return quan,qual   