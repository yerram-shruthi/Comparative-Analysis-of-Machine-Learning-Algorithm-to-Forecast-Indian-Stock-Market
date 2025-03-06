import pandas as pd
from django.conf import settings
import os
from sklearn import metrics
import numpy as np
path =os.path.join(settings.MEDIA_ROOT, 'test.csv')
df = pd.read_csv(path,nrows=200)
df = df[['Open', 'High', 'Low', 'Close']]
X = df.iloc[:,:-1].values
y = df.iloc[:,-1].values
print(f'X Len{len(X)} y len {len(y)}')
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(X,y, train_size=0.80,random_state=0)
print(x_train,x_test,y_train,y_test)




def calc_random_forest_regressor():
        from sklearn.ensemble import RandomForestRegressor
        model = RandomForestRegressor()
        model.fit(x_train, y_train)
        rf_y_pred = model.predict(x_test)
        rf_error_rate = np.sqrt(metrics.mean_squared_error(rf_y_pred.round(), y_test))
        from sklearn.preprocessing import StandardScaler
        sc_X = StandardScaler()
        X_train = sc_X.fit(x_train,y_train)
        print(X_train)
        rf_std=np.std(rf_y_pred)
        return rf_error_rate, rf_std
# X_test = sc_X.transform(x_test)
        # sc_Y = StandardScaler()
        # Y_train = sc_X.fit_transform(y_train.reshape(-1, 1))
        # print(rf_error_rate, Y_train)
        # rf_std=sc_X.copy
def calc_svm_model():
        from sklearn.svm import SVR
        model = SVR()
        model.fit(x_train, y_train)
        svm_y_pred = model.predict(x_test)
        rf_error_rate = np.sqrt(metrics.mean_squared_error(svm_y_pred.round(), y_test))
        from sklearn.preprocessing import StandardScaler
        sc_X = StandardScaler()
        X_train = sc_X.fit(x_train, y_train)
        print(X_train)
        svm_std = np.std(svm_y_pred)
        return rf_error_rate, svm_std

def calc_decision_tree_model():
        from sklearn.tree import DecisionTreeRegressor
        model = DecisionTreeRegressor()
        model.fit(x_train, y_train)
        dt_y_pred = model.predict(x_test)
        dt_error_rate = np.sqrt(metrics.mean_squared_error(dt_y_pred.round(), y_test))
        from sklearn.preprocessing import StandardScaler
        sc_X = StandardScaler()
        X_train = sc_X.fit(x_train, y_train)
        print(X_train)
        dt_std = np.std(dt_y_pred)
        return dt_error_rate, dt_std

def calc_gradient_boosting_model():
        from sklearn.ensemble import GradientBoostingRegressor
        model = GradientBoostingRegressor()
        model.fit(x_train, y_train)
        gbr_y_pred = model.predict(x_test)
        gbr_error_rate = np.sqrt(metrics.mean_squared_error(gbr_y_pred.round(), y_test))
        from sklearn.preprocessing import StandardScaler
        sc_X = StandardScaler()
        X_train = sc_X.fit(x_train, y_train)
        print(X_train)
        gbr_std = np.std(gbr_y_pred)
        return gbr_error_rate, gbr_std

def calc_linear_model():
        from sklearn.linear_model import LinearRegression
        model = LinearRegression()
        model.fit(x_train, y_train)
        lr_y_pred = model.predict(x_test)
        lr_error_rate = np.sqrt(metrics.mean_squared_error(lr_y_pred.round(), y_test))
        from sklearn.preprocessing import StandardScaler
        sc_X = StandardScaler()
        X_train = sc_X.fit(x_train, y_train)
        print(X_train)
        lr_std = np.std(lr_y_pred)
        return lr_error_rate, lr_std