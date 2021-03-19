from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View

# Create your views here.
class LoginView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, template_name="login.html", context=context)   
    def post(self, request, *args, **kwargs):
        result = {}
        data = request.POST
        username = data["username"]
        password = data["password"]
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            #context['form'] = LoginForm()
            print("login success")
            return redirect("/polyp/dashboard/")
        else:
            result["error"] = "Invalid username or password"
            print("Error")



        return render(request, template_name="login.html", context = result)   
