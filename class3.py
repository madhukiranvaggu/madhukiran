import streamlit as st
st.title('energy calculator')

st.header('energy calculator')

col1,col2=st.columns(2)

with col1:
    st.subheader(':red[kinetic energy]')
    m=st.number_input('mass:',key='a')
    v= st.number_input('velocity:',key='b')
    if st.button('calculate',key='abc'):
        st.write(f'the kinetic energy is {0.5*m*v**2}')

with col2:
    st.subheader(':red[potential energy]')
    ma=st.number_input('mass:',key='c')
    h=st.number_input('height:',key='d')
    if st.button('calculate',key='xyz'):
        st.write(f'the potentail energy is {ma*10*h}')

