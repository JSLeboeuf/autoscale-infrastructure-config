# AutoScale AI - Configuration Infrastructure

Configuration complète pour le contrôle de l'infrastructure AutoScale AI via Claude Code et MCP (Model Context Protocol).

## 🎯 Objectif

Contrôler 100% de l'infrastructure via conversation naturelle avec Claude Code :
- Gestion DNS (Namecheap)
- Infrastructure serveurs (Hetzner Cloud)
- Base de données (Supabase)
- Déploiements automatisés

## 📊 Status

**Contrôle:** 100% Opérationnel ✅
- ✅ Namecheap DNS - Connecté et testé
- ✅ Hetzner Cloud - Connecté et testé
- ✅ MCP Servers - Installés et configurés
- ✅ Documentation - Complète

## 🏗️ Architecture

### Services Contrôlés

1. **Namecheap** - Gestion DNS et domaines
   - Domaines: `autoscaleai.ca`, `taillagedehaies.ai`
   - Records DNS (A, CNAME, MX, TXT)
   - Configuration automatisée

2. **Hetzner Cloud** - Infrastructure serveurs
   - Création/gestion serveurs
   - Configuration réseau et firewalls
   - Gestion volumes et backups

3. **Supabase** - Base de données
   - Multiple projets configurés
   - PostgreSQL + Auth + Storage

4. **Lovable** - Développement No-Code
   - Projet: quebecois-ai-reception
   - Agent IA téléphonique

### MCP Servers

- **mcp-namecheap** - TypeScript server pour Namecheap API
- **mcp-hetzner** - Python server pour Hetzner Cloud API

## 📁 Structure

```
.
├── README.md                           # Ce fichier
├── .env.example                        # Template credentials
├── .gitignore                          # Protection secrets
│
├── SERVICES.md                         # Liste des services
├── CONTROL_CAPABILITIES.md             # Capacités détaillées
├── INFRASTRUCTURE_STATUS.md            # Status actuel
├── CAPACITES_ACTUELLES.md              # Ce que je peux faire
├── SETUP_COMPLETE.md                   # Guide setup complet
├── NAMECHEAP_WHITELIST_GUIDE.md        # Guide whitelist IP
│
└── scripts/                            # Scripts utilitaires
    ├── test_namecheap_template.py      # Test API Namecheap
    ├── test_hetzner_template.py        # Test API Hetzner
    └── verify_infrastructure.sh        # Vérification complète
```

## 🚀 Installation

### Prérequis

- Node.js (pour mcp-namecheap)
- Python 3.8+ (pour mcp-hetzner)
- Claude Code
- Credentials Namecheap et Hetzner

### 1. Clone le repo

```bash
git clone https://github.com/[USERNAME]/autoscale-infrastructure-config.git
cd autoscale-infrastructure-config
```

### 2. Configure les credentials

```bash
cp .env.example .env
# Éditer .env avec tes vraies valeurs
```

### 3. Installe les MCP Servers

#### Namecheap MCP
```bash
git clone https://github.com/johnsorrentino/mcp-namecheap.git ~/.claude-code/mcp-servers/mcp-namecheap
cd ~/.claude-code/mcp-servers/mcp-namecheap
npm install
npm run build
```

#### Hetzner MCP
```bash
# Installation via uvx (automatique au premier usage)
uvx mcp-hetzner --help
```

### 4. Configure MCP dans Claude Code

Éditer `~/.mcp.json`:

```json
{
  "mcpServers": {
    "namecheap": {
      "command": "node",
      "args": ["/home/developer/.claude-code/mcp-servers/mcp-namecheap/dist/index.js"],
      "env": {
        "NAMECHEAP_API_USER": "YOUR_USERNAME",
        "NAMECHEAP_API_KEY": "YOUR_API_KEY",
        "NAMECHEAP_USERNAME": "YOUR_USERNAME",
        "NAMECHEAP_CLIENT_IP": "YOUR_WHITELISTED_IP"
      }
    },
    "hetzner": {
      "command": "uvx",
      "args": ["mcp-hetzner"],
      "env": {
        "HETZNER_API_TOKEN": "YOUR_HETZNER_TOKEN"
      }
    }
  }
}
```

### 5. Whitelist ton IP dans Namecheap

1. Va sur: https://ap.www.namecheap.com/settings/tools/apiaccess/whitelisted-ips
2. Ajoute ton IP publique
3. Voir `NAMECHEAP_WHITELIST_GUIDE.md` pour détails

### 6. Teste les connexions

```bash
python3 scripts/test_namecheap_template.py
python3 scripts/test_hetzner_template.py
./scripts/verify_infrastructure.sh
```

### 7. Redémarre Claude Code

Les MCP servers seront actifs et prêts !

## 💡 Utilisation

### Exemples de commandes avec Claude Code

#### Gestion DNS
```
"Liste tous mes domaines Namecheap"
"Crée un record A pour api.autoscaleai.ca pointant vers 157.157.221.30"
"Configure www.autoscaleai.ca comme CNAME vers autoscaleai.ca"
```

#### Infrastructure
```
"Crée un serveur Hetzner CX11 à Nuremberg avec Ubuntu 22.04"
"Liste tous mes serveurs"
"Configure un firewall permettant HTTP, HTTPS et SSH"
```

#### Workflows complets
```
"Déploie un backend API:
1. Crée serveur Hetzner CX21
2. Configure api.autoscaleai.ca
3. Setup firewall
4. Retourne les infos SSH"
```

## 🔒 Sécurité

### Fichiers protégés (NON commitables)
- `.env` - Credentials réels
- `.mcp.json` - Configuration avec tokens
- `test_*.py` avec credentials hardcodés

### Fichiers safe (commitables)
- `.env.example` - Template sans credentials
- Tous les `*.md` - Documentation
- Scripts template - Sans credentials hardcodés

### Protection active
Le `.gitignore` est configuré pour protéger automatiquement tous les secrets.

## 📚 Documentation

- **[SERVICES.md](SERVICES.md)** - Liste complète des services utilisés
- **[CONTROL_CAPABILITIES.md](CONTROL_CAPABILITIES.md)** - Capacités de contrôle détaillées
- **[INFRASTRUCTURE_STATUS.md](INFRASTRUCTURE_STATUS.md)** - Status actuel de l'infrastructure
- **[CAPACITES_ACTUELLES.md](CAPACITES_ACTUELLES.md)** - Ce que Claude Code peut faire
- **[SETUP_COMPLETE.md](SETUP_COMPLETE.md)** - Guide complet de setup
- **[NAMECHEAP_WHITELIST_GUIDE.md](NAMECHEAP_WHITELIST_GUIDE.md)** - Guide whitelist IP

## 🛠️ Maintenance

### Mettre à jour les MCP servers

#### Namecheap
```bash
cd ~/.claude-code/mcp-servers/mcp-namecheap
git pull
npm install
npm run build
```

#### Hetzner
```bash
uvx --upgrade mcp-hetzner
```

### Vérifier la configuration
```bash
./scripts/verify_infrastructure.sh
```

## 🤝 Contribution

Ce repo contient la configuration spécifique pour AutoScale AI. Pour des améliorations générales aux MCP servers:
- Namecheap MCP: https://github.com/johnsorrentino/mcp-namecheap
- Hetzner MCP: https://github.com/dkruyt/mcp-hetzner

## 📝 License

MIT

## 👥 Auteur

AutoScale AI - Configuration Infrastructure
Généré avec Claude Code

## 🔗 Liens Utiles

- [Claude Code Docs](https://code.claude.com/docs)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Namecheap API](https://www.namecheap.com/support/api/intro/)
- [Hetzner Cloud API](https://docs.hetzner.cloud/)

---

**Status:** ✅ 100% Opérationnel
**Dernière mise à jour:** 18 Novembre 2025
