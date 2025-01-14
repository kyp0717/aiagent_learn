Text generation

Copy page
Learn how to generate text from a prompt.
OpenAI provides simple APIs to use a large language model to generate text from a prompt, as you might using ChatGPT. These models have been trained on vast quantities of data to understand multimedia inputs and natural language instructions. From these prompts, models can generate almost any kind of text response, like code, mathematical equations, structured JSON data, or human-like prose.

Quickstart
To generate text, you can use the chat completions endpoint in the REST API, as seen in the examples below. You can either use the REST API from the HTTP client of your choice, or use one of OpenAI's official SDKs for your preferred programming language.

Create a human-like response to a prompt

import OpenAI from "openai";
const openai = new OpenAI();

const completion = await openai.chat.completions.create({
    model: "gpt-4o",
    messages: [
        { role: "developer", content: "You are a helpful assistant." },
        {
            role: "user",
            content: "Write a haiku about recursion in programming.",
        },
    ],
});

console.log(completion.choices[0].message);
Choosing a model
When making a text generation request, the first option to configure is which model you want to generate the response. The model you choose can greatly influence the output, and impact how much each generation request costs.

A large model like gpt-4o will offer a very high level of intelligence and strong performance, while having a higher cost per token.
A small model like gpt-4o-mini offers intelligence not quite on the level of the larger model, but is faster and less expensive per token.
A reasoning model like the o1 family of models is slower to return a result, and uses more tokens to "think", but is capable of advanced reasoning, coding, and multi-step planning.
Experiment with different models in the Playground to see which one works best for your prompts! More information on choosing a model can also be found here.

