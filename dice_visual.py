from die import Die
import pygal

# Create two D6.
die1 = Die()
die2 = Die()

# Make some rolls, and store results in a list.
# results =[]
# for roll in range(1000):
#     result = die1.roll() + die2.roll()
results = [die1.roll() + die2.roll() for roll in range(1000)]
# results.append(result)

# Analyze the results.
# frequencies = []
max_result = die1.num_sides + die2.num_sides
# for value in range(2, max_result+1):
frequencies = [results.count(value) for value in range(2, max_result+1)]
    # frequency = results.count(value)
    # frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = [x + 1 for x in range(1, max_result)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('visuals/dice_visual.svg')
print(frequencies)