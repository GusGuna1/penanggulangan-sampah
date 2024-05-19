import random
def gen_pass(pass_length):
   char = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
   p = ""
   for i in range(pass_length):
      p = p+random.choice(char)
   return p
