c,d,e,f,g,a,b,C = map(int,input().split())


sound = [c,d,e,f,g,a,b,C]


sound_ascending = [1,2,3,4,5,6,7,8]

sound_descending = [8,7,6,5,4,3,2,1]

if sound == sound_ascending:
    print("ascending")

elif sound == sound_descending:
    print("descending")

else:
    print("mixed")