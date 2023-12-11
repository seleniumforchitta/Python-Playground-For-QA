1. Open the link: https://www.amazon.com/customer-preferences/edit?ie=UTF8&preferencesReturnUrl=%2Fref%3Dnav_logo&ref_=topnav_lang_ais

Amazon site opens with Language Settings with 9 options, write the locator for "português - PT - Tradução" option


2. Create a method to verify all the options are correct

total = find_by.xpoath(//div[@data-a-input-name='lop']).size
city = []

for i in range(total):
    temp_city = find.xpath((//div[@data-a-input-name='lop'])[i]/label/input).getattribute('value')
    city.append(temp_city)


3.  does the wait implemented below work? Do you now a better way to implement waits in Selenium?
         try {
        Thread.sleep(1000);
          } catch (InterruptedException e) {
         e.printStackTrace();
          }
try:
        time.sleep(10)
    except Exception as e:
        print(e)

l1=[1, 2, 3, 'a']
l2=l1
l1.append(5)

1. What is the value of l1? What is the value of l2?
2. How do you find the type and memory address of a variable?
l1=[1, 3, 5, 7, 9]
l2=[0, 2, 4, 6, 8]
output ={x: y for x in l1 for y in l2}
print(output)
*args and **kwargs?
Add two lists, alternating elements. If one of the lists is longer than the other, all items should be added to the end:
a = [1, 2, 3, 4, 5]
b = [4, 6, 8]
Result example: c = [1, 4, 2, 6, 3, 8, 4, 5]
1. Open the link: https://www.amazon.com/customer-preferences/edit?ie=UTF8&preferencesReturnUrl=%2Fref%3Dnav_logo&ref_=topnav_lang_ais

Amazon site opens with Language Settings with 9 options, write the locator for "português - PT - Tradução" option


2. Create a method to verify all the options are correct

3.  does the wait implemented below work? Do you now a better way to implement waits in Selenium?
         try {
        Thread.sleep(1000);
          } catch (InterruptedException e) {
         e.printStackTrace();
          }
try:
        time.sleep(10)
    except Exception as e:
        print(e)

Who can see your messages?
to:
