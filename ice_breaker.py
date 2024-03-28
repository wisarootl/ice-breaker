import os

from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from third_parties.linkedin import scrape_linkedin_profile

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

if __name__ == "__main__":

    linkedin_lookup_url = linkedin_lookup_agent(name="Eden Marco")

    summary_template = """
        given the information {information} about a person I want you to create:
        1. A short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(
        linked_profile_url="https://www.linkedin.com/in/harrison-chase-961287118/"
    )

    res = chain.invoke(input={"information": linkedin_data})

    print(linkedin_data)
