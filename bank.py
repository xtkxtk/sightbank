import json
import streamlit as st
with open('banklist.json', 'rt', encoding='UTF8') as f:
    data = json.load(f)

print(type(data))

t_name=""
b_name=""
t_name2=""
b_name2=""
t_m=0
b_m=0
tex=0
passward=''
def loading():
    st.warning('Wait for it...')
    global t_name,b_name,t_m,b_m,by,to,much,tex,passward,pw,t_name2,b_name2

    t_name=to
    passward=pw
    b_name=by
    
    for i in data.keys():
        if t_name in i:
            t_m = data[i]
            t_name2=i
    for i in data.keys():
        if b_name in i:
            b_m = data[i]
            b_name2=i
    t_m = data[t_name2]
    b_m = data[b_name2]
    tex = data['tex-chw_dcdr430127']

    #t_name=t_name.split('-')[0]
    #passward=t_name.split('-')[1]
    #b_name=b_name.split('-')[0]

def sending():
    
    global t_name,b_name,t_m,b_m,by,to,much,tex,pw,passward,data
    if(by=="admin-090927"):
        st.write(data)
    loading()
    print(t_name2)
    
    if(str(pw)==b_name2.split('-')[1]):
        much=int(much)

        if '!' in b_name:
            print('j')
            
            tex=tex+round(much*0.01)
            t_m=t_m+much-round(much*0.01)
            b_m=b_m-much

            data[t_name2]=t_m
            data[b_name2]=b_m
            data['sightbank-430127']=tex

            st.write(b_m+much,'=>',b_m)
            st.write(t_m,'=>',t_m-round(much*0.01))
            st.write('GAS',round(much*0.01))
            with open('banklist.json', 'w') as outfile:
                json.dump(data, outfile)
            st.image(
            "https://i.ibb.co/z5Th2F7/001-57.png",
            width=400, # Manually Adjust the width of the image as per requirement
        )
            st.success("Success")
        else:
            print('dcdr')

            t_m=t_m+round(much*0.7)
            b_m=b_m-much
            tex=tex+round(much*0.3)

            data[t_name2]=t_m
            data[b_name2]=b_m
            data['tex-chw_dcdr430127']=tex

            st.write(b_m+much,'=>',b_m)
            st.write(t_m-round(much*0.7),'=>',t_m)
            with open('banklist.json', 'w', encoding='utf-8') as outfile:
                json.dump(data, outfile,ensure_ascii=False)
            st.image(
            "https://i.ibb.co/z5Th2F7/001-57.png",
            width=400, # Manually Adjust the width of the image as per requirement
        )
            st.success("Success")
    else:
        st.error("PW incorrect")
        

st.title('juan and sight bank')
by = st.text_input('Your account')
pw = st.text_input('Your passward',type="password")
to = st.text_input('Recipent\'s account')
much = st.number_input('amount to be remitted')
if st.button('remmit'):
    sending()
