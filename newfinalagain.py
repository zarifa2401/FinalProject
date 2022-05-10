import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import seaborn as sns


sns.set_style('darkgrid')

st.set_page_config(
        page_title="Streamlit 101: Comparing Crime",
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="expanded",
)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("🏙️ Comparing Major Cites")


@st.cache
def get_data():
    df = pd.read_csv("Boston Crime Data.csv")

    return df


@st.cache
def read_data():
    ny = pd.read_csv("Crime_Map_.csv")

    return ny


nav = st.sidebar.radio("Navigation", ["Maps of Comparison", "Graphs of Boston and New York", "Reducing Crime Incidents"])
if nav == "Maps of Comparison":
    st.image("crimetape.jfif", use_column_width='always')
    st.subheader(" In this project, I will be comparing crime data found for Boston and New Yok city. Respectfully. I will be comparing the two states using graphs that I believed would show the data well.")
    st.map(get_data(), zoom=7)
    st.map(read_data())


if nav == "Graphs of Boston and New York":
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=["Graph for Boston", "Graph for New York"]
        )
    if selected == "Graph for Boston":
        st.title(f"You have selected {selected}")

        data = get_data()
        numeric_colums = data.select_dtypes('int64', 'float64').columns
        print(numeric_colums)
        print(data.info())

        checkbox = st.sidebar.checkbox("Reveal data")

        if checkbox:
            st.dataframe(data=data)

        st.sidebar.subheader("Scatterplot")
        st.subheader("Scatterplot, Histogram, and JointPlot using int64 values")
        select_box1 = st.sidebar.selectbox(label='X AXIS', options=numeric_colums)
        select_box2 = st.sidebar.selectbox(label='Y AXIS', options=numeric_colums)

        sns.relplot(x=select_box1, y=select_box2, data=data, color="red")
        st.pyplot()

        st.sidebar.subheader("Histogram")
        select_box3 = st.sidebar.selectbox(label="Feature", options=numeric_colums)
        histogram_slider = st.sidebar.slider(label="Number of Bins", min_value=5, max_value=100, value=100)
        sns.distplot(data[select_box3], bins=histogram_slider, color="yellow")
        st.pyplot()

        st.sidebar.subheader("Joint Plot")
        select_box3 = st.sidebar.selectbox(label='x', options=numeric_colums)
        select_box4 = st.sidebar.selectbox(label="y", options=numeric_colums)

        sns.jointplot(x=select_box3, y=select_box4, data=data, color="green")
        st.pyplot()

    if selected == "Graph for New York":
        st.title(f"You have selected {selected}")

        data = read_data()
        numeric_colums = data.select_dtypes('int64', 'float64').columns
        print(numeric_colums)
        print(data.info())

        checkbox = st.sidebar.checkbox("Reveal data")

        if checkbox:
            st.dataframe(data=data)

        st.sidebar.subheader("Scatterplot")
        st.subheader("Scatterplot, Histogram, and JointPlot using int64 values")

        select_box1 = st.sidebar.selectbox(label='X AXIS', options=numeric_colums)
        select_box2 = st.sidebar.selectbox(label='Y AXIS', options=numeric_colums)

        sns.relplot(x=select_box1, y=select_box2, data=data, color="orange")

        st.pyplot()
        st.sidebar.subheader("Histogram")
        select_box3 = st.sidebar.selectbox(label="Feature", options=numeric_colums)
        histogram_slider = st.sidebar.slider(label="Number of Bins", min_value=5, max_value=100, value=100)
        sns.distplot(data[select_box3], bins=histogram_slider, color="blue")
        st.pyplot()

        st.sidebar.subheader("Joint Plot")
        select_box3 = st.sidebar.selectbox(label='x', options=numeric_colums)
        select_box4 = st.sidebar.selectbox(label="y", options=numeric_colums)

        sns.jointplot(x=select_box3, y=select_box4, data=data, color="violet")
        st.pyplot()

if nav == "Reducing Crime Incidents":
    st.title(" Reducing Crime In Major Cities")
    st.write("1. Create well-targeted programmes: If the goal is to reduce homicides, then programme selection should be located in hotspot areas and focused on the population group most likely to commit violence crimes, often young males between 10-29 years old. The risk factors for why these young men get involved in criminality also needs to be clearly diagnosed and complemented with a treatment plan that involves the family and community. ")
    st.write("2. Focus on hotspots: We’ve got scientific evidence that a focus on hotspots and ‘hot people’ can prevent or reduce violence. But we need also accompany this with other measures – urban upgrading, better urban planning, situational prevention – especially early childhood intervention.")
    st.write("3. Focus on gun control: Where there are no guns, there are no gun deaths. A simple and practical way to start impacting armed violence is to try to stem the flow of illegal guns. I believe in the gun control approach as a first step.")
    st.write("4. Find the balance between repression and prevention: Local experiences and efforts deal mainly with interpersonal aspects of violence. When illicit or transnational crime starts co-opting state forces, people stop trusting their security forces, governments and start focusing on private and personal security, stop using public spaces. So the idea is not create a system based entirely on repression or prevention, but to find that balance and incorporate rehabilitation and reintegration policies and funding into security strategies.")
    st.write("5. Treat male and female violence as the same issue: Male and female dimensions of violence are connected. We need to look at these issues comprehensively rather than a divide and conquer approach. Research has shown it is not just about single risk factors (i.e. being a male is a risk factor) that determines violence – rather it is the accumulation of risk factors that produce violence.")
    st.write("--Ways to Reduce Crime by Naomi Larsson")
