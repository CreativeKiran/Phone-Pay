#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np
import json
import os


# In[15]:


path_1="C:/Users/akkal/Downloads/pulse-master/aggregated/transaction/country/india/state/" 
agg_tran_state_list=os.listdir(path_1)

agg_transaction ={"State":[],"Year":[],"Quarter":[],"Agg_Transaction_Type":[],"Agg_Transaction_Count":[],"Agg_Transaction_Amount":[]}

for i in agg_tran_state_list:
    path_a= path_1 + i + "/"
    agg_year=os.listdir(path_a)
    
    for j in agg_year:
        path_b=path_a + j + "/"
        agg_quarter=os.listdir(path_b)
        
        for k in agg_quarter:
            path_c=path_b + k
            data= open(path_c,'r')
            Main_data=json.load(data)
            
            try:
                for L in Main_data["data"]["transactionData"]:
                    for M in L["paymentInstruments"]: 
                     count_name=M["count"]
                     amount_name=M["amount"]
                     agg_transaction["State"].append(i)
                     agg_transaction["Year"].append(j)
                     agg_transaction["Quarter"].append(int(k.strip('.json')))
                     agg_transaction["Agg_Transaction_Type"].append(L['name'])
                     agg_transaction["Agg_Transaction_Count"].append(count_name)
                     agg_transaction["Agg_Transaction_Amount"].append(amount_name)
            
            except:
                pass
                     


            
            
df_aggregated_transaction=pd.DataFrame(agg_transaction)        

 


# In[16]:


df_aggregated_transaction


# In[27]:


df_aggregated_transaction.to_csv("C:/Users/akkal/Downloads/phonepay_dataset/.csv", index=False)


# In[30]:


path_2 = "C:/Users/akkal/Downloads/pulse-master/aggregated/user/country/india/state/"
Agg_user_state_list = os.listdir(path_2)

Agg_user = {'State': [], 'Year': [], 'Quarter': [], 'Agg_User_Brands': [], 'Agg_User_Count': [], 'Agg_User_Percentage': []}

for i in Agg_user_state_list:
    path_a = path_2 + i + "/"
    Agg_yr = os.listdir(path_a)

    for j in Agg_yr:
        path_b = path_a + j + "/"
        agg_quarter = os.listdir(path_b)

        for k in agg_quarter:
            path_c = path_b + k
            data = open(path_c, 'r')
            Main_data = json.load(data)

            try:
                for L in Main_data["data"]["usersByDevice"]:
                    brand_name = L["brand"]
                    count_ = L["count"]
                    ALL_percentage = L["percentage"]
                    Agg_user["State"].append(i)
                    Agg_user["Year"].append(j)
                    Agg_user["Quarter"].append(int(k.strip('.json')))
                    Agg_user["Agg_User_Brands"].append(brand_name)
                    Agg_user["Agg_User_Count"].append(count_)
                    Agg_user["Agg_User_Percentage"].append(ALL_percentage * 100)
            except:
                pass

df_aggregated_user = pd.DataFrame(Agg_user)


# In[31]:


df_aggregated_user


# In[32]:


df_aggregated_user.to_csv("C:/Users/akkal/Downloads/phonepay_dataset/user.csv",index=False)


# In[33]:


path_3 ="C:/Users/akkal/Downloads/pulse-master/map/transaction/hover/country/india/state/"
map_trans_state_list = os.listdir(path_3)

map_trans = {'State':[],'Year':[],'Quarter':[],'District':[],'Dist_Transaction_Count':[],'Dist_Transaction_Amount':[]}

for i in map_trans_state_list:
    path_a = path_3 + i + "/"
    agg_yr = os.listdir(path_a)
    
    for j in Agg_yr:
        path_b = path_a + j + "/"
        agg_quarter = os.listdir(path_b)
        
        for k in agg_quarter:
            path_c = path_b + k 
            data= open(path_c,'r')
            Main_data = json.load(data)
            
            try:
                for l in Main_data['data']['hoverDataList']:
                    
                    for m in l['metric']:
                        Trans_count= m['count']
                        Trans_amount=m['amount']
                    
                        map_trans['State'].append(i)
                        map_trans['Year'].append(j)
                        map_trans['Quarter'].append(int(k.strip('.json')))
                        map_trans['District'].append(l['name'])
                        map_trans['Dist_Transaction_Count'].append(Trans_count)
                        map_trans['Dist_Transaction_Amount'].append(Trans_amount)
            except:
                pass
map_trans_list = pd.DataFrame(map_trans)


# In[34]:


map_trans_list


# In[36]:


map_trans_list.to_csv("C:/Users/akkal/Downloads/phonepay_dataset/trans.csv",index=False)


# In[37]:


path_4="C:/Users/akkal/Downloads/pulse-master/map/user/hover/country/india/state/"
map_user_state_list = os.listdir(path_4)

map_user = {"State":[],"Year":[],"Quarter":[],"District":[],"Dist_Registered_Users":[],"Dist_App_Opens":[]}

for i in map_user_state_list:
    path_a = path_4 + i + "/"
    map_yr = os.listdir(path_a)
    
    for j in map_yr:
        path_b = path_a + j + "/"
        map_quarter = os.listdir(path_b)
        
        for k in map_quarter:
            path_c = path_b + k
            data = open(path_c,"r")
            Main_data = json.load(data)
            
            try:
                for dist,info in Main_data['data']['hoverData'].items():
                    district_name = dist
                    reg_users=info['registeredUsers']
                    app_opens=info['appOpens']
                    
                    map_user['State'].append(i)
                    map_user['Year'].append(j)
                    map_user["Quarter"].append(int(k.strip('.json')))
                    map_user["District"].append(district_name)
                    map_user["Dist_Registered_Users"].append(reg_users)
                    map_user['Dist_App_Opens'].append(app_opens)
            except:
                pass
            
map_user_list=pd.DataFrame(map_user)


# In[38]:


map_user_list


# In[39]:


map_user_list.to_csv("C:/Users/akkal/Downloads/phonepay_dataset/map_user.csv",index=False)


# In[40]:


path_5 = "C:/Users/akkal/Downloads/pulse-master/top/transaction/country/india/state/"
top_trans_state_list=os.listdir(path_5)

top_trans_dist = {"State":[],"Year":[],"Quarter":[],"District":[],"Trans_count":[],"Trans_amount":[]}

for i in top_trans_state_list:
    path_a = path_5 + i + "/"
    top_yr = os.listdir(path_a)
    for j in top_yr:
        path_b = path_a + j + "/"
        top_quarter =os.listdir(path_b)
        for k in top_quarter:
            path_c= path_b + k
            data=open(path_c,'r')
            Main_data=json.load(data)
            
            try:
                for l in Main_data['data']['districts']:
                    dist_name = l['entityName']
                    trans_count=l['metric']['count']
                    trans_amount=l['metric']['amount']
                    top_trans_dist["State"].append(i)
                    top_trans_dist["Year"].append(j)
                    top_trans_dist["Quarter"].append(int(k.strip('.json')))
                    top_trans_dist["District"].append(dist_name)
                    top_trans_dist["Trans_count"].append(trans_count)
                    top_trans_dist["Trans_amount"].append(Trans_amount)
            except:
                pass
            
top_trans_district =pd.DataFrame(top_trans_dist)


# In[41]:


top_trans_district


# In[42]:


top_trans_district.to_csv("C:/Users/akkal/Downloads/phonepay_dataset/top_tran_drist.csv",index=False)


# In[43]:


path_6 = "C:/Users/akkal/Downloads/pulse-master/top/transaction/country/india/state/"
top_trans_state_list=os.listdir(path_6)

top_trans_pin = {"State":[],"Year":[],"Quarter":[],"Pin_code":[],"Pin_Trans_count":[],"Pin_Trans_amount":[]}

for i in top_trans_state_list:
    path_a = path_6 + i + "/"
    top_yr = os.listdir(path_a)
    for j in top_yr:
        path_b = path_a + j + "/"
        top_quarter =os.listdir(path_b)
        for k in top_quarter:
            path_c= path_b + k
            data=open(path_c,'r')
            Main_data=json.load(data)
            
            try:
                for l in Main_data['data']['pincodes']:
                    pin_code = l['entityName']
                    trans_count=l['metric']['count']
                    trans_amount=l['metric']['amount']
                    top_trans_pin["State"].append(i)
                    top_trans_pin["Year"].append(j)
                    top_trans_pin['Quarter'].append(int(k.strip('.json')))
                    top_trans_pin["Pin_code"].append(pin_code)
                    top_trans_pin["Pin_Trans_count"].append(trans_count)
                    top_trans_pin['Pin_Trans_amount'].append(trans_amount)
            except:
                pass
            
top_trans_pincode = pd.DataFrame(top_trans_pin)


# In[44]:


top_trans_pincode 


# In[45]:


top_trans_pincode.to_csv("C:/Users/akkal/Downloads/phonepay_dataset/top_tran_pincode.csv",index=False)


# In[46]:


path_7 = "C:/Users/akkal/Downloads/pulse-master/top/user/country/india/state/"
top_trans_state_list=os.listdir(path_7)

top_user_pin = {"State":[],"Year":[],"Quarter":[],"Pin_code":[],"Pin_Registered_Users":[]}

for i in top_trans_state_list:
    path_a = path_7 + i + "/"
    top_yr = os.listdir(path_a)
    for j in top_yr:
        path_b = path_a + j + "/"
        top_quarter =os.listdir(path_b)
        for k in top_quarter:
            path_c= path_b + k
            data=open(path_c,'r')
            Main_data=json.load(data)
            for l in Main_data['data']['pincodes']:
              pin_code = l['name']
              Reg_Users= l['registeredUsers']
              top_user_pin["State"].append(i)
              top_user_pin["Year"].append(j)
              top_user_pin['Quarter'].append(int(k.strip('.json')))
              top_user_pin["Pin_code"].append(pin_code)
              top_user_pin["Pin_Registered_Users"].append(Reg_Users)
            

top_user_pin_list =pd.DataFrame(top_user_pin)


# In[47]:


top_user_pin_list


# In[53]:


top_user_pin_list.to_csv("C:/Users/akkal/Downloads/phonepay_dataset/top_user_pin.csv",index=False)


# In[54]:


path_8="C:/Users/akkal/Downloads/pulse-master/top/user/country/india/state/"
top_user_statelist =os.listdir(path_8)

top_user_list = {"State":[],"Year":[],"Quarter":[],"District":[],"Registered_Users":[]}

for i in top_user_statelist:
    path_a = path_8 + i + "/"
    user_year = os.listdir(path_a)
    for j in user_year:
        path_b = path_a + j + "/"
        user_quarter = os.listdir(path_b)
        for k in user_quarter:
            path_c = path_b + k
            data = open(path_c,'r')
            Main_data= json.load(data)
            for l in Main_data['data']['districts']:
                dist_name = l['name']
                reg_users = l['registeredUsers']
                top_user_list["State"].append(i)
                top_user_list["Year"].append(j)
                top_user_list["Quarter"].append(int(k.strip('.json')))
                top_user_list["District"].append(dist_name)
                top_user_list["Registered_Users"].append(reg_users)
                
top_user_details = pd.DataFrame(top_user_list)


# In[55]:


top_user_details


# In[56]:


top_user_details.to_csv("C:/Users/akkal/Downloads/phonepay_dataset/top_user_details.csv",index=False)


# In[ ]:




