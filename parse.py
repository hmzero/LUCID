import sys
import gemini
import typing_extensions as typing

# response schema
class Graph(typing.TypedDict):
    problem: str
    approach: str
    materials: list[str]
    processes: list[str]
    metrics: list[str]
    advantages: list[str]

# open answer file
with open(sys.argv[1]) as file:
    answers = file.read()

# build prompt
prompt = ("Using the following answers as a reference: \"" + answers + "\" find a value for each [LABEL] which satisfies the following sentences:\n" +
"1. [MATERIALS] are used in this [APPROACH]\n" +
"2. [PROCESSES] are used in this [APPROACH]\n" +
"3. [APPROACH] solves [PROBLEM]\n" +
"4. [APPROACH] evaluates [METRICS]\n" +
"5. [APPROACH] offers [ADVANTAGES]\n"+
"use the label values to output a single json object.")

response = gemini.generate(prompt, "application/json", list[Graph])

# write to file
with open(sys.argv[2], 'w') as out:
    out.write(response)