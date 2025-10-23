# Oddiy arifmetik amallar uchun funksiyalar

def add(a, b):
    return a + b  # Qo‘shish

def sub(a, b):
    return a - b  # Ayirish

def mul(a, b):
    return a * b  # Ko‘paytirish

def div(a, b):
    if b == 0:
        raise ValueError("Nolga bo‘lish mumkin emas!")  # Xatolik
    return a / b  # Bo‘lish

# Belgilar orqali funksiyani chaqirish uchun lug‘at
OPERATIONS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}
