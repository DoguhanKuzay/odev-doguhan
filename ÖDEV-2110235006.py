#!/usr/bin/env python
# coding: utf-8

# # 1.PROGRAM

# ## HIZLANARAK GİDEN BİR ARABANIN SEÇİLEN SÜREDE ALDIĞI YOL

# In[11]:


a=int(input("Arabanın ilk hızını yazınız:"))
a2=int(input("Arabanın ivmesini yazınız:"))
b=int(input("Arabanın kaç saniye gittiğini yazınız:"))
print(((a+(a+b*a2*0.5))*b))


# # 2.PROGRAM

# ## ÜÇGEN OLMA ŞARTI HESAPLAMA

# In[1]:


a=int(input("Üçgenin 1. kenarını giriniz"))
b=int(input("Üçgenin 2. kenarını giriniz"))
c=int(input("Üçgenin 3. kenarını giriniz"))
if a+b>c and a+c>b and c+b>a:
    print("Bu bir üçgen.")
else:
    print("Bu bir üçgen değil.")


# # 3.PROGRAM

# ## BASİT MANTIK SORULARI (5 SORU)

# In[2]:


print("Doktorunuz size 3 hap verir ve bunları yarımşar saat arayla almanızı tavsiye ederse, ilaçların tamamını bitirmeniz ne kadar sürer?")
a=int(input("Lütfen cevabınızı sayı olarak giriniz: "))
if a==1:
    print("Doğru")
    print("Bazı aylar 30, bazıları 31 çeker; kaç ayda 28 gün vardır?")
    b=int(input("Lütfen cevabınızı sayı olarak giriniz: "))
if b==28:
    print("Doğru")
    print("Bir çiftçinin 17 koyunu vardı. Sürüde salgın hastalık oldu, dokuzu ağır hastalandı, diğerleri öldü. Çiftçinin kaç koyunu var?")
    c=int(input("Lütfen cevabınızı sayı olarak giriniz: "))
if c==9:
    print("Doğru")
    print("Gece saat sekizde yatıyorum ve yatarken guguklu saatimi sabah dokuza kuruyorum kaç saat uyurum?")
    d=int(input("Lütfen cevabınızı sayı olarak giriniz: "))
if d==1:
    print("Doğru")
    print("30'u yarıma bölüp 10 eklediniz, kaç etti?")
    e=int(input("Lütfen cevabınızı sayı olarak giriniz: "))
if e==70:
    print("PENTAKILL")
else:
    print("YANLIŞ!!! tekrar dene")


# In[ ]:





# In[ ]:




