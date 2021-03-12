import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import time
from country_mappings import COUNTRY_MAPPINGS
from indicators_mappings import INDICATORS_MAPPINGS

matplotlib.use('Agg')

def main():
    st.title("Delhi and Dhaka Data")
    st.markdown("Select a city to view different charts of various indicators. ")

    #st.markdown(html_temp, unsafe_allow_html=True )

    
    city = st.sidebar.selectbox(label = "Select a City", index = 0,
                               options = list(COUNTRY_MAPPINGS.values()))

    
    indicator = st.sidebar.selectbox("Select the Indicators", index = 0,
                               options = list(INDICATORS_MAPPINGS.values()))
 

    st.subheader( city + ' area chat with all the indicators')

    folder_path='datasets'
    selected_filename = 'final.csv'
    filename = os.path.join(folder_path, selected_filename)

    # Reading Data
    df = pd.read_csv(filename, usecols = ['Ward_No','Ward_Name', 'Area', 'geometry','No_HH','TOT_P','TOT_M','TOT_F','ch_t_t','tenure_o','l_elect','hh_with_lat', 'no_latr', 'latr_pub', 'latr_o', 'have_bath','cf_fw', 'cf_lpg', 'kf_t','hh_bank','asset_bic', 'asset_2w', 'asset_4w', 'asset_tv_c'])

    
    selected_columns_df = ['Ward_No','Ward_Name', 'geometry','No_HH','TOT_P','TOT_M','TOT_F','ch_t_t','tenure_o','l_elect','hh_with_lat', 'no_latr', 'latr_pub', 'have_bath','cf_fw', 'cf_lpg', 'kf_t','hh_bank', 'asset_bic', 'asset_2w', 'asset_4w', 'asset_tv_c']
    df = df[selected_columns_df]


    
    st.subheader( city + ' - ' + indicator)
    #drawing first chat
    
    st.area_chart(df[['TOT_P','TOT_M','TOT_F']], use_container_width = False, width = 800)

    # show datasets
    if st.checkbox("Select to see first 10 Dataset"):
        st.dataframe(df.head(10))
        #number = st.number_input("Number of Rows to View", 5,10)
        #st.dataframe(df.head(number))

    # show columns
    #df = pd.read_csv(filename)
    if st.button("Click to see all the column names"):
        st.write(df.columns)  

    

    # show columns
    if st.checkbox("Selected Columns to Show"):
        all_columns         =   df.columns.tolist()
        selected_columns    =   st.multiselect("Select", all_columns)
        new_df              =   df[selected_columns]
        st.dataframe(new_df)

    # Plot and visualization
    
    #st.subheader("Data Visualization")

    # Seaborn Plot
    #if st.checkbox("Correlation Plot by Seaborn"):
    #    st.write(sns.heatmap(df.corr(), annot=True))
    #    st.pyplot()
    #    st.set_option('deprecation.showPyplotGlobalUse', False)

    #if st.checkbox("Pie Plot"):
    #    all_columns_names       = df.columns.tolist()
    #    if st.button("Generate Plot"):
    #        st.success("Generating a Pie Plot")
    #        st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%"))
    #        st.pyplot()

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





if __name__ == '__main__':
    main()