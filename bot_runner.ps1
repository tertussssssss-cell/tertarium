# Social Bot Runner - Background posting
$scriptPath = "$PSScriptRoot\social_bot.py"
$logFile = "$PSScriptRoot\bot_log.txt"

# Kill old instances
Get-Process -Name "python*" -ErrorAction SilentlyContinue | Where-Object { $_.CommandLine -like "*social_bot.py*" } | Stop-Process -Force -ErrorAction SilentlyContinue

# Start new instance in background
Start-Process -NoNewWindow -FilePath "python" -ArgumentList "$scriptPath" -RedirectStandardOutput $logFile -RedirectStandardError "${logFile}.err"

Write-Host "✅ Social bot lancé en arrière-plan"
Write-Host "   Log: $logFile"