# Jannoo Schule

Eine kleine Schul-Dashboard-Website mit Uhr (lokale Gerätezeit inkl. Millisekunden), Taschenrechner, Fokus-Timer, speicherbarem Stundenplan und optionaler KI-Lernhilfe.

## Wichtig: GitHub Pages und Python

GitHub Pages hostet statische Dateien (HTML/CSS/JavaScript), führt aber **kein Python-Backend** aus. Uhr, Rechner, Timer und Stundenplan funktionieren direkt auf GitHub Pages. Für echte KI-Antworten muss `server.py` auf einem separaten Python-Host laufen; dann muss `fetch('/api/chat', ...)` in `app.js` auf die Backend-Adresse zeigen und CORS dort passend eingerichtet werden.

## Lokal starten

1. Python 3.10+ installieren.
2. Im Projektordner ein Terminal öffnen und ausführen:

   ```bash
   python -m venv .venv
   ```

   Windows:

   ```powershell
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   $env:OPENAI_API_KEY="DEIN_API_KEY"
   python server.py
   ```

   macOS/Linux:

   ```bash
   source .venv/bin/activate
   pip install -r requirements.txt
   export OPENAI_API_KEY="DEIN_API_KEY"
   python server.py
   ```

3. `http://127.0.0.1:5000` öffnen.

**API-Schlüssel niemals in `app.js`, HTML oder ein öffentliches GitHub-Repository schreiben.** Nur als geheime Umgebungsvariable auf dem Backend-Host speichern. API-Nutzung kann Kosten verursachen.

## Auf GitHub Pages veröffentlichen

1. Ein neues GitHub-Repository erstellen.
2. `index.html`, `style.css` und `app.js` hochladen (README kannst du ebenfalls hochladen).
3. Repository → **Settings → Pages** → unter Build and deployment `Deploy from a branch` wählen → Branch `main`, Ordner `/ (root)` → Save.
4. Nach dem Deployment zeigt GitHub die Website-Adresse in Settings → Pages.

Für die echte KI brauchst du zusätzlich einen Python-Host. Die anderen Funktionen laufen ohne Backend. Die Uhr zeigt die Zeit des Geräts; Millisekunden werden im Browser regelmäßig aktualisiert und sind keine präzise Zeitmessung.
