# 🕶️ Gözlük Dünyası – Flask ile Dinamik Ürün Yönetimi

Bu proje, Flask kullanılarak geliştirilen basit ve dinamik bir gözlük satış sitesidir. 
Kullanıcı arayüzü ve admin paneli ile birlikte, ürün ekleme, silme, düzenleme ve listeleme gibi temel CRUD işlemleri yapılabilmektedir. 
Proje, SQLite veritabanı ile desteklenmiştir.

### Admin Paneli
![Admin Paneli](ekran-goruntuleri/admin-paneli.png)

## Proje Özellikleri

- Kullanıcı arayüzünde ürün listesi dinamik olarak görüntülenir.
- Admin panelinden ürün:
  - Eklenebilir 
  - Silinebilir 
  - Güncellenebilir ✏️
- SQLite veritabanı bağlantısı yapılmıştır.
- Tüm sayfalar ortak `base.html` şablonunu kullanır (Jinja2 template inheritance).
- Basit ama işlevsel bir CSS tasarımı mevcuttur.