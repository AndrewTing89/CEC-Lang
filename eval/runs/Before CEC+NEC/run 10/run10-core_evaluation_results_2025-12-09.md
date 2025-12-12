# CEC Agent Evaluation - LangChain + Groq

**Date:** 2025-12-09
**Model:** gemini-2.5-pro
**Agent:** California Electrical Code Agent (LangChain)
**Architecture:** California-First (CEC 2022 primary, NEC 2023 comparison)

## Executive Summary

| Metric | Value |
|--------|-------|
| **Total Questions** | 28 |
| **Successful** | 0 (0.0%) |
| **Failed** | 28 |
| **Total Duration** | 10364.5s |
| **Avg per Question** | 370.2s |

---

## Results by Question


## Baseline

### baseline-001: table_lookup

**Question:** What is the ampacity of 12 AWG copper conductor at 75°C termination?

**Expected:** 20 amperes

**CEC Ref:**  | **NEC Ref:** Table 310.16

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### baseline-002: table_lookup

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Expected:** 6 AWG copper

**CEC Ref:**  | **NEC Ref:** Table 310.16

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### baseline-003: knowledge_simple

**Question:** Where is GFCI protection required in a residential kitchen?

**Expected:** All receptacles that serve the kitchen countertop surfaces shall have GFCI protection. Additionally, dishwashers require GFCI protection.

**CEC Ref:**  | **NEC Ref:** 210.8(A)

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### baseline-004: knowledge_simple

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Expected:** Yes, AFCI protection is required for all 120-volt, 15- and 20-ampere branch circuits supplying outlets in bedrooms.

**CEC Ref:**  | **NEC Ref:** 210.12

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### baseline-005: table_lookup

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Expected:** Yes, 4/0 AWG aluminum or copper-clad aluminum

**CEC Ref:**  | **NEC Ref:** Table 310.12

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### baseline-006: knowledge_simple

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Expected:** 36 inches (3 feet)

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1)

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### baseline-007: knowledge_simple

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Expected:** Minimum of two 20-ampere small appliance branch circuits

**CEC Ref:**  | **NEC Ref:** 210.11(C)(1)

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### baseline-008: knowledge_simple

**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?

**Expected:** Yes, all services supplying dwelling units shall be provided with a surge-protective device (SPD).

**CEC Ref:**  | **NEC Ref:** 230.67

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---


## Core

### core-001: multi_article

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Expected:** 2/0 AWG copper OR 4/0 AWG aluminum. Yes, aluminum is permitted for service conductors per Table 310.12.

**CEC Ref:**  | **NEC Ref:** Table 310.12, 310.12

**Status:** FAIL

**Agent Answer:**


**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_search, cec_search, cec_lookup_table, cec_lookup_table, cec_search, cec_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 0 found
- None

**Response Time:** 160.1s

---

### core-002: multi_article

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Expected:** Requires either a handle tie or common trip breaker to simultaneously disconnect all ungrounded conductors per 210.4(B). Common trip is required if the circuit has both line-to-line and line-to-neutral loads. Neutral must be continuous and not switched. Conductors must be grouped per 210.4(D). Circu...

**CEC Ref:**  | **NEC Ref:** 210.4, 210.4(B), 210.4(D)

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### core-003: nec_2023_updates

**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Expected:** Bathrooms, garages, outdoors, crawl spaces, unfinished basements, kitchens (countertop receptacles and dishwasher), laundry areas, utility rooms with sinks, boathouses, areas with bathtubs or shower stalls, and within 6 feet of sinks.

**CEC Ref:**  | **NEC Ref:** 210.8(A)

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### core-004: nec_2023_updates

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Expected:** Yes, per 230.67. Type 1 or Type 2 SPD required. Must be installed integral to the service equipment or immediately adjacent. Exception allows installation at the first downstream panelboard.

**CEC Ref:**  | **NEC Ref:** 230.67

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### core-005: edge_cases

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Expected:** No, this violates multiple requirements: (1) Minimum 36 inches depth required per 110.26(A)(1), not 24 inches. (2) Panels are prohibited in clothes closets per 240.24(D). (3) Working space width must be 30 inches or equipment width, whichever is greater. (4) No storage allowed in working space per 1...

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1), 240.24(D), 110.26(B)

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### core-006: edge_cases

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Expected:** Yes, this is a code violation per 110.14(A). Terminals shall accommodate only one conductor unless identified for more than one conductor. Per 110.3(B), equipment must be installed according to manufacturer instructions. If the breaker is not listed for two conductors, this is a violation.

**CEC Ref:**  | **NEC Ref:** 110.14(A), 110.3(B)

**Status:** FAIL

**Agent Answer:**
Error: Error calling model 'gemini-2.5-pro' (RESOURCE_EXHAUSTED): 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_requests_per_model_per_day, limit: 0', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_requests_per_model_per_day', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel'}]}]}}

**Tool Usage:**
- CEC Tools: cec_search, cec_search, cec_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 0 found
- None

**Response Time:** 665.0s

---

### core-007: grounding_bonding

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Expected:** Grounds and neutrals must be SEPARATED in the subpanel. The 4-wire feeder includes 2 hot, 1 neutral, and 1 equipment grounding conductor. NO main bonding jumper in subpanel (only at service). Neutral bar must be isolated (not bonded to enclosure). Equipment grounding conductor must be bonded to encl...

**CEC Ref:**  | **NEC Ref:** 250.32, 250.24(A)(5), 408.40

**Status:** FAIL

**Agent Answer:**
Error: Error calling model 'gemini-2.5-pro' (RESOURCE_EXHAUSTED): 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_requests_per_model_per_day, limit: 0', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_requests_per_model_per_day', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel'}]}]}}

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 626.3s

---

### core-008: grounding_bonding

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Expected:** Main Bonding Jumper (MBJ): Located at SERVICE EQUIPMENT, connects grounded conductor (neutral) to equipment grounding conductor. Required at service disconnect per 250.28. System Bonding Jumper (SBJ): Located at SEPARATELY DERIVED SYSTEMS (transformers, generators), same function as MBJ but for SDS....

**CEC Ref:**  | **NEC Ref:** Article 100, 250.28, 250.30

**Status:** FAIL

**Agent Answer:**
Error: Error calling model 'gemini-2.5-pro' (RESOURCE_EXHAUSTED): 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_requests_per_model_per_day, limit: 0', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_requests_per_model_per_day', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel'}]}]}}

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 623.4s

---

### core-009: load_calculations

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Expected:** Minimum of TWO 20-ampere circuits required per 210.11(C)(1). Yes, these circuits can and should serve dining room, pantry, and breakfast room receptacles. They cannot serve lighting outlets or receptacles outside these areas.

**CEC Ref:**  | **NEC Ref:** 210.11(C)(1), 210.52(B)

**Status:** FAIL

**Agent Answer:**
Error: Error calling model 'gemini-2.5-pro' (RESOURCE_EXHAUSTED): 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_requests_per_model_per_day, limit: 0', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_requests_per_model_per_day', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel'}]}]}}

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 947.4s

---

### core-010: load_calculations

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Expected:** Base ampacity: 30A at 90°C (Table 310.16). Temperature correction factor: 0.82 for 50°C (Table 310.15(B)(1)). Bundling adjustment: 0.80 for 6 conductors (Table 310.15(C)(1)). Adjusted ampacity = 30A × 0.82 × 0.80 = 19.68A, approximately 20A.

**CEC Ref:**  | **NEC Ref:** Table 310.16, Table 310.15(B)(1), Table 310.15(C)(1)

**Status:** FAIL

**Agent Answer:**
Error: Error calling model 'gemini-2.5-pro' (RESOURCE_EXHAUSTED): 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_requests_per_model_per_day, limit: 0', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_requests_per_model_per_day', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel'}]}]}}

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 622.0s

---

### core-011: why_questions

**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?

**Expected:** AFCI protection prevents electrical fires caused by arc faults. It detects arcing conditions that standard breakers cannot, including series arcing (broken/damaged wires), parallel arcing (line-to-line or line-to-ground), loose connections, damaged insulation, and deteriorated wire. Required per 210...

**CEC Ref:**  | **NEC Ref:** 210.12

**Status:** FAIL

**Agent Answer:**
Error: Error calling model 'gemini-2.5-pro' (RESOURCE_EXHAUSTED): 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_requests_per_model_per_day, limit: 0', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_requests_per_model_per_day', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel'}]}]}}

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 623.3s

---

### core-012: why_questions

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Expected:** Torque specifications prevent: (1) loose connections causing high resistance and heat generation (fire hazard), (2) poor contact leading to arcing, (3) overtightening causing crushed conductors or damaged terminals. Requirements found in 110.14(D) - must follow manufacturer specifications or Table 1...

**CEC Ref:**  | **NEC Ref:** 110.14(D), 110.3(B)

**Status:** FAIL

**Agent Answer:**
Error: Error calling model 'gemini-2.5-pro' (RESOURCE_EXHAUSTED): 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_requests_per_model_per_day, limit: 0', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_requests_per_model_per_day', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel'}]}]}}

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 622.1s

---


## Inspection

### inspection-001: panel_load_calculation

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Expected:** General lighting: 3000 sq ft × 3 VA = 9000 VA. Small appliance: 2 circuits × 1500 VA = 3000 VA. Laundry: 1500 VA. Subtotal: 13,500 VA. Apply demand factor per Table 220.42: first 3000 VA at 100% = 3000 VA, remaining 10,500 VA at 35% = 3675 VA. Subtotal with demand: 6675 VA. Range: 8000 VA (per Table...

**CEC Ref:**  | **NEC Ref:** 220.40, 220.42, Table 220.42, Table 220.55

**Status:** FAIL

**Agent Answer:**
Error: Error calling model 'gemini-2.5-pro' (RESOURCE_EXHAUSTED): 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_requests_per_model_per_day, limit: 0', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_requests_per_model_per_day', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel'}]}]}}

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 623.1s

---

### inspection-002: clearance_violations

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Expected:** Violations: (1) Depth clearance is 28 inches but 110.26(A)(1) requires minimum 36 inches for 120/240V equipment - VIOLATION. (2) Water heater at 16 inches is within the 30-inch width working space - equipment not related to electrical installation is prohibited in working space per 110.26(B) - VIOLA...

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1), 110.26(B), 110.26(A)(3)

**Status:** FAIL

**Agent Answer:**
Error: Error calling model 'gemini-2.5-pro' (RESOURCE_EXHAUSTED): 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_requests_per_model_per_day, limit: 0', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_requests_per_model_per_day', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel'}]}]}}

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 623.4s

---

### inspection-005: gfci_afci_compliance

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Expected:** Per 2023 NEC: (1) Countertop receptacles (2 circuits): GFCI required per 210.8(A)(6), AFCI required per 210.12(A). Use combination AFCI/GFCI breakers. (2) Dishwasher: GFCI required per 210.8(D), AFCI required per 210.12(A). Use combination AFCI/GFCI breaker. (3) Disposal: GFCI not specifically requi...

**CEC Ref:**  | **NEC Ref:** 210.8(A), 210.8(D), 210.12(A)

**Status:** FAIL

**Agent Answer:**
Error: Error calling model 'gemini-2.5-pro' (RESOURCE_EXHAUSTED): 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_requests_per_model_per_day, limit: 0', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_requests_per_model_per_day', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel'}]}]}}

**Tool Usage:**
- CEC Tools: None
- NEC Tools: nec_search
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 641.1s

---

### inspection-006: subpanel_violations

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Expected:** VIOLATIONS: (1) Neutral bar bonded to enclosure - VIOLATION per 250.24(A)(5) and 408.40. In subpanels, neutral must be isolated from enclosure. (2) Main bonding jumper installed - VIOLATION. MBJ only permitted at service equipment per 250.28, not in subpanels. CORRECT configuration: Remove bond betw...

**CEC Ref:**  | **NEC Ref:** 250.24(A)(5), 250.28, 408.40, 250.32(B)

**Status:** FAIL

**Agent Answer:**
Error: Error calling model 'gemini-2.5-pro' (RESOURCE_EXHAUSTED): 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_requests_per_model_per_day, limit: 0', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_requests_per_model_per_day', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel'}]}]}}

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 623.2s

---

### inspection-007: conduit_fill

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Expected:** Per Chapter 9 Table 1: Maximum 40% fill for more than two conductors. From Chapter 9 Table 4: Trade size 1¼" RMC has 40% fill area of 0.610 square inches. From Chapter 9 Table 5: 10 AWG THHN conductor area is 0.0211 square inches. Calculation: 0.610 in² ÷ 0.0211 in² per conductor = 28.91 conductors....

**CEC Ref:**  | **NEC Ref:** Chapter 9 Table 1, Chapter 9 Table 4, Chapter 9 Table 5, Chapter 9 Note 7

**Status:** FAIL

**Agent Answer:**
Error: Error calling model 'gemini-2.5-pro' (RESOURCE_EXHAUSTED): 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_requests_per_model_per_day, limit: 0', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_requests_per_model_per_day', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel'}]}]}}

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 625.6s

---

### inspection-008: voltage_drop

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?

**Expected:** Voltage drop formula: VD = (2 × L × R × I) / 1000. Where: L = 50 feet (one-way distance), R = 1.29 ohms/1000ft for 12 AWG copper (Chapter 9 Table 8), I = 22 amperes, multiply by 2 for round trip. Calculation: VD = (2 × 50 × 1.29 × 22) / 1000 = 2,838 / 1000 = 2.84 volts. Percentage: (2.84V / 120V) × ...

**CEC Ref:**  | **NEC Ref:** 210.19(A)(1) Informational Note No. 4, Chapter 9 Table 8

**Status:** FAIL

**Agent Answer:**
Error: Error calling model 'gemini-2.5-pro' (RESOURCE_EXHAUSTED): 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_requests_per_model_per_day, limit: 0', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_requests_per_model_per_day', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel'}]}]}}

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 623.5s

---

### inspection-009: derating_calculation

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Expected:** Step 1: Base ampacity of 12 AWG TW copper at 60°C = 20 amperes (Table 310.16). Step 2: Temperature correction for 43°C ambient with 60°C conductor from Table 310.15(B)(1)(1): Correction factor = 0.71 (for 41-45°C range in 60°C column). Step 3: Bundling adjustment for 6 conductors from Table 310.15(C...

**CEC Ref:**  | **NEC Ref:** Table 310.16, Table 310.15(B)(1), Table 310.15(C)(1), 310.15(B), 310.15(C)

**Status:** FAIL

**Agent Answer:**
Error: Error calling model 'gemini-2.5-pro' (RESOURCE_EXHAUSTED): 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_requests_per_model_per_day, limit: 0', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_requests_per_model_per_day', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel'}]}]}}

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 624.7s

---

### inspection-010: grounding_electrode_conductor

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Expected:** Per Table 250.66: For service entrance conductors 1000 kcmil copper (4 × 250 kcmil in parallel), locate the row for 'Over 600 kcmil through 1100 kcmil'. The minimum grounding electrode conductor size is 2/0 AWG copper or 4/0 AWG aluminum. Answer: Minimum 2/0 AWG copper GEC required. Note: If this GE...

**CEC Ref:**  | **NEC Ref:** Table 250.66, 250.66(A)

**Status:** FAIL

**Agent Answer:**
Error: Error calling model 'gemini-2.5-pro' (RESOURCE_EXHAUSTED): 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_requests_per_model_per_day, limit: 0', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_requests_per_model_per_day', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel'}]}]}}

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 622.1s

---


## Analysis

### Key Metrics

- **CEC-Primary Responses**: 2/28
- **Success Rate**: 0.0%
- **Average Response Time**: 370.2s

### Model Information

- **Provider**: Groq
- **Model**: gemini-2.5-pro
- **Framework**: LangChain + LangGraph

