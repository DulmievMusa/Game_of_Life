param(
    [string]$Python = "$PSScriptRoot\.build-tools\python\python.exe"
)

$ErrorActionPreference = 'Stop'
Push-Location $PSScriptRoot
try {
    & $Python -m PyInstaller --noconfirm --clean --onefile --windowed --name GameOfLife main.py
    if ($LASTEXITCODE -ne 0) {
        throw "PyInstaller failed with exit code $LASTEXITCODE"
    }
    Write-Host "Built: $PSScriptRoot\dist\GameOfLife.exe"
}
finally {
    Pop-Location
}
