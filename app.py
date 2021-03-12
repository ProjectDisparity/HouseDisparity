import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import time

matplotlib.use('Agg')

def main():
    st.title("Data Visualization of Delhi and Dhaka")
    st.subheader('Delhi Data Explorer')

    html_temp = """
    <div style="background-color:tomato;"><p style="color:white; font-size:50px;"> 
    Visualization </p></div>
    """
    st.markdown(html_temp, unsafe_allow_html=True )

    def file_selector(folder_path='./datasets'):
        filenames         = os.listdir(folder_path)
        selected_filename = st.selectbox("Selected file to download", filenames) 
        return os.path.join(folder_path, selected_filename)

    filename  = file_selector()
    st.info("You selected {}".format(filename))

    # Reading Data
    df = pd.read_csv(filename)

    # show datasets
    if st.checkbox("Show Dataset"):
        number = st.number_input("Number of Rows to View", 5,10)
        st.dataframe(df.head(number))

    # show columns
    df = pd.read_csv(filename)
    if st.button("Column Names"):
        st.write(df.columns)  

    # show shape
    if st.checkbox("Shape of Datesets"):
        
        data_dim    = st.radio("Data Dimension By ", ("Rows", "Columns"))
        
        if data_dim  == 'Rows':
            st.text("Number of Rows")
            st.write(df.shape[0])  

        elif data_dim  == 'Columns':
            st.text("Number of Columns")
            st.write(df.shape[1])
        else:
            st.write(df.shape)

    # show columns
    if st.checkbox("Selected Columns to Show"):
        all_columns         =   df.columns.tolist()
        selected_columns    =   st.multiselect("Select", all_columns)
        new_df              =   df[selected_columns]
        st.dataframe(new_df)

    # Plot and visualization
    st.subheader("Data Visualization")

    # Seaborn Plot
    if st.checkbox("Correlation Plot by Seaborn"):
        st.write(sns.heatmap(df.corr(), annot=True))
        st.pyplot()
        st.set_option('deprecation.showPyplotGlobalUse', False)

    if st.checkbox("Pie Plot"):
        all_columns_names       = df.columns.tolist()
        if st.button("Generate Plot"):
            st.success("Generating a Pie Plot")
            st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%"))
            st.pyplot()

    st.subheader("Customizable Plot")
    all_columns_names       = df.columns.tolist()
    type_of_plot            = st.selectbox("Select Type of Plot", ["area", "bar", "line","hist", "box", "kde"])
    selected_columns_names  = st.multiselect("Select Columns to Plot", all_columns_names)

    if st.button("Generate Customizable Plot"):
        st.success("Generating plot of {} for {}".format(type_of_plot, selected_columns_names ))

        #Plot by Streamlit
        if type_of_plot     ==   'area':
            custom_data     =   df[selected_columns_names]
            my_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.1)
                my_bar.progress(percent_complete + 1)
            st.area_chart(custom_data)
            st.success('{} plot created'.format(type_of_plot))

        elif type_of_plot     ==   'bar':
            custom_data     =   df[selected_columns_names]
            my_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.1)
                my_bar.progress(percent_complete + 1)
            st.bar_chart(custom_data)
            st.success('{} plot created'.format(type_of_plot))
        
        elif type_of_plot     ==   'line':
            custom_data     =   df[selected_columns_names]
            st.line_chart(custom_data)

        elif type_of_plot     ==   'box':
            custom_plot     =   df[selected_columns_names].plot(kind=type_of_plot)
            st.write(custom_plot)
            st.plyplot()


    # About
    st.sidebar.header("Delhi Visualization")
    st.sidebar.info("Visualizing Delhi Data")
    st.sidebar.markdown("[Common ML Dataset Repo]")




if __name__ == '__main__':
    main()