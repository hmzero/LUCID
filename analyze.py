import sys
import gemini

def analyze (paper1, paper2):
    # open object files
    with open(paper1) as file:
        obj1 = file.read()
    with open(paper2) as file:
        obj2 = file.read()

    # build prompt
    prompt = ("Given the following JSON objects:\n" + obj1 + "\n" + obj2 +
            "For each field, evaluate the similarity of the corresponding data in the two objects. " 
            "Do not compare based on language similarity, prioritize similar entities and scientific compatability. "
            "Use a number from 0 to 100 to indicate the similarity, with 100 being identical. "
            "Also include a breif explanation of the given score."
            "List the name of the object in the schema(i.e. advantages, approach, materials, metrics, problem, processes), "
            "then the number, then the explination. For example, materials: 0.000. explain here."
            "Do not compare anything else")

    response = gemini.generate(prompt)
    
    return response

#print(analyze(sys.argv[1],sys.argv[2]))