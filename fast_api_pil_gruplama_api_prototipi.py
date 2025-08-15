GitHub’a yüklemek için adımlar ve tek komut seti:

1. Yerelde proje klasörünü hazırla.
```
mkdir pil-gruplama && cd pil-gruplama
```

2. Dosyaları ekle:
- `app.py` (API kodun)
- `requirements.txt`
- `Dockerfile`
- `Procfile`
- `.replit`
- `replit.nix`

3. Git repo başlat ve dosyaları ekle:
```
git init
git add .
git commit -m "İlk sürüm"
```

4. GitHub’da yeni boş repo oluştur (ör: `pil-gruplama`).

5. GitHub bağlantısını ekle ve push yap:
```
git branch -M main
git remote add origin https://github.com/<kullanıcı-adın>/pil-gruplama.git
git push -u origin main
```

6. Railway veya Replit’te deploy et:
- Railway: New Project > Deploy from GitHub > repo’yu seç > Deploy.
- Replit: Import from GitHub > repo’yu seç > Run.

Not: `<kullanıcı-adın>` kısmını kendi GitHub kullanıcı adınla değiştir.
