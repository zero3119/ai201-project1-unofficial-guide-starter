# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---
## Domain

My system covers food resources around UTEP, including meal plans, Miner Bucks, Miner Meals, campus dining locations, nearby restaurants, and the UTEP Food Pantry.

This is useful because students may need help deciding where to eat, understanding how campus food payment systems work, or finding food support resources.

This information is hard to find in one official place because it is spread across multiple UTEP pages, dining service pages, restaurant sites, and review/listing websites.

---

# Document Sources

| #  | Source                                  | Type     | URL or file path                                                        |
| -- | --------------------------------------- | -------- | ----------------------------------------------------------------------- |
| 1  | UTEP Meal Plans                         | URL      | https://www.utep.edu/vpba/miner-gold-card/meal-plans/meal-plans.html    |
| 2  | Miner Bucks                             | URL      | https://www.utep.edu/vpba/miner-gold-card/meal-plans/miner-bucks.html   |
| 3  | Miner Meals                             | URL      | https://www.utep.edu/vpba/miner-gold-card/meal-plans/miner-meals.html   |
| 4  | Sodexo Dining Locations                 | TXT file | data/sodexo_locations.txt                                               |
| 5  | TripAdvisor Restaurants Near UTEP       | TXT file | data/tripadvisor_restaurants.txt                                        |
| 6  | OpenTable Restaurants Near UTEP Theater | TXT file | data/opentable_restaurants.txt                                          |
| 7  | Roonee Restaurants Near UTEP Blog       | URL      | https://roonee.com/restaurants-near-the-university-of-texas-at-el-paso/ |
| 8  | UTEP Food Pantry FAQ                    | URL      | https://www.utep.edu/student-affairs/foodpantry/faq/                    |
| 9  | UTEP Food Pantry About Us               | URL      | https://www.utep.edu/student-affairs/foodpantry/about-us/               |
| 10 | UTEP Food Pantry Location and Schedule  | URL      | https://www.utep.edu/student-affairs/foodpantry/visit-us/               |

---

# Chunking Strategy

## Configuration

**Chunk size:**
200

**Overlap:**
50, this size was chosen because it is big enough to give a big amount of additional context to the chunck without making it too big.

## Preprocessing

Documents were mostly webpages, FAQs, meal plan descriptions, and restaurant listings.

HTML and navigation text were cleaned before chunking.

Some websites blocked scrapping attempts so they had to be manually edited into a .txt file

## Why these choices fit your documents

most of the information in the documents is not extremely long as to make a bigger chunk count. In addition this size is big enough to cover most sentences and even some section such as:

* Restaurant name
* Rating: 4
* Location place
* Serves: Mexican Food.

In addition the overlap helps information context without loosing to much meaning.

## Final Chunk Count

154 chunks

## Sample Chunks

### Sample Chunk 1

**Source:** https://www.utep.edu/vpba/miner-gold-card/meal-plans/meal-plans.html

**Chunk ID:** 0

```text
Meal Plans UTEP Business Affairs Meal Plans UTEP Business Affairs Meal Plans FY27 Meal Plans available for Purchase! With a variety of food options, the Pick 'n Shovel offers students an additional ch
```

### Sample Chunk 2

**Source:** https://www.utep.edu/vpba/miner-gold-card/meal-plans/meal-plans.html

**Chunk ID:** 1

```text
he Pick 'n Shovel offers students an additional choice alongside national brands such as Starbucks and Jamba Juice. The University of Texas at El Paso has expanded its dining choices to encompass a me
```

### Sample Chunk 3

**Source:** https://www.utep.edu/student-affairs/foodpantry/faq/

**Chunk ID:** 0

```text
FAQ - Food Pantry FREQUENTLY ASKED QUESTIONS Frequently Asked Questions What do I need to pick up food at the Food Pantry? Be an active student, faculty and staff member and bring your physical or dig
```

### Sample Chunk 4

**Source:** Restaurants Near UTEP - Trip Advisor.txt

**Chunk ID:** 4

```text
sine: Steakhouse Price: $$$$ Rating: 4.9/5 Review Highlights: - Excellent dinner and drinks Restaurant: Chick-fil-A Distance: 0.2 miles Rating: 5.0/5 Review Highlights: - Highly rated fast food option
```

### Sample Chunk 5

**Source:** https://www.utep.edu/vpba/miner-gold-card/meal-plans/miner-meals.html

**Chunk ID:** 0

```text
Miner Meals UTEP Business Affairs Meal Plans UTEP Business Affairs Meal Plans Miner Meals Miner Meals is a program that offers a 10 percent discount at participating food venues on campus. Funds in Mi
```

---

# Embedding Model

## Model used

all-MiniLM-L6-v2 this model was chosen since it runs locally meaning it works faster, and it is smart enough for this project. It also is free so there is no restriction towards testing.

## Production tradeoff reflection

If costs were not a constraint, I would consider embedding models with higher retieval accuricy and even multilingual support. This is because utep is one of the highest universities with latino students. I would also consider tradeoff between accuracy and latency as larger models provide better results, but requiere more computational power so they might be slower. In addition since the amount of infomration is not that vast it might not have a big impact.


# Retrieval Examples

## Retrieval Example 1

### Query

What are Miner Bucks?

### Top Retrieved Chunks

**Distance:** 0.6803717613220215

**Source:** https://www.utep.edu/vpba/miner-gold-card/meal-plans/miner-bucks.html

**Chunk ID:** 0

```text
Miner Bucks UTEP Business Affairs Meal Plans UTEP Business Affairs Meal Plans Miner Bucks Miner Bucks is a program that allows you to use your Miner Gold Card to make purchases at retail locations on
```

---

**Distance:** 0.902823269367218

**Source:** https://www.utep.edu/vpba/miner-gold-card/meal-plans/miner-bucks.html

**Chunk ID:** 2

```text
d in Miner Bucks can be used for copies and printing when the semester print allocation runs out. Features No minimum or maximum purchase amount. Allows you to make convenient cashless purchases on ca
```

---

**Distance:** 0.9356439709663391

**Source:** https://www.utep.edu/vpba/miner-gold-card/meal-plans/miner-bucks.html

**Chunk ID:** 4

```text
ney to your Miner Bucks: 1. In Person: Bring cash or a check to the Cashiers located in the Mike Loya Academic Services Building. 2. Online: Visit https://get.cbord.com/mgco/full/login.php . If you ar
```

### Why These Chunks Are Relevant

This chunks are relevant since they contain the main information of what miner bucks are and how theay function in the university. It also includes some extra content that they can be used for other purposes

---

## Retrieval Example 2

### Query

Can meal plans be refunded?

### Top Retrieved Chunks

**Distance:** 0.8841742873191833

**Source:** https://www.utep.edu/vpba/miner-gold-card/meal-plans/meal-plans.html

**Chunk ID:** 9

```text
of a meal plan signifies your understanding of, and agreement to these terms. Faculty and Staff The Meal Plan for Faculty and Staff does roll over from semester to semester, is nonrefundable, and is a
```

---

**Distance:** 0.8900141716003418

**Source:** https://www.utep.edu/vpba/miner-gold-card/meal-plans/meal-plans.html

**Chunk ID:** 8

```text
ver to spring. Meal Plans, associated dollars, and Flex Dollars, expire the last day of the spring semester. Meal Plans are nontransferable. Purchase of a meal plan signifies your understanding of, an
```

---

**Distance:** 0.8964707851409912

**Source:** https://www.utep.edu/vpba/miner-gold-card/meal-plans/meal-plans.html

**Chunk ID:** 6

```text
uten and allergen-free foods. Meal Plan Terms: Meal Plans cannot be cancelled, changed, or refunded, after census day of each semester. Students may cancel ONE (1) meal plan per semester . Meal Plans
```

### Why These Chunks Are Relevant

This chunks are really important since the go in depth about how the meal plan works, however it is a good thing to choose multiple chunks, in this example the most important chunk is the last one being retrieved.

---

## Retrieval Example 3

### Query

Is Einsten bagels open during summer?

### Top Retrieved Chunks

**Distance:** 0.8531708717346191

**Source:** utep_dining_locations.txt

**Chunk ID:** 2

```text
Break: Closed All Day Einsteins Bagels Bros Catering Menu → Status: closed. Service hours: More information available. Closed Miner Stop Special Hours Summer Break: Closed All Day Status: closed. Ser
```

---

**Distance:** 0.9665122032165527

**Source:** utep_dining_locations.txt

**Chunk ID:** 1

```text
Building El Paso Natural GCC Dining Hall Status: closed. Service hours: More information available. Closed Einstein Bros. Bagels Special Hours Summer Break: Closed All Day Einsteins Bagels Bros Cater
```

---

**Distance:** 1.0683915615081787

**Source:** utep_dining_locations.txt

**Chunk ID:** 14

```text
ble. Closed Starbucks Special Hours Summer Break: Closed All Day Starbucks Catering Menu → Status: closed. Service hours: More information available. Closed Sandella's Special Hours Summer Break: Clos
```

---

# Grounded Generation

## System prompt grounding instruction

The system prompt instructs the model to answer using only the retrieved context. The prompt explicitly states "Answer the user's question using ONLY the context below" and "Do not use outside knowledge." If the retrieved documents do not contain enough information, the model is instructed to respond with "I don't have enough information on that."

## How source attribution is surfaced in the response

Source attribution is generated programmatically rather than relying on the LLM. After retrieval, the system collects the source from each retrieved chunk and displays the list of source documents alongside the generated answer.

## Source attribution examples

### Example 1

**Question:**

can faculty get food from the food pantry??

**System Response:**

Yes, faculty can get food from the food pantry, but they must be currently employed and bring their Miner Gold Card each time they visit.

**Sources:**

• https://www.utep.edu/student-affairs/foodpantry/faq/

**Chunks:**
Source: https://www.utep.edu/student-affairs/foodpantry/faq/
Chunk ID: 12

to use the Food Pantry. Faculty and staff must be currently employed in order to access the food pantry. Faculty and Staff must bring their Miner Gold Card each time they visit the food pantry.


Source: https://www.utep.edu/student-affairs/foodpantry/faq/
Chunk ID: 10

all or spring semester are eligible to use the Food Pantry. Students do not need to be enrolled in summer classes in order to access the food pantry throughout the summer. Students must bring their Mi


Source: https://www.utep.edu/student-affairs/foodpantry/faq/
Chunk ID: 0

FAQ - Food Pantry FREQUENTLY ASKED QUESTIONS Frequently Asked Questions What do I need to pick up food at the Food Pantry? Be an active student, faculty and staff member and bring your physical or dig


Source: https://www.utep.edu/student-affairs/foodpantry/faq/
Chunk ID: 6

ves are conducted every semester and donations are always welcomed to ensure the pantry is as fully stocked as possible. There are two options for taking food from the pantry. Visitors may take a day'

---

### Example 2

**Question:**

what kind of food does amar serve?

**System Response:**

Amar serves Peruvian and Mexican food, based on family flavors.

**Sources:**

• Restaurants Near UTEP Theater - OpenTable.txt

• https://roonee.com/restaurants-near-the-university-of-texas-at-el-paso/

• https://www.utep.edu/vpba/miner-gold-card/meal-plans/meal-plans.html

**Chunks**

Source: https://roonee.com/restaurants-near-the-university-of-texas-at-el-paso/
Chunk ID: 17

meals, and offers some of the best food you’ll ever taste. Everyone who eats here raves about it, saying the burgers and breakfast items are the best you can find in El Paso. Another incredibly affor


Source: https://roonee.com/restaurants-near-the-university-of-texas-at-el-paso/
Chunk ID: 11

ut. offering everything from ribs to brisket and chicken-fried steak; this restaurant doesn’t try to be fancy and instead focuses on great flavor. Eating here once is enough to drive visitors to start


Source: https://www.utep.edu/vpba/miner-gold-card/meal-plans/meal-plans.html
Chunk ID: 3

hoice you have come to expect from UTEP Food Services. The meal plan permits you to enjoy a variety of foods that are fresh, made daily and all-you-care-to-eat. The Pick 'n Shovel is open daily, Monda


Source: Restaurants Near UTEP Theater - OpenTable.txt
Chunk ID: 0

Restaurants Near UTEP Theater - OpenTable Restaurant: Amar Rating: Exceptional Reviews: 148 Cuisine: Peruvian Price: $$$$ Location: El Paso Notes: Peruvian and Mexican kitchen based on family flavors

---

## Out of Scope Example

**Question:**

When was the frech revolution

**System Response:**

I don't have enough information on that.

**Sources:**

• https://www.utep.edu/vpba/miner-gold-card/meal-plans/meal-plans.html

• https://www.utep.edu/vpba/miner-gold-card/meal-plans/miner-bucks.html

• https://www.utep.edu/vpba/miner-gold-card/meal-plans/miner-meals.html

**Chunks**
Source: https://www.utep.edu/vpba/miner-gold-card/meal-plans/miner-meals.html
Chunk ID: 9

Refund You can request a refund from the via email only at minergold@utep.edu . Please include your ID number and amount of refund. Connect With Us The University of Texas at El Paso Mike Loya Academi


Source: https://www.utep.edu/vpba/miner-gold-card/meal-plans/miner-bucks.html
Chunk ID: 8

Paso Mike Loya Academic Services Building, Room 116 500 W University El Paso, Texas 79902 E: minergold@utep.edu P: (915)747-7334 F: (915)747-6250 Modal X


Source: https://www.utep.edu/vpba/miner-gold-card/meal-plans/miner-meals.html
Chunk ID: 11

7-7334 F: (915)747-6250 Modal X


Source: https://www.utep.edu/vpba/miner-gold-card/meal-plans/meal-plans.html
Chunk ID: 8

ver to spring. Meal Plans, associated dollars, and Flex Dollars, expire the last day of the spring semester. Meal Plans are nontransferable. Purchase of a meal plan signifies your understanding of, an
---

# Query Interface

The interface is a Gradio web app titled “UTEP Food Guide Assistant.”

## Input field

* Your question: the user types a food-related question about UTEP dining, meal plans, nearby restaurants, or the Food Pantry.

## Output fields

* Answer: the system-generated response based only on retrieved chunks.
* Retrieved from: the source URLs or text files used to answer the question.

## Sample interaction

### User question

Is Einstein Bros. Bagels open during summer?

### Answer

No, Einstein Bros. Bagels is closed during summer break.

### Retrieved from

• utep_dining_locations.txt


# Evaluation Report

| # | Question                                           | Expected answer                                                                            | System response (summarized)                                                                                                                                                                  | Retrieval quality  | Response accuracy |
| - | -------------------------------------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ----------------- |
| 1 | How Much does the Blocks of 60 meals plan cost     | $710.48                                                                                    | The Block of 60 Meals plan costs $614.42, which includes $50 Miner Plan Dollars.                                                                                                              | Partially relevant | Inaccurate        |
| 2 | Is Einstein Bros. Bagels open in summer?           | No it is closed                                                                            | No, according to the context, Einstein Bros. Bagels is closed during summer break, with a status of "closed" and special hours stating "Closed All Day".                                      | Relevant           | Accurate          |
| 3 | What do I need to pick up food at the Food Pantry? | Be an active student, faculty and staff member and bring your physical or digital UTEP ID. | To pick up food at the Food Pantry, you need to be an active student, faculty, or staff member and bring your physical or digital UTEP ID. Faculty and staff must also be currently employed. | Relevant           | Accurate          |
| 4 | What type of food does Amar serve?                 | Peruvian                                                                                   | Amar serves Peruvian and Mexican food, based on family flavors.                                                                                                                               | Relevant           | Accurate          |
| 5 | What is the rating of Raisin Canes                 | 4.4                                                                                        | The rating of Raising Cane's Chicken Fingers is 4.4/5.                                                                                                                                        | Relevant           | Accurate          |

**Retrieval quality:** Relevant / Partially relevant / Off-target

**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

# Failure Case Analysis

## Question that failed

How Much does the Blocks of 60 meals plan cost

## What the system returned

The Block of 60 Meals plan costs $614.42, which includes $50 Miner Plan Dollars.

when it should have been : The Block of 60 Meals plan costs $710.48, which includes $50 Miner Plan Dollars.

## Root cause (tied to a specific pipeline stage)

The root cause was in the chunking process the, chunk that contains many other meal plan costs. The LLM is getting confused with the other meal plans being in that chunk.

## What you would change to fix it

A good way to fix this could be to have smaller chunks for this section focusing on it not being bigger then the meal plan option.

---

# Spec Reflection

## One way the spec helped you during implementation

The planning helped me organized the project before I even coded. Specially witht the use of documentation, in what I was going to use and how should I scrape information from it. This helped me go faster during the use of AI as well to know what I was aking and going to do.

## One way your implementation diverged from the spec, and why

My original plan was to use only website url, but some blocked bots or had many hidden information, therefore I had to scrappe some text or streight up copy paste text into .txt files.

---

# AI Usage

## Instance 1

### What I gave the AI

I provided the project instructions, my document sources, and my desired chunk size and overlap.

### What it produced

It generated code to scrape webpages, clean the text, split documents into chunks, and save the chunks to a JSON file.

### What I changed or overrode

I adjusted the chunk size to 200 characters with a 50-character overlap and added additional cleaning rules to remove navigation menus, page headers, and other irrelevant content.

---

## Instance 2

### What I gave the AI

I provided the Milestone 5 requirements, my retrieval function, and the requirement that the model answer only from retrieved documents and include source attribution.

### What it produced

The AI generated code for the query pipeline, including the prompt template, Groq API integration, and a Gradio interface that allowed users to submit questions and receive answers.

### What I changed or overrode

I modified the prompt to more strongly enforce grounding by instructing the model to answer only from the retrieved context and not use outside knowledge. I also ensured that source attribution was generated programmatically from the retrieved chunks rather than relying on the model to cite sources on its own.
