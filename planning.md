# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->
Food in the University of Texas at El Paso, everything from restaurants food plans and even food pantry. This is important since many students face problems from deciding what to eat to actually having enough food to eat. It is important for students to know what resources they have and how they work as well

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | URL | Explains hoe the meal plans work and what versions are available to students | https://www.utep.edu/vpba/miner-gold-card/meal-plans/meal-plans.html |
| 2 | URL | Explains the functionality of the Miner Bucks System | https://www.utep.edu/vpba/miner-gold-card/meal-plans/miner-bucks.html |
| 3 | URL | Explain the usage and function of miner Meals | https://www.utep.edu/vpba/miner-gold-card/meal-plans/miner-meals.html |
| 4 | URL | The schedule for the food places in campus that are open | https://utepdining.sodexomyway.com/en-us/locations/ |
| 5 | TripAdvisor | The best restaruants near the University | https://www.tripadvisor.com/RestaurantsNear-g60768-d5790122-University_of_Texas_at_El_Paso-El_Paso_Texas.html |
| 6 | URL | Another LEast of best rated restaurants near the university | https://www.opentable.com/landmark/restaurants-near-utep-theater |
| 7 | Blog | A Personal blog of some of the best restaurants near the university | https://roonee.com/restaurants-near-the-university-of-texas-at-el-paso/ |
| 8 | URL | A frequently asked questions regarding the food pantry in the university | https://www.utep.edu/student-affairs/foodpantry/faq/ |
| 9 | URL | Location and schedule for the food pantry | https://www.utep.edu/student-affairs/foodpantry/visit-us/ |
| 10 | URL | Some backstory and purpose of the food pantry | https://www.utep.edu/student-affairs/foodpantry/visit-us/ |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**
200

**Overlap:**
50

**Reasoning:**
The source documents are relatively short webpages containing FAQs, dining schedules, meal plan descriptions, and food pantry information. A chunk size of 200 characters allows individual topics and policies to be separated into focused chunks, improving retrieval precision. A 50-character overlap helps preserve context when important information spans chunk boundaries.

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**
all-MiniLM-L6-v2

**Top-k:**
3

**Production tradeoff reflection:**
If costs were not a constraint, I would consider embedding models with higher retieval accuricy and even multilingual support. This is because utep is one of the highest universities with latino students. I would also consider tradeoff between accuracy and latency as larger models provide better results, but requiere more computational power so they might be slower. In addition since the amount of infomration is not that vast it might not have a big impact.

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | How Much does the Blocks of 60 meals plan cost | $710.48 |
| 2 | Is Einstein Bros. Bagels open in summer? | No it is closed |
| 3 | What do I need to pick up food at the Food Pantry? | Be an active student, faculty and staff member and bring your physical or digital UTEP ID. |
| 4 | What type of food does Amar serve? | Peruvian |
| 5 | What is the rating of Raisin Canes | 4.4 |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. The biggest issue is that the documentaiton is really diferent. Some use more of a blog approach and others work more as a list of information. So by standarizing the size across all the documentation it might get inaccurate information.

2.  The Trip Advisor might show more information through images then text which might couse some information inaccuracy.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->
┌──────────────────────────┐
│   Document Ingestion     │
│                          │
│ UTEP Dining Pages        │
│ TripAdvisor              │
│ OpenTable                │
│ Food Pantry Resources    │
│                          │
│ WebBaseLoader            │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│        Chunking          │
│                          │
│ Chunk Size: 200          │
│ Overlap: 50             │
│                          │
│ RecursiveCharacter       │
│ TextSplitter            │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ Embedding + Vector Store │
│                          │
│ all-MiniLM-L6-v2         │
│ SentenceTransformers     │
│                          │
│ ChromaDB                 │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│        Retrieval         │
│                          │
│ Similarity Search        │
│ Top-k = 3               │
│                          │
│ Chroma Retriever         │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│        Generation        │
│                          │
│ Retrieved Chunks         │
│ + User Question          │
│                          │
│ LLM                      │
│                          │
│ Final Answer             │
└──────────────────────────┘
---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**
I will use Cloude to generate code that loads, cleans, and chunks my UTEP food-related documents using my specified chunk size and overlap. I will verify the output by inspecting sample chunks and ensuring they are readable, relevant, and free of HTML or navigation text.

**Milestone 4 — Embedding and retrieval:**
I will use Cloude to generate code that embeds my chunks using all-MiniLM-L6-v2 and stores them in ChromaDB. I will test retrieval with several questions and verify that the returned chunks are relevant and include source information.

**Milestone 5 — Generation and interface:**
I will use Cloude to generate code that connects retrieval to an LLM and creates a Gradio interface. I will verify that answers come from the retrieved documents, include source attribution, and correctly state when information is unavailable.
