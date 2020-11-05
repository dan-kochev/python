# задание_1
hello = 'Рад познакомиться, '
python_age = 29
speed_earth = 29.78

name = input("Привет! Как тебя зовут: ")
print(f"Рад познакомиться, {name.title()} !")

user_age = int(input("\nСколько тебе лет? "))
if user_age < python_age:
    print(f"Знаешь ли ты, что язык Python старше тебя? В этом году ему исполнилось {python_age} лет!")
elif user_age == python_age:
    print("Ого! Да ты ровесник Python :)")
else:
    print(f"Представляешь, когда тебе было {(user_age - python_age)} лет, был создан Python!")

print(f"\nИнтересный факт: в данный момент Земля движется со скоростью {speed_earth} км/ч!")

print("\nПока!")
