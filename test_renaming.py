"""
Test script to verify the unified_tools -> knowledge_tools renaming
"""

def test_imports():
    """Test 1: Import all renamed modules and verify no errors"""
    print("=" * 60)
    print("TEST 1: Module Imports")
    print("=" * 60)

    tests_passed = 0
    tests_failed = 0

    # Test 1a: core.tools
    try:
        from core.tools import get_all_tools
        print("[PASS] Test 1a: from core.tools import * - PASS")
        tests_passed += 1
    except Exception as e:
        print(f"[FAIL] Test 1a: from core.tools import * - FAIL: {e}")
        tests_failed += 1

    # Test 1b: CEC knowledge tools
    try:
        from core.cec_knowledge_tools import get_cec_knowledge_tools, CECKnowledgeTools
        print("[PASS] Test 1b: CEC knowledge tools import - PASS")
        tests_passed += 1
    except Exception as e:
        print(f"[FAIL] Test 1b: CEC knowledge tools import - FAIL: {e}")
        tests_failed += 1

    # Test 1c: NEC knowledge tools
    try:
        from core.nec_knowledge_tools import get_knowledge_tools, NECKnowledgeTools
        print("[PASS] Test 1c: NEC knowledge tools import - PASS")
        tests_passed += 1
    except Exception as e:
        print(f"[FAIL] Test 1c: NEC knowledge tools import - FAIL: {e}")
        tests_failed += 1

    # Test 1d: Agent import
    try:
        from core.agent import get_agent, CECAgent
        print("[PASS] Test 1d: Agent import - PASS")
        tests_passed += 1
    except Exception as e:
        print(f"[FAIL] Test 1d: Agent import - FAIL: {e}")
        tests_failed += 1

    print(f"\nTest 1 Summary: {tests_passed} passed, {tests_failed} failed")
    return tests_passed, tests_failed


def test_agent_instantiation():
    """Test 2: Test that the agent can be created"""
    print("\n" + "=" * 60)
    print("TEST 2: Agent Instantiation")
    print("=" * 60)

    try:
        from core.agent import CECAgent
        agent = CECAgent(verbose=False)
        print("[PASS] Test 2: Agent instantiation - PASS")
        print(f"  - Model: {agent.model_name}")
        print(f"  - Tools loaded: {len(agent.tools)}")
        return 1, 0
    except Exception as e:
        print(f"[FAIL] Test 2: Agent instantiation - FAIL: {e}")
        import traceback
        traceback.print_exc()
        return 0, 1


def test_tools_accessibility():
    """Test 3: Verify tools are accessible and correctly configured"""
    print("\n" + "=" * 60)
    print("TEST 3: Tools Module Accessibility")
    print("=" * 60)

    try:
        from core.tools import get_all_tools
        tools = get_all_tools()

        print(f"[PASS] Test 3: Tools module - PASS")
        print(f"  - Total tools loaded: {len(tools)}")
        print(f"\n  Tool list (first 15):")

        for i, tool in enumerate(tools[:15], 1):
            print(f"    {i:2d}. {tool.name}")

        # Verify expected tools exist
        tool_names = {t.name for t in tools}
        expected_tools = [
            'cec_search',
            'cec_exception_search',
            'compare_with_nec',
            'nec_search',
            'nec_exception_search',
            'cec_lookup_conductor_ampacity',
            'cec_lookup_grounding_conductor',
        ]

        missing_tools = [t for t in expected_tools if t not in tool_names]

        if missing_tools:
            print(f"\n  [WARNING] Some expected tools are missing: {missing_tools}")
            return 0, 1
        else:
            print(f"\n  [PASS] All expected tools present")
            return 1, 0

    except Exception as e:
        print(f"[FAIL] Test 3: Tools module - FAIL: {e}")
        import traceback
        traceback.print_exc()
        return 0, 1


def test_knowledge_tools_classes():
    """Test 4: Verify knowledge tools classes can be instantiated"""
    print("\n" + "=" * 60)
    print("TEST 4: Knowledge Tools Classes")
    print("=" * 60)

    tests_passed = 0
    tests_failed = 0

    # Test CEC Knowledge Tools
    try:
        from core.cec_knowledge_tools import CECKnowledgeTools
        cec_tools = CECKnowledgeTools()
        print("[PASS] Test 4a: CECKnowledgeTools instantiation - PASS")
        tests_passed += 1
    except Exception as e:
        print(f"[FAIL] Test 4a: CECKnowledgeTools instantiation - FAIL: {e}")
        tests_failed += 1

    # Test NEC Knowledge Tools
    try:
        from core.nec_knowledge_tools import NECKnowledgeTools
        nec_tools = NECKnowledgeTools()
        print("[PASS] Test 4b: NECKnowledgeTools instantiation - PASS")
        tests_passed += 1
    except Exception as e:
        print(f"[FAIL] Test 4b: NECKnowledgeTools instantiation - FAIL: {e}")
        tests_failed += 1

    print(f"\nTest 4 Summary: {tests_passed} passed, {tests_failed} failed")
    return tests_passed, tests_failed


def main():
    """Run all tests and report results"""
    print("\n" + "=" * 60)
    print("CEC LANG AGENT - RENAMING VERIFICATION TEST SUITE")
    print("Testing: unified_tools -> knowledge_tools renaming")
    print("=" * 60 + "\n")

    total_passed = 0
    total_failed = 0

    # Run all tests
    p, f = test_imports()
    total_passed += p
    total_failed += f

    p, f = test_agent_instantiation()
    total_passed += p
    total_failed += f

    p, f = test_tools_accessibility()
    total_passed += p
    total_failed += f

    p, f = test_knowledge_tools_classes()
    total_passed += p
    total_failed += f

    # Final summary
    print("\n" + "=" * 60)
    print("FINAL TEST SUMMARY")
    print("=" * 60)
    print(f"Total tests passed: {total_passed}")
    print(f"Total tests failed: {total_failed}")

    if total_failed == 0:
        print("\n[SUCCESS] ALL TESTS PASSED - Renaming successful!")
        print("  The CEC Lang agent is working correctly after renaming.")
    else:
        print(f"\n[FAIL] {total_failed} TEST(S) FAILED - Issues detected")
        print("  Please review the errors above.")

    print("=" * 60 + "\n")

    return total_failed == 0


if __name__ == "__main__":
    import sys
    success = main()
    sys.exit(0 if success else 1)
