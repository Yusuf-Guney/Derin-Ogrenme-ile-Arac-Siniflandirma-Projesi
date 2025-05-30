# YOLOv5 Tabanlı Araç Sınıflandırma Projesi

Bu proje, İHA (insansız hava aracı) ile çekilmiş hava görüntüleri üzerinde yer alan araçları otomatik olarak tespit etmek ve sınıflandırmak amacıyla gerçekleştirilmiştir. YOLOv5 modeli kullanılmış ve eğitim Google Colab ortamında GPU desteğiyle gerçekleştirilmiştir.

## 📁 Proje Dosya Yapısı

```
YOLOv5_Arac_Siniflandirma/
├── analysis/                  # Eğitim sonrası analiz grafikleri
├── eğitim_görselleri/        # Modelin eğitildiği örnek görüntüler
├── google_colab_defteri/     # .ipynb uzantılı Colab dosyası
├── model/                    # Eğitilmiş model (best.pt)
├── test_sonuclari/           # Tahmin sonuçları (işaretli görseller)
├── yolov5_arac_siniflandirma_raporu.pdf  # Proje raporu (PDF)
├── data.yaml                 # YOLOv5 eğitim yapılandırma dosyası
└── README.md                 # Bu dosya
```

## 🔗 Bağlantılar

* 🎩 Video Tanıtım: [YouTube Linki](https://www.youtube.com/watch?v=wUR8a0XJOrE)
* 📁 Veri Seti Ham: [Data in Brief](https://www.sciencedirect.com/science/article/pii/S2352340924002336)
* 💻 Veri Seti: [Drive](https://drive.google.com/file/d/1t8VefcJBFV_f7g_11V731jzZYRFCycgz/view?usp=drive_link)

## 📅 Kısa Açıklama

* Veri seti **Data in Brief** yayınından alınmıştır.
* Etiketler .xml formatından YOLO uyumlu .txt formatına dönüştürülmüştür.
* Model eğitimi Google Colab ortamında, GPU desteği kullanılarak yapılmıştır.
* Eğitim süreci boyunca elde edilen analiz ve grafikler `analysis/` klasöründe yer almaktadır.
* Tahmin sonuçları `test_sonuclari/` klasöründe görselleştirilmiştir.
* Projeye ilişkin teknik detaylar ve analizler `yolov5_arac_siniflandirma_raporu.pdf` dosyasında bulunmaktadır.
