#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pickle
import pandas as pd 
import numpy as np
import datetime
import time



def main():
    
    st.title("Flight Fare Prediction")
    

    st.sidebar.subheader("Departure_details:")
    month = pd.to_datetime("today").month
    day = pd.to_datetime("today").day
    year = pd.to_datetime("today").year
    
    depart = st.sidebar.date_input("Date" , datetime.date(year,month,day))
    if depart is not None:
        mon_dep = depart.month
        day_dep = depart.day

        hour_dep = st.sidebar.selectbox("Hour", list(range(0,24)))
        minute_dep = st.sidebar.selectbox("Minute", list(range(0,60)))

    st.subheader("Departure Timing :")
    x = "2020" + "/"  +str(mon_dep) + "/" + str(day_dep) + " " + str(hour_dep) + ":" + str(minute_dep)
    if x is not None:
        
        tim = pd.to_datetime(x)
        if tim is not None:
            st.write(tim)
    

    st.sidebar.subheader("Arrival_details:")
    arrival = st.sidebar.date_input("Date:" , datetime.date(year,month,day))
    if arrival is not None:
    
        mon_arr = arrival.month
        day_arr = arrival.day
        
        

        hour_arr = st.sidebar.selectbox("Hour:", list(range(0,24)))
        minute_arr = st.sidebar.selectbox("Minute:", list(range(0,60)))

    st.subheader("Arrival Timing :")
    x0 = "2020" + "/"  +str(mon_arr) + "/" + str(day_arr) + " " + str(hour_arr) + ":" + str(minute_arr)
    if x0 is not None:
        
        tim1 = pd.to_datetime(x0)
        if tim1 is not None:
            st.write(tim1)
            



     #source
    st.subheader("Select Source city:")
    source = st.selectbox("" , ['Bangalore', 'Mumbai','Delhi','Kolkata',"Chennai"])
    if source == "Bangalore":
        source_inp = 0
    elif source == "Chennai":
        source_inp = 1
    elif source == "Delhi":
        source_inp = 2
    elif source == "Kolkata":
        source_inp = 3
    elif source == "Mumbai":
        source_inp = 4
    
    st.write("Source is: " , source)

    #destination
    st.subheader("Select Destination")
    dest = st.selectbox("" , ['Bangalore', 'Cochin', 'Hyderabad','Delhi','Kolkata'])

    if dest == "Bangalore":
        dest_inp = 0
    elif dest == "Cochin":
        dest_inp = 1
    elif dest == "Delhi":
        dest_inp = 2
    elif dest == "Hyderabad":
        dest_inp = 3
    elif dest == "Kolkata":
        dest_inp = 4
    

    st.write("Destination -->--> ",dest)

    #airline
    st.subheader("Select Airline")
    airline = st.selectbox("  " , ["Air India","GoAir","IndiGo","Jet Airways","Multiple carriers","SpiceJet",
                                    "Vistara","Air Asia"])

    if airline == "Jet Airways":
        air_inp = 4
    elif airline == "IndiGo":
        air_inp = 3
    elif airline == "Air India":
        air_inp = 1
    elif airline == "Multiple carriers":
        air_inp = 5
    elif airline == "SpiceJet":
        air_inp = 6
    elif airline == "Vistara":
        air_inp = 7
    elif airline == "Air Asia":
        air_inp = 0
    elif airline == "GoAir":
        air_inp = 2

    st.write("Airline -->--> " , airline)
    

    st.subheader("no_of_stops")
    stops=st.selectbox("",[0,3,1,2])

    if stops==0:
      stop_inp=3
    
    elif stops==1:
      stop_inp=0
    
    elif stops==2:
      stop_inp=1
    
    elif stops==3:
      stop_inp=2


    st.write("Stops -->--> ", stops)

    if st.checkbox("Duration"):
        if tim1 is not None:
            
            st.write((tim1 - tim))
            
    
    tim2 = str(tim1-tim)
    if tim2 is not None:
        hr = int(tim2.split(':')[0][-2:])
        mini = int(tim2.split(':')[1])
        st.subheader("Duration hrs: ")
        st.write(hr)
        st.subheader("Duration mins: ")
        st.write(mini)

   

    xgb_model = pickle.load(open("xgs_12345.pickle.dat","rb"))

    #prediction

    par = [air_inp , source_inp , dest_inp ,stops , hour_dep , minute_dep , minute_arr,hour_arr ,hr, mini,mon_dep,day_dep]
    arrays=np.array(par,dtype="int64")
    
    
    if st.checkbox("PREDICT"):
        pred = xgb_model.predict([arrays])[0]
        st.write("Your Fare Price is : " , round(pred ,3)  , "INR")
        st.write("*Enjoy your ride....*")

    st.write("""    """)
    st.write("""    """)
   
        
    



if __name__ == "__main__":
    main()

