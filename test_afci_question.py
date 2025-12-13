import sys
sys.path.insert(0, r'C:\Users\Andrews Razer Laptop\Desktop\CEC Lang')
from core.agent import CECAgent

agent = CECAgent(verbose=True, enable_reflection=True)
result = agent.ask("Is AFCI protection required for bedroom circuits in new residential construction?")

print("ANSWER:")
print(result['answer'])
print()
print("TOOLS:", [tc['tool'] for tc in result.get('trace', {}).get('tool_calls_with_outputs', [])])
