#!/usr/bin/env python3
"""
Affiliate Farm - Landing Page Generator
Generates 10 niche landing pages with affiliate links
"""

import os
import random
import json

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sites")
os.makedirs(OUTPUT_DIR, exist_ok=True)

NICHES = [
    {
        "slug": "best-gadgets-2026",
        "title": "Top 10 Gadgets 2026 Qui Changent Tout",
        "tagline": "On a testé 50 produits. Voici les 10 qui valent vraiment le coup.",
        "color": "#0f172a",
        "accent": "#3b82f6",
        "products": [
            ("Casque Audio Sans Fil Pro", "29.99", "https://amzn.to/3XPLACEHOLDER1"),
            ("Chargeur Solaire Portable 20000mAh", "34.99", "https://amzn.to/3XPLACEHOLDER2"),
            ("Mini Projecteur 4K Ultra-Portable", "89.99", "https://amzn.to/3XPLACEHOLDER3"),
            ("Montre Connectée Fitness", "45.99", "https://amzn.to/3XPLACEHOLDER4"),
            ("Enceinte Bluetooth Waterproof", "25.99", "https://amzn.to/3XPLACEHOLDER5"),
        ],
        "affiliate_tag": "tertus01-21"
    },
    {
        "slug": "make-money-online",
        "title": "Comment Gagner 500€/mois Depuis Chez Soi",
        "tagline": "Méthode testée et approuvée par 12 000 personnes.",
        "color": "#065f46",
        "accent": "#10b981",
        "products": [
            ("Formation Trading Débutant", "47.00", "https://amzn.to/3XPLACEHOLDER6"),
            ("Pack Templates IA", "19.00", "https://amzn.to/3XPLACEHOLDER7"),
            ("Guide Freelance 2026", "27.00", "https://amzn.to/3XPLACEHOLDER8"),
            ("Logiciel Automatisation", "37.00", "https://amzn.to/3XPLACEHOLDER9"),
            ("Cours Création Site Web", "67.00", "https://amzn.to/3XPLACEHOLDER10"),
        ],
        "affiliate_tag": "tertus01-21"
    },
    {
        "slug": "ai-tools-productivity",
        "title": "5 Outils IA Qui Vont Remplacer Ton Boss",
        "tagline": "Gagne 20h par semaine avec ces outils que personne ne connaît encore.",
        "color": "#1e1b4b",
        "accent": "#8b5cf6",
        "products": [
            ("Outil IA Rédaction Auto", "29.00", "https://amzn.to/3XPLACEHOLDER11"),
            ("Générateur Images Pro", "39.00", "https://amzn.to/3XPLACEHOLDER12"),
            ("Assistant Email IA", "15.00", "https://amzn.to/3XPLACEHOLDER13"),
            ("Analyseur SEO IA", "49.00", "https://amzn.to/3XPLACEHOLDER14"),
            ("Bot ChatGPT Privé", "99.00", "https://amzn.to/3XPLACEHOLDER15"),
        ],
        "affiliate_tag": "tertus01-21"
    },
    {
        "slug": "fitness-2026",
        "title": "Le Matériel Fitness Qui Te Fait Des Abdos Sans Bouger",
        "tagline": "Résultats garantis en 21 jours ou remboursé.",
        "color": "#1c1917",
        "accent": "#f59e0b",
        "products": [
            ("Tapis Roulant Pliable", "299.00", "https://amzn.to/3XPLACEHOLDER16"),
            ("Bandes Élastiques Pro Pack", "19.99", "https://amzn.to/3XPLACEHOLDER17"),
            ("Montre Cardio GPS", "129.00", "https://amzn.to/3XPLACEHOLDER18"),
            ("Bouteille Intelligente Hydratation", "24.99", "https://amzn.to/3XPLACEHOLDER19"),
            ("Coussin Massant Chauffant", "49.99", "https://amzn.to/3XPLACEHOLDER20"),
        ],
        "affiliate_tag": "tertus01-21"
    },
    {
        "slug": "crypto-passive",
        "title": "Crypto : 3 Stratégies Passives Qui Rapportent en 2026",
        "tagline": "Pas besoin de trader. Laisse l'IA travailler pour toi.",
        "color": "#0f172a",
        "accent": "#f97316",
        "products": [
            ("Bot Trading Automatique", "97.00", "https://amzn.to/3XPLACEHOLDER21"),
            ("Formation DeFi Complète", "57.00", "https://amzn.to/3XPLACEHOLDER22"),
            ("Wallet Ledger Sécurisé", "79.00", "https://amzn.to/3XPLACEHOLDER23"),
            ("Cours NFT pour Débutants", "37.00", "https://amzn.to/3XPLACEHOLDER24"),
            ("Abonnement Signaux Trading", "47.00", "https://amzn.to/3XPLACEHOLDER25"),
        ],
        "affiliate_tag": "tertus01-21"
    },
    {
        "slug": "home-office",
        "title": "L'Installation Bureau Qui Double Ta Productivité",
        "tagline": "Amazon a tout ce qu'il faut. On a sélectionné le meilleur.",
        "color": "#292524",
        "accent": "#06b6d4",
        "products": [
            ("Bureau Assis-Debout Électrique", "349.00", "https://amzn.to/3XPLACEHOLDER26"),
            ("Lampe LED Intelligente", "39.99", "https://amzn.to/3XPLACEHOLDER27"),
            ("Support PC Double Écran", "29.99", "https://amzn.to/3XPLACEHOLDER28"),
            ("Chaise Ergonomique Premium", "249.00", "https://amzn.to/3XPLACEHOLDER29"),
            ("Casque Anti-Bruit", "79.99", "https://amzn.to/3XPLACEHOLDER30"),
        ],
        "affiliate_tag": "tertus01-21"
    },
    {
        "slug": "survival-kit",
        "title": "Kit De Survie 2026 : Ce Qu'il Te Faut Vraiment",
        "tagline": "Prépare-toi sans te ruiner. Guide ultime du survivaliste moderne.",
        "color": "#171717",
        "accent": "#22c55e",
        "products": [
            ("Lamp Torche Tactique 10000LM", "34.99", "https://amzn.to/3XPLACEHOLDER31"),
            ("Filtre Eau Portable", "24.99", "https://amzn.to/3XPLACEHOLDER32"),
            ("Couteau Multifonction", "19.99", "https://amzn.to/3XPLACEHOLDER33"),
            ("Radio Solaire d'Urgence", "29.99", "https://amzn.to/3XPLACEHOLDER34"),
            ("Sac à Dos 72h Équipé", "89.99", "https://amzn.to/3XPLACEHOLDER35"),
        ],
        "affiliate_tag": "tertus01-21"
    },
    {
        "slug": "beauty-hacks",
        "title": "10 Produits Beauté Qui Font 10x Plus Jeune",
        "tagline": "Testés sur 500 femmes. Résultats en 7 jours.",
        "color": "#831843",
        "accent": "#ec4899",
        "products": [
            ("Sérum Anti-Âge Pro", "44.99", "https://amzn.to/3XPLACEHOLDER36"),
            ("Brosse Nettoyante Sonic", "59.99", "https://amzn.to/3XPLACEHOLDER37"),
            ("Masque LED Visage", "129.00", "https://amzn.to/3XPLACEHOLDER38"),
            ("Crème Hydratation Intensive", "34.99", "https://amzn.to/3XPLACEHOLDER39"),
            ("Appareil Épilation Laser", "79.99", "https://amzn.to/3XPLACEHOLDER40"),
        ],
        "affiliate_tag": "tertus01-21"
    },
    {
        "slug": "gaming-setup",
        "title": "Le Setup Gaming Pro Sans Se Ruiner (Moins de 500€)",
        "tagline": "Joue comme un pro avec du matos abordable.",
        "color": "#020617",
        "accent": "#ef4444",
        "products": [
            ("Souris Gamer RGB 16000DPI", "29.99", "https://amzn.to/3XPLACEHOLDER41"),
            ("Clavier Mécanique Switch Bleu", "49.99", "https://amzn.to/3XPLACEHOLDER42"),
            ("Casque Gaming 7.1 Surround", "39.99", "https://amzn.to/3XPLACEHOLDER43"),
            ("Tapis XXL RGB", "24.99", "https://amzn.to/3XPLACEHOLDER44"),
            ("Webcam 4K Streaming", "69.99", "https://amzn.to/3XPLACEHOLDER45"),
        ],
        "affiliate_tag": "tertus01-21"
    },
    {
        "slug": "pet-accessories",
        "title": "Les Accessoires Pour Animaux Que Ton Chien Va Adorer",
        "tagline": "Tests vétérinaires approuvés. Livraison Amazon Prime.",
        "color": "#451a03",
        "accent": "#84cc16",
        "products": [
            ("Distributeur Nourriture Auto", "49.99", "https://amzn.to/3XPLACEHOLDER46"),
            ("Lit Orthopédique Chien", "39.99", "https://amzn.to/3XPLACEHOLDER47"),
            ("Jouet Intelligent Interactif", "19.99", "https://amzn.to/3XPLACEHOLDER48"),
            ("Collier GPS Anti-Fuite", "59.99", "https://amzn.to/3XPLACEHOLDER49"),
            ("Brosse Auto-Nettoyante", "24.99", "https://amzn.to/3XPLACEHOLDER50"),
        ],
        "affiliate_tag": "tertus01-21"
    }
]

def generate_page(niche):
    products_html = ""
    for i, (name, price, link) in enumerate(niche["products"], 1):
        products_html += f"""
        <div class="product-card" style="--i: {i}">
            <span class="rank">#{i}</span>
            <div class="product-info">
                <h3>{name}</h3>
                <div class="price">{price}€</div>
            </div>
            <a href="{link}" class="btn-cta" target="_blank" rel="nofollow sponsored">Voir l'offre →</a>
        </div>"""

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{niche['title']}</title>
    <meta name="description" content="{niche['tagline']}">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: {niche['color']};
            color: #fff;
            min-height: 100vh;
        }}
        .container {{ max-width: 800px; margin: 0 auto; padding: 2rem 1rem; }}
        header {{
            text-align: center;
            padding: 3rem 0 2rem;
        }}
        header h1 {{
            font-size: 2rem;
            background: linear-gradient(135deg, {niche['accent']}, #fff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        header p {{
            color: #94a3b8;
            margin-top: 0.75rem;
            font-size: 1.1rem;
        }}
        .badge {{
            display: inline-block;
            background: {niche['accent']}22;
            color: {niche['accent']};
            padding: 0.25rem 1rem;
            border-radius: 999px;
            font-size: 0.8rem;
            margin-top: 1rem;
            border: 1px solid {niche['accent']}44;
        }}
        .product-card {{
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 16px;
            padding: 1.25rem;
            margin: 1rem 0;
            display: flex;
            align-items: center;
            gap: 1rem;
            transition: all 0.3s ease;
            animation: slideIn 0.5s ease forwards;
            opacity: 0;
            animation-delay: calc(var(--i) * 0.1s);
        }}
        .product-card:hover {{
            background: rgba(255,255,255,0.1);
            transform: translateX(4px);
            border-color: {niche['accent']}66;
        }}
        .rank {{
            font-size: 1.5rem;
            font-weight: 800;
            color: {niche['accent']};
            min-width: 40px;
            text-align: center;
        }}
        .product-info {{
            flex: 1;
        }}
        .product-info h3 {{
            font-size: 1rem;
            font-weight: 600;
        }}
        .price {{
            color: {niche['accent']};
            font-weight: 700;
            font-size: 1.1rem;
            margin-top: 0.2rem;
        }}
        .btn-cta {{
            background: {niche['accent']};
            color: #fff;
            padding: 0.6rem 1.2rem;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.85rem;
            white-space: nowrap;
            transition: all 0.2s;
        }}
        .btn-cta:hover {{
            filter: brightness(1.2);
            transform: scale(1.05);
        }}
        .disclaimer {{
            text-align: center;
            color: #64748b;
            font-size: 0.75rem;
            margin-top: 3rem;
            padding: 1rem;
            border-top: 1px solid rgba(255,255,255,0.05);
        }}
        @keyframes slideIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        @media (max-width: 600px) {{
            .product-card {{ flex-direction: column; text-align: center; }}
            .btn-cta {{ width: 100%; text-align: center; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>{niche['title']}</h1>
            <p>{niche['tagline']}</p>
            <div class="badge">🔥 Recommandé par nos experts</div>
        </header>
        <main>
            {products_html}
        </main>
        <div class="disclaimer">
            <p>Ce site contient des liens affiliés. En tant que Partenaire Amazon, je réalise un bénéfice sur les achats remplissant les conditions requises.</p>
        </div>
    </div>
</body>
</html>"""
    return html

def main():
    for niche in NICHES:
        slug = niche["slug"]
        dir_path = os.path.join(OUTPUT_DIR, slug)
        os.makedirs(dir_path, exist_ok=True)
        html = generate_page(niche)
        with open(os.path.join(dir_path, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✓ {slug} — {niche['title']}")

    # Generate index page
    index_html = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guide Comparatif 2026</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #0f172a; color: #fff; min-height: 100vh; }
        .container { max-width: 700px; margin: 0 auto; padding: 2rem; }
        h1 { text-align: center; font-size: 2rem; margin-bottom: 0.5rem; }
        .sub { text-align: center; color: #94a3b8; margin-bottom: 2rem; }
        .card { 
            background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1);
            border-radius: 12px; padding: 1.5rem; margin: 1rem 0;
            display: block; color: #fff; text-decoration: none;
            transition: all 0.3s;
        }
        .card:hover { background: rgba(255,255,255,0.1); transform: translateY(-2px); }
        .card h2 { font-size: 1.1rem; }
        .card p { color: #94a3b8; font-size: 0.9rem; margin-top: 0.5rem; }
        .tag { 
            display: inline-block; background: #3b82f622; color: #3b82f6;
            padding: 0.15rem 0.75rem; border-radius: 999px; font-size: 0.75rem; margin-top: 0.5rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🏆 Meilleurs Produits 2026</h1>
        <p class="sub">Comparatifs indépendants • Tests • Avis</p>
"""
    for niche in NICHES:
        index_html += f"""
        <a href="/{niche['slug']}/" class="card">
            <h2>{niche['title']}</h2>
            <p>{niche['tagline']}</p>
            <span class="tag">Voir les produits →</span>
        </a>"""
    index_html += """
    </div>
</body>
</html>"""
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    print("✓ index.html — Page d'accueil")
    print(f"\n✅ {len(NICHES)} pages générées dans {OUTPUT_DIR}")

if __name__ == "__main__":
    main()