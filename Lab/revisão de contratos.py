while True:
      variavel = 0 
      ivetor=[]
      fvetor = [] 
      digito_ruim,n_incial=map(str,input().split())
      if digito_ruim == '0' and n_incial == '0':
        break
      n_incial = list(n_incial) 
      for c in range(len(n_incial)):
        if digito_ruim != n_incial[c]:
          ivetor.append(int(n_incial[c]))      
      for c in ivetor:
        if variavel == 0:
          if c != 0:
            variavel=1+variavel  
            fvetor.append(c)
        else:
          variavel=1+variavel
          fvetor.append(c)  
      if sum(ivetor)==0:
        print("0")
      else:  
        for c in fvetor:
          print(c,end=" ".strip())
        print()