import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent

load_dotenv(override=True)

def get_pagila_agent():
    db_url = URL.create(
        drivername="postgresql+psycopg",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "5432")),
        database=os.getenv("DB_NAME"),
    )

    engine = create_engine(
            db_url,
            connect_args={
                "options": "-csearch_path=mrt"
            }
    )

    db = SQLDatabase(
        engine,
        include_tables=["actors", "film_inventory", "film_actor"],
    )

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    return create_sql_agent(
        llm=llm,
        db=db,
        verbose=True,
        agent_type="openai-tools",
    )