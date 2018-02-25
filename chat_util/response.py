import random
import luis_request

postive_templates = []
negative_templates = []

pos_file = open('message_templates/pos.txt', 'r')
pos_arr = pos_file.read().splitlines()
pos_file.close()

neg_file = open('message_templates/neg.txt', 'r')
neg_arr = neg_file.read().splitlines()
neg_file.close()

pos_subj_file = open('message_templates/pos_subj.txt', 'r')
pos_subj_arr = pos_subj_file.read().splitlines()
pos_subj_file.close()

neg_subj_file = open('message_templates/neg_subj.txt', 'r')
neg_subj_arr = neg_subj_file.read().splitlines()
neg_subj_file.close()

ques_file = open('message_templates/questions.txt', 'r')
ques_arr = ques_file.read().splitlines()
ques_file.close()

ques_subj_file = open('message_templates/questions.txt', 'r')
ques_subj_arr = ques_subj_file.read().splitlines()
ques_subj_file.close()

greetings = ['hello', 'hi', 'hey', "how are you?", "hello there!"]
endings = ["have a nice day", "see you later", "bye"]
confuse = ["could you repeat that?", "what did you say?", "i don't seem to understand"]

def respond(cur_senti, prev_senti, subject, user_input):
    luis_res = luis_request.request(user_input)
    intent = result["topScoringIntent"]["intent"]
    entities = result["entities"]

    if luis_request.NONE_INTENT == intent:
        return random.choice(confuse)
    elif luis_request.GREETING_INTENT in intent:
        return random.choice(greetings)
    elif luis_request.END_INTENT in intent:
        return random.choice(endings)

    user_input = user_input.lower()
    
    p_pos_senti = 1.5 - cur_senti - prev_senti
    p_pos_senti = max(min(p_pos_senti, 0.8), 0.2)
    print('Current sentiment', cur_senti)
    if random.uniform(0, 1) > p_pos_senti:
        return generate_sentence(subject, cur_senti).capitalize()
    else:
        return generate_question(subject).capitalize()

def generate_question(subject):
    if subject:
        return random.choice(ques_subj_arr).format(subject).capitalize()
    else:
        return random.choice(ques_arr)

def generate_sentence(subject, cur_senti):
    if cur_senti > 0.5:
        if subject:
            return random.choice(pos_subj_arr).format(subject).capitalize()
        else:
            return random.choice(pos_arr).capitalize()
    else:
        if subject:
            return random.choice(neg_subj_arr).format(subject).capitalize()
        else:
            return random.choice(neg_arr).capitalize()
