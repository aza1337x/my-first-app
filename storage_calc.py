# Файл: storage_calc.py
# Вариант: 23
# Автор: Тулегенов Азамат Эдуардович
# Описание: Калькулятор размеров данных

def main():
    print("=== Калькулятор размеров данных ===")
    
    try:
        bytes_input = int(input("Введите количество байт: "))
    except ValueError:
        print("Ошибка: введите целое число.")
        return
    
    # Перевод в КБ и МБ
    kilobytes = bytes_input / 1024
    megabytes = kilobytes / 1024
    
    print("\n=== Результаты ===")
    print(f"Исходное значение (DEC): {bytes_input}")
    print(f"В двоичной системе (BIN): {bin(bytes_input)[2:]}")  # Убрали 0b
    print(f"В шестнадцатеричной системе (HEX): {hex(bytes_input)[2:].upper()}")  # Убрали 0x и сделали заглавные
    print(f"В килобайтах (КБ): {kilobytes:.2f}")
    print(f"В мегабайтах (МБ): {megabytes:.4f}")

if __name__ == "__main__":
    main()