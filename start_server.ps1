$env:PYTHONIOENCODING='utf-8'
$process = Start-Process -NoNewWindow -PassThru -FilePath "C:\Users\tertu\AppData\Local\Programs\Python\Python313\python.exe" -ArgumentList "-Xutf8 -m http.server 8080 --directory C:\Users\tertu\.openclaw\workspace\affiliate_farm\sites"
Write-Host "Serveur démarré sur http://localhost:8080 PID: $($process.Id)"