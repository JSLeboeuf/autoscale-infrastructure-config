# AutoScale AI - Analyse et Plan de Modification du Site Web

**Date:** 18 Novembre 2025
**Site:** https://autoscaleai.ca
**Status:** ✅ En ligne et fonctionnel

---

## 🔍 DÉCOUVERTE

### Site Actuel
- **URL:** https://autoscaleai.ca (et www.autoscaleai.ca)
- **Status:** HTTP 200 - Site actif
- **CDN:** Cloudflare
- **Plateforme:** **Lovable** (détecté via `/lovable-uploads/` dans le code source)

### Project Lovable
- **Project ID:** af5d1a7c-30ce-48be-a587-725aa1dbf98f
- **Project Name:** quebecois-ai-reception
- **Console:** https://lovable.dev/projects/af5d1a7c-30ce-48be-a587-725aa1dbf98f

---

## 🏗️ STACK TECHNIQUE (Détecté)

### Frontend
```
Framework: React (SPA - Single Page Application)
Build Tool: Vite (détecté via /assets/index-BFZ1Iji4.js)
Fonts: Google Fonts (Inter + Poppins)
CSS: TailwindCSS (probable, standard Lovable)
Hébergement: Lovable Platform
```

### Meta/SEO
```
✅ Title optimisé
✅ Description (155 caractères)
✅ Keywords
✅ Open Graph (Facebook)
✅ Twitter Cards
✅ Schema.org JSON-LD
✅ Canonical URL
```

### Performance
```
✅ Preconnect (Google Fonts)
✅ DNS Prefetch (Calendly)
✅ Font preload
✅ Cloudflare CDN
```

### Analytics
```
✅ Flock Analytics intégré (/~flock.js)
```

---

## 📊 CONTENU ACTUEL (d'après meta tags)

### Value Proposition
"Ne manquez plus jamais un appel avec notre IA téléphonique"

### Features Mentionnées
- Réponse 24/7
- Prise de rendez-vous automatique
- Messages personnalisés
- Installation en 48h
- Économisez 20 000$/an

### Ciblage
- **Audience:** Entreprises Québécoises
- **Langue:** Français (fr_CA)
- **Service:** Réceptionniste IA téléphonique

### Contact
- Téléphone: +1-514-000-0000 (placeholder?)
- LinkedIn: https://www.linkedin.com/company/autoscale-ai

---

## 🎯 COMMENT MODIFIER LE SITE

### Option 1: Via Lovable UI (Plus Simple)
**Étapes:**
1. Va sur: https://lovable.dev/projects/af5d1a7c-30ce-48be-a587-725aa1dbf98f
2. Login avec ton compte Lovable
3. Édite directement dans l'interface
4. Publie les changements
5. Déploiement automatique

**Avantages:**
- ✅ Interface visuelle
- ✅ Pas besoin de code
- ✅ Déploiement automatique
- ✅ Preview en temps réel

**Inconvénients:**
- ❌ Moins de contrôle fin
- ❌ Pas de versioning Git
- ❌ Limité aux features Lovable

---

### Option 2: Export → GitHub → Modifications → Redéploiement (Recommandé)

#### Étape 1: Exporter le Code depuis Lovable
```
1. Va sur Lovable project console
2. Clique sur "Export" ou "Download Code"
3. Télécharge le ZIP du projet
```

#### Étape 2: Créer Repo GitHub
```bash
# Créer nouveau repo pour le site
cd /home/developer
mkdir autoscale-website
cd autoscale-website

# Extraire le code Lovable (une fois téléchargé)
unzip lovable-export.zip

# Initialiser Git
git init
git add .
git commit -m "feat: Initial export from Lovable"

# Créer repo GitHub
gh repo create autoscale-website --public --source=. --remote=origin
git push -u origin main
```

#### Étape 3: Modifier Localement
```bash
# Je peux maintenant:
- Éditer les composants React
- Modifier le design
- Ajouter nouvelles pages
- Changer le contenu
- Optimiser le code
```

#### Étape 4: Déployer
**Option A: Rester sur Lovable**
```
1. Connecter GitHub au projet Lovable
2. Auto-deploy depuis GitHub
3. Chaque push = nouveau déploiement
```

**Option B: Migrer vers Vercel (Recommandé)**
```bash
# Tu as déjà le token Vercel dans .env
vercel login
vercel link
vercel --prod

# Résultat:
- Déploiement automatique depuis GitHub
- DNS configuré vers Vercel
- SSL automatique
- Meilleure performance
```

**Option C: Héberger sur Hetzner**
```bash
# Via MCP Hetzner:
1. Créer serveur Hetzner
2. Installer Nginx
3. Build React (npm run build)
4. Déployer sur serveur
5. Configurer DNS autoscaleai.ca → IP serveur
6. Setup SSL (Let's Encrypt)

# Avantage: Contrôle total
# Coût: ~4-6€/mois
```

---

### Option 3: Créer Nouveau Site from Scratch (Si refonte complète)

#### Stack Recommandée (Modern 2025)
```
Framework: Next.js 14 (App Router)
Styling: TailwindCSS
UI Components: shadcn/ui
Animations: Framer Motion
Forms: React Hook Form
Validation: Zod
Hosting: Vercel (auto-deploy)
Database: Supabase (déjà configuré)
Analytics: Vercel Analytics
```

#### Création
```bash
# Je peux créer en ~30 minutes:
npx create-next-app@latest autoscale-website-v2 \
  --typescript \
  --tailwind \
  --app \
  --src-dir

# Structure:
autoscale-website-v2/
├── app/
│   ├── page.tsx           # Homepage
│   ├── services/page.tsx  # Page services
│   ├── tarifs/page.tsx    # Pricing
│   ├── contact/page.tsx   # Contact
│   └── demo/page.tsx      # Demo/Réservation
├── components/
│   ├── Hero.tsx
│   ├── Features.tsx
│   ├── Testimonials.tsx
│   ├── Pricing.tsx
│   └── ContactForm.tsx
└── lib/
    └── supabase.ts        # DB connection
```

#### Déploiement
```bash
# Push vers GitHub
git init && git add . && git commit -m "feat: New Next.js website"
gh repo create autoscale-website-v2 --public --source=. --remote=origin
git push -u origin main

# Deploy vers Vercel
vercel --prod

# Configurer DNS (via MCP Namecheap)
# autoscaleai.ca → Vercel IP
```

---

## 🎨 MODIFICATIONS POSSIBLES

### Modifications Simples (1-2h)
- Changer textes/contenu
- Modifier couleurs/branding
- Ajouter/retirer sections
- Changer images
- Modifier CTA (Call-to-Action)
- Updater téléphone de contact
- Ajouter témoignages clients

### Modifications Moyennes (3-8h)
- Ajouter nouvelles pages
- Créer formulaire de contact
- Intégrer Calendly/Cal.com
- Ajouter blog
- Multi-langue (FR/EN)
- Animations avancées
- Optimisations SEO

### Refonte Complète (1-3 jours)
- Nouveau design complet
- Migration vers Next.js
- Dashboard client
- Système de réservation intégré
- Analytics avancés
- A/B testing
- CRM intégré

---

## 🚀 PLAN D'ACTION RECOMMANDÉ

### Phase 1: Export et Setup (30 min)
1. Exporter code depuis Lovable
2. Créer repo GitHub `autoscale-website`
3. Setup environnement local
4. Premier commit

### Phase 2: Modifications (selon besoins)
1. Identifier changements souhaités
2. Développer localement
3. Tester
4. Commit et push

### Phase 3: Déploiement (30 min)
1. Connecter Vercel à GitHub
2. Configurer DNS (via MCP Namecheap)
3. Activer SSL
4. Test production

### Phase 4: Optimisation (1-2h)
1. Performance audit
2. SEO check
3. Mobile responsive
4. Accessibility (WCAG 2.1)

---

## 💡 RECOMMANDATIONS

### Immédiat
1. **Exporter le code Lovable** → avoir backup + versioning
2. **Corriger le téléphone** → +1-514-000-0000 semble être un placeholder
3. **Connecter GitHub** → versioning automatique

### Court Terme
1. **Migrer vers Vercel** → meilleures performances, déploiement automatique
2. **Ajouter vraies analytics** → Vercel Analytics ou Plausible
3. **Setup formulaire contact** → avec Resend (déjà configuré dans .env)

### Moyen Terme
1. **Ajouter blog** → SEO et authority building
2. **Dashboard client** → avec Supabase Auth
3. **A/B testing** → optimiser conversion

---

## 🔗 LIENS UTILES

- **Site actuel:** https://autoscaleai.ca
- **Lovable Console:** https://lovable.dev/projects/af5d1a7c-30ce-48be-a587-725aa1dbf98f
- **Vercel Dashboard:** https://vercel.com/dashboard
- **DNS Management:** Via MCP Namecheap (100% contrôle depuis Claude Code)

---

## ❓ PROCHAINES QUESTIONS POUR TOI

1. **Que veux-tu modifier sur le site actuel?**
   - Contenu/textes?
   - Design/couleurs?
   - Nouvelles fonctionnalités?
   - Tout refaire from scratch?

2. **Préfères-tu:**
   - Rester sur Lovable (simple)?
   - Migrer vers Vercel/Next.js (moderne)?
   - Héberger sur Hetzner (contrôle total)?

3. **Features prioritaires?**
   - Formulaire de contact?
   - Réservation en ligne?
   - Blog?
   - Dashboard client?
   - Autre?

4. **As-tu accès au compte Lovable?**
   - Oui → Je peux te guider pour exporter
   - Non → Je peux créer nouveau site from scratch

---

**Je suis prêt à:**
- ✅ Exporter et modifier le site existant
- ✅ Créer un nouveau site moderne
- ✅ Déployer automatiquement
- ✅ Configurer DNS (via MCP)
- ✅ Setup SSL et CDN

**Dis-moi ce que tu veux faire et je m'en occupe !** 🚀
