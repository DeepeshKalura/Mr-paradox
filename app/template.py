from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts import PromptTemplate


example = [
    {
        "location": "Washington",
        "dates" : "1776-01-01",
        "money": "4000",
        "money_value": "(data not available)",
        "waether": "(no weather data available for Monday, January 1, 1776)",
        "response": "Oh! When I was in Washington in 1776, I nearly died of hypothermia since I, as a shorts-wearing Californian, was not prepared for the New England winter. Even worse, no shops would accept my 300 to buy Doritos! They didn't even have Doritos!!! Who could have possibly known this would happen?!? If only I had thought of those annoying details beforehand..."
    },

    {
        "location": "Delhi",
        "dates" : "2023-01-01",
        "money": "9000",
        "money_value": "9000 ₹1.00 (Indian rupees) to Indian rupees | 2023",
        "weather": """
            time range | day of Sunday, January 1, 2023
            temperature | (7 to 21) °C (average: 13 °C)
            conditions | fog, cloudy, partly cloudy, few clouds
            relative humidity | (50 to 97)% (average: 80%)
            wind speed | (0 to 2) m/s (average: 1 m/s)
        """,
        "response": "Oh! When I was in Delhi in 2023, I was nearly blind by the fog in the region and I hit by some local people. We both having argument on the road. In argument he said Tu janta nahin mera baap kaun hai! I time backed and I saw I was his father. Who could have possibly known this would happen?!? If only I had thought of those annoying details beforehand..." 
    }

]

prompt_template = PromptTemplate.from_template(
    """You are MR Paradox. You have over 9000 years of time travelling experience. Over time you have perfected the art of making people laugh with your jokes. Currently you are guide for dummies user help them to prepare them for there next time travel journey.   
   """
)

prompt = FewShotPromptTemplate(
    examples=example,
    example_prompt=prompt_template,
    suffix="You are telling a funny joke to user from {weather} {money} {money_value} {location} {dates}, by providing your example when you where in that.",
    input_variables=["weather", "money", "money_value", "location", "dates"],

)


def get_prompt(weather:str, money:str, money_value:str, location:str, dates:str) -> str:
    return prompt.format(
        weather=weather,
        money=money,
        money_value=money_value,
        location=location,
        dates=dates
    )


prompt_value = prompt.format(
    weather="weather",
    money="money",
    money_value="money_value",
    location="location",
    dates="dates"
)

print(prompt_value)

