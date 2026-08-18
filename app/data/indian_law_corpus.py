"""
indian_law_corpus.py
Curated Indian Statutory Provisions and Landmark Legal Doctrines for ChromaDB Knowledge Base.
"""

INDIAN_LAW_STATUTES = [
    # ─── 1. Indian Contract Act, 1872 ───
    {
        "act": "The Indian Contract Act, 1872",
        "section": "Section 10 & 23 - Valid Contracts & Lawful Consideration",
        "title": "Essential Elements of Valid Agreement & Lawful Object",
        "text": """THE INDIAN CONTRACT ACT, 1872 — SECTION 10 & 23
Section 10: All agreements are contracts if they are made by the free consent of parties competent to contract, for a lawful consideration and with a lawful object, and are not hereby expressly declared to be void.
Section 23: The consideration or object of an agreement is lawful, unless it is forbidden by law; or is of such a nature that, if permitted, it would defeat the provisions of any law; or is fraudulent; or involves or implies injury to the person or property of another; or the Court regards it as immoral, or opposed to public policy. Every agreement of which the object or consideration is unlawful is void."""
    },
    {
        "act": "The Indian Contract Act, 1872",
        "section": "Section 27 - Restraint of Trade & Non-Compete Covenants",
        "title": "Agreement in Restraint of Trade Void (Non-Compete Enforceability)",
        "text": """THE INDIAN CONTRACT ACT, 1872 — SECTION 27: AGREEMENT IN RESTRAINT OF TRADE VOID
Every agreement by which any one is restrained from exercising a lawful profession, trade or business of any kind, is to that extent void.
Exception 1: One who sells the goodwill of a business may agree with the buyer to refrain from carrying on a similar business, within specified local limits, so long as the buyer carries on a like business therein, provided that such limits appear to the Court reasonable.
JUDICIAL DOCTRINE & PRECEDENTS:
1. Niranjan Shankar Golikari v. Century Spg. & Mfg. Co. Ltd. (AIR 1967 SC 1098): Restraints operative during the period of employment are valid and enforceable. However, any negative covenant operative post-termination of employment is void under Section 27.
2. Percept D'Mark (India) (P) Ltd. v. Zaheer Khan (AIR 2006 SC 3426): The Supreme Court ruled that Section 27 is absolute. The doctrine of reasonableness does not apply to post-employment non-competes in India.
3. Permissible Protective Clauses: Non-Solicitation of clients and employees (12 to 24 months), Non-Disclosure of Trade Secrets, and IP Assignment Agreements remain fully enforceable."""
    },
    {
        "act": "The Indian Contract Act, 1872",
        "section": "Section 73 & 74 - Damages & Liquidated Penalties",
        "title": "Breach of Contract, Liquidated Damages vs. Penalties",
        "text": """THE INDIAN CONTRACT ACT, 1872 — SECTION 73 & 74: DAMAGES FOR BREACH
Section 73: When a contract has been broken, the party who suffers by such breach is entitled to receive, from the party who has broken the contract, compensation for any loss or damage caused to him thereby, which naturally arose in the usual course of things.
Section 74: Compensation for breach of contract where penalty stipulated for: When a contract has been broken, if a sum is named in the contract as the amount to be paid in case of such breach (liquidated damages), or if the contract contains any other stipulation by way of penalty, the party complaining of the breach is entitled to receive reasonable compensation not exceeding the amount so named.
JUDICIAL PRECEDENT (Kailash Nath Associates v. DDA, 2015 4 SCC 136):
Liquidated damages named under Section 74 are not awarded automatically. The claimant must prove actual loss or damage suffered, unless proving actual loss is impossible or difficult to prove, in which case the genuine pre-estimated sum may be awarded as reasonable compensation."""
    },

    # ─── 2. MSMED Act, 2006 ───
    {
        "act": "Micro, Small and Medium Enterprises Development Act, 2006",
        "section": "Sections 15, 16 & 17 - Mandatory 45-Day Payment & Penal Interest",
        "title": "Statutory Payment Deadlines & Compound Interest for MSME Suppliers",
        "text": """MICRO, SMALL AND MEDIUM ENTERPRISES DEVELOPMENT (MSMED) ACT, 2006
Section 15: Liability of buyer to make payment: Where any supplier supplies any goods or renders any services to any buyer, the buyer shall make payment therefor on or before the date agreed upon between him and the supplier in writing, or, where there is no agreement, before the appointed day. Provided that in no case the period agreed upon between the supplier and the buyer in writing shall exceed forty-five (45) days from the day of acceptance or deemed acceptance.
Section 16: Date from which and rate at which interest is payable: Where any buyer fails to make payment to the supplier, the buyer shall, notwithstanding anything contained in any agreement, be liable to pay compound interest with monthly rests to the supplier on that amount from the appointed day at three times (3x) of the bank rate notified by the Reserve Bank of India (RBI).
Section 18: Reference to Micro and Small Enterprises Facilitation Council (MSEFC) for recovery and statutory arbitration."""
    },

    # ─── 3. Arbitration and Conciliation Act, 1996 ───
    {
        "act": "The Arbitration and Conciliation Act, 1996",
        "section": "Sections 7, 11 & 20 - Arbitration Agreement, Seat vs. Venue",
        "title": "Arbitration Clause Drafting, Seat Determination & Court Jurisdiction",
        "text": """THE ARBITRATION AND CONCILIATION ACT, 1996 (AMENDED 2015, 2019, 2021)
Section 7: Arbitration agreement must be in writing (contained in a document signed by parties, exchange of letters, telex, telegrams, or electronic communications).
Section 20: Place of Arbitration (Seat vs. Venue):
1. The parties are free to agree on the place of arbitration.
2. Landmark Precedent (Bharat Aluminium Co. [BALCO] v. Kaiser Aluminium, 2012 9 SCC 552): The designation of a 'Seat' of arbitration grants exclusive supervisory jurisdiction to the Courts exercising territorial jurisdiction over that Seat (e.g. High Court of Bombay for Mumbai, High Court of Delhi for New Delhi, High Court of Karnataka for Bengaluru).
3. Venue is merely the geographical convenience for hearings, whereas Seat confers supervisory legal jurisdiction."""
    },

    # ─── 4. Indian Stamp Act, 1899 & Registration Act, 1908 ───
    {
        "act": "The Indian Stamp Act, 1899 & Registration Act, 1908",
        "section": "Section 35 Indian Stamp Act & Section 17 Registration Act",
        "title": "Stamp Duty, e-Stamping & Compulsory Registration Requirements",
        "text": """THE INDIAN STAMP ACT, 1899 & STATE STAMP ACTS (e.g., Maharashtra Stamp Act, Karnataka Stamp Act, Delhi Stamp Rules)
Section 35 (Indian Stamp Act): Instruments not duly stamped are inadmissible in evidence in any Indian court or before any arbitrator, unless properly impounded and statutory deficit duty plus 10x penalty is paid.
Leave and License vs Lease:
- Agreements for lease exceeding eleven (11) months are compulsorily registrable under Section 17 of the Registration Act, 1908.
- 11-Month Leave & License Agreements under the Indian Easements Act, 1882 avoid tenant tenancy rights and require state-specific stamp duty and online e-registration (e.g. in Maharashtra under Section 55 of Maharashtra Rent Control Act).
- Electronic Stamp Papers (e-Stamping via Stock Holding Corporation of India Ltd. - SHCIL) are recognized for commercial contracts."""
    },

    # ─── 5. Digital Personal Data Protection Act, 2023 ───
    {
        "act": "Digital Personal Data Protection Act, 2023 (DPDP Act)",
        "section": "Sections 4, 8 & 33 - Data Fiduciary Obligations & Penalties",
        "title": "Data Protection Compliance & Vendor Data Processing Contracts",
        "text": """DIGITAL PERSONAL DATA PROTECTION (DPDP) ACT, 2023
Section 4: Lawful Processing: Personal data may only be processed for lawful purposes with clear, unconditional consent from the Data Principal or for specified legitimate uses.
Section 8: General Obligations of Data Fiduciary:
1. Ensure data accuracy, implement reasonable technical and organizational security safeguards to prevent data breach.
2. A Data Fiduciary may only engage, appoint, or use a Data Processor to process personal data under a valid contract.
3. Notify the Data Protection Board of India and affected Data Principals in the event of any personal data breach.
Section 33: Schedule of Penalties: Fines up to INR 250 Crores (₹2,500,000,000) for failure to implement reasonable security safeguards or report data breaches."""
    },

    # ─── 6. Specific Relief Act, 1963 & Income Tax (TDS) / GST ───
    {
        "act": "Specific Relief Act, 1963 & Tax Statutes (Income Tax Act, 1961)",
        "section": "Section 10 & 20 Specific Relief Act, TDS Sec 194C/194J, GST",
        "title": "Specific Performance of Contracts, Injunctions, and Tax Deductions (TDS/GST)",
        "text": """SPECIFIC RELIEF (AMENDMENT) ACT, 2018 & INDIAN TAX STATUTES
Specific Performance (Section 10 Specific Relief Act): Specific performance of a contract is mandatory by the court, subject to limited exceptions under Section 11(2), 14, and 16. Substituted performance is available under Section 20.
Tax Deductions at Source (TDS) under Income Tax Act, 1961:
- Section 194C: TDS on payments to contractors/subcontractors (1% for individual/HUF, 2% for companies).
- Section 194J: TDS on fees for professional or technical services (2% for technical services / call centers, 10% for professional services).
- GST: Goods and Services Tax applicable at standard rate (18% for most software/B2B services) with reverse charge mechanism (RCM) where applicable."""
    }
]
