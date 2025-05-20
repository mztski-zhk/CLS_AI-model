from langchain_openai import ChatOpenAI
import src.stt

# init
import os
if not os.environ.get("OPENAI_API_KEY"):
    api_key = os.environ["OPENAI_API_KEY"] = "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"

base_url = "https://openrouter.ai/api/v1"
model = "deepseek/deepseek-v3-base:free"
temperature = 0.4

# create agent
llm = ChatOpenAI(
        base_url=base_url,
        api_key=api_key,
        llm=model,
        temperature=temperature,
        max_iterations=3,
        return_intermediate_steps=True,
    )

if __name__ == "__main__":
    for i in range(4):
        # get user input
        prompt = src.stt.SpeechToText().flow()
        if prompt is None:
            i = i - 1
        print(prompt)

        message = (
            [
                ("system", "You are a helpful assistant."),
                ("user", prompt),
            ]
        )
        
        run_agent = llm.invoke(message)