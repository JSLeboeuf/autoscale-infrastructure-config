# Workflow: Contrôle 100% du Site Lovable via Cursor/Claude Code

**Objectif:** Modifier autoscaleai.ca depuis Cursor avec déploiement automatique

**Infrastructure actuelle:**
- Hébergement: Lovable.dev → Heficed (185.158.133.1)
- DNS: Namecheap ✅ (100% contrôlé via MCP)
- Database: Supabase ✅ (credentials disponibles)
- Code: Lovable project (af5d1a7c-30ce-48be-a587-725aa1dbf98f)

---

## 🎯 PLAN D'ACTION (30 minutes)

### Phase 1: Export Code depuis Lovable (5 min)

#### Option A: Export Direct (Recommandé)
```
1. Va sur: https://lovable.dev/projects/af5d1a7c-30ce-48be-a587-725aa1dbf98f
2. Cherche bouton "Export" ou "Download Code" ou "Settings"
3. Télécharge le ZIP du projet
4. Place-le dans /home/developer/
```

#### Option B: Connexion GitHub depuis Lovable
```
1. Dans Lovable dashboard → Settings → Git Integration
2. Connecte ton compte GitHub
3. Lovable créera automatiquement un repo
4. Clone le repo: git clone https://github.com/[username]/[repo-name]
```

---

### Phase 2: Setup Local (10 min)

#### Extraire et Setup
```bash
# Si export ZIP
cd /home/developer
unzip lovable-export-autoscale.zip -d autoscale-website
cd autoscale-website

# Installer dépendances
npm install

# Créer .env local (avec tes vrais credentials)
cp .env.example .env
# Éditer .env avec credentials Supabase, etc.

# Tester localement
npm run dev
# Site devrait être sur http://localhost:5173 ou 3000
```

#### Initialiser Git (si pas déjà fait)
```bash
git init
git add .
git commit -m "feat: Initial export from Lovable"
```

---

### Phase 3: GitHub Setup (5 min)

```bash
# Créer repo GitHub
gh auth login  # Si pas encore fait (code: CE8C-DC6A)
gh repo create autoscale-website --public --source=. --remote=origin

# Push code
git branch -M main
git push -u origin main

# Résultat: https://github.com/jsleboeuf/autoscale-website
```

---

### Phase 4: Reconnecter Lovable → GitHub (10 min)

#### Dans Lovable Dashboard
```
1. Va sur Settings → Deployments
2. Section "Git Integration"
3. Connect to GitHub
4. Sélectionne repo: autoscale-website
5. Branch: main
6. Enable "Auto-deploy on push"

Configuration:
✅ Auto-deploy: ON
✅ Build command: npm run build
✅ Output directory: dist
✅ Environment variables: [copier depuis Lovable]
```

#### Test du Workflow
```bash
# Localement, fais un petit changement
echo "Test" >> README.md
git add README.md
git commit -m "test: Auto-deploy workflow"
git push

# Lovable devrait:
1. Détecter le push
2. Builder automatiquement
3. Déployer sur autoscaleai.ca
4. Prendre ~1-2 minutes
```

---

## 🔄 WORKFLOW DE DÉVELOPPEMENT (une fois setup)

### Modification Typique

```bash
# 1. Ouvre le projet dans Cursor
cd /home/developer/autoscale-website
cursor .

# 2. Demande à Claude Code de modifier
# Exemple: "Change le titre de la page d'accueil"

# 3. Claude Code modifie les fichiers automatiquement

# 4. Test local
npm run dev
# Vérifie sur http://localhost:5173

# 5. Commit et push
git add .
git commit -m "feat: Update homepage title"
git push

# 6. Lovable déploie automatiquement
# Site mis à jour en 1-2 minutes sur autoscaleai.ca
```

---

## 📁 STRUCTURE ATTENDUE DU PROJET LOVABLE

```
autoscale-website/
├── src/
│   ├── components/
│   │   ├── Hero.tsx
│   │   ├── Features.tsx
│   │   ├── Testimonials.tsx
│   │   └── ...
│   ├── pages/
│   │   └── Index.tsx (ou Home.tsx)
│   ├── App.tsx
│   └── main.tsx
├── public/
│   └── assets/
├── index.html
├── package.json
├── tsconfig.json
├── vite.config.ts
└── tailwind.config.js
```

---

## 🎨 MODIFICATIONS COURANTES

### 1. Changer le Texte
```typescript
// src/pages/Index.tsx ou src/components/Hero.tsx
export const Hero = () => {
  return (
    <div>
      <h1>AutoScale AI - Réceptionniste IA 24/7</h1>
      <p>Nouveau texte ici</p>
    </div>
  )
}
```

### 2. Modifier Couleurs
```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: '#0066FF',    // Nouvelle couleur
        secondary: '#FF6B35',
      }
    }
  }
}
```

### 3. Ajouter Nouvelle Page
```bash
# Créer nouvelle page
touch src/pages/Pricing.tsx

# Contenu:
export const Pricing = () => {
  return <div>Pricing page</div>
}

# Ajouter route (React Router)
# Dans App.tsx ou routes.tsx
```

### 4. Changer Téléphone de Contact
```typescript
// Chercher dans:
grep -r "514-000-0000" src/
# Puis remplacer par vrai numéro
```

---

## 🔐 ENVIRONNEMENT VARIABLES

### Dans Lovable Dashboard
```
Settings → Environment Variables

Ajouter:
VITE_SUPABASE_URL=https://wfqilhplonqcxtuykmrq.supabase.co
VITE_SUPABASE_ANON_KEY=eyJhbGciOi...
VITE_CALENDLY_URL=https://calendly.com/...
VITE_PHONE_NUMBER=+1-514-XXX-XXXX
```

### Local (.env)
```bash
# Même chose mais préfixe VITE_ pour Vite
VITE_SUPABASE_URL=...
VITE_SUPABASE_ANON_KEY=...
```

---

## 🚀 DÉPLOIEMENTS

### Auto-Deploy (Recommandé)
```
Chaque git push → Lovable build & deploy automatiquement
Timeline: 1-2 minutes
Rollback: Possible via Lovable dashboard
```

### Manual Deploy
```
Dans Lovable: Deploy → Trigger Manual Deployment
```

### Preview Deployments
```
Pull Request → Lovable crée preview URL
Exemple: https://preview-123-autoscale.lovable.app
```

---

## 🎯 EXEMPLES CONCRETS

### Exemple 1: Changer le Hero
```bash
# Dans Cursor/Claude Code:
"Change le titre principal en:
'Automatisez Votre Réception Téléphonique avec l'IA'
et le sous-titre en:
'Disponible 24/7, Installation en 48h, Économisez 20 000$/an'"

# Claude Code modifie automatiquement:
# src/components/Hero.tsx ou src/pages/Index.tsx

# Puis:
git add .
git commit -m "feat: Update hero copy"
git push

# → Déployé automatiquement
```

### Exemple 2: Ajouter Formulaire Contact
```bash
"Ajoute un formulaire de contact avec:
- Nom complet
- Email
- Téléphone
- Message
- Bouton 'Réserver une Démo'
- Envoie email via Resend API"

# Claude Code:
1. Crée composant ContactForm.tsx
2. Ajoute validation (React Hook Form + Zod)
3. Intègre API Resend
4. Ajoute à la page

# Commit & push → Déployé
```

### Exemple 3: Ajouter Analytics
```bash
"Ajoute Vercel Analytics et PostHog"

# Claude Code:
1. npm install @vercel/analytics posthog-js
2. Initialise dans App.tsx
3. Ajoute event tracking
4. Configure dashboard

# Commit & push → Analytics actif
```

---

## 🔧 TROUBLESHOOTING

### Build Fails
```bash
# Localement:
npm run build

# Check errors, fix, puis:
git add .
git commit -m "fix: Build errors"
git push
```

### Lovable Deploy Stuck
```
1. Lovable Dashboard → Deployments
2. Click sur deployment failed
3. Voir logs
4. Fix errors localement
5. Push again
```

### Env Variables Missing
```
1. Lovable Dashboard → Settings → Environment Variables
2. Ajouter missing variables
3. Re-deploy (manual trigger)
```

---

## 📊 MONITORING

### Lovable Dashboard
```
- Build logs
- Deploy status
- Traffic analytics (basic)
- Error logs
```

### Ajouter Monitoring Avancé
```bash
# Sentry pour errors
npm install @sentry/react

# Vercel Analytics
npm install @vercel/analytics

# PostHog pour product analytics
npm install posthog-js
```

---

## 💰 COÛTS

### Lovable
```
Free Tier: Limité
Pro: ~$20-40/mois
Enterprise: Custom
```

### Alternative: Migration Vercel
```
Free Tier: Excellent (hobby projects)
Pro: $20/mois
Avantages:
- Meilleure performance
- Analytics inclus
- Edge functions
- Plus de contrôle
```

---

## 🎓 RESSOURCES

### Lovable Docs
- https://docs.lovable.dev/

### React/Vite
- https://react.dev/
- https://vitejs.dev/

### TailwindCSS
- https://tailwindcss.com/docs

### Supabase Integration
- https://supabase.com/docs/guides/with-react

---

## ✅ CHECKLIST FINALE

**Setup Initial:**
- [ ] Export code depuis Lovable
- [ ] Setup repo GitHub
- [ ] Connect Lovable → GitHub
- [ ] Test auto-deploy workflow
- [ ] Configure env variables

**Pour Chaque Modif:**
- [ ] Modifier localement (Cursor/Claude Code)
- [ ] Test en local (npm run dev)
- [ ] Commit descriptif
- [ ] Push vers GitHub
- [ ] Vérifier deploy Lovable (1-2 min)
- [ ] Test en production (autoscaleai.ca)

---

## 🚀 TU ES PRÊT !

**Workflow final:**
```
Cursor → Claude Code modifie → Git push → Lovable deploy → Site mis à jour
```

**Temps total:** ~30 secondes à 2 minutes par modification

**Contrôle:** 100% depuis Cursor/Claude Code

**Prêt à commencer ?** 🔥
