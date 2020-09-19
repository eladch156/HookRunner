$File = $args[0]

Write-Host "Flask - Replace Static Sources on Comiled Html Script"

(Get-Content $File) -replace '(\w+\.js)', '{{ url_for(''static'', filename=''$1'') }}' | Out-File -Encoding UTF8 $File