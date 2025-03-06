from django.shortcuts import render
from .forms import UserRegistrationForm
from django.contrib import messages
from .models import UserRegistrationModel
from django.http import HttpResponse


# Create your views here.
def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = UserRegistrationForm()
            return render(request, 'UserRegistrations.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'UserRegistrations.html', {'form': form})


def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHome.html', {})
            else:
                messages.success(request, 'Your Account has not been activated by Admin.')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})


def UserHome(request):
    return render(request, 'users/UserHome.html', {})

def user_view_data(request):
    import pandas as pd
    from django.conf import settings
    import os
    path =os.path.join(settings.MEDIA_ROOT, 'stockForecast.csv')
    df = pd.read_csv(path)
    print(df)
    df = df[['Date', 'Open', 'High', 'Low', 'Close']]
    # df = df.head(10)
    df = df.head(100).to_html

    return render(request, 'users/view_data.html',{'data': df})
def user_trainset(request):
    from .utility import train_set
    rf_error_rate, rf_std = train_set.calc_random_forest_regressor()
    svm_error_rate, svm_std = train_set.calc_svm_model()
    dt_error_rate,dt_std=train_set.calc_decision_tree_model()
    gbr_error_rate, gbr_std = train_set.calc_gradient_boosting_model()
    lr_error_rate, lr_std = train_set.calc_linear_model()
    rf = {'rf_error_rate': rf_error_rate, 'rf_std': rf_std}
    svm={'svm_error_rate' : svm_error_rate,'svm_std': svm_std}
    dt = {'dt_error_rate': dt_error_rate, 'dt_std': dt_std}
    gbr = {'gbr_error_rate': gbr_error_rate, 'gbr_std': gbr_std}
    lr = {'lr_error_rate': lr_error_rate, 'lr_std': lr_std}
    return render(request,'users/train_set_results.html',{"rf": rf,"svm":svm,"dt":dt,"gbr":gbr,"lr":lr} )
def user_testset(request):
    from .utility import test_set
    rf_error_rate, rf_std = test_set.calc_random_forest_regressor()
    svm_error_rate, svm_std = test_set.calc_svm_model()
    dt_error_rate, dt_std = test_set.calc_decision_tree_model()
    gbr_error_rate, gbr_std = test_set.calc_gradient_boosting_model()
    lr_error_rate, lr_std = test_set.calc_linear_model()

    rf = {'rf_error_rate': rf_error_rate, 'rf_std': rf_std}
    svm = {'svm_error_rate': svm_error_rate, 'svm_std': svm_std}
    dt = {'dt_error_rate': dt_error_rate, 'dt_std': dt_std}
    gbr = {'gbr_error_rate': gbr_error_rate, 'gbr_std': gbr_std}
    lr = {'lr_error_rate': lr_error_rate, 'lr_std': lr_std}
    return render(request, 'users/test_set_result.html', {"rf": rf, "svm": svm, "dt": dt, "gbr": gbr, "lr": lr})


def user_train_deep_learning(request):
    from .utility import deep_learnig_model
    train_error_rate,train_std,test_std,test_error_rate = deep_learnig_model.calculate_rnn_results()
    return render(request, "users/train_set_results.html", {
        "train_std": train_std, "train_error_rate": train_error_rate, "test_std": test_std, "test_error_rate": test_error_rate
    })
def user_prediction(request):
    from .utility.ForeCastModel import StockPriceForeCast
    obj = StockPriceForeCast()
    rslt = obj.start_future_prediction()
    rslt = rslt.to_html
    return render(request, "users/forecast_result.html", {"rslt": rslt})

def analysis(request):
     from .utility.analysis import Forecast_analysis
     rslt = Forecast_analysis()
     return render(request, "users/analysis.html",{"rslt":rslt})
# yts=analysis()