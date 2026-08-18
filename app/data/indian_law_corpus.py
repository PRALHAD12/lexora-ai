"""
indian_law_corpus.py
Comprehensive, Latest Indian Legal Corpus & Supreme Court Precedents (2024–2026 Edition).

Contains:
1. Central Statutory Acts (Indian Contract Act 1872, Arbitration Act 1996, MSMED Act 2006, Stamp Act, DPDP 2023, Companies Act 2013, Specific Relief Act 1963).
2. Landmark Supreme Court of India Constitution Bench Precedents (NN Global 7-Judge Bench 2023, Cox & Kings 2023, Zaheer Khan, BALCO, Kailash Nath, Energy Watchdog).
3. Standard Indian Commercial Contract Archetypes & Clause Banks (Leave & License, MSA, Indian NDA, Founders' Agreement, Employment, Vendor Agreement).
4. Indian Tax (TDS 194C/J/I/Q & GST 18%) and Stamp Duty Schedules.
"""

INDIAN_LAW_STATUTES = [
    # ══════════════════════════════════════════════════════════════════════════
    # 1. THE INDIAN CONTRACT ACT, 1872
    # ══════════════════════════════════════════════════════════════════════════
    {
        "act": "The Indian Contract Act, 1872",
        "section": "Section 10 & 23 - Valid Contracts, Free Consent & Lawful Consideration",
        "title": "Essential Elements of Valid Indian Contract & Public Policy Bar",
        "category": "Contract Formation",
        "text": """THE INDIAN CONTRACT ACT, 1872 — SECTION 10 & 23: ESSENTIALS OF VALID CONTRACT
Section 10: All agreements are contracts if they are made by the free consent of parties competent to contract, for a lawful consideration and with a lawful object, and are not hereby expressly declared to be void.
Section 23: The consideration or object of an agreement is lawful, unless it is forbidden by law; or is of such a nature that, if permitted, it would defeat the provisions of any law; or is fraudulent; or involves or implies injury to the person or property of another; or the Court regards it as immoral, or opposed to public policy. Every agreement of which the object or consideration is unlawful is void ab initio."""
    },
    {
        "act": "The Indian Contract Act, 1872",
        "section": "Section 27 - Restraint of Trade & Non-Compete Covenants",
        "title": "Agreement in Restraint of Trade Void (Non-Compete Enforceability)",
        "category": "Employment & Restrictive Covenants",
        "text": """THE INDIAN CONTRACT ACT, 1872 — SECTION 27: AGREEMENT IN RESTRAINT OF TRADE VOID
Every agreement by which any one is restrained from exercising a lawful profession, trade or business of any kind, is to that extent void.
Statutory Exception 1: One who sells the goodwill of a business may agree with the buyer to refrain from carrying on a similar business within specified reasonable local limits.

LANDMARK SUPREME COURT PRECEDENTS & JUDICIAL DOCTRINE:
1. Percept D'Mark (India) (P) Ltd. v. Zaheer Khan (AIR 2006 SC 3426): The Supreme Court established that Section 27 is absolute. The doctrine of reasonableness or partial restraint does NOT apply to post-employment non-compete clauses in India. Any post-termination non-compete covenant is strictly void and unenforceable.
2. Niranjan Shankar Golikari v. Century Spg. & Mfg. Co. Ltd. (AIR 1967 SC 1098): Restrictive covenants operative DURING the period of employment are valid and enforceable.
3. Permissible & Enforceable Alternatives in India:
   - Non-Solicitation of Clients & Employees (Enforceable for 12 to 24 months).
   - Protection of Confidential Information & Trade Secrets under Common Law & Specific Relief Act.
   - Assignment of Intellectual Property (Inventions & Work Made for Hire)."""
    },
    {
        "act": "The Indian Contract Act, 1872",
        "section": "Section 28 - Restraint of Legal Proceedings & Limitation Clauses",
        "title": "Agreements in Restraint of Legal Proceedings & Curtailment of Limitation",
        "category": "Dispute Resolution",
        "text": """THE INDIAN CONTRACT ACT, 1872 — SECTION 28: RESTRAINT OF LEGAL PROCEEDINGS
Every agreement by which any party thereto is restricted absolutely from enforcing his rights under or in respect of any contract, by the usual legal proceedings in the ordinary tribunals, or which limits the time within which he may thus enforce his rights, is void to that extent.
Key Rule: Clauses extinguishing rights or shortening the statutory limitation period (e.g. 3 years under Limitation Act, 1963) to less than 3 years are void.
Statutory Exceptions: Valid arbitration agreements under Section 28 Exception 1 and Exception 2."""
    },
    {
        "act": "The Indian Contract Act, 1872",
        "section": "Section 55 & 56 - Time as Essence, Frustration & Force Majeure",
        "title": "Effect of Failure to Perform within Time & Doctrine of Frustration",
        "category": "Performance & Termination",
        "text": """THE INDIAN CONTRACT ACT, 1872 — SECTION 55 & 56
Section 55: When a party promises to do a certain thing at or before a specified time, and the intention of the parties was that time should be of the essence of the contract, failure to perform renders the contract voidable at the option of the promisee.
Section 56: An agreement to do an act impossible in itself is void. A contract becomes void when the act becomes impossible or unlawful by reason of some event which the promisor could not prevent (Doctrine of Frustration).
LANDMARK PRECEDENT (Energy Watchdog v. CERC, 2017 14 SCC 80):
The Supreme Court held that where a Force Majeure clause is expressed in the contract, it is governed by Section 32 (contingent contract), not Section 56. Economic unviability, inflation, or change in market conditions does NOT frustrate a commercial contract."""
    },
    {
        "act": "The Indian Contract Act, 1872",
        "section": "Section 73 & 74 - Breach of Contract, Liquidated Damages vs. Penalty",
        "title": "Compensation for Loss or Damage & Proof of Actual Loss Required",
        "category": "Damages & Liability",
        "text": """THE INDIAN CONTRACT ACT, 1872 — SECTION 73 & 74: DAMAGES FOR BREACH
Section 73: Compensation for loss or damage caused by breach of contract which naturally arose in the usual course of things. Remote and indirect losses are not recoverable.
Section 74: Where a sum is named in the contract as the amount to be paid in case of breach (liquidated damages), or if the contract contains any other stipulation by way of penalty, the party complaining of the breach is entitled to receive reasonable compensation not exceeding the amount so named.

LANDMARK PRECEDENTS (Kailash Nath Associates v. DDA, 2015 4 SCC 136 & ONGC v. Saw Pipes Ltd, 2003 5 SCC 705):
1. Liquidated damages named under Section 74 are NOT awarded automatically.
2. The aggrieved party must prove actual loss or damage suffered, unless proving actual loss is impossible or difficult to assess, in which case the genuine pre-estimated sum may be awarded as reasonable compensation.
3. Forfeiture of earnest money or security deposits must be reasonable and cannot operate as an unconscionable penalty."""
    },
    {
        "act": "The Indian Contract Act, 1872",
        "section": "Section 124 & 125 - Contract of Indemnity & Rights of Indemnity Holder",
        "title": "Indemnity Clauses, Defense Obligations & Third-Party Claims",
        "category": "Liability & Indemnification",
        "text": """THE INDIAN CONTRACT ACT, 1872 — SECTION 124 & 125: CONTRACT OF INDEMNITY
Section 124: A contract by which one party promises to save the other from loss caused to him by the conduct of the promisor himself, or by the conduct of any other person, is called a contract of indemnity.
Section 125: The promisee in a contract of indemnity, acting within the scope of his authority, is entitled to recover from the promisor all damages, costs, and sums paid under compromise.
Indian Drafting Best Practice: Ensure indemnities clearly define whether defense costs (attorney fees) are paid on an as-incurred basis and whether liability is capped at contract value (12 months aggregate fees)."""
    },

    # ══════════════════════════════════════════════════════════════════════════
    # 2. THE ARBITRATION AND CONCILIATION ACT, 1996 & CONSTITUTION BENCH RULINGS
    # ══════════════════════════════════════════════════════════════════════════
    {
        "act": "The Arbitration and Conciliation Act, 1996",
        "section": "Section 7, 11 & 20 - Arbitration Agreement, Seat vs. Venue",
        "title": "Arbitration Agreement, Appointment of Arbitrator, Seat vs. Venue Jurisdiction",
        "category": "Dispute Resolution",
        "text": """THE ARBITRATION AND CONCILIATION ACT, 1996 (AMENDED 2015, 2019, 2021)
Section 7: Arbitration agreement must be in writing (contained in document signed by parties or electronic exchanges).
Section 11: Appointment of Arbitrators by High Court (Domestic) or Supreme Court of India (International Commercial Arbitration).
Section 20: Place of Arbitration (Seat vs. Venue):
- Landmark Precedent: Bharat Aluminium Co. (BALCO) v. Kaiser Aluminium (2012 9 SCC 552) & BGS SGS Soma JV (2020 4 SCC 234).
- Designation of a 'Seat' of arbitration confers exclusive supervisory jurisdiction upon the High Court having territorial jurisdiction over that Seat (e.g. Bombay High Court for Mumbai Seat, Delhi High Court for New Delhi Seat, Karnataka High Court for Bengaluru Seat). Venue is merely physical hearing convenience."""
    },
    {
        "act": "The Arbitration and Conciliation Act, 1996",
        "section": "NN Global 7-Judge Bench (2023) - Stamping of Arbitration Agreements",
        "title": "Supreme Court 7-Judge Constitution Bench on Unstamped Arbitration Clauses",
        "category": "Arbitration Precedent",
        "text": """SUPREME COURT 7-JUDGE CONSTITUTION BENCH RULING:
In Re: Interplay between Arbitration Agreements under the Arbitration Act, 1996 and Indian Stamp Act, 1899 (Curative Petition / NN Global Review, 2023 INSC 1066 / 2024 6 SCC 1):
1. The 7-Judge Bench unanimously held that an unstamped or insufficiently stamped underlying commercial contract DOES NOT render the arbitration clause void or unenforceable at the Section 11 referral stage.
2. The defect of non-stamping or insufficient stamping is a CURABLE defect.
3. The arbitral tribunal has the competence to impound the document and direct payment of deficit stamp duty and penalty under Section 33 and 35 of the Indian Stamp Act.
4. Courts will not stall the appointment of arbitrators under Section 11 merely because of stamp duty deficit."""
    },
    {
        "act": "The Arbitration and Conciliation Act, 1996",
        "section": "Cox & Kings 5-Judge Bench (2023) - Group of Companies Doctrine",
        "title": "Binding Non-Signatory Group Companies to Arbitration in India",
        "category": "Arbitration Precedent",
        "text": """SUPREME COURT 5-JUDGE CONSTITUTION BENCH RULING:
Cox and Kings Ltd. v. SAP India Pvt. Ltd. (2023 INSC 1051 / 2024 4 SCC 1):
1. The 5-Judge Constitution Bench upheld the validity of the 'Group of Companies Doctrine' under Indian Arbitration Law.
2. A non-signatory entity within a corporate group can be bound by an arbitration agreement if there is a mutual intention of all parties, determined through:
   - Direct involvement in negotiation, performance, or termination of the contract.
   - Economic reality of the transaction and composite commercial operation.
3. Indian courts must assess mutual commercial intent rather than treating corporate personality as an absolute shield."""
    },

    # ══════════════════════════════════════════════════════════════════════════
    # 3. THE MSMED ACT, 2006 (MSME COMPLIANCE & 45-DAY PAYMENT RULES)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "act": "Micro, Small and Medium Enterprises Development Act, 2006",
        "section": "Sections 15, 16, 17 & 18 - Mandatory 45-Day Payment Deadline & 3x RBI Interest",
        "title": "Statutory Payment Window, Compound Interest & MSEFC Facilitation",
        "category": "Vendor & Supply Chain Compliance",
        "text": """MICRO, SMALL AND MEDIUM ENTERPRISES DEVELOPMENT (MSMED) ACT, 2006
Section 15: Liability of Buyer to Make Payment:
- Where any supplier (registered under Udyam / MSME) delivers goods or renders services, the buyer MUST make payment on or before the agreed date in writing.
- STATUTORY CAP: In no case shall the agreed credit period exceed FORTY-FIVE (45) DAYS from the date of delivery or deemed acceptance. Any contract clause specifying > 45 days is void to that extent.
Section 16: Compound Interest for Delayed Payment:
- If buyer fails to pay within 45 days, buyer is STATUTORILY LIABLE to pay compound interest with monthly rests at THREE TIMES (3x) the Bank Rate notified by the Reserve Bank of India (RBI).
Section 18 & 19: Dispute Reference to MSEFC:
- MSME supplier may approach Micro and Small Enterprises Facilitation Council (MSEFC) for statutory conciliation and arbitration. Pre-deposit of 75% of award amount is mandatory for buyer to appeal."""
    },

    # ══════════════════════════════════════════════════════════════════════════
    # 4. INDIAN STAMP ACT, 1899 & STATE STAMP ACTS (e-STAMPING & REGISTRATION)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "act": "The Indian Stamp Act, 1899 & State Stamp Acts",
        "section": "Section 35 Stamp Act & Section 17 Registration Act, 1908",
        "title": "Stamp Duty Inadmissibility, Impounding & 11-Month Leave and License",
        "category": "Stamping & Registration",
        "text": """INDIAN STAMP ACT, 1899 & STATE STAMP ACTS (MH, DL, KA, TN, TS, UP)
Section 35 (Indian Stamp Act): Instruments not duly stamped are inadmissible in evidence in Indian courts and before arbitrators. Stamping defect requires impounding under Section 33 and payment of deficit duty plus up to 10x penalty.
Registration Requirements under Registration Act, 1908:
- Section 17(1)(d): Leases of immovable property from year to year, or for any term exceeding one year (exceeding 11 months), or reserving a yearly rent, are COMPULSORILY REGISTRABLE.
- 11-Month Leave & License Agreements: Under Section 52 of Indian Easements Act, 1882, executed for 11 months to prevent creation of tenancy rights.
- In Maharashtra: Section 55 of Maharashtra Rent Control Act, 1999 mandates that Leave & License agreements must be in writing and registered online (e-Registration) with stamp duty calculated under Article 36A of Maharashtra Stamp Act (0.25% of total rent + non-refundable deposit).
- Electronic Contracts (IT Act, 2000): e-Sign via Aadhaar / digital signatures (DSC) and e-Stamping via Stock Holding Corporation of India Ltd (SHCIL) are fully legally recognized."""
    },

    # ══════════════════════════════════════════════════════════════════════════
    # 5. DIGITAL PERSONAL DATA PROTECTION ACT, 2023 (DPDP ACT)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "act": "Digital Personal Data Protection Act, 2023 (DPDP Act)",
        "section": "Sections 4, 8 & 33 - Data Fiduciary Duties & ₹250 Cr Penalties",
        "title": "DPDP Compliance, Data Processor Vendor Contracts & Breach Notification",
        "category": "Data Privacy & Tech Compliance",
        "text": """DIGITAL PERSONAL DATA PROTECTION (DPDP) ACT, 2023
Section 4: Lawful Processing: Personal data can only be processed on grounds of clear, unconditional consent from the Data Principal or for specified legitimate uses (employment, compliance with law).
Section 8: Obligations of Data Fiduciary:
1. Implement reasonable technical, operational, and organizational security safeguards to prevent data breach.
2. A Data Fiduciary may only engage a Data Processor under a valid written contract containing data protection safeguards.
3. Intimate the Data Protection Board of India (DPBI) and affected Data Principals in the event of any data breach.
Section 33: Schedule of Penalties: Statutory fines up to INR 250 Crores (₹2,500,000,000) for failure to implement reasonable security safeguards or failure to notify breach."""
    },

    # ══════════════════════════════════════════════════════════════════════════
    # 6. INDIAN TAX WITHHOLDING (TDS) & GOODS AND SERVICES TAX (GST)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "act": "Income Tax Act, 1961 & Central GST Act, 2017",
        "section": "TDS Sections 194C, 194J, 194I, 194Q & GST 18% Standard Rate",
        "title": "Statutory Tax Deductions at Source (TDS), GST Invoicing & ITC Indemnity",
        "category": "Tax & Financial Compliance",
        "text": """INDIAN STATUTORY TAX WITHHOLDING (TDS) & GST COMPLIANCE
Tax Deductions at Source (TDS) under Income Tax Act, 1961:
- Section 194C (Contracts/Sub-contracts): 1% TDS on individuals/HUFs, 2% TDS on corporate contractors.
- Section 194J (Fees for Professional or Technical Services): 2% TDS on technical services / software / BPO; 10% TDS on professional services (legal, medical, architectural).
- Section 194I (Rent): 10% TDS on rent of land, building, or furniture; 2% TDS on plant & machinery.
- Section 194Q (Purchase of Goods): 0.1% TDS on purchase of goods exceeding ₹50 Lakhs.

Goods and Services Tax (GST):
- Standard rate of 18% GST applies to software development, SaaS, marketing, consulting, and commercial leases.
- GST Input Tax Credit (ITC) Indemnity: The service provider must upload invoices to GST portal (GSTR-1) so tax reflects in GSTR-2B; agreement must indemnify client against loss of ITC due to vendor default."""
    },

    # ══════════════════════════════════════════════════════════════════════════
    # 7. STANDARD INDIAN COMMERCIAL CONTRACT ARCHETYPES & CLAUSE BANKS
    # ══════════════════════════════════════════════════════════════════════════
    {
        "act": "Indian Standard Contract Template",
        "section": "Leave and License Agreement (11 Months)",
        "title": "Standard Indian Residential / Commercial Leave and License Agreement",
        "category": "Real Estate / Tenancy",
        "text": """STANDARD INDIAN LEAVE AND LICENSE AGREEMENT (11 MONTHS):
1. Nature: A purely permissive license under Section 52 of the Indian Easements Act, 1882. No tenancy or sub-tenancy rights created in favor of Licensee.
2. Term: Exactly eleven (11) months from Effective Date, avoiding compulsory registration requirements under Section 17 of Registration Act.
3. Consideration & Deposit: Monthly License Fee in INR ₹ payable on or before the 5th of each English calendar month. Interest-free refundable security deposit refundable simultaneously upon vacating premises.
4. Maintenance & Utilities: Licensee pays electricity and water charges as per meter. Licensor pays property taxes and society maintenance charges.
5. Lock-in & Notice Period: Initial 3 to 6 months lock-in period. Either party may terminate by providing 1 month prior written notice."""
    },
    {
        "act": "Indian Standard Contract Template",
        "section": "Master Services Agreement (MSA) & SOW",
        "title": "Standard Indian B2B Master Services Agreement & IP Assignment",
        "category": "Corporate & Tech",
        "text": """STANDARD INDIAN MASTER SERVICES AGREEMENT (MSA):
1. Scope & SOW: Services executed pursuant to individual Statements of Work (SOW) specifying deliverables, milestones, and acceptance criteria.
2. Invoicing & MSMED: Payment within 30 days of invoice receipt, strictly capped at 45 days in compliance with Section 15 of MSMED Act, 2006.
3. Intellectual Property Assignment: All deliverables, software, documentation, and inventions created by Vendor shall constitute 'Work Made for Hire' and are exclusively assigned to Client with worldwide rights under the Indian Copyright Act, 1957.
4. Limitation of Liability: Aggregate liability of either party arising out of breach capped at 100% of the total fees paid in the preceding 12 months, excluding breaches of Confidentiality, IP infringement, or gross negligence.
5. Dispute Resolution: Arbitration under the Arbitration and Conciliation Act, 1996 by a sole arbitrator with Seat and exclusive jurisdiction in Mumbai/Bengaluru/New Delhi."""
    },
    {
        "act": "Indian Standard Contract Template",
        "section": "Founders' Agreement & Reverse Vesting",
        "title": "Indian Startup Founders' Agreement, Equity Vesting & ROFR",
        "category": "Startup & Venture Capital",
        "text": """STANDARD INDIAN STARTUP FOUNDERS' AGREEMENT:
1. Shareholding & Capital Contribution: Initial equity split among co-founders with par value shares under the Companies Act, 2013.
2. Reverse Vesting Schedule: Co-founders' shares vest over a 4-year period with a 1-year cliff (25% vesting after 12 months, balance vesting monthly/quarterly).
3. Good Leaver vs. Bad Leaver: Unvested shares transferred back to the company pool at nominal face value upon departure.
4. Restrictive Covenants: During tenure and for 12–24 months post-departure: Non-solicitation of startup employees and non-solicitation of clients (Section 27 ICA compliant).
5. Transfer Restrictions: Right of First Refusal (ROFR) and Tag-Along rights for remaining co-founders before any third-party share transfers."""
    },
    {
        "act": "Indian Standard Contract Template",
        "section": "Indian Non-Disclosure Agreement (NDA)",
        "title": "Standard Indian Mutual / Unilateral Non-Disclosure Agreement",
        "category": "Confidentiality & Trade Secrets",
        "text": """STANDARD INDIAN NON-DISCLOSURE AGREEMENT (NDA):
1. Scope of Confidential Information: Technical, financial, customer, and proprietary information disclosed in written, oral, or electronic form.
2. Standard Exclusions: Information already publicly known, rightfully received from third parties without confidentiality breach, or required to be disclosed by Indian court order / regulatory authority.
3. Standard Duration: Confidentiality obligations survive for a period of three (3) years from the date of disclosure; trade secrets protected indefinitely.
4. Return & Destruction: Upon written request, Receiving Party must return or certify destruction of all copies within 14 days.
5. Remedies & Injunction: Injunctive relief under Specific Relief Act, 1963 and damages in Indian courts."""
    }
]
