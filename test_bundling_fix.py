"""
Test script for bundling adjustment fix
Tests the full agent response to inspection-009 question multiple times
"""

import sys
sys.path.append(r'C:\Users\Andrews Razer Laptop\Desktop\CEC Lang')

from core.agent import CECAgent

# Initialize agent
agent = CECAgent()

# The inspection-009 question
question = """A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps."""

print("=" * 80)
print("TESTING FULL AGENT WITH INSPECTION-009 QUESTION")
print("=" * 80)
print(f"\nQuestion: {question}")
print(f"\nExpected answer: 20A × 0.71 × 0.80 = 11.36A")
print("=" * 80)

# Run the question 4 times
for i in range(1, 5):
    print(f"\n\n{'=' * 80}")
    print(f"RUN {i}/4")
    print("=" * 80)

    try:
        response = agent.ask(question)
        print(f"\nAgent Response:\n{response}")

        # Check if the answer contains 11.36A or similar
        response_lower = response.lower()
        if '11.36' in response or '11.4' in response:
            print(f"\n[CORRECT] RUN {i}: Found expected answer (11.36A)")
        else:
            print(f"\n[INCORRECT] RUN {i}: Did not find expected answer (11.36A)")

    except Exception as e:
        print(f"\n[ERROR] RUN {i}: {str(e)}")
        import traceback
        traceback.print_exc()

print("\n" + "=" * 80)
print("TESTING COMPLETE")
print("=" * 80)
