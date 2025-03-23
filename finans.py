import csv
import os
import matplotlib.pyplot as plt

# Dosya yolu (Belgeler klasörü yerine, çalıştığı dizinde kayıt yapıyor)
dosya_yolu = os.path.join(os.path.expanduser("~"), "Documents", "finans_verileri.csv")

header = ['Tarih', 'Kategori', 'Tutar']

# Veri dosyasını okuma veya oluşturma
try:
    with open(dosya_yolu, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)
except FileNotFoundError:
    data = [header]

def veri_goruntule():
    print("\nVeriler:")
    for row in data:
        print(row)

def yeni_veri_ekle():
    tarih = input("Tarih (YYYY-AA-GG): ")

    # Kategori doğrulaması
    while True:
        kategori = input("Kategori (Gelir/Gider): ").strip().capitalize()
        if kategori in ["Gelir", "Gider"]:
            break
        print("Hatalı giriş! Lütfen 'Gelir' veya 'Gider' girin.")

    while True:
        try:
            tutar = float(input("Tutar: "))
            break
        except ValueError:
            print("Hatalı giriş! Lütfen geçerli bir sayı girin.")

    # Tutarı tam sayı yapma (eğer kesirli değilse)
    if tutar.is_integer():
        tutar = int(tutar)

    new_data = [tarih, kategori, tutar]
    data.append(new_data)

    # CSV dosyasına yazma
    with open(dosya_yolu, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(new_data)

    print("Yeni veri başarıyla eklendi.")

def gelir_gider_hesapla():
    toplam_gelir = 0
    toplam_gider = 0

    for row in data[1:]:  # Header'ı atla
        try:
            kategori = row[1].strip().capitalize()
            tutar = float(row[2])
        except (ValueError, IndexError):
            print(f"Geçersiz veri atlandı: {row}")
            continue

        if kategori == "Gelir":
            toplam_gelir += tutar
        elif kategori == "Gider":
            toplam_gider += tutar
    
    print(f"\nToplam Gelir: {toplam_gelir}")
    print(f"Toplam Gider: {toplam_gider}")
    print(f"Kâr/Zarar: {toplam_gelir - toplam_gider}")

def grafik_goster():
    gelirler = []
    giderler = []
    tarihler = []

    for row in data[1:]:  # Header'ı atla
        try:
            tarih = row[0]
            kategori = row[1].strip().capitalize()
            tutar = float(row[2])
        except (ValueError, IndexError):
            continue

        if kategori == "Gelir":
            gelirler.append(tutar)
            giderler.append(0)
        elif kategori == "Gider":
            giderler.append(tutar)
            gelirler.append(0)
        
        tarihler.append(tarih)

    if not tarihler:
        print("Grafik gösterilecek veri bulunamadı!")
        return

    plt.figure(figsize=(10, 5))
    plt.bar(tarihler, gelirler, color='green', label='Gelir')
    plt.bar(tarihler, giderler, color='red', label='Gider', bottom=gelirler)
    plt.xlabel("Tarih")
    plt.ylabel("Tutar")
    plt.title("Gelir ve Gider Grafiği")
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()

def verileri_sifirla():
    global data
    onay = input("Tüm verileri silmek istediğinize emin misiniz? (E/H): ").strip().lower()
    if onay == 'e':
        data = [header]
        with open(dosya_yolu, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
        print("Tüm veriler başarıyla sıfırlandı.")

# Ana program döngüsü
while True:
    print("\n1. Verileri Görüntüle")
    print("2. Yeni Veri Ekle")
    print("3. Gelir ve Gideri Hesapla")
    print("4. Grafik Göster")
    print("5. Verileri Sıfırla")
    print("6. Çıkış")
    secim = input("Bir seçenek girin: ")

    if secim == '1':
        veri_goruntule()
    elif secim == '2':
        yeni_veri_ekle()
    elif secim == '3':
        gelir_gider_hesapla()
    elif secim == '4':
        grafik_goster()
    elif secim == '5':
        verileri_sifirla()
    elif secim == '6':
        break
    else:
        print("Geçersiz seçim! Tekrar deneyin.")
