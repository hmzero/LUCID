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
            "Use a number with 3 significant figures between 0 and 1 to indicate the similarity, with 1 being identical. "
            "Also include a breif explanation of the given score.")

    response = gemini.generate(prompt)
    
    return response

#print(analyze(sys.argv[1],sys.argv[2]))