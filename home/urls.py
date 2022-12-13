from django.contrib import admin 
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('project', views.project, name='project'),
    path('downloadzipfile', views.downloadzipfile, name='downloadzipfile'),
    path('code', views.programmingnotes, name='programmingnotes'),
    path('contact', views.contact, name='contact'),


    # html start 
    path('Introduction_of_HTML', views.htmlintro, name='htmlintro'),
    path('heading', views.heading, name='heading'),
    path('paragraphs', views.paragraphs, name='paragraphs'),
    path('textformatting', views.textformatting, name='textformatting'),
    path('anchors', views.anchors, name='anchors'),
    path('lists', views.lists, name='lists'),
    path('tables', views.tables, name='tables'),
    path('comments', views.comments, name='comments'),

    #css start
    path('Introduction_of_CSS', views.cssintro, name='cssintro'),
    path('ImportRule', views.importrule, name='importrule'),
    path('CSSwithJquery', views.CSSwithJquery, name='CSSwithJquery'),
    path('CSSwithJavaScript', views.CSSwithJavaScript, name='CSSwithJavaScript'),
    path('childPseudoClass', views.childPseudoClass, name='childPseudoClass'),
    path('comment', views.comment, name='comment'),
    path('textcenter', views.textcenter, name='textcenter'),
    path('animation', views.animation, name='animation'),

    #javascript start
    path('Introduction_of_JAVASCRIPT', views.javascriptintro, name='javascriptintro'),
    path('use_of_variable', views.use_of_variable , name='use_of_variable'),
    path('commentsjs', views.commentsjs , name='commentsjs'),
    path('dom', views.dom , name='dom'),
    path('prompt', views.prompt , name='prompt'),
    path('confirm', views.confirm , name='confirm'),
    path('createelement', views.createelement , name='createelement'),
    path('AddHTMLcode', views.AddHTMLcode , name='AddHTMLcode'),

    #php start
    path('Introduction_of_PHP', views.phpintro, name='phpintro'),
    path('variable_php', views.variablephp, name='variablephp'),
    path('operators_php', views.operatorsphp, name='operatorsphp'),
    path('string_php', views.stringphp, name='stringphp'),
    path('Function', views.function, name='function'),
    path('While_loop', views.while_loop, name='while_loop'),
    path('DoWhileLoop', views.DoWhileLoop, name='doWhileLoop'),
    path('Switch', views.switch, name='switch'),
    path('Arrays', views.Arrays, name='Arrays'),

    #python start
    path('variablepy', views.variablepython, name='variablepython'),
    path('stringpy', views.stringpython, name='stringpython'),
    path('commentpy', views.commentpython, name='commentpython'),
    path('operatorpy', views.operatorpython, name='operatorpython'),
    path('for_looppy', views.for_looppython, name='for_looppython'),
    path('while_looppy', views.while_looppython, name='while_looppython'),
    path('openfolderpy', views.openfolderpy, name='openfolderpy'),
    path('writefilepy', views.writefilepy, name='writefilepy'),
    path('readfilepy', views.readfilepy, name='readfilepy'),

    #c start
    path('Introduction_of_C', views.cintro, name='cintro'),
    path('scanf', views.scanf_c, name='scanf_c'),
    path('Printf', views.printfff, name='printfff'),
    path('Ifelse', views.Ifelse, name='Ifelse'),
    path('WhileLoop', views.whileloopc, name='whileloopc'),
    path('DoWhileLoopc', views.dowhile, name='dowhile'),
    path('functionc', views.functionc, name='functionc'),
    path('system_c', views.system_c, name='system_c'),
    path('writefilec', views.writefilec, name='writefilec'),
    path('readfilec', views.readfilec, name='readfilec'),

    #KALI LINUX
    path('KaliLinuxIntroduction', views.KaliIntro, name='KaliIntroduction'),

    #WebDesign
    path('WebDesignIntroduction', views.WebIntroduction, name='WebIntroduction'),

    #sql
    path('SQLintroduction', views.SQLintroduction, name='SQLintroduction'),
    path('ShowDatabase', views.ShowDatabase, name='ShowDatabase'),
    path('CreateTable', views.CreateTable, name='CreateTable'),
    path('ShowTables', views.ShowTables, name='ShowTables'),
    path('DescribeTable', views.DescribeTable, name='DescribeTable'),
    path('CreateDatabase', views.CreateDatabase, name='CreateDatabase'),
    path('UseDatabase', views.UseDatabase, name='UseDatabase'),
    path('DropDatabase', views.DropDatabase, name='DropDatabase'),
    path('DropTable', views.DropTable, name='DropTable'),

    
]