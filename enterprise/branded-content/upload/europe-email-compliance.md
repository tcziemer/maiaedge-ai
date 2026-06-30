# Europe Email Compliance: ePrivacy + GDPR (cold outreach)

> **Not legal advice.** This is an operational summary for the MaiaEdge European outreach motion, written to keep us out of trouble, not to replace counsel. National rules change and vary, and the stakes (especially in Germany) are real. Before any new-country send program, confirm with qualified counsel or the company DPO. Facts verified June 2026 (sources at the foot).

---

## The 60-second version

Cold B2B email in Europe lives under **two layers at once**, and you must satisfy both:

1. **GDPR** governs the personal data (a named person's work email is personal data). The usable lawful basis for prospecting is **legitimate interest** (Art 6(1)(f)), which requires a documented balancing test (an LIA).
2. **ePrivacy** governs the act of sending a marketing message. There is no single EU rule: the **ePrivacy Regulation was withdrawn by the Commission in 2025** ("no foreseeable agreement"), so the **ePrivacy Directive, transposed differently in every country, still governs.** This is the layer that varies, and it can override legitimate interest.

The practical result is a country-by-country picture, not one EU rule:

- **Opt-out / legitimate-interest-friendly (cold B2B email workable with conditions):** UK (to corporate subscribers), France (to named professionals), Netherlands. Verified.
- **Strict prior-consent (cold advertising email generally unlawful without opt-in):** **Germany, Austria, and Italy.** All verified. Germany is the headline risk because it is likely Markus's #1 market, but Austria and Italy require opt-in for B2B email too, so cold email is off the table in all three.

**Germany red flag (read this first).** Under UWG §7, sending advertising email without prior express consent is treated as unreasonable harassment and applies identically to B2B and B2C. There is no German B2B exemption, and presumed consent does not count. Enforcement is not just regulators: competitors and trade associations can issue a cease-and-desist (Abmahnung) and seek injunctions, which is fast and can cost more than a fine. **Do not run standard cold-email sequences into German recipients.** Use the consent-free channels below instead.

## Layer 1: GDPR (the data)

- **Lawful basis = legitimate interest, Art 6(1)(f).** Cold prospecting is not consent-based under GDPR, but it requires the three-part test: a legitimate purpose, necessity (email is a proportionate way to reach a business contact about a relevant business matter), and a balancing test that the recipient's rights do not override.
- **Document the LIA.** Keep a written Legitimate Interest Assessment on file. In a French CNIL audit, the LIA is the first document requested, and without it the processing is presumed non-compliant. RevOps owns the template; do not send into a new country without one.
- **Transparency.** The recipient must be able to find out how we got their data and how to object, via an accessible privacy notice (a link is enough). Recording the data source per contact matters.
- **Right to object / erasure.** Honor objections and unsubscribes immediately and permanently. Suppress, do not re-add.
- **Data minimization + retention.** Only the fields we need, kept only as long as needed. Stale, unengaged contacts should age out.
- **Processors.** Smartlead and Apollo process personal data on our behalf, so they are processors and need a data-processing agreement (DPA) in place. Confirm DPAs exist before running European volume through them.

## Layer 2: ePrivacy (the send)

The ePrivacy Directive's marketing-email rule was transposed country by country, and member states chose whether to extend the email opt-in requirement to legal persons (B2B). That single choice is what splits Europe:

- **B2B vs B2C distinction is real but country-dependent.** In some countries the opt-in applies only to individuals (so B2B-to-corporate is opt-out). In others (Germany) it applies to everyone.
- **Generic vs named addresses.** A generic role address (info@, contact@) is generally not personal data, so GDPR bites less, but the ePrivacy send rule and the country regime still apply.
- **Soft opt-in (existing customers only).** Where it exists, you may email an existing customer about similar products if they were given an opt-out at collection and in every message. This does NOT cover cold prospects.

## Country traffic-light (verify before a new-country program)

| Country | Cold B2B email regime | Confidence | Notes |
|---|---|---|---|
| **Germany** | **Prior express consent required (opt-in), B2B and B2C alike** | Verified | UWG §7. No B2B exemption. Abmahnung (competitor cease-and-desist) enforcement. Do not cold-email. |
| **United Kingdom** | Opt-out to corporate subscribers (companies, LLPs, public bodies); individuals (sole traders, most unincorporated partnerships, personal addresses) need consent | Verified | PECR does not cover corporate subscribers; UK GDPR still applies to named-employee addresses. Identify org, give valid contact details + opt-out. |
| **France** | Opt-out for named professionals (legitimate interest), provided the message relates to their profession | Verified | CNIL: clear identity, easy unsubscribe in every message, subject matches content, documented LIA. |
| **Netherlands** | Legitimate-interest-friendly for B2B with fewer restrictions | Verified (directional) | Still honor opt-out + GDPR. |
| **Austria** | **Prior consent required (opt-in), B2B included** | Verified | TKG §107: opt-in applies to legal persons too. Only narrow exceptions (existing-customer soft opt-in; a contested small-volume provision), none a basis for cold prospecting. Regulators expect double opt-in; fines up to €100,000. Do not cold-email. |
| **Italy** | **Prior consent required (opt-in), B2B included** | Verified | Privacy Code Art 130. The Garante requires opt-in for B2B email, not just legitimate interest, and is trending to double opt-in. One of the strictest EU jurisdictions. Soft opt-in for existing customers only. Do not cold-email. |
| **Spain, Nordics, Belgium, Poland, others** | Mixed | Verify | Do not assume. Check the national transposition before sending. |

## Mandatory elements in every outbound (all countries)

- Truthful, identifiable sender. Real From identity (Markus), real company.
- Valid contact details, including a postal address where required, and a working reply path.
- Subject line that matches the content. No bait-and-switch (France and Germany both treat misleading subjects as a violation).
- A clear, simple, free opt-out in every message, honored immediately and permanently.
- No disguised or false header information.
- This is on top of the MaiaEdge copy rules (no em dashes, no credibility anchors in cold, the activity gate). Compliance and craft both apply.

## Hard don'ts

- Do not run cold-email sequences into German recipients without prior express consent. Default to consent-free channels there.
- Do not use purchased or scraped lists. Unlawful in Germany and a GDPR transparency problem everywhere.
- Do not send without a documented LIA for that country.
- Do not ignore or delay an opt-out, and never re-add an opt-out.
- Do not assume one country's rule applies to its neighbor.

## How this shapes the MaiaEdge European motion

- **Route by country, not by one EU template.** Where the regime is opt-out-friendly (UK corporate, France professional, NL), cold email on legitimate interest is workable with the conditions above. Where it is opt-in (Germany, Austria, Italy, all verified), do not cold-email.
- **Germany is the strategic wrinkle, and the GM motion already answers it.** Markus's warmest market is also Europe's most email-restricted. Lead there with the consent-free plays: LinkedIn relationship-building and connection requests (a connection request is not advertising email), events and industry gatherings (Capacity Europe, DE-CIX and IX community, FTTH Council), warm introductions, and referrals from the ecosystem. This is exactly the partner-and-ecosystem half of the GM mandate, so in Germany the motion shifts weight from cold email to relationship and event sourcing by design, not as a workaround.
- **LinkedIn is the safer cold channel in strict markets,** because a connection request and a personal message are not "advertising email" under UWG/ePrivacy. Keep them genuine and relevant per `skills/linkedin-outreach/SKILL.md`; the compliance benefit does not lower the craft bar.
- **The activity gate and opt-out suppression still apply,** on top of everything here.
- **When in doubt, stop and ask.** New country, unusual recipient type (sole trader, generic vs named), or any uncertainty about a German send: check with Cooper / RevOps and counsel before sending. A paused send is cheaper than an Abmahnung.

## Strict-market consent-free play (Germany, Austria, Italy: all verified opt-in markets)

In an opt-in market you cannot open with cold advertising email. This is the concrete substitute: a relationship sequence on channels that are lawful without prior consent, whose secondary objective is to earn documented consent, which is what makes any later email lawful. It is slower than a Smartlead sequence by design. That is the cost of doing it lawfully, and it is the ecosystem half of the GM motion doing the work cold email does elsewhere.

### Channel legality in Germany (verified)

- **LinkedIn connection request, non-promotional: lawful.** A plain connection request is not advertising under UWG §7. This is the safe cold entry point.
- **LinkedIn message: lawful only after the connection is accepted.** Messages fall under UWG §7, so do not send a promotional message to someone who has not accepted. Once connected, a genuine, relevant message is permitted.
- **B2B phone: lawful only under presumed consent (mutmassliche Einwilligung), and the bar is high.** German courts read it narrowly: the offer must closely fit the recipient's concrete business need, ideally with a prior relationship or inquiry, and a same-industry guess is not enough. Document the rationale before you call. Not a blanket option.
- **Email: only after documented consent** (or an existing-customer soft opt-in). Cold advertising email stays off the table.
- **Events and referrals: lawful.** A conversation at a show or a warm introduction is a consent-free, and warmer, start.
- **Austria and Italy share the email opt-in rule (verified), so the same play applies.** Austria (TKG §107) and Italy (Privacy Code Art 130) both require prior consent for B2B marketing email, so the connect-first sequence below is the safe default in all three markets. The precise phone and LinkedIn-message treatment in Austria and Italy was not individually verified here, so confirm those locally before relying on them and default to the German-style caution.

### The sequence (a cadence, not a script; mechanics per `skills/linkedin-outreach/SKILL.md`)

1. **Touch 1, Day 0, LinkedIn connection request.** Plain or one line, signal-grounded, peer voice, no pitch. Lawful as a non-promotional request.
2. **Touch 2, after accept (Day 2 to 5), LinkedIn message.** Now permitted because they accepted. Name the problem in their world (the earned-problem doctrine), one idea, pressure-off. Not a brochure.
3. **Touch 3, Day 7 to 12, light relevance.** React to or comment on their content, or share one relevant, non-promotional thought. Familiarity, not selling.
4. **Touch 4, Day 14 to 21, the soft ask.** Low-pressure invite to a short call or to meet at an upcoming event. If they agree to receive information, that is your consent moment.
5. **Event / referral overlay.** If a show (Capacity Europe, the DE-CIX community, FTTH Council) or a mutual connection is in play, fold it in. It accelerates the sequence and strengthens the legal footing.
6. **Phone only where presumed consent genuinely holds** (close fit to their need, ideally prior contact), with the rationale documented first.

### The consent bridge (how you unlock lawful email)

When a prospect agrees, verbally on a call or in writing, to receive materials or follow-up, record it in HubSpot: who consented, when, and to what. That documented consent is what makes subsequent email lawful in a strict market, and from that point you switch to the normal follow-up motion. Without it, stay on LinkedIn, events, and, where it genuinely holds, phone.

### Carried-over guardrails

The `linkedin-outreach` mechanics still apply in full (35 to 50 words, under the 280-character cap, no sender intro in the body, no credibility anchors in cold, signal-grounded), plus the activity gate (14-day hard stop, 45-day review), honor every opt-out immediately, and no purchased or scraped lists. Compliance lowers the channel risk. It does not lower the craft bar.

### Pacing reality

Plan for weeks, not days, to first conversation in these markets, and fewer concurrent threads than a US cold-email motion would run. Forecast the German build accordingly.

---

## Sources (verified June 2026)

- ePrivacy Regulation withdrawn (2025 Commission work programme): [TechCrunch, "EU abandons ePrivacy reform" (Feb 2025)](https://techcrunch.com/2025/02/12/eu-abandons-eprivacy-reform-as-bloc-shifts-focus-to-competitiveness-and-fostering-data-access-for-ai); [Mailshake, Cold Email Compliance 2026](https://mailshake.com/blog/cold-email-compliance/).
- GDPR legitimate interest three-part test + LIA + ePrivacy override, country variation: [Litemail, GDPR Legitimate Interest for Cold Email 2026](https://litemail.ai/blog/gdpr-legitimate-interest-cold-email-2026); [Prospeo, GDPR Cold Email B2B 2026](https://prospeo.io/s/gdpr-cold-email-b2b).
- Germany UWG §7 (consent required B2B and B2C, no exemption, Abmahnung enforcement): [Overloop, Cold Email Germany GDPR & UWG §7](https://overloop.com/blog/b2b-cold-email-germany-gdpr-compliance); [SRD Rechtsanwalte, email marketing without consent](https://www.srd-rechtsanwaelte.de/en/blog/email-marketing-without-consent); [Certified Senders Alliance, Permission](https://certified-senders.org/email-directive/2-permission/).
- UK PECR corporate subscribers + individual-subscriber consent + UK GDPR: [ICO, B2B marketing](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/); [ICO, PECR electronic mail rules](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-direct-marketing-using-electronic-mail/how-do-we-comply-with-the-pecr-electronic-mail-marketing-rules/).
- France CNIL B2B opt-out for professionals + LIA: [CNIL prospection B2B 2026 (FR)](https://fichierb2b.fr/articles/cnil-prospection-b2b-legal-2026/); [Overloop, B2B cold email France CNIL/RGPD (FR)](https://overloop.com/fr/blog/b2b-cold-email-france-cnil-rgpd).
- Netherlands legitimate-interest-friendly B2B: [Prospeo, GDPR Cold Email Rules 2026](https://prospeo.io/s/gdpr-cold-email).
- Strict-market channel legality (LinkedIn connection requests not advertising under UWG §7; LinkedIn messages permitted only after the connection is accepted; B2B phone lawful only under narrowly-interpreted presumed consent; the multi-channel-then-email-after-consent approach): [Overloop, Cold Email Germany GDPR & UWG §7](https://overloop.com/blog/b2b-cold-email-germany-gdpr-compliance); [Amplifa, cold outreach & GDPR Germany](https://amplifa.ai/en/cold-outreach-gdpr/); [Prospeo, Cold Calling in Germany 2026](https://prospeo.io/s/cold-calling-in-germany).
- Austria (TKG §107: opt-in including legal persons, narrow exceptions, double-opt-in expectation, fines up to €100,000): [DLA Piper, Electronic marketing in Austria](https://www.dlapiperdataprotection.com/index.html?t=electronic-marketing&c=AT); [Lexology, Electronic marketing and internet use in Austria](https://www.lexology.com/library/detail.aspx?g=e37ce971-4a4b-4dc3-9299-03c3c5393584).
- Italy (Privacy Code Art 130: opt-in, Garante requires consent for B2B email not just legitimate interest, double-opt-in trend, soft opt-in for existing customers): [DLA Piper, Electronic marketing in Italy](https://www.dlapiperdataprotection.com/index.html?t=electronic-marketing&c=IT); [DLA Piper Privacy Matters, Italy marketing consent / double opt-in (2025)](https://privacymatters.dlapiper.com/2025/07/italy-marketing-privacy-consent-is-double-opt-in-now-mandatory/).
