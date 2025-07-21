st= input("enter the input:")
coding=True
words=st.split(" ")
if(coding):
    nwords=[]

    for word in words:
     if(len(word)>=3):
      ch1="rty"
      ch2="weo"
      st1= ch1 + word[1:] + word[0]  +ch2
      nwords.append(st1)
     else:
       nwords.append(word[::-1]) 
print("".join(nwords))       
