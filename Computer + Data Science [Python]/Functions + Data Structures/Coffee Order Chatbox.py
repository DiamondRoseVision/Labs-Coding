#!/usr/bin/env python
# coding: utf-8

# ## Coffee taking Order Chatbox

# In[ ]:


def coffee_bot():
  print('Welcome to the cafe!')
 
  size = get_size()
  drink_type = get_drink_type()
  mon = milk_or_nah()
  fin = order_fin()
  print('Thanks {}! Your drink will be ready shortly! One {} {} {}'.format(fin, size, drink_type, mon))
def print_mess():
  print("I'm sorry, that's not a valid option! Please pick from available options")
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    return 'Small'
  elif res == 'b':
    return 'Medium'
  elif res == 'c':
    return 'Large'
  else:
    print_mess()
    return get_size()
def get_drink_type():
  dri = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>')
  if dri == 'a':
    return 'Brewed Coffee'
  elif dri == 'b':
    return 'Mocha'
  elif dri == 'c':
    return 'Latte'
  else:
    print_mess()
    return get_drink_type()
def milk_opt():
  m_opt = input('What kind of milk would you like milk with that? \n[a] 2% Milk [b] Non-fat Milk [c] Soy Milk \n')
  if m_opt == 'a':
    return ' 2% Milk'
  elif m_opt == 'b':
    return 'Non-fat Milk'
  elif m_opt == 'c':
    return 'Soy Milk'
  else:
    print_message()
    return milk_opt()
def order_fin():
  return input('And what\'s the name for your order? \n')

def milk_or_nah():
  m_or_n = input('Would you like milk with that? \n[a] Yes [b] No \n')
  if m_or_n == 'a':
    return milk_opt()
  elif m_or_n == 'b':
    return('No milk')
    order_fin()
  else:
    print_message()
    return milk_opt
  
coffee_bot()


# In[ ]:




