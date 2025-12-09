"""
Simple test for bundling adjustment fix - direct tool and agent testing
"""

import sys
sys.path.append(r'C:\Users\Andrews Razer Laptop\Desktop\CEC Lang')

from core.tools import cec_lookup_ampacity_adjustment
from core.agent import CECAgent

print("=" * 80)
print("BUNDLING ADJUSTMENT FIX - COMPREHENSIVE TEST REPORT")
print("=" * 80)

# ============================================================================
# PART 1: Tool-Level Testing (Direct bundling adjustment lookups)
# ============================================================================
print("\n" + "=" * 80)
print("PART 1: TOOL-LEVEL TESTING")
print("=" * 80)

test_cases = [
    (4, 0.80, "4 conductors (4-6 range)"),
    (6, 0.80, "6 conductors (4-6 range)"),
    (7, 0.70, "7 conductors (7-9 range)"),
    (15, 0.50, "15 conductors (10-20 range)"),
    (25, 0.45, "25 conductors (21-30 range)"),
]

tool_results = []
for num_conductors, expected_factor, description in test_cases:
    result = cec_lookup_ampacity_adjustment.invoke({
        'adjustment_type': 'bundling',
        'num_conductors': num_conductors
    })

    # Extract the factor from the result string
    if str(expected_factor) in result:
        status = "PASS"
        tool_results.append(True)
    else:
        status = "FAIL"
        tool_results.append(False)

    print(f"\n[{status}] {description}")
    print(f"  Expected: {expected_factor}")
    print(f"  Result: {result[:100]}...")

print(f"\nTool Test Summary: {sum(tool_results)}/{len(tool_results)} tests passed")

# ============================================================================
# PART 2: Agent-Level Testing (Full question with calculations)
# ============================================================================
print("\n" + "=" * 80)
print("PART 2: AGENT-LEVEL TESTING (inspection-009 question)")
print("=" * 80)

question = """A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps."""

print(f"\nQuestion: {question}")
print(f"\nExpected Answer: 20A × 0.71 × 0.80 = 11.36A")
print("\n" + "-" * 80)

agent = CECAgent()
agent_results = []

for i in range(1, 5):
    print(f"\nRun {i}/4...", end=" ")

    try:
        response = agent.ask(question)

        # Extract answer from dict if necessary
        if isinstance(response, dict):
            answer = response.get('answer', str(response))
        else:
            answer = response

        # Check for correct answer
        if '11.36' in answer or '11.4' in answer:
            print("PASS - Found 11.36A")
            agent_results.append(True)
        else:
            print("FAIL - Did not find 11.36A")
            agent_results.append(False)
            # Print a snippet of the answer for debugging
            snippet = answer[:200] if len(answer) > 200 else answer
            print(f"  Answer snippet: {snippet}...")

    except Exception as e:
        print(f"ERROR - {str(e)}")
        agent_results.append(False)

print(f"\nAgent Test Summary: {sum(agent_results)}/{len(agent_results)} tests passed")

# ============================================================================
# FINAL SUMMARY
# ============================================================================
print("\n" + "=" * 80)
print("FINAL SUMMARY")
print("=" * 80)
print(f"\nTool-Level Tests:  {sum(tool_results)}/{len(tool_results)} passed")
print(f"Agent-Level Tests: {sum(agent_results)}/{len(agent_results)} passed")

if sum(tool_results) == len(tool_results) and sum(agent_results) == len(agent_results):
    print("\n✓✓✓ ALL TESTS PASSED - Fix is working correctly! ✓✓✓")
    print("\nConclusion: The bundling adjustment fix is SUFFICIENT.")
    print("- All conductor counts return correct bundling factors")
    print("- Agent consistently calculates correct adjusted ampacity (11.36A)")
elif sum(tool_results) == len(tool_results):
    print("\n⚠ Tool tests passed, but agent tests had issues")
    print("\nConclusion: Tool fix is good, but agent may need additional work.")
else:
    print("\n✗ Some tests FAILED - Fix needs more work")
    print("\nConclusion: The bundling adjustment fix is NOT SUFFICIENT.")

print("=" * 80)
