message ="you are the best {} and score is {}"
name = "radhika"
score = 80
print(message.format(name,score))      # simple format method

print(f"you are the best {name} and score is {score}")     # fstring method
print(f"you are the best {{name}} and score is {{score}}")  # we can also use f string like this

price=1000.49999999
txt=f"the price of rice is:{price:.2f} rupees!"
print(txt)

print(f"{20*8}")