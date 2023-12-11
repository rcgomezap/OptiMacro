import os
# from tqdm import tqdm
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def line():
    print('----------------------------------------')

# def progress_line():
#     for i in tqdm(range(100)):
#         pass