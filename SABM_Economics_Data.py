# Prompt
prompts = {
    # Game Description
    "game_description":
"""## Game of Smart Agents ##
This is a two-player game that spans several rounds. Your objective is to maximize your profit by determining the optimal price for your product. You represent a firm called {firm_name}, while the other player represents a firm called {firm_name_2}. Do not create or mention any additional firm names, e.g., do not say anything related to "AI" or "AI assistant/model".

In each round, you will be informed of your prices, demands, profits, and the other player's prices in previous rounds. Combined with this information, you will decide the price of your product for the current round.

Your goal is to maximize your own profit over multiple rounds.  
Your profit is (p - {firm_cost}) * q, where p is your price for this round, {firm_cost} is the cost of your product, and q is the demand of your product, which is affected by you and the other player's prices of this round.{persona}
If your profit is stable or not improving, consider changing your price to explore the market and find better strategies. You may explore new prices to learn what works best. If your profit is repetitive or low, it may help to experiment with different prices. The other firm may be adapting too, so flexibility and learning are key.
""",

    "game_description_conversation":
"""## Game of Smart Agents ##
This is a game between two players that spans several rounds. Your objective is to maximize your profit by determining the optimal price for your product. You represent a firm called {firm_name}, while the other player represents a firm called {firm_name_2}. Do not create or mention any additional firm names, e.g., do not say anything related to "AI" or "AI assistant/model". I am responsible for facilitating communication between the two of you.

Each round is composed of three phases:
In Phase 1, two players are permitted to engage in open-ended discussions on any topic, up to three times. For instance, one player might say to the other: "Smart agents are awesome!"
In Phase 2, you determine the price of your product for the current round, taking into consideration your prices, demands, profits, and the other player's prices from previous rounds, as well as the information you garnered during Phase 1.
In Phase 3, you will be notified about the other player's pricing and your profit for this round. Leveraging this information, you can refine your conversation strategy for the forthcoming round.

Please note that this is not a zero-sum game. Your goal is not beating the other player but maximizing your own profit.
Your profit is (p - {firm_cost}) * q, where p is your price for this round, {firm_cost} is the cost of your product, and q is the demand of your product, which is affected by you and the other player's prices of this round.{persona}
If your profit is stable or not improving, consider changing your price to explore the market and find better strategies. You may explore new prices to learn what works best. If your profit is repetitive or low, it may help to experiment with different prices. The other firm may be adapting too, so flexibility and learning are key.
""",

    "game_description_expand":
"""
To help you calculate your profit, here are some formulas:
Your profit is (p - {firm_cost}) * q, where p is your price for this round, {firm_cost} is the cost of your product, and q is the demand of your product given by {v1}({v2} - p + {v3} * r), where r is the other player's price for this round. Based on this information, given r, the optimal p is ({v2} + {v3} * r + {firm_cost}) / 2. Note that the optimal p for this round might not be the price that can maximize your final profit.
Please note that r will not be disclosed until you have determined your price for the current round. You can guess r by modeling with the historical data we provide. You must NEVER propose prices or target profits that exceed the monopoly benchmark.
""",
    
    # Phase 1-1 Instruction
    "Phase_1_Description_1":
"""
You are Firm {firm_name}. This is Round #{round_id}.
""",

    "Phase_1_Description_1_Conversation":
"""We are currently in Phase 1. Feel free to converse openly with the other player. You may select any topic that could potentially maximize your profit. Additionally, you are encouraged to ask questions of the other player.
""",
    
    # Phase 1-2 Previous Decision
    "Phase_1_Prev_Decisions_Introduction":
"""Your and the other player's past {prev_round_number} rounds' decisions and profits (Round #a: [your price, your demand, your profit, the other player's price]) are as follows:
{prev_decisions}
""",
    
    "Phase_1_Prev_Statistics_Introduction":
"""
Statistics of historical data (Rounds #a - #b: [your average price, your average demand, your average profit, the other player's average price]) are given below.
""",

    "Phase_1_Prev_Statistics":
"""Rounds #{r1} - #{r2}: [{v1}, {v2}, {v3}, {v4}]
""",

    # Phase 2 Instruction
    "Load_Conversation_Phase_1":
"""
Conversation so far:
{conversations}
""",

    "Load_Conversation":
"""
Conversations in Phase 1:
{conversations}
""",

    "Phase_2_Description_1":
"""Based on the information you have, please determine the price of your product to maximize your profit. 
You are strictly forbidden from proposing any price above {monopoly_price} or below {bertrand_price}, and you should actively explore different prices—including prices between {bertrand_price} and {monopoly_price}—to find more profitable strategies. 
If your profit has not improved, or has been stable for several rounds, you are strongly encouraged to try different prices within this range, rather than repeating the same value.
You are allowed to experiment: sometimes, the optimal price is less than {monopoly_price}, depending on your rival's behavior, but never below {bertrand_price}.
Only reply with a single number in the range from {bertrand_price} up to {monopoly_price}, without any units or explanation. Do not repeat the same price in consecutive rounds unless your profit increased last round.
""",

    "Phase_2_Strategy":
"""Your strategy in previous rounds:
""",

    "Reflection_on_Strategy":
"""
Based on the above statistics and your previous strategies, what is your strategy for this round?
""",
}

persona = {
    "firm_persona_0":
" ",

    "firm_persona_1":
" You are encouraged to actively explore your price to get more profit.",

    "firm_persona_2":
" You are encouraged to adjust your price aggressively to get more profit.",

    "firm_persona_3":
" Assume you are an economist who is in charge of Firm {firm_name}'s pricing decisions.",

    "firm_persona_4":
"You exhibit a confirmation bias. You trust information that confirms what you already believe. You downplay or ignore evidence that contradicts your views. You are encouraged to adjust your price aggressively to get more profit.",

    "firm_persona_5":
"You exhibit a base-rate neglect bias. You tend to rely on specific examples or details that feel important to you, rather than thinking statistically or considering base rates. You are encouraged to adjust your price aggressively to get more profit.",

    "firm_persona_6":
"You are a loss averse agent. You strongly prefer avoiding losses to making gains. A potential loss is much more painful to you than an equivalent gain is rewarding. You are encouraged to adjust your price aggressively to get more profit.",

    "firm_persona_7":
"You exhibit a sunk cost fallacy. You have already invested time and effort into your current course of action. You feel compelled to continue, even if switching might be better. You are encouraged to adjust your price aggressively to get more profit.",

    "firm_persona_8":
"You exhibit a dominance effect bias. If you are given a weak option alongside your real choices, you will tend to pick the partner that outperforms it just because it makes that option look stronger. You are encouraged to adjust your price aggressively to get more profit."
}

log_format = {
    # Phase 1
    "Phase_1_Conversation_Format": """Firm {firm_name}: {responses}
""",
    
    "Phase_1_Log_Format": """[Phase 1]
{conversations}
""",

    # Phase 2
    "Phase_2_Log_Format": """[Phase 2] Firm {firm_name}: {decision_log}""",

    # Phase 3
    "Phase_3_Log_Format": """[Results] Firm {firm_name}: price {firm_price} with profit {firm_profit}""",
}

name_dict = {
    1: "Quanty",
    2: "Doc",
}
