from calculator_operations import OPERATIONS

def calculator():
    print("Oddiy kalkulyator (+, -, *, /)")
    print("Chiqish uchun 'exit' deb yozing.\n")

    while True:
        user_input = input("Masalani kiriting (masalan: 5 + 3): ")

        if user_input.lower() == 'exit':
            print("Dastur tugadi.")
            break

        try:
            # Foydalanuvchi kiritgan ma'lumotni bo‘lish
            num1_str, operator, num2_str = user_input.split()
            num1 = float(num1_str)
            num2 = float(num2_str)

            # Belgini tekshirish
            if operator not in OPERATIONS:
                print("❌ Noto‘g‘ri amal belgisi! Faqat +, -, *, / ishlatish mumkin.")
                continue

            # Hisoblash
            result = OPERATIONS[operator](num1, num2)
            print("Natija:", result)

        except ValueError as e:
            print("❌ Xatolik:", e)
        except Exception:
            print("❌ Noto‘g‘ri kiritildi. Masalan: 5 + 3")

if __name__ == "__main__":
    calculator()
