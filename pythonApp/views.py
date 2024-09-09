from django.shortcuts import render

def home(request):
    return render(request,'pythonApp/python_home.html',{'active_nav': 'python'})

def intro(request):
    return render(request,'pythonApp/python_intro.html',{'active_page': 'introduction','active_nav': 'python'})

def variables(request):
    return render(request,'pythonApp/python_var.html',{'active_page': 'variables','active_nav': 'python'})

def datatypes(request):
    return render(request,'pythonApp/python_dtypes.html',{'active_page': 'datatypes','active_nav': 'python'})

def typecast(request):
    return render(request,'pythonApp/python_typecast.html',{'active_page': 'typecasting','active_nav': 'python'})

def strings(request):
    return render(request,'pythonApp/python_strings.html',{'active_page': 'strings','active_nav': 'python'})

def boolean(request):
    return render(request,'pythonApp/python_boolean.html',{'active_page': 'boolean','active_nav': 'python'})

def operators(request):
    return render(request,'pythonApp/python_operators.html',{'active_page': 'operators','active_nav': 'python'})

def condstatement(request):
    return render(request,'pythonApp/python_condstate.html',{'active_page': 'condstate','active_nav': 'python'})

def loops(request):
    return render(request,'pythonApp/python_loops.html',{'active_page': 'loops','active_nav': 'python'})

def list(request):
    return render(request,'pythonApp/python_list.html',{'active_page': 'list','active_nav': 'python'})

def tuples(request):
    return render(request,'pythonApp/python_tuples.html',{'active_page': 'tuple','active_nav': 'python'})

def set(request):
    return render(request,'pythonApp/python_set.html',{'active_page': 'set','active_nav': 'python'})

def dict(request):
    return render(request,'pythonApp/python_dict.html',{'active_page': 'dict','active_nav': 'python'})

def function(request):
    return render(request,'pythonApp/python_function.html',{'active_page': 'function','active_nav': 'python'})

def classes(request):
    return render(request,'pythonApp/python_class.html',{'active_page': 'class','active_nav': 'python'})

def inheritance(request):
    return render(request,'pythonApp/python_inheritance.html',{'active_page': 'inheritance','active_nav': 'python'})

def polymorphism(request):
    return render(request,'pythonApp/python_polymorphism.html',{'active_page': 'polymorphism','active_nav': 'python'})

def scope(request):
    return render(request,'pythonApp/python_scope.html',{'active_page': 'scope','active_nav': 'python'})

def modules(request):
    return render(request,'pythonApp/python_modules.html',{'active_page': 'modules','active_nav': 'python'})

def exception(request):
    return render(request,'pythonApp/python_exceptions.html',{'active_page': 'exception','active_nav': 'python'})

def filehandling(request):
    return render(request,'pythonApp/python_filehandling.html',{'active_page': 'filehandling','active_nav': 'python'})

def jsonhandling(request):
    return render(request,'pythonApp/python_json_handling.html',{'active_page': 'json','active_nav': 'python'})

def regex(request):
    return render(request,'pythonApp/python_regex_handling.html',{'active_page': 'regex','active_nav': 'python'})

def generators(request):
    return render(request,'pythonApp/python_generator.html',{'active_page': 'generators','active_nav': 'python'})

def decorators(request):
    return render(request,'pythonApp/python_decorators.html',{'active_page': 'decorators','active_nav': 'python'})

def lambdafnct(request):
    return render(request,'pythonApp/python_lambdafnct.html',{'active_page': 'lambdafnct','active_nav': 'python'})

def iterators(request):
    return render(request,'pythonApp/python_iterators.html',{'active_page': 'iterators','active_nav': 'python'})

def contextmanager(request):
    return render(request,'pythonApp/python_contextmanager.html',{'active_page': 'contextmanager','active_nav': 'python'})


