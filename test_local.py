#!/usr/bin/env python3
"""
Test rapide de TradingAgents avec un modele local (LM Studio)
"""
from dotenv import load_dotenv
load_dotenv()

from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# Config pour LM Studio
config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "lm studio"
config["backend_url"] = "http://localhost:1234/v1"
config["deep_think_llm"] = "openai/gpt-oss-20b"      # Modele pour reflexion profonde
config["quick_think_llm"] = "ministral-3-8b-reasoning-2512"  # Modele rapide

# Parametres LM Studio (ajuste selon tes besoins)
config["llm_context_length"] = 32768    # Taille du contexte (n_ctx)
config["llm_max_tokens"] = 4096         # Max tokens en sortie
config["llm_temperature"] = 0.7         # Temperature (0.0 = deterministe, 2.0 = creatif)

print("=== Configuration ===")
print(f"Provider: {config['llm_provider']}")
print(f"Backend URL: {config['backend_url']}")
print(f"Deep Think Model: {config['deep_think_llm']}")
print(f"Quick Think Model: {config['quick_think_llm']}")
print(f"Context Length: {config['llm_context_length']}")
print(f"Max Tokens: {config['llm_max_tokens']}")
print(f"Temperature: {config['llm_temperature']}")
print()

# Cree le graphe
print("=== Initialisation du graphe ===")
ta = TradingAgentsGraph(debug=True, config=config)

# Lance l'analyse
print("\n=== Lancement de l'analyse ===")
ticker = "AAPL"
date = "2024-12-01"
print(f"Ticker: {ticker}")
print(f"Date: {date}")
print()

try:
    state, decision = ta.propagate(ticker, date)
    print("\n=== DECISION FINALE ===")
    print(decision)
except Exception as e:
    print(f"\n=== ERREUR ===")
    print(f"{type(e).__name__}: {e}")
    print("\nVerifie que:")
    print("1. LM Studio tourne sur localhost:1234")
    print("2. Un modele est charge")
    print("3. Ta cle ALPHA_VANTAGE_API_KEY est valide dans .env")
