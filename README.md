Elbette! İşte senin projen için sade ve açıklayıcı bir `README.md` içeriği:

````markdown
# CREWAI Project

Bu proje, belirli bir konu hakkında Hugging Face modellerini kullanarak araştırma verisi toplar ve bu verilerle Markdown formatında otomatik olarak bir araştırma yazısı üretir.

## 🔧 Kurulum

1. Sanal ortamı etkinleştir:
   ```bash
   .\venv\Scripts\activate
   ```
````

2. Gerekli paketleri yükle:

   ```bash
   pip install -r requirements.txt
   ```

3. Ortam değişkenini tanımla (PowerShell için):

   ```bash
   $env:HUGGINGFACE_API_KEY="hf_XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
   ```

## 🚀 Kullanım

```bash
python main.py
```

1. Sizden bir konu girmeniz istenecek.
2. Hugging Face üzerinden araştırma verisi toplanacak.
3. `output/` klasöründe Markdown formatında bir araştırma raporu oluşturulacak.

## 📁 Çıktılar

- Üretilen dosyalar `output/` klasörüne `.md` uzantılı olarak kaydedilir.
- Dosya adı otomatik olarak konuyla eşleşecek şekilde oluşturulur.

## 📦 Bağımlılıklar

(Tüm bağımlılıklar `requirements.txt` içinde belirtilmiştir.)

## 🛑 Notlar

- Ana proje dizininde `.env` dosyası oluşturup içerisine kendi Hugging Face API anahtarınızı eklemeyi unutmayın.

---

Bu proje sadece eğitim ve araştırma amaçlıdır.
