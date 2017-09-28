import math

x = 14567/1234

print(x)

y = 123+456-123/456+123

print(y)

x = 16

myans = math.sqrt(x)



print(myans)

x = 4

y = 3

myans2 = math.pow(x,y)

print(myans2)

x = 64

myans3 = math.log2(x)

print(myans3)

pi = 3.14

myans4 = format(pi, ".4f")

print(myans4)

x = 1.2

myans5 = math.sin(x)

print(myans5)

x = 3.14

myans6 = math.cos(x)

print(myans6)

x = 3.14

myans7 = math.sin(x/2)

print(myans7)

domain = "urvesh.bhowan@ncirl.ie"

newDomain = domain.split("@")

domain2 = newDomain[1]

newUrl = "www." + domain2

print(newUrl)

splitemail = "ringo@thebeetles.co.uk".split("@")

domain3 = splitemail[1]

url = "www." + domain3

print(url)



song = "we wish you a merry christmas"
splitsong = song.split()
print(splitsong)


mySong2 = "It was Christmas Eve babe, In the drunk tank, An old man said to me won't see another one"

splitsong2 = mySong2.split()
print(splitsong2)

lastSong = "Have yourself a merry little Christmas, Let your hear be light"
splitSong3 = lastSong.split("your")
print(splitSong3)

myAddress = "Wotton,Ashbourne Rd, The Ward ,Co.Dublin ,Ireland"
mynewAddress = myAddress.split("Ireland")
print(mynewAddress)
#Question 3(a)

p0 = 3/12

p1 = 9/12

entropy = ((-p0)*math.log2(p0)) + ((-p1)*math.log2(p1))

print(entropy)

i0 = 4/12

entropy2 = ((-i0)*math.log2(i0)) * 3

print(entropy2)
#Question 3(b)

#Question 3(c)

#Question 3(d)

#Question 4(a)

dictionary = {"Team": "Leinster", "Form": "(W, D, W, L, W)", "Ground": "RDS"}

dictionary["Ground"] = "Aviva"

dictionary["Form"] = "(D, W, L, W, W) "

print(dictionary)

masterList = {"Team": "Leinster", "Form": "(W, D, W, L, W)", "Ground": "RDS","Team": "Munster", "Form": "(W, L, L, L, W)", "Ground": "Thomand Park",
"Team": "Connacht", "Form": "(W, W, W, L, L)", "Ground": "Thomand Park",
"Team": "Ulster", "Form": "(W, D, W, D, W)", "Ground": "Ravendale"}

#print(masterList[8]["W"])

#Question5

#for line in open('file.txt'):
 #   for word in line.split():
  #      if word.endswith('ing'):
   #         print(word)

#Question6

#Question7

#Question8



