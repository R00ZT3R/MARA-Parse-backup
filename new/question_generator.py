from scripts.questiongenerator import QuestionGenerator
from scripts.questiongenerator import print_qa
import torch

device = torch.device('cuda')
# assert device == torch.device('cuda'), "Not using CUDA. Set: Runtime > Change runtime type > Hardware Accelerator: GPU"

qg = QuestionGenerator()
with open('test_data/indian_matchmaking.txt', 'r') as a:
    article = a.read()

qa_list = qg.generate(
    article, 
    num_questions=1, 
    answer_style='all'
)
print(qa_list)
