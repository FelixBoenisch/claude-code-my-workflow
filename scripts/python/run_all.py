"""Run the full analysis pipeline end-to-end."""
import importlib
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from lib import manifest

SCRIPTS = [
    "01_sample_summary",
    "02_balance",
    "03_h1_delegation",
    "04_logit_delegation",
    "05_h2_punishment",
    "06_logit_punishment",
    "07_performance",
    "08_mechanism_effort",
    "09_consort",
    "10_payoffs",
    "11_hypo_delegation",
    "12_order_effects",
    "13_belief_distributions",
    "14_player_b_beliefs",
    "15_player_b_attitudes",
    "16_power",
    "17_logit_extended",
    "18_punishment_robustness",
    "19_attention_comparison",
    "20_punishment_figure",
    "21_realized_vs_anticipated",
    "22_belief_specs",
    "23_beliefs_vs_performance",
    "24_performance_by_delegation",
    "25_punishment_extensive",
]

def main() -> None:
    manifest.reset()
    for name in SCRIPTS:
        print(f"\n=========== {name} ===========")
        mod = importlib.import_module(name)
        mod.main()
    print("\n=== pipeline complete ===")


if __name__ == "__main__":
    main()
