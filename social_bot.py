#!/usr/bin/env python3
"""
Social Bot - Post automation for Reddit & Pinterest (ASCII-safe)
"""

import random
import time
import webbrowser
import os
import sys

SITES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sites")
SITE_URL = "http://localhost:8080"

REDDIT_SUBREDDITS = [
    "gadgets", "deals", "amazondeals", "productivity", "fitness",
    "crypto", "homeoffice", "survival", "skincare", "gaming",
    "dogs", "cats", "amazon_prime", "amazonfinds", "tech",
    "BuyItForLife", "Frugal", "shopping", "frugalmalefashion",
    "dealsreddit"
]

PINTEREST_BOARDS = [
    "Tech Gadgets", "Home Office", "Fitness", "Beauty Tips",
    "Gaming Setup", "Pet Lovers", "Survival Gear", "Make Money Online"
]

POST_TEMPLATES = {
    "gadgets": [
        "I tested 50 gadgets this year. Here are the 10 that actually surprised me {url}",
        "Stop wasting money on bad tech. These 10 gadgets are actually worth it {url}",
        "Amazon has some hidden gems right now. Here's my top 10 {url}",
    ],
    "money": [
        "I make 500 EUR/month from home doing this. Full guide {url}",
        "No BS guide to making money online in 2026 {url}",
        "Quit your 9-5 with these 5 income streams {url}",
    ],
    "ai": [
        "These AI tools just replaced my entire team {url}",
        "5 AI tools that will save you 20 hours a week {url}",
        "If you're not using these AI tools, you're losing money {url}",
    ],
    "fitness": [
        "I got abs in 21 days with this gear. No gym needed {url}",
        "Home gym setup under 200 EUR. Full breakdown {url}",
        "Best fitness gadgets of 2026 (tested) {url}",
    ],
    "crypto": [
        "3 passive crypto strategies that work in 2026 {url}",
        "I let AI trade for me. Here's what happened {url}",
        "Crypto passive income without trading {url}",
    ],
    "homeoffice": [
        "My home office setup doubled my productivity {url}",
        "Best home office gear under 500 EUR {url}",
        "Ergonomic setup that saved my back {url}",
    ],
    "survival": [
        "2026 survival kit: what you actually need {url}",
        "Don't panic buy. Here's the real survival kit {url}",
        "Survival gear that won't break the bank {url}",
    ],
    "beauty": [
        "10 beauty products that make you look 10 years younger {url}",
        "I tested 50 beauty products. These 10 actually work {url}",
        "Dermatologist-approved beauty hacks {url}",
    ],
    "gaming": [
        "Pro gaming setup under 500 EUR {url}",
        "Best budget gaming gear that pros actually use {url}",
        "I built a gaming setup for 500 EUR. Here's how {url}",
    ],
    "pets": [
        "My dog's favorite accessories on Amazon {url}",
        "Best pet products tested by vets {url}",
        "Smart pet gear that makes life easier {url}",
    ]
}

def get_niche_from_slug(slug):
    mapping = {
        "best-gadgets-2026": "gadgets",
        "make-money-online": "money",
        "ai-tools-productivity": "ai",
        "fitness-2026": "fitness",
        "crypto-passive": "crypto",
        "home-office": "homeoffice",
        "survival-kit": "survival",
        "beauty-hacks": "beauty",
        "gaming-setup": "gaming",
        "pet-accessories": "pets",
    }
    return mapping.get(slug, "gadgets")

def get_slugs():
    slugs = []
    for d in os.listdir(SITES_DIR):
        if os.path.isdir(os.path.join(SITES_DIR, d)):
            slugs.append(d)
    return slugs

def open_reddit_post(subreddit, title):
    url = f"https://www.reddit.com/r/{subreddit}/submit?title={title}"
    webbrowser.open(url)
    print(f"  [Reddit] r/{subreddit}")
    time.sleep(1.5)

def open_pinterest_pin(board, description, image_url="https://picsum.photos/800/1200"):
    url = "https://www.pinterest.com/pin/create/button/"
    pin_url = f"{url}?url={SITE_URL}&media={image_url}&description={description}&board={board}"
    webbrowser.open(pin_url)
    print(f"  [Pinterest] {board}")
    time.sleep(1.5)

def main():
    slugs = get_slugs()
    if not slugs:
        print("No pages found!")
        return

    print("=" * 60)
    print("SOCIAL BOT - AFFILIATE FARM")
    print("=" * 60)
    print(f"\nPages available: {len(slugs)}")
    sys.stdout.flush()
    
    while True:
        print("\n--- NEW POSTING CYCLE ---")
        sys.stdout.flush()
        
        for slug in slugs:
            niche_key = get_niche_from_slug(slug)
            page_url = f"{SITE_URL}/{slug}/"
            templates = POST_TEMPLATES.get(niche_key, POST_TEMPLATES["gadgets"])
            
            template = random.choice(templates)
            post_text = template.format(url=page_url)
            
            print(f"\n[Page] {slug}")
            print(f"  Text: {post_text[:80]}...")
            sys.stdout.flush()
            
            # Post to 2 random subreddits
            subreddits = random.sample(REDDIT_SUBREDDITS, min(2, len(REDDIT_SUBREDDITS)))
            for sr in subreddits:
                open_reddit_post(sr, post_text[:295])
            
            # Post to 1 Pinterest board
            board = random.choice(PINTEREST_BOARDS)
            open_pinterest_pin(board, post_text)
        
        print("\n[DONE] Cycle complete for all pages.")
        print(f"[WAIT] Next cycle in 60 minutes...")
        sys.stdout.flush()
        
        try:
            time.sleep(3600)
        except KeyboardInterrupt:
            print("\n[STOP] Stopped by user.")
            break

if __name__ == "__main__":
    main()