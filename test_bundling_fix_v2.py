"""
Test script for bundling adjustment fix
Tests the full agent response to inspection-009 question multiple times
Saves output to file to avoid Unicode issues
"""

import sys
sys.path.append(r'C:\Users\Andrews Razer Laptop\Desktop\CEC Lang')

from core.agent import CECAgent

# Initialize agent
agent = CECAgent()

# The inspection-009 question
question = """A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps."""

output_file = r'C:\Users\Andrews Razer Laptop\Desktop\CEC Lang\test_results.txt'

with open(output_file, 'w', encoding='utf-8') as f:
    f.write("=" * 80 + "\n")
    f.write("TESTING FULL AGENT WITH INSPECTION-009 QUESTION\n")
    f.write("=" * 80 + "\n")
    f.write(f"\nQuestion: {question}\n")
    f.write(f"\nExpected answer: 20A × 0.71 × 0.80 = 11.36A\n")
    f.write("=" * 80 + "\n")

    # Run the question 4 times
    results = []
    for i in range(1, 5):
        f.write(f"\n\n{'=' * 80}\n")
        f.write(f"RUN {i}/4\n")
        f.write("=" * 80 + "\n")
        print(f"\nRunning test {i}/4...")

        try:
            response = agent.ask(question)
            f.write(f"\nAgent Response:\n{response}\n")

            # Check if the answer contains 11.36A or similar
            response_lower = response.lower()
            if '11.36' in response or '11.4' in response:
                f.write(f"\n[CORRECT] RUN {i}: Found expected answer (11.36A)\n")
                results.append(True)
                print(f"  -> CORRECT: Found 11.36A")
            else:
                f.write(f"\n[INCORRECT] RUN {i}: Did not find expected answer (11.36A)\n")
                results.append(False)
                print(f"  -> INCORRECT: Answer not found")

        except Exception as e:
            f.write(f"\n[ERROR] RUN {i}: {str(e)}\n")
            import traceback
            f.write(traceback.format_exc())
            results.append(False)
            print(f"  -> ERROR: {str(e)}")

    f.write("\n" + "=" * 80 + "\n")
    f.write("SUMMARY\n")
    f.write("=" * 80 + "\n")
    f.write(f"Correct answers: {sum(results)}/4\n")
    f.write(f"Incorrect answers: {4 - sum(results)}/4\n")

print(f"\n\nTest complete. Results saved to: {output_file}")
print(f"Correct answers: {sum(results)}/4")
