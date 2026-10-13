# Copy Cognition Today skill folders into a client skills directory.
# Run from the repository root:
#   .\tools\install.ps1
#   .\tools\install.ps1 -Client cursor -Scope user
#   .\tools\install.ps1 -Skills monitor-and-regulate-thinking,create-through-recomposition

param(
    [ValidateSet("cursor", "claude", "codex", "agents")]
    [string]$Client = "cursor",

    [ValidateSet("user", "project")]
    [string]$Scope = "user",

    [string[]]$Skills = @(
        "monitor-and-regulate-thinking",
        "create-through-recomposition",
        "manage-working-context"
    )
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$skillsRoot = Join-Path $repoRoot "skills"

if (-not (Test-Path (Join-Path $skillsRoot "monitor-and-regulate-thinking\SKILL.md"))) {
    throw "Run this script from a clone of cognition-today-skills. Expected $skillsRoot\<skill>\SKILL.md"
}

$dest = switch ("$Client-$Scope") {
    "cursor-user" { Join-Path $env:USERPROFILE ".cursor\skills" }
    "cursor-project" { Join-Path $repoRoot ".cursor\skills" }
    "claude-user" { Join-Path $env:USERPROFILE ".claude\skills" }
    "claude-project" { Join-Path $repoRoot ".claude\skills" }
    "codex-user" { Join-Path $env:USERPROFILE ".codex\skills" }
    "codex-project" { Join-Path $repoRoot ".codex\skills" }
    "agents-user" { Join-Path $env:USERPROFILE ".agents\skills" }
    "agents-project" { Join-Path $repoRoot ".agents\skills" }
}

New-Item -ItemType Directory -Force $dest | Out-Null

foreach ($name in $Skills) {
    $source = Join-Path $skillsRoot $name
    $skillFile = Join-Path $source "SKILL.md"
    if (-not (Test-Path $skillFile)) {
        throw "Skill folder not found: $source"
    }
    Copy-Item -Recurse -Force $source $dest
    $copied = Join-Path $dest $name
    Write-Host "Installed $name -> $copied"
}

Write-Host ""
Write-Host "Restart the client if the skills do not appear."
Write-Host "In Cursor, check Customize -> Skills, then try /<skill-folder-name> in Agent chat."
