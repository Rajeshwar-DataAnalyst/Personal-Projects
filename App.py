import streamlit as st
import preprocessor
import helper
import seaborn as sns
import matplotlib.pyplot as plt
st.sidebar.title('WhatApps_Chat_Analyzer')
upload_file = st.sidebar.file_uploader('Upload File')
if upload_file is not None:
    bytes_data = upload_file.getvalue()
    data = bytes_data.decode('utf-8')
    df = preprocessor.preprocess(data)

    st.dataframe(df)
    user_list = df['user'].unique().tolist()
    user_list.remove('notification')
    user_list.sort()
    user_list.insert(0,"Overall")

    selected_user = st.sidebar.selectbox("Choose User", user_list)


    if st.sidebar.button('Analyze'):

        num_messages, words, media, links = helper.fetch_stats(selected_user, df)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Total Media Shared")
            st.title(media)
        with col4:
            st.header("Total links Shared")
            st.title(links)

        if selected_user == 'Overall':
            st.title('Most Busy User')
            x, new_df = helper.most_busy_user(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values,color = 'brown')
                plt.xticks(rotation = 'vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)
        st.title('Wordcloud')
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # most common words
        st.title('Most Common Words')
        most_common_df = helper.most_common_words(selected_user, df)

        fig, ax = plt.subplots()
        ax.barh(most_common_df[0],most_common_df[1])
        plt.xticks(rotation=90)
        st.pyplot(fig)

        st.dataframe(most_common_df)

        # emoji analysis
        st.title("Emoji's Analysis")
        emoji_df = helper.emoji_helper(selected_user,df)
        st.dataframe(emoji_df)

        col1,col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig,ax = plt.subplots()
            ax.pie(emoji_df[1].head(5),labels = emoji_df[0])
            st.pyplot(fig)
