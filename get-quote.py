import random

def main(file_path):
  # print("Keep it logically awesome.")

  #f = open("quotes.txt")
  #quotes = f.readlines()
  #f.close()

  #print(quotes)
  ##This new modulation uses the random module and picks random quote 
   with open(file_path, 'r') as file:
        quotes = file.readlines()
   random_quote = random.choice(quotes).strip()
   return random_quote

if __name__== "__main__":
     file_path = 'path/to/quotes.txt'
     random_quote = main(file_path)
     print(random_quote)

     
