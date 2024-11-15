import streamlit as st
import random
st.sidebar.header("Welcome")
page=st.sidebar.radio("Games",["User guessing game","machine guessing game"])
if page=='User guessing game':
    start_range=st.number_input("Enter starting range:",min_value=1,max_value=100)
    end_range=st.number_input("Enter ending range:",min_value=1,max_value=100)
    if start_range>=end_range:
        st.write("starting range is less than ending range")
    else:
        if'number_to_guess' not in st.session_state:
            st.session_state.number_to_guess = random.randint(start_range,end_range)
            st.session_state.attempts = 0
            st.session_state.game_started=True
            

    # Title
    st.title("Number Guessing Game ")

    # Instructions
    st.write(f"I'm thinking of a number between{start_range}and{end_range}. Can you guess it?")

    # Input for the guess
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100)

    # Button to submit the guess
    if st.button("Guess"):
        st.session_state.attempts += 1

        # Check if the guess is correct, too low, or too high
        if guess < st.session_state.number_to_guess:
            st.write(" Too low! Try again.")
        elif guess > st.session_state.number_to_guess:
            st.write("Too high! Try again.")
        else:
            st.write(f"Congratulations! You've guessed the number in {st.session_state.attempts} attempts!")

elif page=='machine guessing game':

    if "min_value" not in st.session_state:
        st.session_state.min_value = 1
        st.session_state.max_value = 100
        st.session_state.attempts = 0
        st.session_state.machine_guess = (st.session_state.min_value + st.session_state.max_value) // 2
        st.session_state.game_active = False

    # Title
    st.title("Simple Machine Guessing Game")
    st.write("Think of a number within the range you set, and the machine will try to guess it!")

    # Step 1: Get the range from the player
    min_value = st.number_input("Enter the minimum value for the range:", value=1)
    max_value = st.number_input("Enter the maximum value for the range:", value=100)

    # Start the game
    if st.button("Start Game"):
        if min_value >= max_value:
            st.write("Minimum value must be less than the maximum value.")
        else:
            
            st.session_state.min_value = min_value
            st.session_state.max_value = max_value
            st.session_state.attempts = 1
            st.session_state.machine_guess = (min_value + max_value) // 2
            st.session_state.game_active = True
            st.write(f"The machine's guess is {st.session_state.machine_guess}")

    if st.session_state.game_active:
        feedback = st.radio("How is the machine's guess?", ("Correct", "Too Low", "Too High"))

        if st.button("Submit"):
            if feedback == "Correct":
                st.write(f"The machine guessed it! The number was {st.session_state.machine_guess}.")
                st.write(f"Attempts: {st.session_state.attempts}")
                st.session_state.game_active = False  # End the game
            else:
                # Update the range based on feedback
                if feedback == "Too Low":
                    st.session_state.min_value = st.session_state.machine_guess + 1
                elif feedback == "Too High":
                    st.session_state.max_value = st.session_state.machine_guess - 1

                # Make a new guess
                st.session_state.machine_guess = (st.session_state.min_value + st.session_state.max_value) // 2
                st.session_state.attempts += 1
                st.write(f"The machine's new guess is {st.session_state.machine_guess}")

            
