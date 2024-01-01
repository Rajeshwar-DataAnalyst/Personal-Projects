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

    # st.dataframe(df)
    user_list = df['user'].unique().tolist()
    user_list.remove('notification')
    user_list.sort()
    user_list.insert(0,"Overall")

    selected_user = st.sidebar.selectbox("Choose User", user_list)


    if st.sidebar.button('Analyze'):

        num_messages, words, media, links = helper.fetch_stats(selected_user, df)
        st.title('Top Statistics')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Media Shared")
            st.title(media)
        with col4:
            st.header("links Shared")
            st.title(links)

        #daily timeline
        st.title('Daily Timeline')
        daily_timeline = helper.daily_timeline(selected_user,df)
        fig,ax = plt.subplots()
        ax.plot(daily_timeline['only_date'],daily_timeline['message'],color = 'black')
        plt.xticks(rotation = 90)
        st.pyplot(fig)


        #monthly timeline
        st.title('Monthly Timeline')
        timeline = helper.monthly_timeline(selected_user,df)
        fig,ax = plt.subplots()
        ax.plot(timeline['time'],timeline['message'],color = '#00cc00')
        plt.xticks(rotation = 90)
        st.pyplot(fig)


        #Activity Map
        st.title('Activity Map')
        col1, col2 = st.columns(2)

        with col1:
            st.header('Most busy day')
            busy_day = helper.week_activity_map(selected_user,df)
            fig,ax = plt.subplots()
            ax.bar(busy_day.index,busy_day.values,color = '#cc9900')
            plt.xticks(rotation = 90)
            st.pyplot(fig)

        with col2:
            st.header('Most busy Month')
            busy_Month = helper.month_activity_map(selected_user,df)
            fig,ax = plt.subplots()
            ax.bar(busy_Month.index,busy_Month.values,color = '#0066ff')
            plt.xticks(rotation = 90)
            st.pyplot(fig)
        
        st.title('Weekly Activity Map')
        user_heatmap = helper.activity_heatmap(selected_user,df)
        fig,ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)


        if selected_user == 'Overall':
            st.title('Most Busy User')
            x, new_df = helper.most_busy_user(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values,color = 'red')
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

        # st.title('Pair Plot')
        # fig,ax = plt.subplots()
        # ax = sns.pairplot(df)
        # st.pyplot(fig)











        # # emoji analysis
        # st.title("Emoji's Analysis")
        # emoji_df = helper.emoji_helper(selected_user,df)
        # st.dataframe(emoji_df)

        # col1,col2 = st.columns(2)

        # with col1:
        #     st.dataframe(emoji_df)
        # with col2:
        #     fig,ax = plt.subplots()
        #     ax.pie(emoji_df[1].head(5),labels = emoji_df[0])
        #     st.pyplot(fig)
