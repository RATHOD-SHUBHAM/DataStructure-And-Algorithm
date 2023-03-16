'''
dic = {}

start = 0

0 1 2 3 4 5 6 7 8 9 10 11
H E L L O _ W O R L D  ! 

--------------------------
i = 0
H not in dictionary --> so add it and CALULATE the length of the substring

dic = {h:0}

len = i - start + 1 = 1

increment i
i = 1
------------------------------------------------

i = 1
E not in dictionary --> so add CALULATE the length of the substring


dic = {h:0
       E:1}

len = i - start + 1 = 2

increment i
i = 2

------------------------------------------------

i = 2
L not in dictionary --> so add it and CALULATE the length of the substring


dic = {h:0
       E:1
       L:2}

len = i - start + 1 = 3

increment i
i = 3

------------------------------------------------

i = 3
dic = {h:0
       E:1
       L:2}

L  in dictionary and 
Both L occured after start 
so that means it can be added to substring but we should not add it.

So change our start to index to L so that we can start our new substring from L

start = dic[l] + 1 = 3 # check second O index 7 to undestand better

now add i to dictionary and calculate the length of the substring
dic = {h:0
       E:1
       L:3 }

   
len = i - start + 1 = 1

increment i
i = 4

------------------------------------------------

i = 4
O not in dictionary --> so add it and CALULATE the length of the substring

start = 3
dic = {h:0
       E:1
       L:2
       O:4}

len = i - start + 1 = 2

increment i
i = 5

------------------------------------------------
i = 5
space not in dictionary --> so add it and CALULATE the length of the substring

start = 3
dic = {h:0
       E:1
       L:2
       O:4
       _:5}

len = i - start + 1 = 3

increment i
i = 6

------------------------------------------------

i = 6
W not in dictionary --> so add it and CALULATE the length of the substring

start = 3
dic = {h:0
       E:1
       L:2
       O:4
       _:5
       W:6}

len = i - start + 1 = 4

increment i
i = 6

------------------------------------------------
i = 7

start = 3
dic = {h:0
       E:1
       L:2
       O:4
       _:5
       W:6}

O in dictionary and 
Both O occured after start 
so that means it can be added to substring but we should not add it.

So change our start to index to L so that we can start our new substring from L

start = dic[O] + 1 = 5

now add i to dictionary and calculate the length of the substring
dic = {h:0
       E:1
       L:2
       O:7
       _:5
       W:6}

   
len = i - start + 1 = 3

increment i
i = 8

------------------------------------------------

i = 8
R not in dictionary --> so add it and CALULATE the length of the substring

start = 5
dic = {h:0
       E:1
       L:2
       O:7
       _:5
       W:6
       R:8}

len = i - start + 1 = 4

increment i
i = 9

------------------------------------------------

i = 9

start = 5
dic = {h:0
       E:1
       L:2
       O:7
       _:5
       W:6
       R:8}

L in dictionary and 
But L occured Before start 
so that means it can be added to substring.--> so add it and CALULATE the length of the substring

start = 5
dic = {h:0
       E:1
       L:9
       O:7
       _:5
       W:6
       R:8}

len = i - start + 1 = 5

increment i
i = 10
------------------------------------------------

i = 10
D not in dictionary --> so add it and CALULATE the length of the substring

start = 5
dic = {h:0
       E:1
       L:2
       O:7
       _:5
       W:6
       R:8
       D:10}

len = i - start + 1 = 6

increment i
i = 11
------------------------------------------------

i = 11
! not in dictionary --> so add it and CALULATE the length of the substring

start = 5
dic = {h:0
       E:1
       L:2
       O:7
       _:5
       W:6
       R:8
       D:10
       !:11}

len = i - start + 1 = 7

increment i
i = 12
'''