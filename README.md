# SözlükLens — Ekşi Sözlük Görsel Beğeni Analizi

Bu proje, Ekşi Sözlük’teki “Sözlük Yazarlarının Çektiği Fotoğraflar” başlığında paylaşılan 68.292 görselin beğeni sayıları ve çeşitli özelliklerinin analizini, görsellerin sınıflandırılmasını ve bir makine öğrenmesi modeli geliştirilmesini içermektedir.
Görseller Selenium ile web scraping yöntemiyle toplanmış, indirme işlemlerinde ise çok sayıda görseli hızlıca çekebilmek için multithreading kullanılmıştır.
---

##  Proje Çalıştırma Adımları

Projeyi çalıştırmadan önce aşağıdaki iki dosyada gerekli düzenlemeleri yapmanız gerekir:

`config.py` -> `project_root` değişkenine proje dosyalarını indirdiğiniz klasörün path'i girilmelidir.
                Örnek:
                project_root = r"C:\Users\kullanici_adiniz\Desktop\Projeler\Project Eksi Sozluk"

`env_login.env` -> Görsellerin aldığı beğenileri görebilmek için kullanıcı girişi yapılması şartı bulunduğu için; 
                  `MY_EKSISOZLUK_EMAIL ve MY_EKSISOZLUK_PASSWORD` değişkenlerine aşağıdaki gibi email ve şifrenizi girmeniz gerekmekte.
                   MY_EKSISOZLUK_EMAIL="örnek_mail_adresi[at]gmail.com"
                   MY_EKSISOZLUK_PASSWORD="örnek_şifre_123"

1. **`app-1 prepare links.ipynb`**  
   - Bu Ekşi Sözlük üzerinde görsel içeren entry’lerin linklerini toplar.

2. **`app-2 download images.ipynb`**  
    - Bu ise toplanan linkleri önce Multithreading yöntemi ile yüksek performans ile indirir.
    - Ardından indirilemeyen görsellerin sayfalarına Selenium ile giderek görseli tarayıcıda açarak indirir. 

4. **`app-3 analysis.ipynb`**  
   - İndirilen görselleri sınıflandırır (örneğin doğa, manzara, kedi, cadde vs.).  
   - Görselleri barındıran entry bilgilerini işler.  
   - EDA (Keşifsel Veri Analizi) yapar ve görsel metrikleri hesaplar.  
   - Beğeni eğilimlerini inceler ve çıkarımlar yapar.
   - Makine öğrenme modelini inşa eder.

---
