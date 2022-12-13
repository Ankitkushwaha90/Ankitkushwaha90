from django.shortcuts import render
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')

def downloadzipfile(request):
    return render(request, 'static/MusicPlay.zip')

def about(request):
    return render(request, 'about.html')

def project(request):
    return render(request, 'project.html')

def programmingnotes(request):
    return render(request, 'programmingnotes.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

    return render(request, 'contact.html')


# html start
def htmlintro(request):
    return render(request, 'htmldocs.html')

def heading(request):
    return render(request, 'heading.html')

def paragraphs(request):
    return render(request, 'paragraphs.html')

def textformatting(request):
    return render(request, 'textformatting.html')

def anchors(request):
    return render(request, 'anchorsandhyperlinks.html')

def lists(request):
    return render(request, 'lists.html')

def tables(request):
    return render(request, 'tables.html')

def comments(request):
    return render(request, 'comments.html')


# css start
def cssintro(request):
    return render(request, 'cssdocs.html')

def importrule(request):
    return render(request, 'importrule.html')

def CSSwithJquery(request):
    return render(request, 'csswithjquery.html')

def CSSwithJavaScript(request):
    return render(request, 'csswithjavascript.html')

def childPseudoClass(request):
    return render(request, 'childPseudoClass.html')

def comment(request):
    return render(request, 'comment.html')

def textcenter(request):
    return render(request, 'textcenter.html')

def animation(request):
    return render(request, 'animation.html')


# javascript start
def javascriptintro(request):
    return render(request, 'javascriptdocs.html')
def use_of_variable(request):
    return render(request, 'use_of_variable.html')
def commentsjs(request):
    return render(request, 'commentsjs.html')
def dom(request):
    return render(request, 'dom.html')
def prompt(request):
    return render(request, 'prompt.html')
def confirm(request):
    return render(request, 'confirm.html')
def createelement(request):
    return render(request, 'createelement.html')
def AddHTMLcode(request):
    return render(request, 'AddHTMLcode.html')



# php start
def phpintro(request):
    return render(request, 'phpdocs.html')
def variablephp(request):
    return render(request, 'variable.html')
def stringphp(request):
    return render(request, 'stringphp.html')
def operatorsphp(request):
    return render(request, 'operatorsphp.html')
def function(request):
    return render(request, 'function.html')
def while_loop(request):
    return render(request, 'while_loop.html')
def DoWhileLoop(request):
    return render(request, 'do_while_loop.html')
def switch(request):
    return render(request, 'switch.html')
def Arrays(request):
    return render(request, 'Arrays.html')


# python start
def variablepython(request):
    return render(request, 'variablepy.html')
def stringpython(request):
    return render(request, 'stringpy.html')
def commentpython(request):
    return render(request, 'commentpy.html')
def operatorpython(request):
    return render(request, 'operatorpy.html')
def for_looppython(request):
    return render(request, 'for_looppy.html')
def while_looppython(request):
    return render(request, 'while_looppy.html')
def openfolderpy(request):
    return render(request, 'openfolderpy.html')
def readfilepy(request):
    return render(request, 'readfilepy.html')
def writefilepy(request):
    return render(request, 'writefilepy.html')


# c start
def cintro(request):
    return render(request, 'cdocs.html')
def scanf_c(request):
    return render(request, 'scanf.html')
def printfff(request):
    return render(request, 'printf.html')
def Ifelse(request):
    return render(request, 'ifelse.html')
def whileloopc(request):
    return render(request, 'whileloopc.html')
def dowhile(request):
    return render(request, 'dowhileloopc.html')
def functionc(request):
    return render(request, 'functionc.html')
def system_c(request):
    return render(request, 'system_c.html')
def writefilec(request):
    return render(request, 'writefilec.html')
def readfilec(request):
    return render(request, 'readfilec.html')

#KALI LINUX
def KaliIntro(request):
    return render(request, 'KaliIntroduction.html')

#WEBDESIGN
def WebIntroduction(request):
    return render(request, 'WebDesignintroduction.html')

#SQLfolder
def SQLintroduction(request):
    return render(request, 'sql_intro.html')
def ShowDatabase(request):
    return render(request, 'showdatabase.html')
def CreateTable(request):
    return render(request, 'CreateTable.html')
def ShowTables(request):
    return render(request, 'ShowTables.html')
def DescribeTable(request):
    return render(request, 'describe_table.html')
def CreateDatabase(request):
    return render(request, 'createDatabase.html')
def UseDatabase(request):
    return render(request, 'UseDatabase.html')
def DropDatabase(request):
    return render(request, 'DropDatabase.html')
def DropTable(request):
    return render(request, 'DropTable.html')
