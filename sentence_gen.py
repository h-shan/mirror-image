import random

postive_templates = []
negative_templates = []

pos_file = open('positive.txt', 'r')
pos_arr = pos_file.read().splitlines()
pos_file.close()

neg_file = open('negative', 'r')
neg_arr = neg_file.read().splitlines()
neg_file.close()

ques_file = open('question', 'r')
ques_arr = ques_file.read().splitlines()
ques_file.close()



def respond(cur_senti, prev_senti, subject):
	p_pos_senti = 1.5 - cur_senti - prev_senti
	if random() <= p_pos_senti:
		return generate_sentence(subject, cur_senti)
	else:
		ques_temp = random.choice(ques_arr)
		return ques_temp.replace("{{}}", subject)
		



def generate_sentence(subject, cur_senti):
	if cur_senti > 0.5:
		pos_temp = random.choice(pos_arr)
		return pos_temp.replace("{{}}", subject)

	else:
		neg_temp = reandom.choice(neg_arr)
		return neg_temp.replace("{{}}", subject)




