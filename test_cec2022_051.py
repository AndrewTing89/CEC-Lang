import sys
sys.path.insert(0, r"C:\Users\Andrews Razer Laptop\Desktop\CEC Lang")
from core.agent import CECAgent

agent = CECAgent(enable_reflection=True)
result = agent.ask("Calculate the general lighting load in volt-amperes for a 5,000 square foot office building per CEC 2022 Table 220.12.")

print("\n" + "=" * 80)
print("FINAL ANSWER:")
print("=" * 80)
answer = result.get('answer', '')
print(answer)

# Check for the correct unit load (1.3 VA/ft²) vs incorrect (14 VA/m²)
if "1.3" in answer and ("VA/ft" in answer or "6,500" in answer or "6500" in answer):
    print("\n" + "=" * 80)
    print("VERDICT: CORRECT")
    print("=" * 80)
    print("Uses 1.3 VA/ft^2 and calculates 6,500 VA")
elif "14" in answer and "VA/m" in answer:
    print("\n" + "=" * 80)
    print("VERDICT: WRONG")
    print("=" * 80)
    print("Uses 14 VA/m^2 (incorrect metric value)")
else:
    print("\n" + "=" * 80)
    print("VERDICT: UNCLEAR")
    print("=" * 80)
    print("Cannot determine which unit load was used")
