import pandas as pd
import streamlit as st


dfData = pd.read_csv("Herramientas3_2023_banco.csv.csv")
df = dfData.select_dtypes(exclude="number")
dfJobs = dfData.drop_duplicates(subset=["job"])
jobs = dfJobs [["job"]]
jobs = dfJobs ["job"].values.tolist()

print(jobs)
st.header('Prediccion del banco')

clearJob = df['job'].unique().tolist()
clearMarital = df['marital'].unique().tolist()
clearEducation = df['education'].unique().tolist()
clearDefault = df['default'].unique().tolist()
clearHousing = df['housing'].unique().tolist()
clearLoan = df['loan'].unique().tolist()
clearContact = df['contact'].unique().tolist()
clearPoutcome = df['poutcome'].unique().tolist()



age = st.number_input('Inserte su edad', value=18)
job = st.selectbox("Seleccione su trabajo", clearJob)
marital = st.selectbox("Seleccione su estado civil", clearMarital)
education = st.selectbox("Seleccione su nivel educativo", clearEducation)
default = st.selectbox("Seleccione una opción", clearDefault)
housing = st.selectbox("Cuenta con vivienda propia", clearHousing)
loan = st.selectbox("Ha tenido algún préstamo anteriormente", clearLoan)
contact = st.selectbox("Seleccione su tipo de contacto", clearContact)
duration = st.slider("Selecciona la duracion que te gustaria", min_value=0, max_value=49018, value=0)
campaign = st.slider("Selecciona la campaña que desea", min_value=1, max_value=56, value=1)
pdays = st.slider("Selecciona los días festivos que desea", min_value=0, max_value=999, value=0)
previous = st.slider("Selecciona la opcion previa", min_value=0, max_value=7, value=0)
poutcome = st.selectbox("Seleccione una opción", clearPoutcome)
emp = st.slider("Selecciona la opcion que le interese", min_value= -0.1, max_value= 3.4, value=-0.1 )
cons = st.slider("Selecciona la opcion que requiera", min_value=92.201, max_value= 94.767, value=92.201)
conf = st.slider("Selecciona la opcion", min_value= -50.8, max_value=-26.9, value=-50.8)
euribor3m = st.slider("Selecciona la opcion que desea", min_value=0.634, max_value=5.045, value=0.634)
employed = st.slider("selecciona el numero de empleada", min_value=4963.6, max_value=5228.1, value=5963.6)


if st.button('Buscar'):
    st.write('No existe')
else:
    st.write('Si existe')
