from typing import List


class Survey:
    
    def __init__(self, question : str) -> None:
        self.question = question
        self.responses : List[str] = []
    def show_question(self):
        print(self.question)

    def store_response(self, new_response : str):
        self.responses.append(new_response)

    def show_results(self):
        print("Survey results")
        print(len(self.responses))
        for res in self.responses:
            print(f"- {res}")


sur = Survey("apa kabar")
sur.store_response("baik")
sur.store_response("haha")

print(sur.show_results())
