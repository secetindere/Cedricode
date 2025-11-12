from flask import Flask
import random

app = Flask(__name__)

technologia_random = [
  "Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
  "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
  "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.",
  "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
  "Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.",
  "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
  "Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır.",
  "Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."
]

egitim_random = [
  "Dijital farkındalık eğitimleri, özellikle gençler arasında teknoloji kullanımını dengelemeye yardımcı olur.",
  "Teknoloji bağımlılığıyla mücadelede ebeveynlerin bilinçlendirilmesi kritik öneme sahiptir.",
  "Okullarda verilen bilinçli internet kullanımı dersleri, çocukların dijital dünyada daha güvenli hareket etmelerini sağlar.",
  "Eğitim kurumları, öğrencilerin teknolojiyle olan ilişkisini dengelemeyi hedefleyen programlar geliştirmelidir.",
  "Teknoloji okuryazarlığı, sadece cihaz kullanmak değil; aynı zamanda dijital dengeyi koruyabilmektir.",
  "Uzmanlara göre, teknoloji bağımlılığını azaltmanın en etkili yollarından biri kontrollü ekran süresi eğitimleridir."
]

@app.route("/")
def ana_sayfa():
  return """
  <h1>Ana Sayfa</h1>
  <p><a href='/rastgele_teknoloji'>Teknoloji hakkında rastgele bir bilgi göster</a></p>
  <p><a href='/egitim'>Eğitim hakkında rastgele bir bilgi göster</a></p>
  """

@app.route("/rastgele_teknoloji")
def rastgele_teknoloji():
  return f"<p>{random.choice(technologia_random)}</p><p><a href='/'>Ana sayfaya dön</a></p>"

@app.route("/egitim")
def egitim():
  return f"<p>{random.choice(egitim_random)}</p><p><a href='/'>Ana sayfaya dön</a></p>"

if __name__ == "__main__":
  app.run(debug=True)
