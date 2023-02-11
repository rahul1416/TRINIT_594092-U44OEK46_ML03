import streamlit as st
import pickle
import numpy as np
from temp import find_Current_Weather
import datetime
from Rainfall import give_Rainfall

# def add_bg_from_url():
#     st.markdown(
#          f"""
#          <style>
#          .stApp {{
#              background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
#              background-attachment: fixed;
#              background-size: cover
#          }}
#          </style>
#          """,
#          unsafe_allow_html=True
#      )

# add_bg_from_url() 

# page_bg_img="""
# <style>
#     [data-testid="stAppViewContainer"]{
#         background-image: url("https://img.freepik.com/free-photo/sunny-meadow-landscape_1112-134.jpg?w=2000&t=st=1676146888~exp=1676147488~hmac=36da3c992667d0d73abf51b818ef33cda446a2dbe4cbb75d7ceaf8adbc1d5707");
#         background-size: cover;
#     }
# </style>"""

# st.markdown(page_bg_img, unsafe_allow_html=True)



def load_modelREg():
    with open('LogREgmodel.pkl','rb') as file:
        leg_data=pickle.load(file)
    return leg_data

linear_Reg_Model=load_modelREg()

def load_modelKnn():
    with open('Knnmodel.pkl','rb') as file:
        knn_data=pickle.load(file)
    return knn_data
KNN_Model=load_modelKnn()

def load_modelRF():
    with open('RFmodel.pkl','rb') as file:
        Rf_data=pickle.load(file)
    return Rf_data
Rainforest_Model=load_modelRF()

def showpredict_page():
    st.title("Crop Prediction")

    st.write("""### We need some information to predict the Crop.""")

    states = {'ANDAMAN And NICOBAR ISLANDS', 'ARUNACHAL PRADESH', 'ASSAM',
       'MEGHALAYA', 'MANIPUR', 'MIZORAM', 'NAGALAND', 'TRIPURA',
       'WEST BENGAL', 'SIKKIM', 'ORISSA', 'JHARKHAND', 'BIHAR',
       'UTTAR PRADESH', 'UTTARANCHAL', 'HARYANA', 'CHANDIGARH', 'DELHI',
       'PUNJAB', 'HIMACHAL', 'JAMMU AND KASHMIR', 'RAJASTHAN',
       'MADHYA PRADESH', 'GUJARAT', 'DADAR NAGAR HAVELI', 'DAMAN AND DUI',
       'MAHARASHTRA', 'GOA', 'CHATISGARH', 'ANDHRA PRADESH', 'TAMIL NADU',
       'PONDICHERRY', 'KARNATAKA', 'KERALA', 'LAKSHADWEEP'}

    state_dis={'ANDAMAN And NICOBAR ISLANDS': ['NICOBAR', 'SOUTH ANDAMAN', 'N & M ANDAMAN'],
 'ARUNACHAL PRADESH': ['LOHIT',
  'EAST SIANG',
  'SUBANSIRI F.D',
  'TIRAP',
  'ANJAW (LOHIT)',
  'LOWER DIBANG',
  'CHANGLANG',
  'PAPUM PARE',
  'LOW SUBANSIRI',
  'UPPER SIANG',
  'WEST SIANG',
  'DIBANG VALLEY',
  'WEST KAMENG',
  'EAST KAMENG',
  'TAWANG(W KAME',
  'KURUNG KUMEY'],
  'Chattisgarh':['Raipur'],
  'Telangana':['Warangal'],
 'ASSAM': ['CACHAR',
  'DARRANG',
  'GOALPARA',
  'KAMRUP',
  'LAKHIMPUR',
  'NORTH CACHAR',
  'NAGAON',
  'SIVASAGAR',
  'BARPETA',
  'DHUBRI',
  'DIBRUGARH',
  'JORHAT',
  'KARIMGANJ',
  'KOKRAJHAR',
  'SHONITPUR',
  'GOLAGHAT',
  'TINSUKIA',
  'HAILAKANDI',
  'DHEMAJI(LAKHI',
  'KARBI ANGLONG',
  'UDALGURI(DARA',
  'KAMRUP METROP',
  'CHIRANG(BONGAI',
  'BAKSA BARPETA',
  'BONGAIGAON',
  'MORIGAON',
  'NALBARI'],
 'MEGHALAYA': ['EAST KHASI HI',
  'JAINTIA HILLS',
  'EAST GARO HIL',
  'RI-BHOI',
  'SOUTH GARO HI',
  'W KHASI HILL',
  'WEST GARO HIL'],
 'MANIPUR': ['IMPHAL EAST',
  'SENAPATI',
  'TAMENGLONG',
  'CHANDEL',
  'UKHRUL',
  'THOUBAL',
  'BISHNUPUR',
  'IMPHAL WEST',
  'CHURACHANDPUR'],
 'MIZORAM': ['AIZAWL',
  'CHAMPHAI',
  'KOLASIB',
  'LUNGLEI',
  'CHHIMTUIPUI',
  'LAWNGTLAI',
  'MAMIT',
  'SAIHA',
  'SERCHHIP'],
 'NAGALAND': ['KOHIMA',
  'TUENSANG',
  'MOKOKCHUNG',
  'DIMAPUR',
  'WOKHA',
  'MON',
  'ZUNHEBOTO',
  'PHEK',
  'KEPHRIE',
  'LONGLENG',
  'PEREN'],
 'TRIPURA': ['NORTH TRIPURA', 'SOUTH TRIPURA', 'WEST TRIPURA', 'DHALAI'],
 'WEST BENGAL': ['COOCH BEHAR',
  'DARJEELING',
  'JALPAIGURI',
  'MALDA',
  'SOUTH DINAJPUR',
  'NORTH DINAJPUR',
  'BANKURA',
  'BIRBHUM',
  'BURDWAN',
  'HOOGHLY',
  'HOWRAH',
  'PURULIA',
  'MURSHIDABAD',
  'NADIA',
  'NORTH 24 PARG',
  'SOUTH 24 PARG',
  'EAST MIDNAPOR',
  'WEST MIDNAPOR',
  'KOLKATA'],
 'SIKKIM': ['NORTH SIKKIM', 'EAST SIKKIM', 'WEST SIKKIM', 'SOUTH SIKKIM'],
 'ORISSA': ['BALASORE',
  'BOLANGIR',
  'KANDHAMAL/PHU',
  'CUTTACK',
  'DHENKANAL',
  'GANJAM',
  'KALAHANDI',
  'KEONDJHARGARH',
  'KORAPUT',
  'MAYURBHANJ',
  'PURI',
  'SAMBALPUR',
  'SUNDARGARH',
  'BHADRAK',
  'JAJPUR',
  'KENDRAPARA',
  'ANGUL',
  'NAWAPARA',
  'MALKANGIRI',
  'NAWARANGPUR',
  'NAYAGARH',
  'KHURDA',
  'BARGARH',
  'JHARSUGUDA',
  'DEOGARH',
  'RAYAGADA',
  'GAJAPATI',
  'JAGATSINGHAPU',
  'BOUDHGARH',
  'SONEPUR'],
 'JHARKHAND': ['BOKARO',
  'DHANBAD',
  'DUMKA',
  'HAZARIBAG',
  'PALAMU',
  'RANCHI',
  'SAHIBGANJ',
  'WEST SINGHBHUM',
  'DEOGHAR',
  'GIRIDIH',
  'GODDA',
  'GUMLA',
  'LOHARDAGA',
  'CHATRA',
  'KODERMA',
  'PAKUR',
  'EAST SINGHBHU',
  'GARHWA',
  'SERAIKELA-KHA',
  'JAMTARA',
  'LATEHAR',
  'SIMDEGA',
  'KHUNTI(RANCHI',
  'RAMGARH'],
 'BIHAR': ['BHAGALPUR',
  'EAST CHAMPARAN',
  'DARBHANGA',
  'GAYA',
  'MUNGER',
  'MUZAFFARPUR',
  'WEST CHAMPARAN',
  'PURNEA',
  'GOPALGANJ',
  'MADHUBANI',
  'AURANGABAD',
  'BEGUSARAI',
  'BHOJPUR',
  'NALANDA',
  'PATNA',
  'KATIHAR',
  'KHAGARIA',
  'SARAN',
  'MADHEPURA',
  'NAWADA',
  'ROHTAS',
  'SAMASTIPUR',
  'SITAMARHI',
  'SIWAN',
  'VAISHALI',
  'JAHANABAD',
  'BUXAR',
  'ARARIA',
  'BANKA',
  'BHABUA',
  'JAMUI',
  'KISHANGANJ',
  'SHEIKHPURA',
  'SUPAUL',
  'LAKHISARAI',
  'SHEOHAR',
  'ARWAL',
  'SAHARSA'],
 'UTTAR PRADESH': ['ALLAHABAD',
  'AZAMGARH',
  'BAHRAICH',
  'BALLIA',
  'BANDA',
  'BARABANKI',
  'BASTI',
  'DEORIA',
  'FAIZABAD',
  'FARRUKHABAD',
  'FATEHPUR',
  'GHAZIPUR',
  'GONDA',
  'GORAKHPUR',
  'HARDOI',
  'JAUNPUR',
  'KANPUR NAGAR',
  'KHERI LAKHIMP',
  'LUCKNOW',
  'MIRZAPUR',
  'PRATAPGARH',
  'RAE BARELI',
  'SITAPUR',
  'SULTANPUR',
  'UNNAO',
  'VARANASI',
  'SONBHADRA',
  'MAHARAJGANJ',
  'MAU',
  'SIDDHARTH NGR',
  'KUSHINAGAR',
  'AMBEDKAR NAGAR',
  'KANNAUJ',
  'BALRAMPUR',
  'KAUSHAMBI',
  'SAHUJI MAHARA',
  'KANPUR DEHAT',
  'CHANDAULI',
  'SANT KABIR NGR',
  'SANT RAVIDAS',
  'SHRAVASTI NGR',
  'AGRA',
  'ALIGARH',
  'BAREILLY',
  'BIJNOR',
  'BADAUN',
  'BULANDSHAHAR',
  'ETAH',
  'ETAWAH',
  'HAMIRPUR',
  'JALAUN',
  'JHANSI',
  'LALITPUR',
  'MAINPURI',
  'MATHURA',
  'MEERUT',
  'MORADABAD',
  'MUZAFFARNAGAR',
  'PILIBHIT',
  'RAMPUR',
  'SAHARANPUR',
  'SHAHJAHANPUR',
  'GHAZIABAD',
  'FIROZABAD',
  'MAHOBA',
  'MAHAMAYA NAGA',
  'AURAIYA',
  'BAGPAT',
  'JYOTIBA PHULE',
  'GAUTAM BUDDHA',
  'KANSHIRAM NAG'],
 'UTTARANCHAL': ['ALMORA',
  'CHAMOLI',
  'DEHRADUN',
  'GARHWAL PAURI',
  'NAINITAL',
  'PITHORAGARH',
  'GARHWAL TEHRI',
  'UTTARKASHI',
  'HARIDWAR',
  'CHAMPAWAT',
  'RUDRAPRAYAG',
  'UDHAM SINGH N',
  'BAGESHWAR'],
 'HARYANA': ['AMBALA',
  'GURGAON',
  'HISAR',
  'JIND',
  'KARNAL',
  'MAHENDRAGARH',
  'ROHTAK',
  'BHIWANI',
  'FARIDABAD',
  'KURUKSHETRA',
  'SIRSA',
  'SONEPAT(RTK)',
  'YAMUNANAGAR',
  'KAITHAL',
  'PANIPAT',
  'REWARI',
  'FATEHABAD',
  'JHAJJAR',
  'PANCHKULA',
  'MEWAT',
  'PALWAL(FRD)'],
 'CHANDIGARH': ['CHANDIGARH'],
 'DELHI': ['NEW DELHI',
  'CENTRAL DELHI',
  'EAST DELHI',
  'NORTH DELHI',
  'NE DELHI',
  'SW DELHI',
  'NW DELHI',
  'SOUTH DELHI',
  'WEST DELHI'],
 'PUNJAB': ['AMRITSAR',
  'BATHINDA',
  'FEROZEPUR',
  'GURDASPUR',
  'HOSHIARPUR',
  'JALANDHAR',
  'KAPURTHALA',
  'LUDHIANA',
  'PATIALA',
  'RUPNAGAR',
  'SANGRUR',
  'FARIDKOT',
  'MOGA',
  'NAWANSHAHR',
  'FATEHGARH SAH',
  'MUKTSAR',
  'MANSA',
  'BARNALA',
  'SAS NAGAR(MGA)',
  'TARN TARAN'],
 'HIMACHAL': ['BILASPUR',
  'CHAMBA',
  'KANGRA',
  'KINNAUR',
  'KULLU',
  'LAHUL & SPITI',
  'MANDI',
  'HAMIRPUR',
  'SHIMLA',
  'SIRMAUR',
  'SOLAN',
  'UNA'],
 'JAMMU AND KASHMIR': ['ANANTNAG',
  'BARAMULLA',
  'DODA',
  'JAMMU',
  'KATHUA',
  'LADAKH (LEH)',
  'UDHAMPUR',
  'BADGAM',
  'KUPWARA',
  'PULWAMA',
  'SRINAGAR',
  'KARGIL',
  'POONCH',
  'RAJOURI',
  'BANDIPORE',
  'GANDERWAL',
  'KULGAM/(ANT)',
  'SHOPAN',
  'SAMBA',
  'KISTWAR',
  'REASI',
  'RAMBAN(DDA)'],
 'RAJASTHAN': ['BARMER',
  'BIKANER',
  'CHURU',
  'SRI GANGANAGA',
  'JAISALMER',
  'JALORE',
  'JODHPUR',
  'NAGAUR',
  'PALI',
  'HANUMANGARH',
  'AJMER',
  'ALWAR',
  'BANSWARA',
  'BHARATPUR',
  'BHILWARA',
  'BUNDI',
  'CHITTORGARH',
  'DUNGARPUR',
  'JAIPUR',
  'JHALAWAR',
  'JHUNJHUNU',
  'KOTA',
  'SAWAI MADHOPUR',
  'SIKAR',
  'SIROHI',
  'TONK',
  'UDAIPUR',
  'DHOLPUR',
  'BARAN',
  'DAUSA',
  'RAJSAMAND',
  'KARAULI',
  'PRATAPGARH(CHT'],
 'MADHYA PRADESH': ['BETUL',
  'VIDISHA',
  'BHIND',
  'DATIA',
  'DEWAS',
  'DHAR',
  'GUNA',
  'GWALIOR',
  'HOSHANGABAD',
  'INDORE',
  'JHABUA',
  'MANDSAUR',
  'MORENA',
  'KHANDWA',
  'KHARGONE',
  'RAISEN',
  'RAJGARH',
  'RATLAM',
  'SEHORE',
  'SHAJAPUR',
  'SHIVPURI',
  'UJJAIN',
  'BHOPAL',
  'HARDA',
  'NEEMUCH',
  'SHEOPUR',
  'BARWANI',
  'ASHOKNAGAR(GNA',
  'BURHANPUR',
  'ALIRAJPUR(JBA)',
  'BALAGHAT',
  'CHHATARPUR',
  'CHHINDWARA',
  'JABALPUR',
  'MANDLA',
  'NARSINGHPUR',
  'PANNA',
  'REWA',
  'SAGAR',
  'SATNA',
  'SEONI',
  'SHAHDOL',
  'SIDHI',
  'TIKAMGARH',
  'KATNI',
  'DINDORI',
  'UMARIA',
  'DAMOH',
  'ANUPPUR(SHAHD',
  'SINGRAULI'],
 'GUJARAT': ['AHMEDABAD',
  'BANASKANTHA',
  'BARODA',
  'BHARUCH',
  'VALSAD',
  'DANGS',
  'KHEDA',
  'MEHSANA',
  'PANCHMAHALS',
  'SABARKANTHA',
  'SURAT',
  'GANDHINAGAR',
  'NARMADA(BRC)',
  'NAVSARI(VSD)',
  'ANAND(KHR)',
  'PATAN(MHSN)',
  'DAHOD(PNML)',
  'TAPI(SRT)',
  'AMRELI',
  'BHAVNAGAR',
  'JAMNAGAR',
  'JUNAGADH',
  'KUTCH',
  'RAJKOT',
  'SURENDRANAGAR',
  'PORBANDAR'],
 'DADAR NAGAR HAVELI': ['DNH'],
 'DAMAN AND DUI': ['DAMAN', 'DIU'],
 'MAHARASHTRA': ['MUMBAI CITY',
  'RAIGAD',
  'RATNAGIRI',
  'THANE',
  'SINDHUDURG',
  'MUMBAI SUB',
  'AHMEDNAGAR',
  'DHULE',
  'JALGAON',
  'KOLHAPUR',
  'NASHIK',
  'PUNE',
  'SANGLI',
  'SATARA',
  'SOLAPUR',
  'NANDURBAR',
  'AURANGABAD',
  'BEED',
  'NANDED',
  'OSMANABAD',
  'PARBHANI',
  'LATUR',
  'JALNA',
  'HINGOLI',
  'AKOLA',
  'AMRAVATI',
  'BHANDARA',
  'BULDHANA',
  'CHANDRAPUR',
  'NAGPUR',
  'YAVATMAL',
  'WARDHA',
  'GADCHIROLI',
  'WASHIM',
  'GONDIA'],
 'GOA': ['NORTH GOA', 'SOUTH GOA'],
 'CHATISGARH': ['BASTAR',
  'BILASPUR',
  'DURG',
  'RAIGARH',
  'RAIPUR',
  'SURGUJA',
  'RAJNANDGAON',
  'DANTEWADA',
  'KANKER (NORH',
  'JANJGIR-CHAMP',
  'KORBA',
  'JASHPUR',
  'DHAMTARI',
  'MAHASAMUND',
  'KORIYA',
  'KOWARDHA (KAB',
  'NARAYANPUR',
  'BIJAPUR'],
 'ANDHRA PRADESH': ['EAST GODAVARI',
  'WEST GODAVARI',
  'GUNTUR',
  'KRISHNA',
  'NELLORE',
  'PRAKASAM',
  'SRIKAKULAM',
  'VISAKHAPATNAM',
  'VIZIANAGARAM',
  'ADILABAD',
  'HYDERABAD',
  'KARIMNAGAR',
  'KHAMMAM',
  'MAHABUBNAGAR',
  'MEDAK',
  'NALGONDA',
  'NIZAMABAD',
  'WARANGAL',
  'RANGAREDDY',
  'ANANTAPUR',
  'CHITTOOR',
  'KUDDAPAH',
  'KURNOOL'],
 'TAMIL NADU': ['VELLORE',
  'COIMBATORE',
  'DHARMAPURI',
  'KANYAKUMARI',
  'CHENNAI',
  'MADURAI',
  'NILGIRIS',
  'RAMANATHAPURA',
  'SALEM',
  'THANJAVUR',
  'TIRUCHIRAPPAL',
  'TIRUNELVELI',
  'ERODE',
  'PUDUKKOTTAI',
  'DINDIGUL',
  'VIRUDHUNAGAR',
  'SIVAGANGA',
  'THOOTHUKUDI',
  'TIRUVANNAMALA',
  'NAGAPATTINAM',
  'VILUPPURAM',
  'CUDDALORE',
  'KANCHIPURAM',
  'TIRUVALLUR',
  'THENI',
  'NAMAKKAL',
  'KARUR',
  'PERAMBALUR',
  'TIRUVARUR',
  'KRISHNAGIRI',
  'ARIYALUR',
  'TIRUPUR'],
 'PONDICHERRY': ['PONDICHERRY', 'KARAIKAL', 'MAHE', 'YANAM'],
 'KARNATAKA': ['UTTAR KANNADA',
  'DAKSHIN KANDA',
  'UDUPI',
  'BELGAM',
  'BIDAR',
  'BIJAPUR',
  'DHARWAD',
  'GULBARGA',
  'YADGIR',
  'RAICHUR',
  'BAGALKOTE',
  'GADAG',
  'HAVERI',
  'KOPPAL',
  'BANGALORE RUR',
  'BELLARY',
  'CHIKMAGALUR',
  'CHITRADURGA',
  'KODAGU',
  'HASSAN',
  'KOLAR',
  'MANDYA',
  'MYSORE',
  'SHIMOGA',
  'TUMKUR',
  'BANGALORE URB',
  'CHAMARAJANAGA',
  'DAVANGERE',
  'RAMNAGAR(BNGR)',
  'CHICKBALLAPUR'],
 'KERALA': ['ALAPPUZHA',
  'CANNUR',
  'ERNAKULAM',
  'KOTTAYAM',
  'KOZHIKODE',
  'MALAPPURAM',
  'PALAKKAD',
  'KOLLAM',
  'THRISSUR',
  'THIRUVANANTHA',
  'IDUKKI',
  'KASARGOD',
  'PATHANAMTHITTA',
  'WAYANAD'],
 'LAKSHADWEEP': ['LAKSHADWEEP']}
    
    state= st.selectbox("State" ,states)
    state=state.upper()
    try:
        lst=set(state_dis[state])
        print(lst)
        # dict_dist=Convert(lst)
        district=st.selectbox("District",lst)
    except Exception as e:
        print(e,"erroe is this")
        district=state
    # district=st.selectbox("District",districts)
    monthstoday=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    date = datetime.datetime.today().month
    # st.write("Month:  ",monthstoday[date-1])


    N=st.number_input('N content in soil')
    P=st.number_input('P content in soil')
    K=st.number_input('K content in soil')

    # temp=st.slider("temp",0,50,28)
    # hum=st.slider("humidity",1,200,72)
    ph=st.number_input("pH",1,14,5)
    rainfall=give_Rainfall(district.upper(),monthstoday[0])
    # print(type(rainfall[0]))

    ok=st.button("Tell me the Crop")

    
    if(ok):
        temperature,humidty,clouds=find_Current_Weather(district)
        col1, col2, col3,col4 = st.columns(4)
        col1.metric("Temperature", temperature,)
        col2.metric("pH", ph,"")
        col3.metric("Humidity", humidty, "4%")
        # col4.metric("Clouds", clouds )
        col4.metric("Rainfall", rainfall[0])
        # col4.metric("Icon", st.image(icon))

        x=np.array([[N,P,K,temperature,humidty,ph,rainfall[0]]])
        cropA=linear_Reg_Model.predict(x)
        cropB=KNN_Model.predict(x)
        cropC=Rainforest_Model.predict(x)
        crop=cropA
        other=[cropA,cropB,cropC]
        if(cropC==cropB):
            crop=cropC
       
        # print(crop[0])
        st.subheader(f"The optimal Crop is {crop[0]}")
        
        for crops in other:
            if crops[0]!=crop[0]:
                st.subheader(f"{crops[0]}")



