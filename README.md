### Parmak İşaretlerinden Alınan Veri ile Led Kontrolü

Bu repo **[Ahmed ELTAYEB](https://www.linkedin.com/in/ahmed-eltayeb113/)** ile geliştirmekte olduğumuz projemizin bir kısmını barındırıyor.

#### Özet

Bu kısımda, bilgisayar görüşü, LED kullanımı ve mikrodenetleyici programlamasını bir araya getirerek basit bir kullanıcı etkileşim sistemi oluşturmayı amaçlamaktadır. Parmak işaretlerine dayalı bu etkileşim yöntemi, çeşitli uygulamalar için uyarlanabilir ve geliştirilebilir.

#### Kullanılan Malzemeler

- **Arduino Uno**
- **LED'ler (5 adet)**
- **220Ω dirençler (her LED için bir adet)**
- **Bağlantı kabloları**
- **Breadboard**
- **Kamera (USB kamera veya dahili kamera)**
- **Bilgisayar (Python programını çalıştırmak için)**

#### Devre Şeması

LED'lerin Arduino Uno'ya nasıl bağlanacağını gösteren bir devre şeması:

- LED1: Arduino dijital pin 2
- LED2: Arduino dijital pin 3
- LED3: Arduino dijital pin 4
- LED4: Arduino dijital pin 5
- LED5: Arduino dijital pin 6

Her LED, bir 220Ω direnç üzerinden toprak hattına (GND) bağlanmıştır.

#### Yazılım Bileşenleri

1. **Python Programı:**
   - **OpenCV ve mediapipe Kütüphanesi:** Parmak işaretlerini tespit etmek ve tanımlamak için kullanılır.
   - **Serial Kütüphanesi:** Arduino ile seri iletişim kurmak için kullanılır.
   - **pyttsx3 Kütüphanesi:** Parmak işaretlerini konumlarına göre seslendirme uygulaması için kullanıldı.
2. **Arduino Kodu:**
   - Arduino, seri port üzerinden gelen veriyi okuyarak ilgili LED'leri kontrol eder.

#### Kurulum ve Çalıştırma

1. **Arduino Kodunun Yüklenmesi:**
   - `led_control.ino` dosyasını Arduino IDE ile açın.
   - Arduino Uno'nuzu bilgisayarınıza bağlayın.
   - Kodu Arduino'ya yükleyin.
   - Serial port seçiminde dikkatli olun!
2. **Python Programının Çalıştırılması:**
   - Gerekli Python kütüphanelerini yükleyin:
     ```sh
     pip install requirements.txt
     ```
   - python dosyasını çalıştırın:
     ```sh
     python finger_tracking.py
     ```

     
  https://github.com/Talha-Bicak/Hand-Gesture-LED-Control/assets/119726909/55bf4697-9c8a-43b3-a763-500681d0cc0f


## İletişim

 Beni [LinkedIn](https://www.linkedin.com/in/muhammed-talha-bıçak) üzerinden takip edebilirsiniz.

 GitHub üzerinden takip edebilir ve mesaj gönderebilirsiniz: [@talha-bicak](https://github.com/talha-bicak)


