import random

bot = random.randint(1, 25)

print("\n\n== Tebak Angka ==\n\n* antara 1 - 25\n\n")
coba = 5

while coba > 0:
    user = int(input('Tebak Angka : '))
    if user > bot:
        coba -= 1
        print("\n# Tebakan Lebih Besar #\n")
        print(f'Kesempatan tersisa {coba} kali lagi')
    elif user < bot:
        coba -= 1
        print("\n# Tebakan Lebih Kecil #\n")
        print(f'Kesempatan tersisa {coba} kali lagi')
    elif user == bot:
        coba -= 1
        print("\n# Tebakan Benar #\n")
        print(f'Angka tebakan adalah {bot}\n')
        print(f'Kesempatan tersisa {coba}')
        print("\n== Terimakasih Telah Bermain ==\n\n")
        break
if coba == 0:
    print("\nKesempatan habis")
    print("\n# Kamu Kalah #\n")
    print(f'Angka tebakan adalah {bot}')
    print("\n== Terimakasih Telah Bermain ==\n\n")