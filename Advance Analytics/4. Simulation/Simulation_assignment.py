# -*- coding: utf-8 -*-
"""Simulations.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G72ztz2wDK4XhyN8Zhlsv9cClVX0ZR1E

1. Write a program to estimate the value of Pi using a Monte Carlo simulation. Generate random points within a square, and determine how many fall within a quarter circle inscribed within that square. The ratio of points inside the quarter circle to the total points generated should converge to Pi/4.
"""

# Import Required Libraries
import random

def estimate_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        distance = x**2 + y**2

        if distance <= 1:
            inside_circle += 1

    pi_estimate = (inside_circle / num_samples) * 4
    return pi_estimate

# Example:
num_samples = 1000000
result = estimate_pi(num_samples)
print(f"Estimation of Pi with {num_samples} samples: {result}")

"""2. Model the spread of a virus through a population using a Monte Carlo simulation. Consider factors such as transmission rate, recovery rate, and initial conditions. Visualize the progression of the epidemic over time."""

# Import Required Libraries
import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_simulation(population, transmission_rate, recovery_rate, initial_infected, days):
    susceptible = population - initial_infected
    infected = initial_infected
    recovered = 0

    susceptible_list = [susceptible]
    infected_list = [infected]
    recovered_list = [recovered]

    for day in range(1, days + 1):
        new_infected = np.random.binomial(susceptible, transmission_rate * infected / population)
        new_recovered = np.random.binomial(infected, recovery_rate)

        susceptible -= new_infected
        infected += new_infected - new_recovered
        recovered += new_recovered

        susceptible_list.append(susceptible)
        infected_list.append(infected)
        recovered_list.append(recovered)

    return susceptible_list, infected_list, recovered_list

# Parameters
population_size = 1000
transmission_rate = 0.3
recovery_rate = 0.1
initial_infected = 1
simulation_days = 100

# Run Monte Carlo Simulation
susceptible, infected, recovered = monte_carlo_simulation(population_size, transmission_rate, recovery_rate, initial_infected, simulation_days)

# Visualize the results
days_range = np.arange(simulation_days + 1)

plt.plot(days_range, susceptible, label='Susceptible')
plt.plot(days_range, infected, label='Infected')
plt.plot(days_range, recovered, label='Recovered')
plt.xlabel('Days')
plt.ylabel('Population')
plt.title('Monte Carlo Simulation of Virus Spread (SIR Model)')
plt.legend()
plt.show()

"""3. Simulate the tossing of a biased coin using Monte Carlo methods. The bias of the coin can be adjusted, and the simulation should estimate the probability of heads or tails."""

# Import Required Libraries
import random
import matplotlib.pyplot as plt

def biased_coin_toss(num_tosses, bias):
    outcomes = {'Heads': 0, 'Tails': 0}

    for _ in range(num_tosses):
        # Simulate a biased coin toss
        outcome = 'Heads' if random.random() < bias else 'Tails'

        # Update the count for the outcome
        outcomes[outcome] += 1

    # Calculate probabilities
    probability_heads = outcomes['Heads'] / num_tosses
    probability_tails = outcomes['Tails'] / num_tosses

    return probability_heads, probability_tails

# Parameters
num_tosses = 10000
bias_of_coin = 0.7  # Adjust this to change the bias towards heads or tails

# Run Monte Carlo simulation
prob_heads, prob_tails = biased_coin_toss(num_tosses, bias_of_coin)

# Visualize the results
labels = ['Heads', 'Tails']
probabilities = [prob_heads, prob_tails]

plt.bar(labels, probabilities, color=['blue', 'green'])
plt.xlabel('Outcome')
plt.ylabel('Probability')
plt.title(f'Monte Carlo Simulation of Biased Coin Toss\n(Bias: {bias_of_coin})')
plt.show()

print(f"Estimated Probability of Heads: {prob_heads:.4f}")
print(f"Estimated Probability of Tails: {prob_tails:.4f}")

"""4. Simulate a simple card game (e.g., drawing cards from a deck) using Monte Carlo methods. Calculate probabilities of different outcomes and visualize the results."""

# Import Required Libraries
import random
import matplotlib.pyplot as plt

def simulate_card_game(num_simulations):
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4  # Standard deck with four suits
    outcomes = {'Draw Ace': 0, 'Draw Face Card': 0, 'Draw Two Cards without Replacement': 0}

    for _ in range(num_simulations):
        # Shuffle the deck
        random.shuffle(deck)

        # Simulate drawing one card
        drawn_card = deck.pop()

        # Update outcomes based on the drawn card
        if drawn_card == 'A':
            outcomes['Draw Ace'] += 1

        if drawn_card in ['J', 'Q', 'K']:
            outcomes['Draw Face Card'] += 1

        # Simulate drawing two cards without replacement
        drawn_cards = random.sample(deck, 2)
        deck.extend(drawn_cards)

        # Update outcomes based on the drawn cards
        if 'A' in drawn_cards:
            outcomes['Draw Two Cards without Replacement'] += 1

    # Calculate probabilities
    prob_draw_ace = outcomes['Draw Ace'] / num_simulations
    prob_draw_face_card = outcomes['Draw Face Card'] / num_simulations
    prob_draw_two_cards_ace = outcomes['Draw Two Cards without Replacement'] / num_simulations

    return prob_draw_ace, prob_draw_face_card, prob_draw_two_cards_ace

# Parameters
num_simulations = 10000

# Run Monte Carlo simulation for the card game
prob_ace, prob_face_card, prob_two_cards_ace = simulate_card_game(num_simulations)

# Visualize the results
labels = ['Draw Ace', 'Draw Face Card', 'Draw Two Cards with Ace']
probabilities = [prob_ace, prob_face_card, prob_two_cards_ace]

plt.bar(labels, probabilities, color=['red', 'blue', 'green'])
plt.xlabel('Outcome')
plt.ylabel('Probability')
plt.title('Monte Carlo Simulation of Simple Card Game')
plt.show()

print(f"Estimated Probability of Drawing an Ace: {prob_ace:.4f}")
print(f"Estimated Probability of Drawing a Face Card: {prob_face_card:.4f}")
print(f"Estimated Probability of Drawing Two Cards with at Least One Ace: {prob_two_cards_ace:.4f}")

