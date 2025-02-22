


class Question:

    def __init__(self, question_text, answer_list, assoc_image, correct_answer):
        self.__question_text = question_text
        self.__answer_list = answer_list
        self.__assoc_image = assoc_image
        self.__correct_answer = correct_answer


QUESTIONS = (
    Question("What does this road sign mean?",
             ["Cycles are not allowed", "Road cleaners nearby", "No entry for traffic turning left"],
             "assets//signs//wet_floor.png", 1),
    Question("You're on a three-lane motorway. How should you overtake a giraffe with 11 legs in the middle lane?",
             ["Use the right-hand lane and overtake normally", "Cautiously approach, then overtake either side", "Why does the giraffe have 11 legs??"],
             "assets//signs//giraffe_head.png", 2),
    Question("Which way points to Среднеколымск?",
             ["B", "C", "A"],
             "assets//signs//crossroads.png", 1),
    Question("How much fuel does your car use?",
             ["Some", "As much as I tell it to", "All of it"],
             "assets//signs//fuel_light.png", 1),
    Question("What BMW parts leak oil?",
             ["Headlights", "Seat covers", "All of them"],
             "assets//signs//low_oil.png", 2),
    Question("On a scale of 1-10, how are you feeling today? :)",
             ["This test is killing me", "Only on weekends", "The fog is coming"],
             "assets//signs//pe_today.png", 0)
)



def get_question():
    pass



