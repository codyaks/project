print('hello,I am chatbot what is your name?')
name=input()
print('hello',name,'how are you?,good or bad?')
feel=input().lower()
if feel=='good':
    print('that is great ',name)
elif feel=='bad':
    print ('oh hope that you feel better soon ')
hobby=input('so,what are your hobbies?')
print(hobby,'that is very interesting')
print('do you have a pet?,yes or no')
pet=input().lower()
if pet=='yes':
    type=input('what kind of pet do you have?')
    print('wow,I like',type)
elif pet=='no':
    print('oh,no pet for you')
print('it was nice talking to you',name,'bye!')