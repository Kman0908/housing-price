import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import streamlit as st
from src.pipeline.predict_pipeline import Predict, CustomData

st.set_page_config(page_title='House Price Predictor', page_icon='🏠', layout='wide')

st.title('🏠 House Price Predictor')
st.markdown('Fill in the house details below to get a predicted sale price.')

# ── FORM ──────────────────────────────────────────────────────────────────────
with st.form('prediction_form'):

    st.subheader('📍 Location & Lot')
    c1, c2, c3 = st.columns(3)
    Neighborhood = c1.selectbox('Neighborhood', ['Blmngtn', 'Blueste', 'BrDale', 'BrkSide', 'ClearCr', 'CollgCr', 'Crawfor', 'Edwards', 'Gilbert', 'IDOTRR', 'MeadowV', 'Mitchel', 'NAmes', 'NPkVill', 'NWAmes', 'NoRidge', 'NridgHt', 'OldTown', 'SWISU', 'Sawyer', 'SawyerW', 'Somerst', 'StoneBr', 'Timber', 'Veenker'])
    MSZoning       = c2.selectbox('MS Zoning', ['RL', 'RM', 'FV', 'RH', 'C (all)'])
    LotConfig      = c3.selectbox('Lot Config', ['Inside', 'Corner', 'CulDSac', 'FR2', 'FR3'])
    LotShape       = c1.selectbox('Lot Shape', ['Reg', 'IR1', 'IR2', 'IR3'])
    LandContour    = c2.selectbox('Land Contour', ['Lvl', 'Bnk', 'HLS', 'Low'])
    LandSlope      = c3.selectbox('Land Slope', ['Gtl', 'Mod', 'Sev'])
    LotFrontage    = c1.number_input('Lot Frontage (ft)', min_value=21, max_value=313, value=69)
    LotArea        = c2.number_input('Lot Area (sqft)', min_value=1300, max_value=215245, value=9478)
    Condition1     = c3.selectbox('Condition 1', ['Norm', 'Feedr', 'Artery', 'PosN', 'PosA', 'RRNn', 'RRAn', 'RRNe', 'RRAe'])

    st.subheader('🏗️ Building')
    c1, c2, c3 = st.columns(3)
    MSSubClass     = c1.selectbox('MS SubClass', [20, 30, 40, 45, 50, 60, 70, 75, 80, 85, 90, 120, 150, 160, 180, 190])
    BldgType       = c2.selectbox('Building Type', ['1Fam', '2fmCon', 'Duplex', 'TwnhsE', 'Twnhs'])
    HouseStyle     = c3.selectbox('House Style', ['1Story', '1.5Fin', '1.5Unf', '2Story', '2.5Fin', '2.5Unf', 'SFoyer', 'SLvl'])
    OverallQual    = c1.slider('Overall Quality (1-10)', 1, 10, 6)
    OverallCond    = c2.slider('Overall Condition (1-9)', 1, 9, 5)
    YearBuilt      = c3.number_input('Year Built', min_value=1872, max_value=2010, value=1973)
    YearRemodAdd   = c1.number_input('Year Remodeled', min_value=1950, max_value=2010, value=1994)
    RoofStyle      = c2.selectbox('Roof Style', ['Gable', 'Hip', 'Flat', 'Gambrel', 'Mansard', 'Shed'])

    st.subheader('🧱 Exterior')
    c1, c2, c3 = st.columns(3)
    Exterior1st  = c1.selectbox('Exterior 1st', ['AsbShng', 'AsphShn', 'BrkComm', 'BrkFace', 'CBlock', 'CemntBd', 'HdBoard', 'ImStucc', 'MetalSd', 'Plywood', 'Stone', 'Stucco', 'VinylSd', 'Wd Sdng', 'WdShing'])
    ExterQual      = c2.selectbox('Exterior Quality', ['TA', 'Gd', 'Ex', 'Fa'])
    ExterCond      = c3.selectbox('Exterior Condition', ['TA', 'Gd', 'Ex', 'Fa', 'Po'])
    MasVnrArea     = c1.number_input('Masonry Veneer Area', min_value=0, max_value=1600, value=0)
    Foundation     = c2.selectbox('Foundation', ['PConc', 'CBlock', 'BrkTil', 'Slab', 'Stone', 'Wood'])

    st.subheader('🏚️ Basement')
    c1, c2, c3 = st.columns(3)
    BsmtQual       = c1.selectbox('Basement Quality', ['None', 'TA', 'Gd', 'Ex', 'Fa'])
    BsmtCond       = c2.selectbox('Basement Condition', ['None', 'TA', 'Gd', 'Fa', 'Po'])
    BsmtExposure   = c3.selectbox('Basement Exposure', ['None', 'No', 'Mn', 'Av', 'Gd'])
    BsmtFinType1   = c1.selectbox('Basement Fin Type 1', ['None', 'Unf', 'LwQ', 'Rec', 'BLQ', 'ALQ', 'GLQ'])
    BsmtFinType2   = c2.selectbox('Basement Fin Type 2', ['None', 'Unf', 'LwQ', 'Rec', 'BLQ', 'ALQ', 'GLQ'])
    BsmtFinSF1     = c3.number_input('Basement Fin SF1', min_value=0, max_value=5644, value=0)
    BsmtFinSF2     = c1.number_input('Basement Fin SF2', min_value=0, max_value=1474, value=0)
    BsmtUnfSF      = c2.number_input('Basement Unfinished SF', min_value=0, max_value=2336, value=477)
    TotalBsmtSF    = c3.number_input('Total Basement SF', min_value=0, max_value=6110, value=991)
    BsmtFullBath   = c1.number_input('Basement Full Bath', min_value=0, max_value=3, value=0)
    BsmtHalfBath   = c2.number_input('Basement Half Bath', min_value=0, max_value=2, value=0)

    st.subheader('🔌 Utilities & Systems')
    c1, c2, c3 = st.columns(3)
    Heating        = c1.selectbox('Heating Type', ['GasA', 'GasW', 'Grav', 'Wall', 'Floor', 'OthW'])
    HeatingQC      = c2.selectbox('Heating Quality', ['Ex', 'Gd', 'TA', 'Fa', 'Po'])
    CentralAir     = c3.selectbox('Central Air', ['Y', 'N'])
    Electrical     = c1.selectbox('Electrical', ['SBrkr', 'FuseA', 'FuseF', 'FuseP', 'Mix'])

    st.subheader('📐 Living Area')
    c1, c2, c3 = st.columns(3)
    _1stFlrSF      = c1.number_input('1st Floor SF', min_value=334, max_value=4692, value=1087)
    _2ndFlrSF      = c2.number_input('2nd Floor SF', min_value=0, max_value=2065, value=0)
    LowQualFinSF   = c3.number_input('Low Quality Finished SF', min_value=0, max_value=572, value=0)
    GrLivArea      = c1.number_input('Above Grade Living Area SF', min_value=334, max_value=5642, value=1464)
    FullBath       = c2.number_input('Full Bathrooms', min_value=0, max_value=3, value=2)
    HalfBath       = c3.number_input('Half Bathrooms', min_value=0, max_value=2, value=0)
    BedroomAbvGr   = c1.number_input('Bedrooms Above Grade', min_value=0, max_value=8, value=3)
    KitchenAbvGr   = c2.number_input('Kitchens Above Grade', min_value=0, max_value=3, value=1)
    KitchenQual    = c3.selectbox('Kitchen Quality', ['TA', 'Gd', 'Ex', 'Fa'])
    TotRmsAbvGrd   = c1.number_input('Total Rooms Above Grade', min_value=2, max_value=14, value=6)
    Functional     = c2.selectbox('Functional', ['Typ', 'Min1', 'Min2', 'Mod', 'Maj1', 'Maj2', 'Sev'])
    Fireplaces     = c3.number_input('Fireplaces', min_value=0, max_value=3, value=1)
    FireplaceQu    = c1.selectbox('Fireplace Quality', ['None', 'TA', 'Gd', 'Ex', 'Fa', 'Po'])

    st.subheader('🚗 Garage')
    c1, c2, c3 = st.columns(3)
    GarageType     = c1.selectbox('Garage Type', ['None', 'Attchd', 'Detchd', 'BuiltIn', 'Basment', 'CarPort', '2Types'])
    GarageFinish   = c2.selectbox('Garage Finish', ['None', 'Unf', 'RFn', 'Fin'])
    GarageQual     = c3.selectbox('Garage Quality', ['None', 'TA', 'Gd', 'Ex', 'Fa', 'Po'])
    GarageCond     = c1.selectbox('Garage Condition', ['None', 'TA', 'Gd', 'Ex', 'Fa', 'Po'])
    GarageYrBlt    = c2.number_input('Garage Year Built', min_value=1900, max_value=2010, value=1980)
    GarageCars     = c3.number_input('Garage Cars', min_value=0, max_value=4, value=2)
    GarageArea     = c1.number_input('Garage Area (sqft)', min_value=0, max_value=1418, value=480)
    PavedDrive     = c2.selectbox('Paved Drive', ['Y', 'P', 'N'])

    st.subheader('🏡 Outdoor Areas')
    c1, c2, c3 = st.columns(3)
    WoodDeckSF     = c1.number_input('Wood Deck SF', min_value=0, max_value=857, value=0)
    OpenPorchSF    = c2.number_input('Open Porch SF', min_value=0, max_value=547, value=25)
    EnclosedPorch  = c3.number_input('Enclosed Porch SF', min_value=0, max_value=552, value=0)
    _3SsnPorch     = c1.number_input('3 Season Porch SF', min_value=0, max_value=508, value=0)
    ScreenPorch    = c2.number_input('Screen Porch SF', min_value=0, max_value=480, value=0)
    PoolArea       = c3.number_input('Pool Area SF', min_value=0, max_value=738, value=0)
    MiscVal        = c1.number_input('Misc Value ($)', min_value=0, max_value=15500, value=0)

    st.subheader('📄 Sale Info')
    c1, c2, c3 = st.columns(3)
    SaleType       = c1.selectbox('Sale Type', ['COD', 'CWD', 'Con', 'ConLD', 'ConLI', 'ConLw', 'New', 'Oth', 'WD'])
    SaleCondition  = c2.selectbox('Sale Condition', ['Normal', 'Abnorml', 'Partial', 'AdjLand', 'Alloca', 'Family'])
    MoSold         = c3.slider('Month Sold', 1, 12, 6)
    YrSold         = c1.selectbox('Year Sold', [2006, 2007, 2008, 2009, 2010])

    submitted = st.form_submit_button('🔮 Predict Price', use_container_width=True)

# ── PREDICTION ────────────────────────────────────────────────────────────────
if submitted:
    try:
        data = CustomData(
            MSSubClass=MSSubClass,
            MSZoning=MSZoning,
            LotFrontage=float(LotFrontage),
            LotArea=LotArea,
            LotShape=LotShape,
            LandContour=LandContour,
            LotConfig=LotConfig,
            LandSlope=LandSlope,
            Neighborhood=Neighborhood,
            Condition1=Condition1,
            BldgType=BldgType,
            HouseStyle=HouseStyle,
            OverallQual=OverallQual,
            OverallCond=OverallCond,
            YearBuilt=YearBuilt,
            YearRemodAdd=YearRemodAdd,
            RoofStyle=RoofStyle,
            Exterior1st=Exterior1st,
            MasVnrArea=float(MasVnrArea),
            ExterQual=ExterQual,
            ExterCond=ExterCond,
            Foundation=Foundation,
            BsmtQual=BsmtQual,
            BsmtCond=BsmtCond,
            BsmtExposure=BsmtExposure,
            BsmtFinType1=BsmtFinType1,
            BsmtFinSF1=BsmtFinSF1,
            BsmtFinType2=BsmtFinType2,
            BsmtFinSF2=BsmtFinSF2,
            BsmtUnfSF=BsmtUnfSF,
            TotalBsmtSF=TotalBsmtSF,
            Heating=Heating,
            HeatingQC=HeatingQC,
            CentralAir=CentralAir,
            Electrical=Electrical,
            _1stFlrSF=_1stFlrSF,
            _2ndFlrSF=_2ndFlrSF,
            LowQualFinSF=LowQualFinSF,
            GrLivArea=GrLivArea,
            BsmtFullBath=BsmtFullBath,
            BsmtHalfBath=BsmtHalfBath,
            FullBath=FullBath,
            HalfBath=HalfBath,
            BedroomAbvGr=BedroomAbvGr,
            KitchenAbvGr=KitchenAbvGr,
            KitchenQual=KitchenQual,
            TotRmsAbvGrd=TotRmsAbvGrd,
            Functional=Functional,
            Fireplaces=Fireplaces,
            FireplaceQu=FireplaceQu,
            GarageType=GarageType,
            GarageYrBlt=float(GarageYrBlt),
            GarageFinish=GarageFinish,
            GarageCars=GarageCars,
            GarageArea=GarageArea,
            GarageQual=GarageQual,
            GarageCond=GarageCond,
            PavedDrive=PavedDrive,
            WoodDeckSF=WoodDeckSF,
            OpenPorchSF=OpenPorchSF,
            EnclosedPorch=EnclosedPorch,
            _3SsnPorch=_3SsnPorch,
            ScreenPorch=ScreenPorch,
            PoolArea=PoolArea,
            MiscVal=MiscVal,
            MoSold=MoSold,
            YrSold=YrSold,
            SaleType=SaleType,
            SaleCondition=SaleCondition,
        )

        df = data.get_data_as_dataframe()
        pipeline = Predict()
        prediction = pipeline.predict(df)

        st.success(f'### 💰 Predicted Sale Price: ${prediction[0]:,.0f}')

    except Exception as e:
        st.error(f'Prediction failed: {e}')