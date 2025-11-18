#!/bin/bash
# Script pour créer le repo GitHub et pusher

echo ""
echo "════════════════════════════════════════════════════════════"
echo "  📤 PUSH VERS GITHUB"
echo "════════════════════════════════════════════════════════════"
echo ""

# Check if gh is authenticated
if ! gh auth status >/dev/null 2>&1; then
    echo "⚠️  GitHub CLI n'est pas authentifié"
    echo ""
    echo "Options:"
    echo ""
    echo "1. Authentifie-toi avec gh:"
    echo "   gh auth login"
    echo ""
    echo "2. Ou créé le repo manuellement sur GitHub puis:"
    echo "   git push -u origin main"
    echo ""
    exit 1
fi

# Get GitHub username
GITHUB_USER=$(gh api user -q .login)

echo "✅ GitHub CLI authentifié"
echo "   Username: $GITHUB_USER"
echo ""

# Check if repo already exists
if gh repo view $GITHUB_USER/autoscale-infrastructure-config >/dev/null 2>&1; then
    echo "ℹ️  Le repo existe déjà"
    echo ""
else
    echo "📝 Création du repo GitHub..."
    gh repo create autoscale-infrastructure-config \
        --public \
        --description "Configuration complète pour contrôler l'infrastructure AutoScale AI via Claude Code (MCP servers: Namecheap, Hetzner)" \
        --source=. \
        --remote=origin

    if [ $? -eq 0 ]; then
        echo "✅ Repo créé avec succès"
    else
        echo "❌ Erreur lors de la création du repo"
        exit 1
    fi
    echo ""
fi

# Push to GitHub
echo "📤 Push vers GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "════════════════════════════════════════════════════════════"
    echo "  ✅ SUCCÈS!"
    echo "════════════════════════════════════════════════════════════"
    echo ""
    echo "   Repo URL: https://github.com/$GITHUB_USER/autoscale-infrastructure-config"
    echo ""
    echo "   Tu peux maintenant:"
    echo "   • Partager la configuration"
    echo "   • Cloner sur d'autres machines"
    echo "   • Collaborer avec d'autres"
    echo ""
    echo "════════════════════════════════════════════════════════════"
    echo ""
else
    echo ""
    echo "❌ Erreur lors du push"
    echo ""
    echo "Essaie manuellement:"
    echo "   git push -u origin main"
    echo ""
fi
