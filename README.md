````markdown
# CREWAI: Otomatik Araştırma Yazısı Üretimi

Bu proje, kullanıcıdan alınan bir konuya göre Hugging Face modellerini kullanarak araştırma verisi toplar ve bu verilerle Markdown formatında otomatik bir araştırma yazısı oluşturur.

---

## 🛠️ Kurulum Adımları

Projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edin:

### 1️⃣ Proje Dosyalarını Klonlayın (Eğer GitHub üzerinden alacaksanız)

```bash
git clone https://github.com/can645ari/crewai_project.git
cd crewai_project
````

### 2️⃣ Sanal Ortam Oluşturun ve Aktifleştirin

#### Sanal ortam oluşturma:

```bash
python -m venv venv
```

#### Sanal ortamı aktifleştirme:

**Windows:**

```bash
.\venv\Scripts\activate
```

**MacOS / Linux:**

```bash
source venv/bin/activate
```

### 3️⃣ Gerekli Paketleri Yükleyin

```bash
pip install -r requirements.txt
```

---

## 🔐 Ortam Değişkeni Tanımlama

Uygulamanın çalışabilmesi için Hugging Face API anahtarınızı ortam değişkeni olarak tanımlamanız gerekir.

### PowerShell (Windows) için:

```bash
$env:HUGGINGFACE_API_KEY="hf_XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
```

### MacOS / Linux için:

```bash
export HUGGINGFACE_API_KEY="hf_XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
```

Projenizin ana dizininde `.env` dosyası oluşturup aşağıdaki şekilde API anahtarınızı tanımlayın:

```
HUGGINGFACE_API_KEY=hf_XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

---

## 🚀 Kullanım

```bash
python main.py
```

1. Sizden bir konu girmeniz istenir.
2. Hugging Face API üzerinden araştırma verileri toplanır.
3. `output/` klasöründe, girilen konuya göre adlandırılmış `.md` uzantılı bir araştırma raporu oluşturulur.

---

## 📁 Çıktılar

* Üretilen dosyalar `output/` klasöründe saklanır.
* Dosya adları, girilen konu başlığına göre otomatik olarak belirlenir.

---

## 📦 Bağımlılıklar

Projenin çalışması için gerekli tüm Python kütüphaneleri `requirements.txt` dosyasında tanımlanmıştır.

Yüklemek için:

```bash
pip install -r requirements.txt
```

## 📄 Lisans

Bu proje eğitim ve geliştirme amacıyla sunulmuştur.

---
