from __future__ import annotations

import json
import shutil
import textwrap
import urllib.request
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SITE = REPO / "hugo-site"
SOURCE = REPO.parent


def write(rel: str, content: str) -> None:
    path = SITE / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")


def write_repo(rel: str, content: str) -> None:
    path = REPO / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")


def q(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def qlist(values: list[str]) -> str:
    return json.dumps(values, ensure_ascii=False)


def yaml_list(values: list[str]) -> str:
    if not values:
        return "  []"
    return "\n".join(f"  - {q(value)}" for value in values)


def yaml_links(links: list[dict]) -> str:
    rows = [
        f"  - name: {q(link['name'])}\n    url: {q(link['url'])}"
        for link in links
    ]
    return "\n".join(rows) if rows else "  []"


PUBLICATIONS = [
    {
        "slug": "interaction-spectrum-auctions-mobile-market-competition",
        "title": "Interaction of Spectrum Auctions and Mobile Market Competition: Review of Theory and Evidence from European 4G Auctions",
        "date": "2026-02-01",
        "authors": ["Daniel Ershov", "David Salant"],
        "publication_types": ["journal_article"],
        "publication": "International Journal of Industrial Organization, 106, Article 103287",
        "status": "published",
        "areas": ["competition-policy"],
        "tags": ["spectrum auctions", "mobile markets", "competition policy"],
        "summary": "European 4G auction evidence links low-band auction outcomes to later concentration and prices when incumbent operators entered auctions with higher pre-auction shares.",
        "abstract": "This paper examines how ex ante market structure affects spectrum auctions and subsequent mobile market outcomes. We review the relevant theory and present evidence from European 4G auctions showing that low-band auctions are followed by higher concentration and prices in markets where incumbent operators had higher pre-auction shares, without corresponding improvements in coverage or investment.",
        "main_finding": "Low-band auctions are followed by higher concentration and prices in markets where incumbent operators had higher pre-auction shares, without corresponding improvements in coverage or investment.",
        "policy_relevance": "Spectrum auction design should account for how pre-auction asymmetries affect downstream competition, not only auction revenue or licence allocation.",
        "links": [
            {"name": "DOI", "url": "https://doi.org/10.1016/j.ijindorg.2026.103287"},
            {"name": "UCL Discovery", "url": "https://discovery.ucl.ac.uk/id/eprint/10224601/"},
            {"name": "SSRN", "url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4607235"},
            {"name": "Working Paper PDF", "url": "https://www.dropbox.com/scl/fi/e37obsju9k20i7q8o6iy7/Auction_Competition_Sept2025.pdf?rlkey=ikowjxmhashic4k108qzm0g7e&st=ahr238bu&dl=0"},
        ],
        "bibkey": "ershov2026spectrum",
    },
    {
        "slug": "estimating-complementarity-large-choice-sets",
        "title": "Estimating Complementarity with Large Choice Sets: An Application to Mergers",
        "date": "2025-12-01",
        "authors": ["Daniel Ershov", "Mathieu Marcoux", "Scott Orr", "Jean-William P. Laliberté"],
        "publication_types": ["journal_article"],
        "publication": "RAND Journal of Economics, 56(4), 689-707",
        "status": "published",
        "areas": ["demand-estimation-and-market-structure"],
        "tags": ["demand estimation", "complementarity", "mergers", "discrete choice"],
        "summary": "A GMM estimator identifies demand complementarity with price endogeneity and large choice sets, changing merger counterfactuals in chips and soda.",
        "abstract": "Standard discrete choice models assume that products are substitutes. This paper develops a GMM estimator that identifies demand complementarity with price endogeneity and large choice sets, applies it to chips and soda, and shows that accounting for complementarity can substantially change merger counterfactuals.",
        "main_finding": "Accounting for chip-soda complementarity lowers predicted soda price increases from a PepsiCo/Frito-Lay and Dr Pepper merger by about 30% relative to a substitutes-only model; post-merger chip prices decrease.",
        "policy_relevance": "Merger simulations in large differentiated-product markets can be misleading when they impose substitution patterns that rule out complementarity.",
        "links": [
            {"name": "DOI", "url": "https://doi.org/10.1111/1756-2171.70024"},
            {"name": "SSRN", "url": "https://ssrn.com/abstract=3802097"},
            {"name": "UCL Discovery", "url": "https://discovery.ucl.ac.uk/id/eprint/10189990/"},
        ],
        "bibkey": "ershov2025complementarity",
    },
    {
        "slug": "how-much-influencer-marketing-undisclosed",
        "title": "Frontiers: How Much Influencer Marketing Is Undisclosed? Evidence from Twitter",
        "date": "2025-05-01",
        "authors": ["Daniel Ershov", "Yanting He", "Stephan Seiler"],
        "publication_types": ["journal_article"],
        "publication": "Marketing Science, 44(3), 505-515",
        "status": "published",
        "areas": ["influencer-marketing-and-disclosure", "competition-policy"],
        "tags": ["influencer marketing", "advertising disclosure", "consumer protection", "social media"],
        "summary": "Using more than 100 million Twitter posts, the paper estimates that 96% of sponsored influencer posts are undisclosed; a lower-bound classification still implies 82%.",
        "abstract": "We study the disclosure of influencer posts on Twitter across a large set of brands using more than 100 million posts and a text-based classifier for undisclosed sponsorship. In the preferred empirical specification, 96% of sponsored posts are not disclosed; a lower-bound classification still implies an undisclosed share of 82%. Despite stronger enforcement of disclosure regulations, the share of undisclosed posts decreases only slightly over time. Compared to disclosed posts, undisclosed posts tend to be associated with young brands with a large Twitter following.",
        "main_finding": "Most sponsored influencer advertising in the Twitter data is undisclosed: 96% in the preferred specification and 82% under a lower-bound classification.",
        "policy_relevance": "Disclosure enforcement can miss most sponsored content consumers encounter, so researchers and regulators need tools that detect non-disclosed advertising directly.",
        "links": [
            {"name": "DOI", "url": "https://doi.org/10.1287/mksc.2024.0838"},
            {"name": "SSRN", "url": "https://ssrn.com/abstract=4626503"},
            {"name": "CEPR VoxEU Column", "url": "https://cepr.org/voxeu/columns/majority-influencer-advertising-undisclosed"},
        ],
        "bibkey": "ershov2025undisclosed",
    },
    {
        "slug": "ai-cognitive-offloading-critical-thinking-ucl",
        "title": "Long Reads: Is AI the End of Critical Thinking?",
        "date": "2025-09-12",
        "authors": ["Daniel Ershov"],
        "publication_types": ["report"],
        "publication": "UCL School of Management Long Reads",
        "status": "policy",
        "areas": ["digital-platforms-and-online-markets"],
        "tags": ["AI", "large language models", "cognitive offloading", "critical thinking"],
        "summary": "UCL School of Management long read arguing that AI tools such as ChatGPT are more likely to support complex problem solving than eliminate human critical thinking.",
        "abstract": "This UCL School of Management long read argues that the adoption of AI platforms such as ChatGPT does not signal the death of critical thinking. It places concerns about LLMs and cognitive offloading in historical context, comparing them to earlier concerns about writing, calculators, and Wikipedia, and argues that effective use of LLMs still requires prompting, interpretation, diagnosis of model failures, and human judgment.",
        "main_finding": "LLMs can automate some tasks, but complex decisions still require users to understand the model's failures, interpret outputs, and apply context-specific human judgment.",
        "policy_relevance": "Education and workplace AI policy should focus on how users develop prompting, evaluation, and problem-solving skills rather than treating AI use as a simple substitute for thinking.",
        "links": [
            {"name": "UCL Long Read", "url": "https://www.mgmt.ucl.ac.uk/news/long-reads-1-ai-and-cognitive-offloading"},
        ],
        "bibkey": "ershov2025cognitiveoffloading",
    },
    {
        "slug": "effects-advertising-disclosure-regulations-social-media",
        "title": "The Effects of Advertising Disclosure Regulations on Social Media: Evidence from Instagram",
        "date": "2025-03-01",
        "authors": ["Daniel Ershov", "Matthew Mitchell"],
        "publication_types": ["journal_article"],
        "publication": "RAND Journal of Economics, 56(1), 74-90",
        "status": "published",
        "areas": ["influencer-marketing-and-disclosure", "competition-policy"],
        "tags": ["advertising disclosure", "Instagram", "regulation", "difference-in-differences"],
        "summary": "German Instagram disclosure rules increased disclosure but also increased sponsored content by 12%, raised exposure to undisclosed sponsorship, and reduced engagement.",
        "abstract": "We study the effects of advertising disclosure regulations in social media markets using Instagram data from Germany and Spain and a difference-in-differences approach. The German strengthening of disclosure rules increased the use of disclosure terms, but also increased sponsored content by 12% and raised the share of undisclosed sponsored content consumers were exposed to. We also find reductions in engagement, suggesting that followers were likely negatively affected.",
        "main_finding": "Disclosure rules increased disclosure, but they also increased sponsored content by 12% and raised consumers' exposure to undisclosed sponsored posts.",
        "policy_relevance": "Disclosure regulation can change the supply of sponsored content, not only labeling compliance; this matters for consumer-protection policy on social media.",
        "links": [
            {"name": "DOI", "url": "https://doi.org/10.1111/1756-2171.12493"},
            {"name": "UCL Discovery", "url": "https://discovery.ucl.ac.uk/id/eprint/10190654/"},
            {"name": "Replication Package", "url": "https://www.openicpsr.org/openicpsr/project/195082/view"},
            {"name": "ACM-EC Abstract", "url": "https://dl.acm.org/doi/10.1145/3391403.3399477"},
            {"name": "ACM-EC Full Version", "url": "https://www.dropbox.com/s/c6qn4us6gugwqqi/Influencers_ACM_EC_Website.pdf?dl=0"},
        ],
        "notes": ["Extended abstract published in the ACM-EC 2020 Conference Proceedings."],
        "bibkey": "ershov2025disclosure",
    },
    {
        "slug": "majority-influencer-advertising-undisclosed-cepr",
        "title": "The Majority of Influencer Advertising Is Undisclosed",
        "date": "2025-05-15",
        "authors": ["Daniel Ershov", "Yanting He", "Stephan Seiler"],
        "publication_types": ["report"],
        "publication": "VoxEU Column, CEPR",
        "status": "cepr_contribution",
        "areas": ["influencer-marketing-and-disclosure"],
        "tags": ["influencer marketing", "advertising disclosure", "consumer protection", "CEPR", "VoxEU"],
        "summary": "CEPR VoxEU column on the scale of undisclosed influencer advertising and why disclosure rules can miss hidden sponsorship.",
        "abstract": "This CEPR VoxEU column summarizes evidence that most sponsored influencer advertising on Twitter is not disclosed, discusses the scale of hidden sponsorship, and explains why disclosure rules can miss most sponsored content consumers encounter.",
        "links": [
            {"name": "CEPR VoxEU Column", "url": "https://cepr.org/voxeu/columns/majority-influencer-advertising-undisclosed"},
        ],
        "bibkey": "ershov2025voxundisclosed",
    },
    {
        "slug": "sharing-news-left-right",
        "title": "Sharing News Left and Right: Frictions and Misinformation on Twitter",
        "date": "2024-08-01",
        "authors": ["Daniel Ershov", "Juan S. Morales"],
        "publication_types": ["journal_article"],
        "publication": "The Economic Journal, 134(662), 2391-2417",
        "status": "published",
        "areas": ["digital-platforms-and-online-markets", "competition-policy"],
        "tags": ["misinformation", "Twitter", "social media", "political economy"],
        "summary": "Twitter's October 2020 sharing friction reduced news sharing, with larger reductions for left-wing outlets than right-wing outlets.",
        "abstract": "On October 20, 2020, prior to the U.S. presidential election, Twitter changed its sharing interface by adding friction before users could retweet links they had not opened. Using tweets from U.S. news media outlets, we show that the intervention reduced news sharing and that reductions were larger for left-wing outlets than for right-wing outlets. Examining Twitter activity data for news-sharing users, we find that conservatives were less responsive to Twitter's intervention. Using web traffic data, we also document that the policy significantly reduced visits to news media outlets' websites.",
        "main_finding": "The sharing friction reduced news sharing, but the reduction was asymmetric: content from left-wing outlets fell more than content from right-wing outlets, and conservative users were less responsive.",
        "policy_relevance": "Small platform-design frictions can change political news diffusion and misinformation exposure in ways that vary across ideological groups.",
        "links": [
            {"name": "DOI", "url": "https://doi.org/10.1093/ej/ueae027"},
            {"name": "UCL Discovery", "url": "https://discovery.ucl.ac.uk/id/eprint/10190653/"},
            {"name": "CEPR VoxEU Column", "url": "https://cepr.org/voxeu/columns/sharing-news-left-and-right"},
            {"name": "Working Paper", "url": "https://www.carloalberto.org/wp-content/uploads/2021/05/no.651.pdf"},
            {"name": "Earlier PDF", "url": "https://www.dropbox.com/scl/fi/9q94v88nj6rdpfzgd3qfx/newssharing_EJ3_aug2023.pdf?rlkey=wevonj2hb9wo4nwv95ijjpbw5&dl=0"},
        ],
        "bibkey": "ershov2024news",
    },
    {
        "slug": "sharing-news-left-right-cepr",
        "title": "Sharing News Left and Right",
        "date": "2024-10-04",
        "authors": ["Daniel Ershov", "Juan S. Morales"],
        "publication_types": ["report"],
        "publication": "VoxEU Column, CEPR",
        "status": "cepr_contribution",
        "areas": ["digital-platforms-and-online-markets"],
        "tags": ["misinformation", "Twitter", "social media", "political economy", "CEPR", "VoxEU"],
        "summary": "CEPR VoxEU column on how Twitter's October 2020 sharing friction affected news diffusion and political asymmetries.",
        "abstract": "This CEPR VoxEU column summarizes evidence from Twitter's October 2020 interface change, showing how sharing frictions affected news diffusion and political asymmetries in misinformation exposure.",
        "links": [
            {"name": "CEPR VoxEU Column", "url": "https://cepr.org/voxeu/columns/sharing-news-left-and-right"},
        ],
        "bibkey": "ershov2024voxnews",
    },
    {
        "slug": "pricing-algorithms-third-party-facilitators-collusion",
        "title": "Pricing Algorithms as Third-Party Facilitators of Collusion",
        "date": "2024-12-01",
        "authors": ["Robert Clark", "Daniel Ershov", "Jean-François Houde"],
        "publication_types": ["report"],
        "publication": "The Antitrust Source, December 2024",
        "status": "policy",
        "areas": ["algorithmic-pricing-and-competition", "competition-policy"],
        "tags": ["pricing algorithms", "collusion", "third-party facilitators", "antitrust"],
        "summary": "The Antitrust Source article on how pricing algorithms may act as third-party facilitators of collusion, drawing on recent U.S. cases and economic evidence on algorithmic pricing.",
        "abstract": "Several recent U.S. cases have highlighted the possibility that pricing algorithms can act as third-party facilitators of collusion. This article discusses that possibility and examines the economics of algorithmic pricing and competition, including the role that pricing software can play when third-party providers sell algorithms to multiple competitors in the same market.",
        "main_finding": "Pricing algorithms may play an analogous role to a hub by collecting data from competing firms and potentially coordinating pricing decisions across competitors.",
        "policy_relevance": "Antitrust analysis of algorithmic pricing should consider whether third-party software providers can facilitate coordination by helping firms overcome information-sharing and monitoring problems.",
        "links": [
            {"name": "ABA Article PDF", "url": "https://www.americanbar.org/content/dam/aba/publications/antitrust/source/2024/december/pricing-algorithms-third-party-facilitators-collusion.pdf"},
        ],
        "bibkey": "clark2024pricingalgorithms",
    },
    {
        "slug": "algorithmic-pricing-competition-cpi-antitrust-chronicle",
        "title": "Algorithmic Pricing and Competition",
        "date": "2023-06-01",
        "authors": ["Robert Clark", "Daniel Ershov"],
        "publication_types": ["report"],
        "publication": "CPI Antitrust Chronicle, June 2023",
        "status": "policy",
        "areas": ["algorithmic-pricing-and-competition", "competition-policy"],
        "tags": ["algorithmic pricing", "competition policy", "retail gasoline", "antitrust"],
        "summary": "CPI Antitrust Chronicle article summarizing empirical evidence on AI-driven algorithmic pricing adoption in German retail gasoline markets and its implications for competition.",
        "abstract": "This CPI Antitrust Chronicle article examines the impact of AI-driven algorithmic pricing software. It summarizes empirical evidence from Germany's retail gasoline market, where algorithmic pricing software became widely available in 2017. The evidence suggests that adoption increased margins, especially in competitive markets, indicating that algorithmic pricing may have softened competition.",
        "main_finding": "Adoption of algorithmic pricing increased margins in the German retail gasoline market, with stronger effects in competitive markets and in small oligopoly markets where all stations adopted.",
        "policy_relevance": "Competition authorities should evaluate algorithmic pricing using empirical evidence on market structure, adoption patterns, and pricing responses, not only theoretical concerns about algorithmic collusion.",
        "links": [
            {"name": "CPI Article PDF", "url": "https://www.competitionpolicyinternational.com/wp-content/uploads/2023/06/3-ALGORITHMIC-PRICING-AND-COMPETITION-Robert-Clark-Daniel-Ershov.pdf"},
        ],
        "bibkey": "clark2023cpialgorithmic",
    },
    {
        "slug": "algorithmic-pricing-competition-german-retail-gasoline-market",
        "title": "Algorithmic Pricing and Competition: Empirical Evidence from the German Retail Gasoline Market",
        "date": "2024-03-01",
        "authors": ["Stephanie Assad", "Robert Clark", "Daniel Ershov", "Lei Xu"],
        "publication_types": ["journal_article"],
        "publication": "Journal of Political Economy, 132(3), 723-771",
        "status": "published",
        "areas": ["algorithmic-pricing-and-competition", "competition-policy"],
        "tags": ["algorithmic pricing", "retail gasoline", "competition", "structural breaks"],
        "summary": "Algorithmic pricing adoption increases margins in Germany's retail gasoline market, but only for non-monopoly stations; in duopolies, margins rise only when both stations adopt.",
        "abstract": "We provide empirical evidence on the relationship between algorithmic pricing and competition in Germany's retail gasoline market, where algorithmic pricing software became widely available in 2017. Because adoption dates are unknown, we identify adopting stations by testing for structural breaks in algorithmic-pricing markers and instrument for station adoption using headquarters adoption. Adoption increases margins, but only for non-monopoly stations; in duopoly markets, margins rise only when both stations adopt.",
        "main_finding": "Algorithmic pricing adoption increases margins only outside monopoly markets; in duopolies, margins rise only when both stations adopt.",
        "policy_relevance": "The competitive effects of pricing algorithms depend on market structure and rival adoption, which matters for antitrust analysis of algorithmic pricing.",
        "links": [
            {"name": "DOI", "url": "https://doi.org/10.1086/726906"},
            {"name": "UCL Discovery", "url": "https://discovery.ucl.ac.uk/id/eprint/10187765/"},
            {"name": "CESifo Working Paper", "url": "https://www.ifo.de/en/cesifo/publications/2020/working-paper/algorithmic-pricing-and-competition-empirical-evidence-german"},
            {"name": "Paper PDF", "url": "https://www.dropbox.com/s/8p8k6dttbellw3r/ACEX_Feb_2023.pdf?dl=0"},
            {"name": "Data Appendix", "url": "https://www.dropbox.com/s/3dl6c5le5x78l2e/ACEX_Nov29_2021_data_appendix.pdf?dl=0"},
        ],
        "notes": ["Lead article in the March 2024 issue of the Journal of Political Economy."],
        "bibkey": "assad2024algorithmic",
    },
    {
        "slug": "variety-based-congestion-online-markets",
        "title": "Variety-Based Congestion in Online Markets: Evidence from Mobile Apps",
        "date": "2024-05-01",
        "authors": ["Daniel Ershov"],
        "publication_types": ["journal_article"],
        "publication": "American Economic Journal: Microeconomics, 16(2), 180-203",
        "status": "published",
        "areas": ["digital-platforms-and-online-markets", "demand-estimation-and-market-structure"],
        "tags": ["mobile apps", "online markets", "congestion", "entry", "consumer search"],
        "summary": "Using Android app store data and a store redesign, the paper shows that entry creates congestion externalities and erodes about 40% of consumer variety welfare gains.",
        "abstract": "In many online markets, consumers spend time and effort browsing through products. The addition of new products can make other products less visible, creating congestion externalities. Using Android app store data and a redesign of part of the store, I show that more apps directly reduce per-app usage and downloads. The natural experiment also increases long-run entry, but a structural demand model that accounts for congestion externalities suggests that 40% of consumer variety welfare gains are lost from higher congestion.",
        "main_finding": "More app variety increases entry but reduces per-app usage and downloads; accounting for congestion implies that 40% of consumer variety welfare gains are lost.",
        "policy_relevance": "Platform design affects the welfare value of variety because search and discovery frictions can turn entry into congestion.",
        "links": [
            {"name": "DOI", "url": "https://doi.org/10.1257/mic.20200347"},
            {"name": "AEA Article Page", "url": "https://www.aeaweb.org/articles?id=10.1257/mic.20200347"},
            {"name": "UCL Discovery", "url": "https://discovery.ucl.ac.uk/id/eprint/10187767/"},
            {"name": "Replication Package", "url": "https://www.openicpsr.org/openicpsr/project/181301/version/V1/view"},
            {"name": "AEA Research Highlight", "url": "https://www.aeaweb.org/research/congestion-variety-based-apps"},
        ],
        "notes": ["A previous draft circulated under the title Consumer Product Discovery Costs, Entry, Quality and Congestion in Online Markets."],
        "bibkey": "ershov2024variety",
    },
    {
        "slug": "autonomous-algorithmic-collusion",
        "title": "Autonomous Algorithmic Collusion: Economic Research and Policy Implications",
        "date": "2021-09-23",
        "authors": ["Stephanie Assad", "Emilio Calvano", "Giacomo Calzolari", "Robert Clark", "Vincenzo Denicolò", "Daniel Ershov", "Justin Johnson", "Sergio Pastorello", "Andrew Rhodes", "Lei Xu", "Matthijs Wildenbeest"],
        "publication_types": ["journal_article"],
        "publication": "Oxford Review of Economic Policy, 37(3), 459-478",
        "status": "published",
        "areas": ["algorithmic-pricing-and-competition", "competition-policy"],
        "tags": ["algorithmic collusion", "competition policy", "pricing algorithms"],
        "summary": "Review of economic research on autonomous algorithmic collusion and the policy questions facing competition authorities.",
        "abstract": "This article reviews economic research on autonomous algorithmic collusion and discusses its implications for competition policy. It connects theoretical, experimental, and empirical evidence to the institutional questions facing competition authorities.",
        "main_finding": "The economic evidence points to specific mechanisms through which autonomous algorithms can soften competition, but the strength of those mechanisms depends on market and algorithm design.",
        "policy_relevance": "Competition authorities need evidence on when algorithmic systems change competitive conduct, not only general claims about algorithmic collusion.",
        "links": [
            {"name": "DOI", "url": "https://doi.org/10.1093/oxrep/grab011"},
        ],
        "bibkey": "assad2021collusion",
    },
    {
        "slug": "market-incentives-business-innovation-canada",
        "title": "Market Incentives for Business Innovation: Results from Canada",
        "date": "2012-03-01",
        "authors": ["Charles Bérubé", "Marc Duhamel", "Daniel Ershov"],
        "publication_types": ["journal_article"],
        "publication": "Journal of Industry, Competition and Trade, 12(1), 47-65",
        "status": "published",
        "areas": ["competition-policy"],
        "tags": ["innovation", "competition", "Canada", "firm behavior"],
        "summary": "Evidence from Canada on how market incentives and competitive conditions relate to business innovation.",
        "abstract": "This paper studies how market incentives shape business innovation using evidence from Canada. It links competitive conditions and firm incentives to observed innovation outcomes.",
        "main_finding": "Canadian firm evidence links market incentives and competitive conditions to observed innovation outcomes.",
        "policy_relevance": "Innovation policy should consider how market incentives shape firms' returns to innovation.",
        "links": [
            {"name": "DOI", "url": "https://doi.org/10.1007/s10842-011-0122-5"},
        ],
        "bibkey": "berube2012innovation",
    },
    {
        "slug": "what-happens-when-dating-goes-online",
        "title": "What Happens When Dating Goes Online? Evidence from U.S. Marriage Markets and Health Outcomes",
        "date": "2026-01-19",
        "authors": ["Daniel Ershov", "Jessica Fong", "Pinar Yildirim"],
        "publication_types": ["report"],
        "publication": "CEPR Discussion Paper No. 21054",
        "status": "working_paper",
        "areas": ["digital-platforms-and-online-markets"],
        "tags": ["online dating", "marriage", "divorce", "assortative matching", "health outcomes"],
        "summary": "Online dating affected U.S. marriage markets differently across desktop and mobile eras: desktop usage raised divorce rates, while mobile activity lowered marriage and divorce rates.",
        "abstract": "This paper studies how online dating platforms affected marital outcomes, assortative matching, and sexually transmitted disease rates in the United States. In the desktop era, a 1% increase in online dating sessions raises divorce rates by 0.50%. In the mobile era, a 1% increase in online dating activity lowers marriage and divorce rates by 0.40% and 0.33%, respectively. Across both eras, we find no evidence that greater online dating usage increases average STD rates; average effects are negative or statistically insignificant, although they are positive for some subpopulations. We develop a search and matching model in which technological changes affect search costs, market size, and market noise.",
        "main_finding": "The effects of online dating differ sharply by era: desktop activity increases divorce, while mobile activity lowers marriage and divorce rates; average STD effects are negative or statistically insignificant.",
        "policy_relevance": "Digital matching technologies can change family formation and health outcomes through search costs, market size, and market noise.",
        "links": [
            {"name": "CEPR Discussion Paper", "url": "https://cepr.org/publications/dp21054"},
            {"name": "SSRN", "url": "https://ssrn.com/abstract=6076486"},
            {"name": "NBER Working Paper", "url": "https://www.nber.org/papers/w34757"},
        ],
        "bibkey": "ershov2026dating",
    },
    {
        "slug": "outsourcing-algorithm-development-contractors-llms",
        "title": "Outsourcing Algorithm Development: Evidence from Contractors and LLMs",
        "date": "2025-12-09",
        "authors": ["Daniel Ershov", "Elizabeth Lyons"],
        "publication_types": ["report"],
        "publication": "CEPR Discussion Paper No. 20901",
        "status": "working_paper",
        "areas": ["algorithmic-pricing-and-competition"],
        "tags": ["algorithm development", "large language models", "contractors", "pricing algorithms"],
        "summary": "Pricing algorithms produced by contractors and LLMs are mostly supervised-learning routines; economics prompts improve contractor algorithms but can raise LLM prices through demand-estimation mistakes.",
        "abstract": "Algorithmic pricing is widely deployed across many markets, but firms rarely write their own algorithms; they commission them from third-party developers or potentially generate them through large language models. We study pricing algorithms commissioned from Upwork programmers and generated by two LLMs dominant through mid-2025. Across 225 generated algorithms, none uses reinforcement learning. Most are supervised-learning algorithms that predict prices directly from observables. An economic-fundamentals prompt improves the efficiency of contractor algorithms but raises LLM prices above the competitive benchmark by pushing LLMs toward misspecified demand estimation.",
        "main_finding": "Most commissioned and LLM-generated pricing algorithms are supervised-learning routines; economic prompts improve contractor algorithms but can push LLMs toward pricing mistakes that raise prices.",
        "policy_relevance": "Firms' delegation of algorithm design affects competitive outcomes, so algorithmic-pricing policy should account for third-party contractors and LLM-generated code.",
        "links": [
            {"name": "Paper PDF", "url": "https://www.dropbox.com/scl/fi/sr2pxijusnesgvh6bpojc/AI_Pricing_Delegation.pdf?rlkey=yvqoojtusionvatx95vdk1oc0&st=4lvo77v4&dl=0"},
            {"name": "CEPR Discussion Paper", "url": "https://cepr.org/publications/dp20901"},
            {"name": "Earlier SSRN Version", "url": "https://ssrn.com/abstract=3798847"},
        ],
        "bibkey": "ershov2025outsourcing",
    },
    {
        "slug": "expansion-influencer-advertising-ncaa-nil",
        "title": "Expansion of Influencer Advertising: Evidence from the NCAA NIL Policy",
        "date": "2026-01-01",
        "authors": ["Daniel Ershov", "Marit Hinnosaar", "Jiewei Li"],
        "publication_types": ["report"],
        "publication": "Working paper",
        "status": "working_paper",
        "areas": ["influencer-marketing-and-disclosure", "digital-platforms-and-online-markets"],
        "tags": ["influencer advertising", "NCAA", "NIL policy", "social media"],
        "summary": "Studies how the NCAA name, image, and likeness policy expanded influencer advertising opportunities and changed sponsored social media activity.",
        "abstract": "This project studies how the NCAA name, image, and likeness policy expanded influencer advertising opportunities and changed the market for sponsored social media activity.",
        "links": [],
        "bibkey": "ershov2026nil",
    },
    {
        "slug": "learned-complementarity",
        "title": "Learned Complementarity",
        "date": "2024-11-14",
        "authors": ["Daniel Ershov", "Max J. Pachali", "Adam N. Smith"],
        "publication_types": ["report"],
        "publication": "Working paper",
        "status": "working_paper",
        "areas": ["demand-estimation-and-market-structure"],
        "tags": ["learned complementarity", "demand for bundles", "consumer learning", "quantitative marketing"],
        "summary": "Consumer complementarity in DIY home improvement purchases grows with category experience, creating measurable value from moving along the learning path.",
        "abstract": "Product substitution patterns are often treated as static. This paper studies dynamic complementarity in DIY home improvement purchases, documents that co-purchase likelihood rises with category experience, and estimates a model in which consumers sequentially realize super-additive utility from co-consumption over time. The estimates reveal substantial heterogeneity in substitution patterns within and across households, and the economic value of moving one step on the path of learned complementarity is roughly $1, about 5% of the average purchase price in the data.",
        "main_finding": "Complementarity rises with category experience, and moving one step along the learned-complementarity path is worth roughly $1, about 5% of the average purchase price.",
        "links": [
            {"name": "SSRN", "url": "https://ssrn.com/abstract=4925803"},
        ],
        "bibkey": "ershov2024learned",
    },
    {
        "slug": "competing-superstars-mobile-app-market",
        "title": "Competing with Superstars in the Mobile App Market",
        "date": "2022-03-01",
        "authors": ["Daniel Ershov"],
        "publication_types": ["report"],
        "publication": "NET Institute Working Paper 18-02",
        "status": "resting",
        "areas": ["digital-platforms-and-online-markets"],
        "tags": ["mobile apps", "entry", "product quality", "competition"],
        "summary": "The surprise emergence of superstar mobile games increases entry in some niches, lowers entrant quality, intensifies price competition, and induces incumbents to raise quality.",
        "abstract": "Firms in many markets face demand uncertainty when deciding where to enter new products. The appearance of a popular competitor, or superstar, resolves part of this demand uncertainty and can expand demand, but it also intensifies competition. Using Google Play Store mobile game data and the surprise emergence of superstar products for identification, I show that entry increases in niches where a superstar appears unless those niches were already popular. New entrants reduce quality and price competition intensifies; incumbents respond by investing in higher quality.",
        "main_finding": "Superstar entry increases entry in previously less-popular niches, reduces new-entrant quality, intensifies price competition, and induces incumbents to raise quality.",
        "links": [
            {"name": "Paper PDF", "url": "http://www.netinst.org/Ershov_18-02.pdf"},
            {"name": "NET Institute Working Paper", "url": "https://www.netinst.org/Competing-with-Superstars-in-the-Mobile-App-Market/"},
        ],
        "bibkey": "ershov2022superstars",
    },
    {
        "slug": "estimating-effects-deregulation-ontario-wine",
        "title": "Estimating the Effects of Deregulation in the Ontario Wine Retail Market",
        "date": "2016-01-01",
        "authors": ["Daniel Ershov", "Victor Aguirregabiria", "Junichi Suzuki"],
        "publication_types": ["report"],
        "publication": "Resting paper",
        "status": "resting",
        "areas": ["demand-estimation-and-market-structure", "competition-policy"],
        "tags": ["deregulation", "wine retail", "spatial demand", "competition"],
        "summary": "A spatial demand model of Ontario wine retail evaluates how retail entry, product-range deregulation, and price competition affect consumption and welfare.",
        "abstract": "This paper studies the impact of competition in the Ontario wine market and evaluates alternative deregulation policies. Ontario's wine retail market combines the government-owned Liquor Control Board of Ontario and two private companies that can sell only a limited subset of Ontario wines and face restrictions on store numbers. The empirical analysis estimates a spatial demand model for differentiated products using LCBO store sales, prices, and product characteristics, then simulates deregulation proposals including retail competition, broader product ranges for private retailers, and price competition.",
        "main_finding": "Relative to a pure monopoly benchmark, entry by additional competitors increases consumption and consumer welfare; expanding existing competitors' product range also raises welfare while keeping consumption stable.",
        "policy_relevance": "Retail deregulation can affect consumer welfare through entry, assortment, and price competition, and these margins need to be evaluated separately.",
        "links": [
            {"name": "Paper PDF", "url": "https://drive.google.com/file/d/0B3Je5Po6VB4NRHFOdUo5LWpDcGs/view"},
        ],
        "bibkey": "ershov2016wine",
    },
]


def bibtex(pub: dict) -> str:
    year = pub["date"][:4]
    fields = {
        "title": pub["title"],
        "author": " and ".join(pub["authors"]),
        "year": year,
    }
    if pub["publication"]:
        fields["journal" if "journal_article" in pub["publication_types"] else "howpublished"] = pub["publication"]
    doi = None
    for link in pub["links"]:
        if link["url"].startswith("https://doi.org/"):
            doi = link["url"].replace("https://doi.org/", "")
    if doi:
        fields["doi"] = doi
    rows = [f"@article{{{pub['bibkey']},"]
    for key, value in fields.items():
        rows.append(f"  {key} = {{{value}}},")
    rows[-1] = rows[-1].rstrip(",")
    rows.append("}")
    return "\n".join(rows)


def front_matter(pub: dict) -> str:
    links = yaml_links(pub["links"])
    notes = yaml_list(pub.get("notes", []))
    return f"""---
title: {q(pub['title'])}
slug: {q(pub['slug'])}
date: {pub['date']}
authors: {qlist(pub['authors'])}
publication_types: {qlist(pub['publication_types'])}
publication: {q(pub['publication'])}
status: {q(pub['status'])}
areas: {qlist(pub['areas'])}
tags: {qlist(pub['tags'])}
summary: {q(pub.get('summary', pub['abstract']))}
abstract: {q(pub['abstract'])}
main_finding: {q(pub.get('main_finding', ''))}
policy_relevance: {q(pub.get('policy_relevance', ''))}
notes:
{notes}
links:
{links}
bibtex: {q(bibtex(pub))}
---
"""


def make_site() -> None:
    default_config = SITE / "hugo.toml"
    if default_config.exists():
        default_config.unlink()

    write("hugo.yaml", """
    baseURL: "/"
    title: "Daniel Ershov"
    languageCode: en-us
    defaultContentLanguage: en
    enableRobotsTXT: true

    module:
      imports:
        - path: github.com/HugoBlox/hugo-blox-builder/modules/blox-tailwind

    outputs:
      home: [HTML, RSS, JSON]

    params:
      description: "Daniel Ershov is an Assistant Professor in the Marketing & Analytics group at the UCL School of Management."
      author: "Daniel Ershov"
      appearance:
        theme_day: custom
        theme_night: custom
        color_mode: light
        font: native
        font_size: L
      header:
        navbar:
          enable: true
          show_search: true
          logo:
            text: "Daniel Ershov"
      features:
        search:
          provider: pagefind
      extensions:
        css:
          - css/custom.css

    taxonomies:
      tag: tags
      category: categories
      publication_type: publication_types

    permalinks:
      publication: /publication/:slug/
      talk: /talk/:slug/
      software: /software/:slug/

    menu:
      main:
        - name: CV
          url: /bio/
          weight: 10
        - name: Research
          url: /publication/
          weight: 20
        - name: People
          url: /authors/
          weight: 40
        - name: Presentations
          url: /talk/
          weight: 45
        - name: Teaching
          url: /teaching/
          weight: 50
        - name: Contact
          url: /contact/
          weight: 60

    markup:
      goldmark:
        renderer:
          unsafe: true
      tableOfContents:
        startLevel: 2
        endLevel: 3
    """)

    write("go.mod", """
    module github.com/danielershov/danielershov.github.io-site

    go 1.22

    require github.com/HugoBlox/hugo-blox-builder/modules/blox-tailwind v0.10.0
    """)

    write("package.json", """
    {
      "private": true,
      "scripts": {
        "build": "hugo --gc --minify",
        "pagefind": "pagefind --site public"
      },
      "devDependencies": {
        "pagefind": "^1.5.0"
      }
    }
    """)

    write("i18n/en.yaml", """
    - id: read_more
      translation: "Read"
    - id: download_pdf
      translation: "Download PDF"
    - id: publisher_version
      translation: "Publisher's Version"
    - id: cite
      translation: "Cite"
    - id: see_also
      translation: "See Also"
    """)

    write("data/profile.json", json.dumps({
        "name": "Daniel Ershov",
        "title": "Assistant Professor (Lecturer)",
        "institution": "UCL School of Management",
        "email": "d.ershov@ucl.ac.uk",
        "location": "London, United Kingdom",
        "orcid": "0000-0001-7989-2571",
        "intro": "Daniel Ershov is a quantitative marketing and empirical industrial organization researcher studying how digital technologies change competition, regulation, and market outcomes. He is an Assistant Professor in the Marketing & Analytics group at the UCL School of Management. His articles have appeared in the Journal of Political Economy, Marketing Science, American Economic Journal: Microeconomics, RAND Journal of Economics, The Economic Journal, International Journal of Industrial Organization, and Oxford Review of Economic Policy.",
        "links": [
            {"name": "Email", "url": "mailto:d.ershov@ucl.ac.uk"},
            {"name": "CV", "url": "files/DErshov_CV_SES_2026.pdf"},
            {"name": "UCL Profile", "url": "https://profiles.ucl.ac.uk/89002-daniel-ershov/about"},
            {"name": "CEPR", "url": "https://cepr.org/about/people/daniel-ershov"},
            {"name": "Google Scholar", "url": "https://scholar.google.com/citations?hl=en&user=VkzWG2YAAAAJ"},
            {"name": "Bluesky", "url": "https://bsky.app/profile/ershovd.bsky.social"},
            {"name": "LinkedIn", "url": "https://www.linkedin.com/in/daniel-ershov-355a22403/"},
            {"name": "X", "url": "https://x.com/ershov_daniel"},
        ],
    }, ensure_ascii=False, indent=2))

    write("data/research_areas.json", json.dumps({
        "areas": [
            {
                "slug": "algorithmic-pricing-and-competition",
                "title": "Algorithmic Pricing and Competition",
                "description": "Pricing algorithms, outsourced algorithm design, and the conditions under which algorithmic systems change competitive conduct.",
                "featured": [
                    "algorithmic-pricing-competition-german-retail-gasoline-market",
                    "outsourcing-algorithm-development-contractors-llms",
                    "autonomous-algorithmic-collusion"
                ],
                "subcategories": ["algorithmic pricing", "pricing algorithms", "competition policy"]
            },
            {
                "slug": "competition-policy",
                "title": "Competition Policy",
                "description": "Research on market regulation, auction design, innovation incentives, and the empirical basis for competition policy.",
                "featured": [
                    "interaction-spectrum-auctions-mobile-market-competition",
                    "market-incentives-business-innovation-canada"
                ],
                "subcategories": ["competition policy", "market regulation", "spectrum auctions", "innovation"]
            },
            {
                "slug": "digital-platforms-and-online-markets",
                "title": "Digital Platforms and Online Markets",
                "description": "Empirical work on search, entry, congestion, matching, and information frictions in online markets.",
                "featured": [
                    "variety-based-congestion-online-markets",
                    "what-happens-when-dating-goes-online",
                    "sharing-news-left-right",
                    "competing-superstars-mobile-app-market"
                ],
                "subcategories": ["platforms", "online markets", "mobile apps", "matching"]
            },
            {
                "slug": "influencer-marketing-and-disclosure",
                "title": "Influencer Marketing and Disclosure",
                "description": "Research on hidden advertising, disclosure regulation, and the changing supply of sponsored content on social media.",
                "featured": [
                    "how-much-influencer-marketing-undisclosed",
                    "effects-advertising-disclosure-regulations-social-media",
                    "expansion-influencer-advertising-ncaa-nil"
                ],
                "subcategories": ["influencer marketing", "advertising disclosure", "consumer protection"]
            },
            {
                "slug": "demand-estimation-and-market-structure",
                "title": "Demand Estimation and Market Structure",
                "description": "Demand estimation, complementarity, deregulation, and market design questions in differentiated-product markets.",
                "featured": [
                    "estimating-complementarity-large-choice-sets",
                    "learned-complementarity",
                    "estimating-effects-deregulation-ontario-wine"
                ],
                "subcategories": ["demand estimation", "complementarity", "deregulation", "innovation"]
            }
        ]
    }, ensure_ascii=False, indent=2))

    write("data/featured_publications.yaml", """
    - what-happens-when-dating-goes-online
    - outsourcing-algorithm-development-contractors-llms
    - learned-complementarity
    """)

    write("data/selected_publications.yaml", """
    - algorithmic-pricing-competition-german-retail-gasoline-market
    - how-much-influencer-marketing-undisclosed
    - effects-advertising-disclosure-regulations-social-media
    """)

    write("data/recent_working_papers.yaml", """
    - what-happens-when-dating-goes-online
    - outsourcing-algorithm-development-contractors-llms
    - expansion-influencer-advertising-ncaa-nil
    - learned-complementarity
    """)

    coauthors = {
        "Adam N. Smith": {"url": "https://www.adamnsmith.com/", "type": "website"},
        "David Salant": {"url": "https://scholar.google.com/citations?user=WbvHHLsAAAAJ&hl=en", "type": "profile"},
        "Elizabeth Lyons": {"url": "https://lizlyons.me/", "type": "website"},
        "Jean-François Houde": {"url": "https://jfhoude.econ.wisc.edu/", "type": "website"},
        "Jean-William P. Laliberté": {"url": "https://sites.google.com/view/jwlaliberte", "type": "website"},
        "Jessica Fong": {"url": "https://www.jessica-fong.com/", "type": "website"},
        "Juan S. Morales": {"url": "https://sites.google.com/view/jsmorales/juan-s-morales", "type": "website"},
        "Lei Xu": {"url": "https://leixu.org/", "type": "website"},
        "Marit Hinnosaar": {"url": "https://marit.hinnosaar.net/", "type": "website"},
        "Mathieu Marcoux": {"url": "https://marcouxmat.github.io/", "type": "website"},
        "Matthew Mitchell": {"url": "https://matthewmitchelltoronto.weebly.com/", "type": "website"},
        "Max J. Pachali": {"url": "https://sites.google.com/site/mjpachali/", "type": "website"},
        "Pinar Yildirim": {"url": "https://pinaryildirim.com/", "type": "website"},
        "Robert Clark": {"url": "https://sites.google.com/site/robertclark09site/", "type": "website"},
        "Scott Orr": {"url": "https://sites.google.com/site/pscottorr/papers", "type": "website"},
        "Stephan Seiler": {"url": "https://www.seilerstephan.com/", "type": "website"},
        "Stephanie Assad": {"url": "https://geds-sage.gc.ca/en/GEDS?dn=Q049U1RFUEhBTklFLkFTU0FEQENCLUJDLkdDLkNBLE9VPUEtQSxPVT1NRC1ERixPVT1NTVBCLURHRlBNLE9VPUNCQy1CQ0MsT1U9SVNFRC1JU0RFLE89R0MsQz1DQQ%3D%3D&pgid=015", "type": "profile"},
        "Victor Aguirregabiria": {"url": "https://sites.google.com/view/victoraguirregabiriaswebsite/home", "type": "website"},
        "Yanting He": {"url": "https://scholar.google.com/citations?user=MzzeVi0AAAAJ&hl=zh-CN", "type": "profile"},
    }
    write("data/coauthors.json", json.dumps(coauthors, ensure_ascii=False, indent=2))

    phd_students = [
        {"name": "Jacopo Bregolin", "placement": "University of Liverpool"},
        {"name": "Vatsala Shreeti", "placement": "Bank for International Settlements"},
        {"name": "Sarah Lemaire", "placement": "European Commission Joint Research Centre"},
        {"name": "Luise Eisfeld", "placement": "HEC Lausanne"},
        {"name": "Nicolas Martinez", "placement": "Cornerstone"},
        {"name": "Luca Bennati", "placement": "Bank of Mexico"},
        {"name": "Max Sandiumenge i Boy", "placement": "CREST"},
    ]
    write("data/phd_students.json", json.dumps(phd_students, ensure_ascii=False, indent=2))

    legacy_map = {"entries": {}}
    for pub in PUBLICATIONS:
        if pub["status"] == "published":
            tab = "articles"
        elif pub["status"] == "resting":
            tab = "resting-papers"
        elif pub["status"] in {"cepr_contribution", "policy"}:
            tab = "policy"
        else:
            tab = "working-papers"
        legacy_map["entries"][pub["slug"]] = {"tab": tab, "legacy": pub["status"]}
    write("data/writings_legacy_map.json", json.dumps(legacy_map, ensure_ascii=False, indent=2))

    write("content/_index.md", """
    ---
    title: "Daniel Ershov"
    type: landing
    ---
    """)

    write("content/publication/_index.md", """
    ---
    title: "Research"
    aliases:
      - /research/
      - /writings/
    ---
    Published articles, working papers, policy writing, and older working papers.
    """)

    for pub in PUBLICATIONS:
        write(f"content/publication/{pub['slug']}/index.md", front_matter(pub))

    write("content/bio/_index.md", """
    ---
    title: "Bio & C.V."
    page_class: "bio-cv-page"
    aliases:
      - /cv/
    ---

    Daniel Ershov is an Assistant Professor in the Marketing & Analytics group at the UCL School of Management. He is also a CEPR Research Affiliate, CESifo Research Network Affiliate, Associate Researcher at the Toulouse School of Economics, affiliated researcher at ANITI, and Research Associate at CRESSE.

    His research is in quantitative marketing and empirical industrial organization. He studies firm competition, market regulation, online markets, algorithmic pricing, influencer marketing, and digitization. His articles have appeared in the Journal of Political Economy, Marketing Science, American Economic Journal: Microeconomics, RAND Journal of Economics, The Economic Journal, International Journal of Industrial Organization, and Oxford Review of Economic Policy.

    Daniel received his Ph.D. in Economics from the University of Toronto, where his committee was Victor Aguirregabiria, Avi Goldfarb, and Heski Bar-Isaac. He also holds an M.Sc. in Economics from the London School of Economics and a B.Soc.Sc. Honours in Economics from the University of Ottawa.

    ## Current Positions and Affiliations

    - Assistant Professor (Lecturer), UCL School of Management, 2022-present
    - Associate Researcher, Toulouse School of Economics, 2022-present
    - Research Affiliate, CEPR, 2021-present
    - Research Affiliate, CESifo, 2019-present
    - Affiliated Researcher, ANITI, 2020-present
    - Research Associate, CRESSE, 2024-present

    ## Employment History

    - Assistant Professor (Lecturer), UCL School of Management, July 2022-present
    - Visiting Lecturer, Imperial College Business School, January 2022-July 2022
    - Assistant Professor (Junior Chair), Toulouse School of Economics, 2017-2022
    - Economist, Government of Canada, 2009-2012

    ## Education

    - Ph.D. in Economics, University of Toronto, 2017
    - M.Sc. in Economics, London School of Economics, 2009
    - B.Soc.Sc. Honours in Economics, summa cum laude, University of Ottawa, 2008

    ## Awards

    - Best Paper Award, Association of Competition Economists, 2025
    - CESifo Distinguished Affiliate Award, 2019
    - NET Institute Summer Grant, NYU Stern, 2018
    - Hartle Award, University of Toronto, 2018
    - Summer Institute for Field Experiments, University of Chicago, 2017
    - NBER Digitization PhD Workshop, Stanford University, 2015-2017
    - Ontario Graduate Scholarship, University of Toronto, 2015-2017
    - CRESSE Fellowship in Competition Policy, 2015
    - Joseph-Armand Bombardier CGS Doctoral Scholarship, SSHRC, 2012-2015
    - Highest degree GPA in Economics, University of Ottawa, 2008
    - Undergraduate Merit Scholarship, University of Ottawa, 2004-2008

    ## Students

    - Jacopo Bregolin, University of Liverpool
    - Vatsala Shreeti, Bank for International Settlements
    - Sarah Lemaire, European Commission Joint Research Centre
    - Luise Eisfeld, HEC Lausanne
    - Nicolas Martinez, Cornerstone
    - Luca Bennati, Bank of Mexico
    - Max Sandiumenge i Boy, CREST

    ## Professional Activities

    - Seminar Organizer, UCL School of Management Marketing & Analytics, 2025-2026
    - PhD Recruitment Head, UCL School of Management Marketing & Analytics, 2024-2025
    - EU Commission Expert Group on Data Access for Research under the DSA Article 40, 2023
    - Co-organizer, CEPR Virtual IO Seminar Series, 2020
    - Co-organizer, Virtual Digital Economy Seminar, 2020/21 and 2021/22
    - Co-organizer, TSE Digital Workshop, 2018/19, 2019/20, and 2020/21
    - Co-organizer, TSE Digital Economics Conference, 2019-2022
    - TSE Placement Committee, 2019/2020 and 2020/2021

    ## Refereeing

    Econometrica; Review of Economic Studies; American Economic Review; Journal of Political Economy; Marketing Science; Management Science; Quantitative Marketing & Economics; RAND Journal of Economics; MIS Quarterly; Journal of the European Economic Association; American Economic Journal: Microeconomics; The Economic Journal; JPE: Microeconomics; Journal of Industrial Economics; Review of Industrial Organization; International Journal of Industrial Organization; European Economic Review; Economic Inquiry; International Economic Review; Information Economics and Policy.

    ## C.V.

    [Download the current C.V.]({{< staticrel "files/DErshov_CV_SES_2026.pdf" >}})

    Current PDF: June 2026.
    """)

    write("content/teaching/_index.md", """
    ---
    title: "Teaching"
    ---

    ## UCL School of Management

    - Managerial Applications of AI, undergraduate
    - Machine Learning and AI for Marketing Science, MSc
    - International Strategy, undergraduate
    - Extended Project / Undergraduate Dissertation, undergraduate

    ## Imperial College Business School

    - PhD Course on Algorithms and Econometrics
    - Industrial Organization, undergraduate

    ## Toulouse School of Economics

    - Empirical Industrial Organization, PhD
    - Topics in Applied Industrial Organization, M2
    - Economics of the Internet / Digital Economics, M2
    - Applied Econometrics, M1
    - Executive Education

    ## University of Toronto

    - Empirical Industrial Organization, undergraduate
    """)

    write("content/contact/_index.md", """
    ---
    title: "Contact"
    ---

    Daniel Ershov  
    UCL School of Management  
    1 Canada Square  
    London E14 5AB  
    United Kingdom

    Email: [d.ershov@ucl.ac.uk](mailto:d.ershov@ucl.ac.uk)

    - [UCL profile](https://profiles.ucl.ac.uk/89002-daniel-ershov/about)
    - [CEPR profile](https://cepr.org/about/people/daniel-ershov)
    - [Google Scholar](https://scholar.google.com/citations?hl=en&user=VkzWG2YAAAAJ)
    - [Bluesky](https://bsky.app/profile/ershovd.bsky.social)
    - [LinkedIn](https://www.linkedin.com/in/daniel-ershov-355a22403/)
    - [Twitter / X](https://x.com/ershov_daniel)
    """)

    write("content/authors/_index.md", """
    ---
    title: "People"
    aliases:
      - /people/
    ---

    Daniel's research is collaborative. This page lists coauthors represented in the research on this site and PhD students with placements.

    <!-- Review unlinked co-author names before publication. Links in data/coauthors.json were resolved by best-effort web search and should be checked by the owner. -->
    """)

    write("content/research-areas/_index.md", """
    ---
    title: "Research Areas"
    ---

    Daniel's research spans five connected areas. The [Research]({{< staticrel "publication/" >}}) page lets you filter papers by these areas.

    ## Algorithmic Pricing and Competition

    Pricing algorithms, outsourced algorithm design, and the conditions under which algorithmic systems change competitive conduct.

    ## Competition Policy

    Market regulation, spectrum auctions, innovation incentives, and the empirical basis for competition policy.

    ## Digital Platforms and Online Markets

    Search, entry, congestion, matching, and information frictions in online markets.

    ## Influencer Marketing and Disclosure

    Hidden advertising, disclosure regulation, and the changing supply of sponsored content on social media.

    ## Demand Estimation and Market Structure

    Demand estimation, complementarity, deregulation, and market design questions in differentiated-product markets.
    """)

    write("content/software/_index.md", """
    ---
    title: "Replication and Code"
    ---

    Public replication packages and code are linked from individual paper pages when available.

    - [The Effects of Advertising Disclosure Regulations on Social Media]({{< staticrel "publication/effects-advertising-disclosure-regulations-social-media/" >}}): OpenICPSR replication package.
    - [Variety-Based Congestion in Online Markets]({{< staticrel "publication/variety-based-congestion-online-markets/" >}}): OpenICPSR replication package.
    - [Algorithmic Pricing and Competition]({{< staticrel "publication/algorithmic-pricing-competition-german-retail-gasoline-market/" >}}): data appendix.
    """)

    write("content/talk/_index.md", """
    ---
    title: "Presentations"
    aliases:
      - /presentation/
      - /presentations/
    ---

    Selected seminars, workshops, and conference presentations.

    ## 2026

    - University of Liverpool
    - Markets & Waves

    ## 2025

    - UCLA Anderson, postponed
    - London Quantitative Marketing Workshop
    - NABE TEC Europe
    - University of London Workshop on Competition and Regulation in Digital Markets
    - Koç University
    - Association of Competition Economists Conference

    ## 2024

    - Competition and Markets Authority
    - Yelp
    - Frontier Economics
    - University of London Workshop on Competition and Regulation in Digital Markets
    - Oxford
    - Copenhagen

    ## 2023

    - LSE
    - Keystone
    - Amazon
    - City, University of London Workshop on Competition and Regulation in Digital Markets
    - Quantitative Marketing and Economics, discussant
    - CEPR Workshop on Digital Mergers
    - Israeli IO Day, cancelled

    ## 2022

    - Indian School of Business
    - Norwich DigEcon Workshop
    - ENSAI Economic Days Workshop
    - FCC

    ## 2021

    - CEPR Virtual IO Seminar
    - Bocconi
    - Virtual Quantitative Marketing Seminar
    - Padova
    - UCLA Anderson Marketing
    - Chicago Booth Marketing
    - Stanford
    - Stockholm School of Economics
    - Imperial College Marketing
    - EARIE
    - QME
    - Bank of Colombia
    - Cambridge Judge
    - UCL School of Management
    - Queen's Smith Business School
    - eQMS
    - APIOC

    ## 2020

    - University of East Anglia
    - LSE, cancelled
    - University of Bologna
    - IO²
    - Oxford Consumer Search and Digital Platforms Workshop, cancelled
    - ACM-EC
    - NBER Economics of AI
    - TSE Digital Workshop
    - Telecom Paris
    - Tel Aviv Coller
    - CESifo Economics of Digitization
    - University of Amsterdam Conference on Algorithmic Collusion
    - FTC

    ## 2019

    - TSE Digital Economics Conference
    - Imperial College
    - TSE Food Economics Conference
    - MaCCI Summer Institute
    - CESifo Economics of Digitization
    - Israeli IO Day

    ## 2018

    - CEMFI
    - TSE Digital Workshop
    - CSIO-IDEI Workshop
    - Canadian Economics Association
    - Université de Montréal
    - BECCLE Competition Policy Conference
    - TSE Food Economics Workshop
    - Barcelona GSE Summer Forum Digital Economics Workshop
    - UCL School of Management
    - CREST/ECODEC Workshop
    - Telecom Paris
    - NET Institute Conference

    ## 2017

    - Toulouse School of Economics
    - Sciences Po
    - Tilburg
    - Ryerson
    - Bank of Canada
    - IIOC
    - 8th Annual Consumer Search and Switching Costs Workshop
    - 8th Annual Searle Internet Commerce Conference
    - University of Toronto
    - CRESSE
    - EARIE
    - Jornadas de Economia Industrial
    - Trento
    - Mannheim

    ## 2016

    - University of Toronto
    - KU Leuven
    - Canadian Economics Association
    - Jornadas de Economia Industrial
    - EARIE
    """)

    write("assets/css/custom.css", CSS)
    write("layouts/baseof.html", BASEOF)
    write("layouts/_partials/components/headers/navbar.html", NAVBAR)
    write("layouts/_partials/components/search-modal.html", SEARCH_MODAL)
    write("layouts/_partials/site_footer.html", FOOTER)
    write("layouts/_partials/related_finder.html", RELATED)
    write("layouts/_default/list.html", DEFAULT_LIST)
    write("layouts/_default/single.html", DEFAULT_SINGLE)
    write("layouts/landing/list.html", LANDING)
    write("layouts/publication/list.html", PUBLICATION_LIST)
    write("layouts/publication/single.html", PUBLICATION_SINGLE)
    write("layouts/authors/list.html", AUTHORS_LIST)
    write("layouts/talk/list.html", SIMPLE_SECTION_LIST)
    write("layouts/software/list.html", SIMPLE_SECTION_LIST)
    write("layouts/shortcodes/staticrel.html", "{{- (.Get 0) | relURL -}}\n")
    write("layouts/index.json", INDEX_JSON)
    write("layouts/404.html", NOT_FOUND)

    write_repo(".github/workflows/deploy.yml", DEPLOY)
    write_repo(".gitignore", """
    hugo-site/public/
    hugo-site/resources/_gen/
    hugo-site/.hugo_build.lock
    hugo-site/node_modules/
    hugo-site/_vendor/
    preview/
    .DS_Store
    """)
    write_repo("UPDATING.md", UPDATING)
    write_repo("WEBSITE_PRINCIPLES.md", PRINCIPLES)

    files_dir = SITE / "static" / "files"
    files_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SOURCE / "DErshov_CV_SES_2026.pdf", files_dir / "DErshov_CV_SES_2026.pdf")

    logo_dir = SITE / "static" / "images"
    logo_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SOURCE / "logo_white.png", logo_dir / "ucl-school-management-light.png")
    shutil.copy2(SOURCE / "logo_purple.png", logo_dir / "ucl-school-management-dark.png")

    make_images()


CSS = r"""
:root {
  --color-bg: #fafafa;
  --color-surface: #f4edfb;
  --color-surface-strong: #eedeff;
  --color-text: #26173a;
  --color-text-muted: #604d73;
  --color-accent: #361a54;
  --color-accent-bright: #993bff;
  --color-accent-mid: #ba82ff;
  --color-institution: #361a54;
  --color-link: #361a54;
  --color-link-hover: #741cff;
  --color-border: #ddbdff;
  --color-focus: #30d6ff;
  --content-width: 1200px;
  --header-height: 72px;
}

html,
html.dark,
.dark {
  background: var(--color-bg) !important;
  color: var(--color-text) !important;
  color-scheme: light !important;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  background: var(--color-bg);
  color: var(--color-text);
  font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 16px;
  line-height: 1.55;
}

a {
  color: var(--color-link);
  text-decoration-thickness: 1px;
  text-underline-offset: 0.16em;
}

a:hover {
  color: var(--color-link-hover);
}

img {
  max-width: 100%;
  height: auto;
}

.skip-link {
  position: absolute;
  top: -100px;
  left: 16px;
  z-index: 100;
  background: var(--color-text);
  color: var(--color-bg);
  padding: 0.65rem 0.8rem;
  border-radius: 6px;
}

.skip-link:focus {
  top: 14px;
}

:focus-visible {
  outline: 3px solid var(--color-focus);
  outline-offset: 3px;
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

.site-header {
  position: sticky;
  top: 0;
  z-index: 50;
  background: rgba(250, 250, 250, 0.96);
  border-bottom: 1px solid var(--color-border);
  backdrop-filter: blur(10px);
}

.nav-inner {
  max-width: var(--content-width);
  margin: 0 auto;
  min-height: var(--header-height);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 18px;
  gap: 24px;
}

.site-brand {
  color: var(--color-accent);
  font-weight: 800;
  text-transform: uppercase;
  text-decoration: none;
  letter-spacing: 0;
  white-space: nowrap;
}

.nav-actions {
  display: flex;
  align-items: center;
  gap: 18px;
}

.nav-links {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 18px;
}

.nav-links a {
  color: var(--color-text);
  font-size: 0.94rem;
  text-decoration: none;
}

.nav-links a:hover,
.nav-links a[aria-current="page"] {
  color: var(--color-accent-bright);
}

.icon-button,
.hamburger {
  border: 0;
  background: transparent;
  color: var(--color-text);
  padding: 6px;
  line-height: 0;
  cursor: pointer;
}

.hamburger {
  display: none;
}

.page-shell,
.section-wrap {
  max-width: var(--content-width);
  margin: 0 auto;
  padding: 36px 18px;
}

.prose {
  max-width: 830px;
}

.prose p {
  margin-bottom: 1.25em;
}

.prose h1,
.prose h2,
.prose h3 {
  line-height: 1.2;
  margin: 1.6em 0 0.55em;
}

.prose h1 {
  font-size: clamp(2rem, 4vw, 3.2rem);
  margin-top: 0;
}

.prose h2 {
  font-size: 1.45rem;
}

.prose h3 {
  font-size: 1.1rem;
}

.bio-cv-page {
  max-width: 980px;
}

.bio-cv-page h1 {
  color: var(--color-accent);
}

.bio-cv-page > p:first-of-type {
  border-left: 6px solid var(--color-accent);
  background: var(--color-surface);
  border-radius: 8px;
  padding: 18px 20px;
}

.bio-cv-page h2 {
  border-top: 1px solid var(--color-border);
  color: var(--color-accent);
  padding-top: 1rem;
}

.bio-cv-page ul {
  list-style: none;
  padding: 0;
  margin: 0 0 1.5rem;
  display: grid;
  gap: 8px;
}

.bio-cv-page li {
  border: 1px solid var(--color-border);
  border-radius: 8px;
  background: #fff;
  padding: 10px 12px;
}

.bio-cv-page h2 + p {
  border: 1px solid var(--color-border);
  border-radius: 8px;
  background: #fff;
  padding: 12px;
}

.hero {
  display: grid;
  grid-template-columns: 240px minmax(0, 1fr);
  align-items: start;
  gap: 48px;
  padding-top: 54px;
  padding-bottom: 42px;
}

.hero-photo {
  width: 200px;
  height: 200px;
  border-radius: 999px;
  object-fit: cover;
  border: 5px solid var(--color-surface-strong);
  box-shadow: 0 12px 30px rgba(54, 26, 84, 0.18);
}

.ucl-mark {
  display: inline-flex;
  width: min(230px, 100%);
  line-height: 0;
  margin-bottom: 1.1rem;
}

.ucl-logo {
  display: block;
  width: 100%;
  height: auto;
}

.hero h1 {
  font-size: clamp(2.4rem, 5vw, 4.4rem);
  line-height: 1.05;
  margin: 0 0 0.45rem;
}

.hero .kicker {
  color: var(--color-accent);
  font-weight: 700;
  margin: 0 0 0.35rem;
}

.hero .institution {
  color: var(--color-text-muted);
  margin: 0 0 1.1rem;
}

.hero .intro {
  max-width: 820px;
  font-size: 1.08rem;
}

.hero-secondary-links {
  display: flex;
  flex-wrap: wrap;
  gap: 8px 16px;
  margin-top: 0.85rem;
  color: var(--color-text-muted);
  font-size: 0.95rem;
}

.hero-secondary-links a {
  color: var(--color-accent);
  font-weight: 700;
}

.button-row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 1.3rem;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 40px;
  padding: 0.58rem 0.85rem;
  border: 1px solid var(--color-accent);
  border-radius: 7px;
  font-weight: 700;
  text-decoration: none;
  transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
}

.btn-primary {
  background: var(--color-accent);
  color: #fafafa;
}

.btn-secondary {
  color: var(--color-accent);
  background: transparent;
}

.btn-chip {
  border-color: var(--color-border);
  color: var(--color-text);
  background: var(--color-surface);
  font-size: 0.9rem;
}

.btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 22px rgba(54, 26, 84, 0.16);
}

.home-section {
  border-top: 1px solid var(--color-border);
  padding-top: 34px;
}

.section-head {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 16px;
}

.section-head h2 {
  margin: 0;
}

.paper-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 14px;
}

.paper-card {
  display: flex;
  flex-direction: column;
  min-height: 240px;
  border: 1px solid var(--color-border);
  border-radius: 8px;
  background: #fff;
  padding: 16px;
}

.paper-card .paper-type {
  color: var(--color-accent-bright);
  font-size: 0.78rem;
  font-weight: 800;
  text-transform: uppercase;
}

.paper-card .paper-title {
  display: block;
  color: var(--color-text);
  font-weight: 850;
  margin: 0.45rem 0 0.4rem;
  text-decoration: none;
}

.paper-card .paper-meta {
  color: var(--color-text-muted);
  font-size: 0.9rem;
}

.paper-summary {
  color: var(--color-text);
  font-size: 0.92rem;
  line-height: 1.45;
  margin: 0.75rem 0 0;
}

.paper-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 8px 12px;
  margin-top: auto;
  padding-top: 0.8rem;
  font-size: 0.84rem;
  font-weight: 700;
}

.paper-actions a {
  color: var(--color-accent);
}

.policy-grid {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

#research-areas {
  scroll-margin-top: calc(var(--header-height) + 18px);
}

.research-areas {
  border-top: 1px solid var(--color-border);
  padding-top: 34px;
}

.accordion {
  display: grid;
  gap: 12px;
}

.area-panel {
  border: 1px solid var(--color-border);
  border-radius: 8px;
  background: var(--color-surface);
  overflow: clip;
}

.area-panel summary {
  cursor: pointer;
  padding: 18px 20px;
  font-weight: 800;
  color: var(--color-text);
}

.area-body {
  padding: 0 20px 20px;
}

.area-body p {
  color: var(--color-text-muted);
  margin-top: 0;
}

.compact-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.compact-list li {
  padding: 8px 0;
  border-top: 1px solid var(--color-border);
}

.pub-tabs {
  position: sticky;
  top: var(--header-height);
  z-index: 20;
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  padding: 12px 0;
  background: var(--color-bg);
  border-bottom: 1px solid var(--color-border);
  box-shadow: 0 6px 14px rgba(54, 26, 84, 0.05);
}

.tab-btn {
  border: 1px solid transparent;
  border-radius: 999px;
  background: transparent;
  color: var(--color-text);
  padding: 0.5rem 0.75rem;
  cursor: pointer;
  font-weight: 700;
}

.tab-btn.active {
  border-color: var(--color-accent);
  color: var(--color-accent);
  background: var(--color-surface-strong);
}

.writings-grid {
  display: grid;
  grid-template-columns: 260px minmax(0, 1fr);
  gap: 30px;
  align-items: start;
  margin-top: 22px;
}

.filters {
  position: sticky;
  top: calc(var(--header-height) + 72px);
  border: 1px solid var(--color-border);
  border-radius: 8px;
  background: var(--color-surface);
  padding: 16px;
}

.filters-summary {
  display: none;
  cursor: pointer;
  font-weight: 800;
  color: var(--color-accent);
}

.filters label,
.filter-label {
  display: block;
  color: var(--color-text-muted);
  font-size: 0.88rem;
  font-weight: 700;
  margin: 0.85rem 0 0.35rem;
}

.filters input[type="search"],
.filters select {
  width: 100%;
  border: 1px solid var(--color-border);
  border-radius: 6px;
  background: #fff;
  color: var(--color-text);
  padding: 0.52rem 0.6rem;
}

.checkbox-list {
  max-height: 200px;
  overflow: auto;
  display: grid;
  gap: 6px;
  padding: 4px 0;
}

.check-row {
  display: flex;
  align-items: center;
  gap: 8px;
  line-height: 1.2;
  color: var(--color-text);
  font-size: 0.92rem;
}

.check-row input {
  margin: 0;
  flex: 0 0 auto;
}

.pub-toolbar {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 12px;
  align-items: center;
  margin-bottom: 10px;
}

.result-count {
  color: var(--color-text-muted);
  font-size: 0.92rem;
}

.pub-list {
  border-top: 1px solid var(--color-border);
}

.pub-item,
.pub-list-item {
  display: block;
  padding: 10px 0;
  border-bottom: 1px solid var(--color-border);
}

.pub-citation {
  line-height: 1.35;
}

.pub-citation .authors,
.pub-citation .venue,
.pub-citation .meta {
  color: var(--color-text-muted);
  font-size: 0.9rem;
}

.pub-citation .title {
  font-weight: 800;
  color: var(--color-text);
  text-decoration: none;
}

.pub-citation .title:hover {
  color: var(--color-link-hover);
}

.pub-summary {
  color: var(--color-text);
  font-size: 0.94rem;
  line-height: 1.45;
  margin: 0.5rem 0 0;
}

.pub-links {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 1rem;
}

.pub-links-inline {
  margin-top: 0.65rem;
}

.publication-detail {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 270px;
  gap: 34px;
  align-items: start;
}

.metadata-card,
.gk-see-also {
  border: 1px solid var(--color-border);
  background: var(--color-surface);
  border-radius: 8px;
  padding: 16px;
}

.metadata-card dl {
  margin: 0;
}

.metadata-card dt {
  font-size: 0.78rem;
  color: var(--color-text-muted);
  font-weight: 800;
  text-transform: uppercase;
  margin-top: 0.8rem;
}

.metadata-card dt:first-child {
  margin-top: 0;
}

.metadata-card dd {
  margin: 0.15rem 0 0;
}

.gk-see-also {
  margin-top: 28px;
}

.gk-see-also h2 {
  margin-top: 0;
  font-size: 1.1rem;
}

.gk-see-also ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.gk-see-also li {
  padding: 7px 0;
  border-top: 1px solid var(--color-border);
}

.kind-label {
  color: var(--color-accent);
  font-weight: 800;
  font-size: 0.82rem;
  margin-right: 0.35rem;
}

.people-list {
  columns: 2;
  column-gap: 42px;
  list-style: none;
  padding: 0;
}

.people-list li {
  break-inside: avoid;
  padding: 6px 0;
}

.person-meta {
  color: var(--color-text-muted);
  font-size: 0.9rem;
}

.search-modal {
  position: fixed;
  inset: 0;
  z-index: 90;
  display: none;
  align-items: flex-start;
  justify-content: center;
  padding: 10vh 18px 18px;
  background: rgba(54, 26, 84, 0.42);
}

.search-modal.open {
  display: flex;
}

.search-panel {
  width: min(760px, 100%);
  background: var(--color-bg);
  border: 1px solid var(--color-border);
  border-radius: 8px;
  box-shadow: 0 24px 70px rgba(54, 26, 84, 0.24);
  padding: 18px;
}

.search-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
}

#search-input {
  width: 100%;
  border: 1px solid var(--color-border);
  border-radius: 6px;
  padding: 0.7rem 0.8rem;
}

.search-results {
  margin-top: 14px;
  max-height: 55vh;
  overflow: auto;
}

.search-result {
  padding: 10px 0;
  border-top: 1px solid var(--color-border);
}

.site-footer {
  margin-top: 40px;
  background: var(--color-accent);
  color: #fafafa;
}

.footer-inner {
  max-width: var(--content-width);
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 18px;
  padding: 24px 18px;
  align-items: end;
}

.footer-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
}

.footer-ucl {
  display: inline-flex;
  width: 170px;
  line-height: 0;
  justify-self: end;
}

.site-footer a {
  color: #fafafa;
}

.credit {
  font-size: 0.82rem;
  color: #ddbdff;
  text-align: right;
}

.theme-toggle,
button[accesskey="t"] {
  display: none !important;
}

@media (max-width: 760px) {
  .nav-inner {
    display: grid;
    grid-template-columns: 1fr auto auto;
    padding: 14px;
  }

  .nav-actions {
    display: contents;
  }

  .site-brand {
    grid-column: 1;
  }

  .icon-button {
    grid-column: 2;
    justify-self: end;
  }

  .hamburger {
    display: inline-flex;
    grid-column: 3;
    justify-self: end;
  }

  .nav-links {
    display: none;
    position: static;
    grid-column: 1 / -1;
    width: 100%;
    flex-direction: column;
    align-items: stretch;
    gap: 0;
    padding: 8px 0 0;
    background: var(--color-bg);
  }

  .nav-links.open {
    display: flex;
  }

  .nav-links a {
    padding: 12px 0;
    border-top: 1px solid var(--color-border);
  }

  .hero {
    grid-template-columns: 1fr;
    gap: 16px;
    text-align: left;
    justify-items: start;
    padding-top: 28px;
    padding-bottom: 26px;
  }

  .hero h1 {
    font-size: 2.4rem;
  }

  .hero .intro {
    font-size: 1rem;
  }

  .ucl-mark {
    width: min(190px, 100%);
    margin-bottom: 0.8rem;
  }

  .button-row {
    justify-content: flex-start;
  }

  .writings-grid,
  .publication-detail {
    grid-template-columns: 1fr;
  }

  .section-head {
    align-items: flex-start;
    flex-direction: column;
  }

  .paper-grid {
    grid-template-columns: 1fr;
  }

  .filters {
    position: static;
    padding: 0;
  }

  .filters-summary {
    display: block;
    padding: 14px 16px;
  }

  .filters-body {
    border-top: 1px solid var(--color-border);
    padding: 0 16px 16px;
  }

  .people-list {
    columns: 1;
  }

  .footer-inner {
    grid-template-columns: 1fr;
  }

  .footer-ucl {
    justify-self: start;
  }

  .credit {
    text-align: left;
  }
}

@media (max-width: 640px) {
  .pub-tabs {
    top: 60px;
  }

  .hero-photo {
    width: 136px;
    height: 136px;
  }

  .publication-detail img {
    float: none;
    width: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    scroll-behavior: auto !important;
    transition: none !important;
  }

  .btn:hover {
    transform: none;
  }
}
"""


BASEOF = r"""
<!doctype html>
<html lang="{{ .Site.LanguageCode | default "en" }}">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ if .IsHome }}{{ .Site.Title }}{{ else }}{{ .Title }} | {{ .Site.Title }}{{ end }}</title>
    <meta name="description" content="{{ with .Params.description }}{{ . }}{{ else }}{{ .Site.Params.description }}{{ end }}">
    {{ $css := resources.Get "css/custom.css" | minify | fingerprint }}
    <link rel="stylesheet" href="{{ $css.RelPermalink }}">
    <link rel="icon" href="{{ "favicon.ico" | relURL }}">
    <link rel="icon" type="image/png" sizes="32x32" href="{{ "favicon-32x32.png" | relURL }}">
    <link rel="apple-touch-icon" href="{{ "apple-touch-icon.png" | relURL }}">
  </head>
  <body>
    <a class="skip-link" href="#main-content">Skip to content</a>
    {{ partial "components/headers/navbar.html" . }}
    <main id="main-content">
      {{ block "main" . }}{{ end }}
    </main>
    {{ partial "components/search-modal.html" . }}
    {{ partial "site_footer.html" . }}
  </body>
</html>
"""


NAVBAR = r"""
<header class="site-header">
  <div class="nav-inner">
    <a class="site-brand" href="{{ "/" | relURL }}">{{ upper (.Site.Params.header.navbar.logo.text | default .Site.Title) }}</a>
    <div class="nav-actions">
      <nav class="nav-links" id="site-menu" aria-label="Main navigation">
        {{ $current := .RelPermalink }}
        {{ range .Site.Menus.main }}
          {{ $url := .URL | relURL }}
          <a href="{{ $url }}" {{ if eq $current $url }}aria-current="page"{{ end }}>{{ .Name }}</a>
        {{ end }}
      </nav>
      <button class="icon-button js-search-open" type="button" aria-label="Search">
        <svg aria-hidden="true" width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="11" cy="11" r="8"></circle>
          <path d="m21 21-4.3-4.3"></path>
        </svg>
      </button>
      <button class="hamburger" type="button" aria-label="Menu" aria-controls="site-menu" aria-expanded="false">
        <svg aria-hidden="true" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M4 6h16M4 12h16M4 18h16"></path>
        </svg>
      </button>
    </div>
  </div>
</header>
<script>
(function() {
  var toggle = document.querySelector('.hamburger');
  var menu = document.querySelector('#site-menu');
  if (!toggle || !menu) return;
  toggle.addEventListener('click', function() {
    var open = menu.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
})();
</script>
"""


SEARCH_MODAL = r"""
<div class="search-modal" id="search-modal" role="dialog" aria-modal="true" aria-labelledby="search-title">
  <div class="search-panel">
    <div class="search-head">
      <h2 id="search-title">Search</h2>
      <button class="icon-button js-search-close" type="button" aria-label="Close search">
        <svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M18 6 6 18M6 6l12 12"></path>
        </svg>
      </button>
    </div>
    <input id="search-input" type="search" placeholder="Search Daniel Ershov's site" autocomplete="off">
    <div class="search-results" id="search-results" aria-live="polite"></div>
  </div>
</div>
<script>
(function() {
  var modal = document.getElementById('search-modal');
  var input = document.getElementById('search-input');
  var results = document.getElementById('search-results');
  var closeBtn = document.querySelector('.js-search-close');
  var openButtons = document.querySelectorAll('.js-search-open');
  var pagefind = null;
  var pagefindPromise = null;

  function openSearch() {
    modal.classList.add('open');
    setTimeout(function() { input.focus(); }, 0);
    loadPagefind();
  }

  function closeSearch() {
    modal.classList.remove('open');
    input.value = '';
    results.innerHTML = '';
  }

  function loadPagefind() {
    if (pagefind) return Promise.resolve(pagefind);
    if (pagefindPromise) return pagefindPromise;
    pagefindPromise = import('{{ "pagefind/pagefind.js" | relURL }}')
      .then(async function(mod) {
        pagefind = mod;
        await pagefind.options({ excerptLength: 22 });
        return pagefind;
      })
      .catch(function() {
        pagefind = null;
        return null;
      });
    return pagefindPromise;
  }

  async function doSearch(query) {
    if (!query) {
      results.innerHTML = '';
      return;
    }
    await loadPagefind();
    if (!pagefind) {
      results.innerHTML = '<p><a href="https://www.google.com/search?q=site%3Adanielershov.github.io+' + encodeURIComponent(query) + '">Search with Google</a></p>';
      return;
    }
    var search = await pagefind.search(query);
    var rows = await Promise.all(search.results.slice(0, 8).map(function(result) { return result.data(); }));
    results.innerHTML = rows.map(function(row) {
      return '<div class="search-result"><a href="' + row.url + '">' + row.meta.title + '</a><p>' + row.excerpt + '</p></div>';
    }).join('') || '<p>No results.</p>';
  }

  openButtons.forEach(function(btn) { btn.addEventListener('click', openSearch); });
  closeBtn.addEventListener('click', closeSearch);
  modal.addEventListener('click', function(event) { if (event.target === modal) closeSearch(); });
  document.addEventListener('keydown', function(event) {
    if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k') {
      event.preventDefault();
      openSearch();
    }
    if (event.key === 'Escape' && modal.classList.contains('open')) closeSearch();
  });
  input.addEventListener('input', function() { doSearch(input.value.trim()); });
})();
</script>
"""


FOOTER = r"""
<footer class="site-footer">
  <div class="footer-inner">
    <nav class="footer-nav" aria-label="Footer navigation">
      {{ range .Site.Menus.main }}
        <a href="{{ .URL | relURL }}">{{ .Name }}</a>
      {{ end }}
      <a href="mailto:{{ .Site.Data.profile.email }}">{{ .Site.Data.profile.email }}</a>
    </nav>
    <a class="footer-ucl" href="https://www.ucl.ac.uk/school-management/" aria-label="UCL School of Management">
      <img class="ucl-logo" src="{{ "images/ucl-school-management-dark.png" | relURL }}" width="300" height="140" alt="UCL School of Management">
    </a>
    <div class="credit">Created using <a href="https://garyking.org/mysite">GaryKing.org/mysite</a></div>
  </div>
</footer>
"""


DEFAULT_LIST = r"""
{{ define "main" }}
<section class="page-shell prose{{ with .Params.page_class }} {{ . }}{{ end }}">
  <h1>{{ .Title }}</h1>
  {{ .Content }}
</section>
{{ end }}
"""


DEFAULT_SINGLE = r"""
{{ define "main" }}
<article class="page-shell prose">
  <p><a href="{{ "/" | relURL }}">Home</a> / {{ .Title }}</p>
  <h1>{{ .Title }}</h1>
  {{ .Content }}
</article>
{{ end }}
"""


LANDING = r"""
{{ define "main" }}
{{ $profile := .Site.Data.profile }}
<section class="section-wrap hero">
  <img class="hero-photo" src="{{ "images/daniel-ershov.jpg" | relURL }}" width="200" height="200" alt="Portrait of Daniel Ershov, UCL School of Management">
  <div>
    <a class="ucl-mark" href="https://www.ucl.ac.uk/school-management/" aria-label="UCL School of Management">
      <img class="ucl-logo" src="{{ "images/ucl-school-management-light.png" | relURL }}" width="300" height="140" alt="UCL School of Management">
    </a>
    <p class="kicker">{{ $profile.title }}</p>
    <h1>{{ $profile.name }}</h1>
    <p class="institution">{{ $profile.institution }}</p>
    <p class="intro">{{ $profile.intro }}</p>
    <div class="button-row">
      <a class="btn btn-primary" href="{{ "publication/" | relURL }}">Research</a>
      <a class="btn btn-secondary" href="{{ "files/DErshov_CV_SES_2026.pdf" | relURL }}">Download CV</a>
      <a class="btn btn-secondary" href="mailto:{{ $profile.email }}">Email</a>
    </div>
    <div class="hero-secondary-links" aria-label="Profile links">
      <a href="{{ "bio/" | relURL }}">Bio</a>
      <a href="https://profiles.ucl.ac.uk/89002-daniel-ershov/about">UCL Profile</a>
      <a href="https://scholar.google.com/citations?hl=en&user=VkzWG2YAAAAJ">Google Scholar</a>
      <a href="https://cepr.org/about/people/daniel-ershov">CEPR</a>
    </div>
  </div>
</section>

<section class="section-wrap home-section">
  <div class="section-head">
    <h2>Selected Peer-Reviewed Publications</h2>
    <a class="btn btn-chip" href="{{ "publication/" | relURL }}#articles">All articles</a>
  </div>
  <div class="paper-grid">
    {{ range .Site.Data.selected_publications }}
      {{ with $.Site.GetPage (printf "/publication/%s" .) }}
        <article class="paper-card">
          <span class="paper-type">Publication</span>
          <a class="paper-title" href="{{ .RelPermalink }}">{{ .Title }}</a>
          <div class="paper-meta">{{ delimit .Params.authors ", " }}. {{ .Date.Format "2006" }}.<br>{{ .Params.publication }}</div>
          <p class="paper-summary">{{ .Params.summary }}</p>
          {{ with .Params.links }}
            <div class="paper-actions">
              {{ range first 3 . }}
                <a href="{{ .url }}">{{ .name }}</a>
              {{ end }}
            </div>
          {{ end }}
        </article>
      {{ end }}
    {{ end }}
  </div>
</section>

<section class="section-wrap home-section">
  <div class="section-head">
    <h2>Recent Working Papers</h2>
    <a class="btn btn-chip" href="{{ "publication/" | relURL }}#working-papers">All working papers</a>
  </div>
  <div class="paper-grid">
    {{ range .Site.Data.recent_working_papers }}
      {{ with $.Site.GetPage (printf "/publication/%s" .) }}
        <article class="paper-card">
          <span class="paper-type">Working paper</span>
          <a class="paper-title" href="{{ .RelPermalink }}">{{ .Title }}</a>
          <div class="paper-meta">{{ delimit .Params.authors ", " }}.<br>{{ .Params.publication }}</div>
          <p class="paper-summary">{{ .Params.summary }}</p>
          {{ with .Params.links }}
            <div class="paper-actions">
              {{ range first 3 . }}
                <a href="{{ .url }}">{{ .name }}</a>
              {{ end }}
            </div>
          {{ end }}
        </article>
      {{ end }}
    {{ end }}
  </div>
</section>

<section class="section-wrap home-section">
  <div class="section-head">
    <h2>Policy & Public Writing</h2>
    <a class="btn btn-chip" href="{{ "publication/" | relURL }}#policy">All policy writing</a>
  </div>
  <div class="paper-grid policy-grid">
    {{ $policy := where (where .Site.RegularPages "Section" "publication") "Params.status" "in" (slice "cepr_contribution" "policy") }}
    {{ range $policy.ByDate.Reverse }}
      <article class="paper-card">
        <span class="paper-type">Policy</span>
        <a class="paper-title" href="{{ .RelPermalink }}">{{ .Title }}</a>
        <div class="paper-meta">{{ delimit .Params.authors ", " }}. {{ .Date.Format "2006" }}.<br>{{ .Params.publication }}</div>
        <p class="paper-summary">{{ .Params.summary }}</p>
        {{ with .Params.links }}
          <div class="paper-actions">
            {{ range first 2 . }}
              <a href="{{ .url }}">{{ .name }}</a>
            {{ end }}
          </div>
        {{ end }}
      </article>
    {{ end }}
  </div>
</section>

<section class="section-wrap research-areas" id="research-areas">
  <h2>Research Areas</h2>
  <div class="accordion">
    {{ range $area := .Site.Data.research_areas.areas }}
      <details class="area-panel">
        <summary>{{ $area.title }}</summary>
        <div class="area-body">
          <p>{{ $area.description }}</p>
          <ul class="compact-list">
            {{ range first 5 $area.featured }}
              {{ with $.Site.GetPage (printf "/publication/%s" .) }}
                <li><a href="{{ .RelPermalink }}">{{ .Title }}</a><br><span class="pub-citation"><span class="venue">{{ .Params.publication }}</span></span></li>
              {{ end }}
            {{ end }}
          </ul>
          <div class="button-row">
            <a class="btn btn-chip" href="{{ "publication/" | relURL }}#area={{ $area.slug }}">View research</a>
          </div>
        </div>
      </details>
    {{ end }}
  </div>
</section>
{{ end }}
"""


PUBLICATION_LIST = r"""
{{ define "main" }}
{{ $pages := where .Site.RegularPages "Section" "publication" }}
<section class="page-shell">
  <div class="prose">
    <h1>{{ .Title }}</h1>
    {{ .Content }}
  </div>

  {{ $tabs := slice
    (dict "id" "all" "label" "All")
    (dict "id" "articles" "label" "Articles")
    (dict "id" "working-papers" "label" "Working Papers")
    (dict "id" "policy" "label" "Policy")
    (dict "id" "resting-papers" "label" "Older Working Papers")
  }}
  <nav class="pub-tabs" role="tablist" aria-label="Research filters">
    {{ range $tabs }}
      <button class="tab-btn" type="button" data-tab="{{ .id }}" role="tab" aria-selected="false">{{ .label }}</button>
    {{ end }}
  </nav>

  <div class="writings-grid">
    <details class="filters" id="research-filters" aria-label="Publication filters" open>
      <summary class="filters-summary">Filter research</summary>
      <div class="filters-body">
        <label for="pub-search">Search</label>
        <input id="pub-search" type="search" placeholder="Title, author, venue">

        <label for="area-filter">Research area</label>
        <select id="area-filter">
          <option value="">All areas</option>
          {{ range .Site.Data.research_areas.areas }}
            <option value="{{ .slug }}">{{ .title }}</option>
          {{ end }}
        </select>

        <div class="filter-label">Year</div>
        <div class="checkbox-list" id="year-filters">
          {{ range $pages.ByDate.Reverse.GroupByDate "2006" }}
            <label class="check-row"><input type="checkbox" value="{{ .Key }}"> <span>{{ .Key }}</span></label>
          {{ end }}
        </div>

        <div class="button-row">
          <button class="btn btn-chip" type="button" id="reset-filters">Reset</button>
        </div>
      </div>
    </details>

    <div>
      <div class="pub-toolbar">
        <div class="result-count" aria-live="polite"></div>
        <label>Sort
          <select id="sort-pubs">
            <option value="newest">Newest first</option>
            <option value="oldest">Oldest first</option>
            <option value="az">Title A-Z</option>
            <option value="za">Title Z-A</option>
          </select>
        </label>
        <button class="btn btn-chip" type="button" id="download-bibtex">Download citations</button>
      </div>

      <div class="pub-list" id="pub-list">
        {{ range $pages.ByDate.Reverse }}
          {{ $paper := . }}
          {{ $slug := path.Base (path.Dir .File.Path) }}
          {{ $tab := "working-papers" }}
          {{ if eq .Params.status "published" }}{{ $tab = "articles" }}{{ end }}
          {{ if eq .Params.status "resting" }}{{ $tab = "resting-papers" }}{{ end }}
          {{ if in (slice "cepr_contribution" "policy") .Params.status }}{{ $tab = "policy" }}{{ end }}
          {{ $authors := delimit .Params.authors ", " }}
          {{ $types := .Params.publication_types | jsonify }}
          {{ $areas := .Params.areas | jsonify }}
          {{ $search := printf "%s %s %s %s" .Title $authors .Params.publication .Params.abstract | lower }}
          <article class="pub-item" data-tab="{{ $tab }}" data-year="{{ .Date.Format "2006" }}" data-types="{{ $types }}" data-areas="{{ $areas }}" data-title="{{ .Title }}" data-date="{{ .Date.Format "20060102" }}" data-search="{{ $search }}" data-bibtex="{{ .Params.bibtex }}">
            <div class="pub-citation">
              <span class="authors">{{ $authors }}.</span>
              <span class="meta">{{ .Date.Format "2006" }}.</span>
              <a class="title" href="{{ .RelPermalink }}">{{ .Title }}</a>.
              {{ with .Params.publication }}<span class="venue">{{ . }}.</span>{{ end }}
              {{ with .Params.summary }}<p class="pub-summary">{{ . }}</p>{{ end }}
              {{ with .Params.links }}
                <div class="pub-links pub-links-inline">
                  <a class="btn btn-chip" href="{{ $paper.RelPermalink }}">Details</a>
                  {{ range first 4 . }}
                    <a class="btn btn-chip" href="{{ .url }}">{{ .name }}</a>
                  {{ end }}
                </div>
              {{ else }}
                <div class="pub-links pub-links-inline">
                  <a class="btn btn-chip" href="{{ $paper.RelPermalink }}">Details</a>
                </div>
              {{ end }}
            </div>
          </article>
        {{ end }}
      </div>
    </div>
  </div>
</section>

<script>
(function() {
  var tabs = document.querySelectorAll('.tab-btn');
  var list = document.getElementById('pub-list');
  var items = Array.prototype.slice.call(document.querySelectorAll('.pub-item'));
  var countEl = document.querySelector('.result-count');
  var search = document.getElementById('pub-search');
  var area = document.getElementById('area-filter');
  var years = Array.prototype.slice.call(document.querySelectorAll('#year-filters input[type="checkbox"]'));
  var sort = document.getElementById('sort-pubs');
  var reset = document.getElementById('reset-filters');
  var cite = document.getElementById('download-bibtex');
  var filterPanel = document.getElementById('research-filters');
  var activeTab = 'all';

  function syncFilterPanel() {
    if (!filterPanel) return;
    if (window.matchMedia('(max-width: 760px)').matches) {
      filterPanel.removeAttribute('open');
    } else {
      filterPanel.setAttribute('open', '');
    }
  }

  function selectedYears() {
    return years.filter(function(y) { return y.checked; }).map(function(y) { return y.value; });
  }

  function setHash() {
    var parts = [activeTab];
    if (area.value) parts.push('area=' + encodeURIComponent(area.value));
    if (search.value.trim()) parts.push('q=' + encodeURIComponent(search.value.trim()));
    var ys = selectedYears();
    if (ys.length) parts.push('years=' + ys.join(','));
    history.replaceState(null, '', '#' + parts.join('&'));
  }

  function parseHash() {
    var raw = location.hash.replace(/^#/, '');
    if (!raw) return;
    raw.split('&').forEach(function(part, index) {
      if (index === 0 && part.indexOf('=') === -1) activeTab = part || 'all';
      var kv = part.split('=');
      if (kv[0] === 'area') area.value = decodeURIComponent(kv[1] || '');
      if (kv[0] === 'q') search.value = decodeURIComponent(kv[1] || '');
      if (kv[0] === 'years') {
        var selected = (kv[1] || '').split(',');
        years.forEach(function(y) { y.checked = selected.indexOf(y.value) > -1; });
      }
    });
  }

  function filter() {
    var q = search.value.trim().toLowerCase();
    var areaValue = area.value;
    var ys = selectedYears();
    var visible = 0;
    items.forEach(function(item) {
      var itemAreas = JSON.parse(item.dataset.areas || '[]');
      var show = (activeTab === 'all' || item.dataset.tab === activeTab);
      if (q && item.dataset.search.indexOf(q) === -1) show = false;
      if (areaValue && itemAreas.indexOf(areaValue) === -1) show = false;
      if (ys.length && ys.indexOf(item.dataset.year) === -1) show = false;
      item.style.display = show ? '' : 'none';
      if (show) visible++;
    });
    tabs.forEach(function(btn) {
      var on = btn.dataset.tab === activeTab;
      btn.classList.toggle('active', on);
      btn.setAttribute('aria-selected', on ? 'true' : 'false');
    });
    countEl.textContent = visible + ' of ' + items.length + ' results';
    setHash();
  }

  function sortItems() {
    var mode = sort.value;
    items.sort(function(a, b) {
      if (mode === 'oldest') return Number(a.dataset.date) - Number(b.dataset.date);
      if (mode === 'az') return a.dataset.title.localeCompare(b.dataset.title);
      if (mode === 'za') return b.dataset.title.localeCompare(a.dataset.title);
      return Number(b.dataset.date) - Number(a.dataset.date);
    });
    items.forEach(function(item) { list.appendChild(item); });
    filter();
  }

  tabs.forEach(function(btn) {
    btn.addEventListener('click', function() {
      activeTab = btn.dataset.tab;
      filter();
    });
  });
  search.addEventListener('input', filter);
  area.addEventListener('change', filter);
  years.forEach(function(y) { y.addEventListener('change', filter); });
  sort.addEventListener('change', sortItems);
  reset.addEventListener('click', function() {
    activeTab = 'all';
    search.value = '';
    area.value = '';
    years.forEach(function(y) { y.checked = false; });
    sort.value = 'newest';
    sortItems();
  });
  cite.addEventListener('click', function() {
    var visible = items.filter(function(item) { return item.style.display !== 'none'; });
    var body = visible.map(function(item) { return item.dataset.bibtex; }).join('\n\n');
    var blob = new Blob([body], { type: 'application/x-bibtex' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = 'daniel-ershov-citations.bib';
    a.click();
    URL.revokeObjectURL(url);
  });

  syncFilterPanel();
  window.addEventListener('resize', syncFilterPanel);
  parseHash();
  sortItems();
})();
</script>
{{ end }}
"""


PUBLICATION_SINGLE = r"""
{{ define "main" }}
<article class="page-shell publication-detail">
  <div class="prose">
    <p><a href="{{ "/" | relURL }}">Home</a> / <a href="{{ "publication/" | relURL }}">Research</a></p>
    <h1>{{ .Title }}</h1>
    <p class="pub-citation">
      <span class="authors">{{ delimit .Params.authors ", " }}.</span>
      <span class="meta">{{ .Date.Format "2006" }}.</span>
      {{ with .Params.publication }}<span class="venue">{{ . }}.</span>{{ end }}
    </p>
    {{ with .Params.abstract }}
      <h2 id="abstract">Abstract</h2>
      <p>{{ . }}</p>
    {{ end }}
    {{ with .Params.main_finding }}
      <h2 id="main-finding">Main Finding</h2>
      <p>{{ . }}</p>
    {{ end }}
    {{ with .Params.policy_relevance }}
      <h2 id="policy-relevance">Policy Relevance</h2>
      <p>{{ . }}</p>
    {{ end }}
    {{ with .Params.notes }}
      <h2 id="notes">Notes</h2>
      <ul>
        {{ range . }}<li>{{ . }}</li>{{ end }}
      </ul>
    {{ end }}
    {{ with .Params.links }}
      <div class="pub-links">
        {{ range . }}
          <a class="btn btn-chip" href="{{ .url }}">{{ .name }}</a>
        {{ end }}
      </div>
    {{ end }}
    {{ .Content }}
    {{ partial "related_finder.html" . }}
  </div>
  <aside class="metadata-card">
    <dl>
      <dt>Authors</dt>
      <dd>{{ delimit .Params.authors ", " }}</dd>
      <dt>Year</dt>
      <dd>{{ .Date.Format "2006" }}</dd>
      {{ with .Params.publication }}<dt>Venue</dt><dd>{{ . }}</dd>{{ end }}
      {{ with .Params.tags }}<dt>Tags</dt><dd>{{ delimit . ", " }}</dd>{{ end }}
    </dl>
  </aside>
</article>
{{ end }}
"""


RELATED = r"""
{{ $current := . }}
{{ $candidates := slice }}
{{ range where .Site.RegularPages "Section" "publication" }}
  {{ if ne .RelPermalink $current.RelPermalink }}
    {{ $score := 0 }}
    {{ range .Params.areas }}
      {{ if in ($current.Params.areas | default slice) . }}{{ $score = add $score 3 }}{{ end }}
    {{ end }}
    {{ range .Params.tags }}
      {{ if in ($current.Params.tags | default slice) . }}{{ $score = add $score 2 }}{{ end }}
    {{ end }}
    {{ range .Params.authors }}
      {{ if in ($current.Params.authors | default slice) . }}{{ $score = add $score 1 }}{{ end }}
    {{ end }}
    {{ if ge $score 3 }}
      {{ $candidates = $candidates | append (dict "page" . "score" $score) }}
    {{ end }}
  {{ end }}
{{ end }}
{{ if gt (len $candidates) 0 }}
<section class="gk-see-also">
  <h2>See Also</h2>
  <ul>
    {{ range first 8 (sort $candidates "score" "desc") }}
      {{ $p := .page }}
      {{ $label := "Paper" }}
      {{ if eq $p.Params.status "working_paper" }}{{ $label = "Paper" }}{{ end }}
      {{ if eq $p.Params.status "resting" }}{{ $label = "Paper" }}{{ end }}
      {{ if in (slice "cepr_contribution" "policy") $p.Params.status }}{{ $label = "Policy" }}{{ end }}
      <li><span class="kind-label">[{{ $label }}]</span><a href="{{ $p.RelPermalink }}">{{ $p.Title }}</a></li>
    {{ end }}
  </ul>
</section>
{{ end }}
"""


AUTHORS_LIST = r"""
{{ define "main" }}
{{ $owner := .Site.Title }}
{{ $exclude := slice "Jiewei Li" "Junichi Suzuki" "Justin Johnson" "Marc Duhamel" "Charles Bérubé" "Andrew Rhodes" "Matthijs Wildenbeest" "Sergio Pastorello" "Vincenzo Denicolò" "Emilio Calvano" "Giacomo Calzolari" }}
{{ $names := slice }}
{{ range where .Site.RegularPages "Section" "publication" }}
  {{ range .Params.authors }}
    {{ if and (ne . $owner) (not (in $exclude .)) (not (in $names .)) }}
      {{ $names = $names | append . }}
    {{ end }}
  {{ end }}
{{ end }}
<section class="page-shell prose">
  <h1>{{ .Title }}</h1>
  {{ .Content }}
  <h2>Coauthors</h2>
  <ul class="people-list">
    {{ range sort $names }}
      {{ $entry := index $.Site.Data.coauthors . }}
      <li>{{ if $entry }}<a href="{{ $entry.url }}">{{ . }}</a>{{ else }}{{ . }}<!-- Missing reviewed external URL for {{ . }} -->{{ end }}</li>
    {{ end }}
  </ul>
  <h2>PhD Students</h2>
  <ul class="people-list">
    {{ range .Site.Data.phd_students }}
      <li><strong>{{ .name }}</strong><br><span class="person-meta">{{ .placement }}</span></li>
    {{ end }}
  </ul>
</section>
{{ end }}
"""


SIMPLE_SECTION_LIST = r"""
{{ define "main" }}
<section class="page-shell prose">
  <h1>{{ .Title }}</h1>
  {{ .Content }}
  {{ if .Pages }}
    <ul class="compact-list">
      {{ range .Pages.ByDate.Reverse }}
        <li><a href="{{ .RelPermalink }}">{{ .Title }}</a></li>
      {{ end }}
    </ul>
  {{ end }}
</section>
{{ end }}
"""


INDEX_JSON = r"""
{{- $pages := where .Site.RegularPages "Params.private" "ne" true -}}
[
{{- range $i, $p := $pages -}}
  {{- if $i }},{{ end }}
  {
    "title": {{ $p.Title | jsonify }},
    "url": {{ $p.RelPermalink | jsonify }},
    "section": {{ $p.Section | jsonify }},
    "summary": {{ ($p.Params.abstract | default $p.Summary) | plainify | jsonify }}
  }
{{- end -}}
]
"""


NOT_FOUND = r"""
{{ define "main" }}
<section class="page-shell prose">
  <h1>Page Not Found</h1>
  <p>The page may have moved. Use search or return to the research page.</p>
  <div class="button-row">
    <button class="btn btn-primary js-search-open" type="button">Search</button>
    <a class="btn btn-secondary" href="{{ "publication/" | relURL }}">Research</a>
  </div>
</section>
{{ end }}
"""


DEPLOY = r"""
name: Deploy Hugo site to Pages

on:
  push:
    branches: ["main"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

defaults:
  run:
    shell: bash
    working-directory: hugo-site

jobs:
  build:
    runs-on: ubuntu-latest
    env:
      HUGO_VERSION: 0.148.2
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Install Hugo CLI
        run: |
          wget -O ${{ runner.temp }}/hugo.deb https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.deb
          sudo dpkg -i ${{ runner.temp }}/hugo.deb

      - name: Install Dart Sass
        run: sudo snap install dart-sass

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 22

      - name: Install Node.js dependencies
        run: npm install

      - name: Setup Pages
        id: pages
        uses: actions/configure-pages@v5

      - name: Build with Hugo
        env:
          HUGO_ENVIRONMENT: production
          TZ: Europe/London
        run: hugo --gc --minify --baseURL "${{ steps.pages.outputs.base_url }}/"

      - name: Build Pagefind search index
        run: npx pagefind --site public

      - uses: actions/upload-pages-artifact@v3
        with:
          path: hugo-site/public

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
"""


UPDATING = r"""
# Updating Daniel Ershov's Website

The site is a Hugo website in `hugo-site/`. Most updates are ordinary Markdown edits.

## Add a Paper

Copy an existing folder under `hugo-site/content/publication/`, rename the folder with a stable slug, and edit `index.md`. Keep the front matter fields `title`, `date`, `authors`, `publication_types`, `publication`, `status`, `areas`, `tags`, `abstract`, and `links`.

Use `status: "published"` for journal articles, `status: "working_paper"` for active working papers, `status: "policy"` or `status: "cepr_contribution"` for policy writing, and `status: "resting"` for resting papers. The Research page tabs are generated from this field.

## Update the C.V.

Replace `hugo-site/static/files/DErshov_CV_SES_2026.pdf` with the new PDF and keep the filename stable, or update the links in `hugo-site/data/profile.json` and `hugo-site/content/bio/_index.md`.

## Update Research Areas

Edit `hugo-site/data/research_areas.json`. The homepage accordions and the Research page area filter read this file.

## People Page

The People page has separate coauthor and PhD student sections. Coauthors are auto-populated from publication front matter, with external links stored in `hugo-site/data/coauthors.json`. PhD students are stored in `hugo-site/data/phd_students.json`.

## Preview Locally

From `hugo-site/`, run:

```bash
hugo server --buildDrafts --disableFastRender
```

The local preview is private to your machine. Nothing goes public until changes are pushed to GitHub and the Pages workflow runs.
"""


PRINCIPLES = r"""
# Website Principles

This site is designed as a maintainable academic website rather than a marketing page. The Research page is the main archival surface: dense citation rows, client-side filters, stable slugs, and BibTeX export.

The repository keeps source content in Markdown, reusable site data in `hugo-site/data/`, static files in `hugo-site/static/`, and template behavior in `hugo-site/layouts/`. URLs should remain stable after publication; change titles in front matter rather than renaming content folders.

The visual system uses UCL's official purple-led palette with off-white surfaces and dense typography for academic browsing. The site forces light mode, includes keyboard-visible focus states, and uses Pagefind for static search.

Deployment is handled by GitHub Actions. Pushing to `main` will build Hugo, build the Pagefind index, and deploy to GitHub Pages. Review locally before pushing.
"""


def make_images() -> None:
    static = SITE / "static"
    images = static / "images"
    images.mkdir(parents=True, exist_ok=True)
    urls = [
        "https://lh3.googleusercontent.com/sitesv/AA5AbUCndniYEufhiaYRKZv0z2SImBQv6WhzK7X6-MkGnj1xocCBYGQr4zMl6f7j7CBCb06GsvvIE6TRe46BLhnsjQu1-ycAxy9UCM6ESlKglby_zBgRiWhAs9Pd4KR1JLlJRlDnHqbV1L56A7L-hVCfFCCS-VhQ9NZwTmUEJBW_G1CGazwv3eAUTaSmXCJ31hPx_MpklsK6P9DCbMg__XSc41oFwRx-DwAhYMYdS7zWsuk%3Dw1280",
        "https://cepr.org/sites/default/files/styles/logo/public/profile-photos/107215-cropped_headshot_b278419de0f260dae165fb8cd386a946.jpg?itok=AlS6ytnR",
    ]
    raw = images / "daniel-ershov-source.jpg"
    if not raw.exists():
        last_error = None
        for url in urls:
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(req, timeout=30) as response:
                    raw.write_bytes(response.read())
                break
            except Exception as exc:
                last_error = exc
        if not raw.exists():
            raise last_error
    try:
        from PIL import Image, ImageDraw, ImageFont

        img = Image.open(raw).convert("RGB")
        w, h = img.size
        side = min(w, h)
        left = max(0, int((w - side) * 0.5))
        top = max(0, int((h - side) * 0.18))
        if top + side > h:
            top = h - side
        img = img.crop((left, top, left + side, top + side)).resize((720, 720))
        img.save(images / "daniel-ershov.jpg", quality=86, optimize=True)

        def font(size: int):
            candidates = [
                "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
                "/Library/Fonts/Arial Bold.ttf",
            ]
            for candidate in candidates:
                if Path(candidate).exists():
                    return ImageFont.truetype(candidate, size)
            return ImageFont.load_default()

        for size, name in [(32, "favicon-32x32.png"), (180, "apple-touch-icon.png")]:
            icon = Image.new("RGB", (size, size), "#361a54")
            draw = ImageDraw.Draw(icon)
            fnt = font(int(size * 0.42))
            text = "DE"
            box = draw.textbbox((0, 0), text, font=fnt)
            draw.text(((size - (box[2] - box[0])) / 2, (size - (box[3] - box[1])) / 2 - size * 0.03), text, fill="white", font=fnt)
            icon.save(static / name)
        ico = Image.open(static / "favicon-32x32.png")
        ico.save(static / "favicon.ico")
    except Exception:
        shutil.copy2(raw, images / "daniel-ershov.jpg")


if __name__ == "__main__":
    make_site()
