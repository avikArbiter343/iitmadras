import streamlit as st

def largest_num(a, b, c):
    return max(a, b, c)

st.title('Find the Largest Number')
st.write('Enter three numbers below and click the button to find the largest among them.')

# Get user input
a = st.number_input('Enter the first number:')
b = st.number_input('Enter the second number:')
c = st.number_input('Enter the third number:')

# Find the largest number and display the result
if st.button('Find largest'):
    result = largest_num(a, b, c)
    st.write(f'The largest number is {result}.')
