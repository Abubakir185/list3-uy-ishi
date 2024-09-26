# 1. `for` sikli yordamida vazifa: - Besh xil raqamlar ro'yxatini tuzing. - 
# Ro'yxatdagi har bir raqamni alohida qatorga chiqarish uchun "for" siklidan foydalaning.

sonlar = [1, 2, 3, 4, 5]

for i in sonlar:
    print(i)


# 2. `while` tsikli yordamida vazifa: - 
# Besh xil nomdan iborat ro'yxat tuzing. - `while` siklidan foydalanib, ro`yxatning barcha nomlarini chop eting.


print("5 ta son kiriting!")

sonlar = []

for i in range(1, 6):
    son = int(input(f"son{i}: "))
    sonlar.append(son)

print(sonlar)




#  3. `for` tsikli yordamida ro`yxat elementlarini jamlash topshirig`i: - Raqamlar ro'yxatini tuzing. - “For” siklidan foydalanib,
#  roʻyxatning har bir elementini aylanib chiqing va ularning yigʻindisini hisoblang. - Qabul qilingan summani chop eting.

sonlar = [1, 2, 6, 9]
sum = 0

for i in sonlar:
    sum += i 

print(sum)



#  4. `while` tsikli yordamida elementni qidirish vazifasi: - 
# Turli raqamlarni o'z ichiga olgan ro'yxat tuzing. - "While" tsikli bilan ro'yxatdagi birinchi juft sonni toping. - Topilgan raqamni chop eting. 


sonlar = [1, 2, 3, 4, 5]
uzunlik = len(sonlar)
index = 0

while index != uzunlik -1:
    if sonlar[index] % 2 == 0:
        print(sonlar[index])
        break
    index += 1



# 5. “For” tsikli yordamida roʻyxat elementlarini oʻchirish vazifasi: - Bir nechta raqamlardan iborat ro'yxat yarating. - "For" tsiklidan foydalanib, 
# ro'yxatning har bir elementini aylantiring va 5 dan kichik bo'lgan barcha raqamlarni olib tashlang. - O'zgartirilgan ro'yxatni chiqarish.

sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
katta = []

for i in sonlar:
    if i >= 5:
        katta.append(i)
        
print(katta)

# 6. `while` siklidan foydalanib ro`yxatga elementlar qo`shish vazifasi: - Bo'sh ro'yxat yarating. - “While” tsikli yordamida 
# foydalanuvchidan raqamlarni so'rang va foydalanuvchi 0 raqamini kiritmaguncha ularni ro'yxatga qo'shing. - Olingan ro'yxatni ko'rsatish.

list = []

son = int(input("son kiriting: "))
list.append(son)

while son != 0:
    son = int(input("son kiriting: "))
    list.append(son)
    
print(list)

# 7. `for` tsikli yordamida ro`yxat elementlarini indekslash topshirig`i: - Bir nechta turli elementlardan iborat ro'yxat yarating. - 
# "For" siklidan foydalanib, ro'yxatning har bir elementini indeksi bilan birga chiqaring (masalan, "Indeks 0: element").


list = [123, "aaaa", True]
uzunlik = len(list)

for index in range(uzunlik):
    print(f"{index} -> {list[index]}")
