param(
    # Commit Message (default="overlay update")
    [Parameter(Mandatory = $false)]
    [string]
    $commitMessage = "overlay update"
)

$OverlayUpdateScriptPath = Join-Path -Path $PSScriptRoot -ChildPath "generateMap.py"
$RepositoryBaseFolderPath = (Get-Item $PSScriptRoot).Parent.Parent.FullName

Write-Host "----- START: Overlay Update -----"
python.exe $OverlayUpdateScriptPath
Write-Host "----- END: Overlay Update -----"

Write-Host "----- GIT: Add -----"
git.exe "-C" $RepositoryBaseFolderPath "add" "*"

Write-Host "----- GIT: Commit -----"
git.exe "-C" $RepositoryBaseFolderPath "commit" "-m" $commitMessage

Write-Host "----- GIT: Push -----"
git.exe "-C" $RepositoryBaseFolderPath "push"

Write-Host "----- DONE! -----"


